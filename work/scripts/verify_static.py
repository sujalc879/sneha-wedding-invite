#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime, timedelta, timezone
import json
import re

ROOT=Path(__file__).resolve().parents[2]
html=(ROOT/'public/index.html').read_text()
details=(ROOT/'DETAILS.md').read_text()
dna=(ROOT/'work/STYLE_DNA.md').read_text()
checks=[]


def check(name,condition,detail=''):
    checks.append({'name':name,'status':'PASS' if condition else 'FAIL','detail':detail})
    print(('PASS' if condition else 'FAIL')+': '+name)


def table_rows(section):
    text=details.split(section,1)[1].split('\n## ',1)[0]
    return [[cell.strip() for cell in line.strip().strip('|').split('|')] for line in text.splitlines() if line.startswith('|')][2:]


main=table_rows('## Wedding details')
functions=table_rows('## Functions')
values=[cell for row in main for cell in row[1:] if cell]+[cell for row in functions for cell in row if cell]
missing=[value for value in values if value not in html]
check('All populated DETAILS.md data cells appear verbatim in index.html',not missing,str(missing))
check('Complete exact DETAILS.md snapshot in first HTML comment',details in html)
forbidden=dna.split('FORBIDDEN STRINGS',1)[1].strip().splitlines()
leaks=[]
for file in (ROOT/'public').iterdir():
    if file.suffix=='.html':
        text=file.read_text().casefold()
        leaks.extend(value for value in forbidden if value.casefold() in text)
check('No personal text from the reference in public/',not leaks,str(leaks))
check('No prohibited unfinished-content strings',not re.search(r'lorem|\bTODO\b|Your Name|\.\.\.',html,re.I))
check('No external JavaScript or raw HTML insertion',not re.search(r'<script[^>]+src\s*=|\.innerHTML\s*=',html,re.I))
check('STYLE_DNA.md is at most 25 lines',len(dna.splitlines())<=25,str(len(dna.splitlines())))


class Parser(HTMLParser):
    def __init__(self):
        super().__init__();self.urls=[];self.styles=[];self.ids=[];self.uses=[];self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.append(a['id'])
        for key in ['src','href']:
            if a.get(key):self.urls.append((tag,a[key]))
        if tag=='link' and a.get('rel')=='stylesheet':self.styles.append(a.get('href',''))
        if tag=='use':self.uses.append(a.get('href','').lstrip('#'))
        if tag=='img':self.images.append(a)


parser=Parser();parser.feed(html)
allowed=['https://fonts.googleapis.com','https://fonts.gstatic.com','https://www.google.com/maps/search/?api=1&query=Rambagh+Palace+Jaipur','http://www.w3.org/2000/svg']
bad=[url for tag,url in parser.urls if url.startswith(('http:','https:')) and not any(url.startswith(prefix) for prefix in allowed)]
check('External resources/links limited to Google Fonts and the exact sample Maps link',not bad,str(bad))
check('Only Google Fonts stylesheet',len(parser.styles)==1 and parser.styles[0].startswith('https://fonts.googleapis.com/'))
check('Unique IDs and all literal SVG references resolve',len(parser.ids)==len(set(parser.ids)) and set(parser.uses).issubset(set(parser.ids)))
check('Noindex, fixed-offset countdown, title and Open Graph title/description present',all(value in html for value in ['noindex,nofollow','2027-02-14T18:30:00+05:30','<title>','property="og:title"','property="og:description"']))
check('Unknown Site URL has no empty or fabricated og:url / og:image',not re.search(r'property="og:(?:url|image)"',html))
files=list((ROOT/'public').iterdir());check('Only permitted public files',all(re.fullmatch(r'index\.html|photo[1-5]\.jpg|og\.jpg',p.name) for p in files))
total=sum(p.stat().st_size for p in files);check('Size budgets: HTML under 250KB and public under 2.5MB',(ROOT/'public/index.html').stat().st_size<250_000 and total<2_500_000,str(total)+' bytes total')
palette=set(re.findall(r'#[0-9a-fA-F]{6}\b',dna));used=set(re.findall(r'#[0-9a-fA-F]{6}\b',html));check('All literal hex colours use the sampled palette',used<=palette,str(used-palette))

rows=[]
data=dict(main)
for item,value in main:
    display=value or '— omitted —'
    flag='Temporary fictional demo; replace before sharing.' if item in ['Bride','Groom','Main date','Main time','Venue'] else ''
    if item=='RSVP number':flag='Optional, blank: no WhatsApp button or invented contact.'
    if item=='Site URL':flag='Unknown: og:url and og:image omitted.'
    if 'outfit' in item:flag='Fictional SVG portrait; real likeness awaits supplied photos.'
    rows.append([item,value or 'EMPTY',display,'YES' if not value or value in html else 'NO',flag])
rows.append(['Countdown timestamp','14 February 2027; 6:30 PM; +05:30','2027-02-14T18:30:00+05:30','YES','Technical value only; display remains exact.'])
rows.append(['RSVP wa.me href','EMPTY','— omitted —','YES','No personal telephone number fabricated.'])
main_weekday=datetime.strptime(data['Main date'],'%d %B %Y').strftime('%A');check('Main weekday matches the stated day',main_weekday==data['Main day'],main_weekday)
rows.append(['Main computed weekday',data['Main day'],main_weekday,'YES' if main_weekday==data['Main day'] else 'FLAG','Computed with Python; never rewritten.'])
for index,event in enumerate(functions,1):
    name,date,day,time,venue,dress,maps=event
    for label,typed,used in [('Name',name,name),('Date',date,date),('Day',day,day),('Time',time,time),('Venue',venue,venue or data['Venue']),('Dress code',dress,dress or data['Dress code']),('Maps link',maps,maps or (data['Maps link'] if not venue else ''))]:
        flag='Inherited main value.' if not typed and used else ''
        if label=='Maps link' and venue and not maps:flag='Own venue has no directions link.'
        rows.append([f'Function {index} {label}',typed or 'EMPTY',used or '— omitted —','YES',flag])
    weekday=datetime.strptime(date,'%d %B %Y').strftime('%A');check(f'{name} computed weekday matches {day}',weekday==day,weekday)
    rows.append([f'Function {index} computed weekday',day,weekday,'YES' if weekday==day else 'FLAG','Computed with Python; never rewritten.'])
    if name=='Wedding':check('Wedding function agrees with main date and time',date==data['Main date'] and time==data['Main time'])
rows.extend([
 ['Calendar end-time rule','Start only supplied','Start + 3 hours','DERIVED','Hidden constant CONFIG.calendarDurationHours = 3; end times never displayed.'],
 ['Real photos','None supplied','Three original inline SVG scenes','APPROVED','User explicitly approved temporary illustrations. Photo EXIF, likeness and crop checks are deferred.'],
 ['OG photograph','None supplied','Omitted','APPROVED','No real photo or published URL yet.'],
])
def escape(value):return str(value).replace('|','\\|').replace('\n',' ')
report='# Data checklist\n\nAll data below belongs to a user-approved temporary fictional demo. Source: DETAILS.md.\n\n| Item | As typed in DETAILS.md | As used in index.html | Match | Flag |\n|---|---|---|---|---|\n'
report+='\n'.join('| '+' | '.join(escape(value) for value in row)+' |' for row in rows)+'\n'
(ROOT/'work/CHECKLIST.md').write_text(report)
check('All populated source data cells also appear verbatim in CHECKLIST.md',all(value in report for value in values))
result={'status':'PASS' if all(item['status']=='PASS' for item in checks) else 'FAIL','checks':checks,'totalPublicBytes':total,'deferred':['Real photo dimensions/EXIF and face crops: user-approved SVG demo has no photos.']}
(ROOT/'work/STATIC_RESULTS.json').write_text(json.dumps(result,indent=2))
if result['status']!='PASS':raise SystemExit(1)
