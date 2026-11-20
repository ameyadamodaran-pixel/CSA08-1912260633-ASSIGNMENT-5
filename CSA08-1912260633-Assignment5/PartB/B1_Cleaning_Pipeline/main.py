import csv, sqlite3, statistics, re
from pathlib import Path
BASE=Path(__file__).resolve().parent
INPUT=BASE/'input'/'messy_air.csv'
DB=BASE/'air_quality.sqlite'
OUTPUT=BASE/'output'
OUTPUT.mkdir(exist_ok=True)

def clean_rows(path):
    cleaned=[]; rejected=[]; seen=set()
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            try:
                station=row['station'].strip().title(); date=row['date'].strip(); hour=int(row['hour'])
                vals={k:(None if row[k].strip().upper() in ('','NA','N/A','NULL') else float(row[k])) for k in ['pm25','pm10','no2','temperature']}
                if not station or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',date): raise ValueError('invalid station/date')
                if vals['pm25'] is not None and (vals['pm25']<0 or vals['pm25']>999): raise ValueError('PM2.5 out of accepted range')
                if vals['pm10'] is not None and vals['pm10']<0: raise ValueError('negative PM10')
                if vals['no2'] is not None and vals['no2']<0: raise ValueError('negative NO2')
                if vals['temperature'] is not None and vals['temperature']>60: vals['temperature']=(vals['temperature']-32)*5/9
                key=(station,date,hour)
                if key in seen: rejected.append((row,'duplicate station/date/hour')); continue
                seen.add(key)
                cleaned.append((station,date,hour,vals['pm25'],vals['pm10'],vals['no2'],vals['temperature']))
            except Exception as e: rejected.append((row,str(e)))
    # Fill PM2.5 missing values using median of valid PM2.5 readings
    valid=[r[3] for r in cleaned if r[3] is not None]
    median=statistics.median(valid) if valid else None
    result=[]
    for r in cleaned:
        if r[3] is None and median is not None:
            r=list(r);r[3]=median;r=tuple(r)
        result.append(r)
    return result,rejected

def main():
    rows,rejected=clean_rows(INPUT)
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.executescript('DROP TABLE IF EXISTS readings; CREATE TABLE readings(station TEXT,date TEXT,hour INTEGER,pm25 REAL,pm10 REAL,no2 REAL,temperature_c REAL,PRIMARY KEY(station,date,hour)); CREATE INDEX idx_station_date ON readings(station,date);')
    cur.executemany('INSERT INTO readings VALUES(?,?,?,?,?,?,?)',rows); con.commit()
    q=cur.execute('SELECT station, AVG(pm25) FROM readings GROUP BY station ORDER BY station').fetchall()
    with open(OUTPUT/'cleaned_readings.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['station','date','hour','pm25','pm10','no2','temperature_c']);w.writerows(rows)
    with open(OUTPUT/'rejected_rows.txt','w',encoding='utf-8') as f:
        for row,reason in rejected:f.write(f'{row} | {reason}\n')
    with open(OUTPUT/'sql_results.txt','w',encoding='utf-8') as f:
        f.write('Station average PM2.5\n');f.write(str(q)+'\n')
    print('Cleaned rows:',len(rows));print('Rejected rows:',len(rejected));print('Station averages:',q);print('Cleaned CSV:',OUTPUT/'cleaned_readings.csv')
    con.close()
if __name__=='__main__': main()
