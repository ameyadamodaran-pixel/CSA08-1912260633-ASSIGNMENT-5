import sqlite3, csv, tempfile, os

def station_average(con, name):
    # Parameterized query prevents input from being interpreted as SQL code.
    cur=con.execute('SELECT AVG(pm25) FROM readings WHERE station = ?', (name,))
    return cur.fetchone()[0]

def load_file(path):
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader=csv.DictReader(f)
            required={'station','date','pm25'}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                return 'ERROR: missing required column(s)'
            count=sum(1 for row in reader if row.get('station') and row.get('date'))
            return f'OK: parsed {count} data row(s)'
    except UnicodeDecodeError:
        return 'ERROR: encoding is not UTF-8'
    except csv.Error as e:
        return f'ERROR: CSV parse issue: {e}'
    except OSError as e:
        return f'ERROR: file read failed: {e}'

def main():
    con=sqlite3.connect(':memory:')
    con.execute('CREATE TABLE readings(station TEXT, date TEXT, pm25 REAL)')
    con.executemany('INSERT INTO readings VALUES(?,?,?)',[('Adyar','2026-10-01',48),('Guindy','2026-10-01',95),("O'Brien",'2026-10-01',60)])
    print('Adyar average:',station_average(con,'Adyar'))
    for attack in ["Adyar' OR '1'='1", "O'Brien"]:
        print(repr(attack),'=>',station_average(con,attack))
    # Build test files and show validation responses.
    tests={'missing_column.csv':'station,date\nAdyar,2026-10-01\n','wrong_delimiter.csv':'station;date;pm25\nAdyar;2026-10-01;48\n','empty.csv':'','bad_encoding.csv':b'\xff\xfe\xfa'}
    for name,content in tests.items():
        with open(name,'wb') as f: f.write(content.encode() if isinstance(content,str) else content)
        print(name,':',load_file(name));os.remove(name)
    con.close()
if __name__=='__main__': main()
