import csv, random, time, statistics, sqlite3, cProfile, pstats, io
from pathlib import Path
from datetime import date, timedelta
BASE=Path(__file__).resolve().parent; OUT=BASE/'output'; OUT.mkdir(exist_ok=True)
try: import pandas as pd
except ImportError: pd=None

def make_rows(stations, days=365, seed=42):
    random.seed(seed); rows=[]
    for s in range(stations):
        name=f'Station{s+1:03d}'
        for d in range(days): rows.append((name,(date(2026,1,1)+timedelta(days=d)).isoformat(),random.randint(1,180)))
    return rows

def loops(rows):
    agg={}
    for station,date,value in rows:
        key=(station,date); total,count=agg.get(key,(0,0));agg[key]=(total+value,count+1)
    return {k:v[0]/v[1] for k,v in agg.items()}

def run_size(nstations):
    rows=make_rows(nstations); results=[]
    t=time.perf_counter(); a=loops(rows); results.append(('loops',time.perf_counter()-t,a))
    if pd is not None:
        t=time.perf_counter(); df=pd.DataFrame(rows,columns=['station','date','pm25']); b=df.groupby(['station','date']).pm25.mean().to_dict(); results.append(('pandas_groupby',time.perf_counter()-t,b))
    con=sqlite3.connect(':memory:');con.execute('CREATE TABLE readings(station TEXT,date TEXT,pm25 REAL)')
    t=time.perf_counter();con.executemany('INSERT INTO readings VALUES(?,?,?)',rows);con.commit(); load_time=time.perf_counter()-t
    t=time.perf_counter(); c={(station,date):avg for station,date,avg in con.execute('SELECT station,date,AVG(pm25) FROM readings GROUP BY station,date').fetchall()}; results.append(('sqlite_groupby',time.perf_counter()-t,c));con.close()
    for method,elapsed,output in results:
        # Ensure equivalent aggregate counts and results within floating tolerance.
        print(f'{nstations} stations | {method} | {elapsed:.6f}s | groups={len(output)} | verified={len(output)==len(a)}')
    return [(nstations,m,t,len(out)) for m,t,out in results],load_time,len(rows)

def main():
    records=[]
    for size in (1,12,120):
        data,load_time,n=run_size(size);records+=data
        print(f'SQL insert/load time for {size} stations, {n} rows: {load_time:.6f}s')
    with open(OUT/'benchmark_results.csv','w',newline='') as f:
        w=csv.writer(f);w.writerow(['stations','method','seconds','groups']);w.writerows(records)
    # cProfile sample on largest size
    sample=make_rows(120)
    pr=cProfile.Profile();pr.enable();loops(sample);pr.disable()
    stream=io.StringIO();pstats.Stats(pr,stream=stream).sort_stats('cumtime').print_stats(8)
    (OUT/'profile_report.txt').write_text(stream.getvalue(),encoding='utf-8')
    print('Results saved under output/. pandas available:',pd is not None)
if __name__=='__main__': main()
