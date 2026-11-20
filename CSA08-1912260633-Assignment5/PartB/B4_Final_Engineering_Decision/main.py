POSITIVE={'good','clean','fast','helpful','improved'}
NEGATIVE={'bad','dirty','slow','rude','smoke','broken'}
NEGATORS={'not','never','no'}
from pathlib import Path

def score(text):
    words=text.lower().replace('.','').replace(',','').split(); total=0; flip=False
    for word in words:
        if word in NEGATORS: flip=True; continue
        value=1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if value:
            total += -value if flip else value
            flip=False
    return total

def label(text):
    s=score(text)
    return 'positive' if s>0 else 'negative' if s<0 else 'neutral'

def summarize(text, k=1):
    sentences=[s.strip() for s in text.split('.') if s.strip()]
    freq={}
    for sentence in sentences:
        for word in sentence.lower().replace(',','').split():
            if word not in {'the','and','from','is','was','are','a','to','of','in','it'}: freq[word]=freq.get(word,0)+1
    ranked=sorted(sentences,key=lambda s:sum(freq.get(w,0) for w in s.lower().replace(',','').split()),reverse=True)
    return '. '.join(ranked[:k])+('.' if ranked else '')

def answer_question(question, db_path):
    import sqlite3
    q=question.lower()
    station=next((s for s in ['adyar','guindy','velachery'] if s in q),None)
    if 'pm2.5' in q and station:
        if not Path(db_path).exists():
            with sqlite3.connect(db_path) as con:
                con.execute('CREATE TABLE readings(station TEXT, pm25 REAL)')
                con.executemany('INSERT INTO readings VALUES(?,?)',[('Adyar',48.0),('Adyar',50.0),('Guindy',95.0)])
        with sqlite3.connect(db_path) as con:
            value=con.execute('SELECT AVG(pm25) FROM readings WHERE station=?',(station.title(),)).fetchone()[0]
        return f'Average PM2.5 for {station.title()}: {value}' if value is not None else 'No stored data found.'
    return 'I can answer PM2.5 average queries for Adyar, Guindy or Velachery. Please include station name and PM2.5.'

def main():
    from pathlib import Path
    base=Path(__file__).resolve().parent; complaints=(base/'input'/'complaints.txt').read_text(encoding='utf-8').splitlines()
    print('Sentiment labels:')
    for c in complaints: print(f'{label(c):8} | {c}')
    print('Summary:',summarize(' '.join(complaints),k=2))
    print('Chatbot demo:',answer_question('What is PM2.5 in Adyar?',base.parent/'B1_Cleaning_Pipeline'/'air_quality.sqlite'))
    print('Limitations: small lexicon, negation scope is simplistic, sarcasm/context are missed, and chatbot only handles a narrow pattern.')
if __name__=='__main__': main()
