#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime, timedelta, timezone
import json
import re
import subprocess

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
data=dict(main)
js="const fs=require('fs'),vm=require('vm');const html=fs.readFileSync('public/index.html','utf8');const script=html.match(/<script>([\\s\\S]*?)<\\/script>/)[1];const start=script.indexOf('const CONFIG'),end=script.indexOf('const $',start);process.stdout.write(JSON.stringify(vm.runInNewContext(script.slice(start,end)+';CONFIG')));"
config=json.loads(subprocess.check_output(['node','-e',js],cwd=ROOT,text=True))
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
allowed=['https://fonts.googleapis.com','https://fonts.gstatic.com','http://www.w3.org/2000/svg',data['Maps link']]+[row[6] for row in functions if row[6]]
bad=[url for tag,url in parser.urls if url.startswith(('http:','https:')) and not any(url.startswith(prefix) for prefix in allowed)]
check('External resources/links limited to Google Fonts and exact recorded Maps links',not bad,str(bad))
check('Only Google Fonts stylesheet',len(parser.styles)==1 and parser.styles[0].startswith('https://fonts.googleapis.com/'))
check('Unique IDs and all literal SVG references resolve',len(parser.ids)==len(set(parser.ids)) and set(parser.uses).issubset(set(parser.ids)))
check('Noindex, fixed-offset countdown, title and Open Graph title/description present',all(value in html for value in ['noindex,nofollow',config['countdownTimestamp'],'<title>','property="og:title"','property="og:description"']))
check('Unknown Site URL has no empty or fabricated og:url / og:image',not re.search(r'property="og:(?:url|image)"',html))
files=list((ROOT/'public').iterdir());check('Only permitted public files',all(re.fullmatch(r'index\.html|photo[1-5]\.jpg|og\.jpg',p.name) for p in files))
total=sum(p.stat().st_size for p in files);check('Size budgets: HTML under 250KB and public under 2.5MB',(ROOT/'public/index.html').stat().st_size<250_000 and total<2_500_000,str(total)+' bytes total')
palette=set(re.findall(r'#[0-9a-fA-F]{6}\b',dna));used=set(re.findall(r'#[0-9a-fA-F]{6}\b',html));check('All literal hex colours use the sampled palette',used<=palette,str(used-palette))

def parse_time(value):
    match=re.fullmatch(r'(\d{1,2})[.:](\d{2})\s*(am|pm)\.?',value,re.I)
    if not match:raise ValueError('Unsupported exact time: '+value)
    return int(match[1])%12+(12 if match[3].lower()=='pm' else 0),int(match[2])

def parse_date(value,year):
    value=re.sub(r'(\d+)(st|nd|rd|th)\b',r'\1',value)
    for fmt in ['%d %B %Y','%d %b %Y']:
        try:return datetime.strptime(value,fmt)
        except ValueError:pass
    return datetime.strptime(value+' '+str(year),'%d %b %Y')

offset=data['Time zone offset'];sign=1 if offset[0]=='+' else -1
fixed_zone=timezone(sign*timedelta(hours=int(offset[1:3]),minutes=int(offset[4:6])))
main_date=parse_date(data['Main date'],2027);hour,minute=parse_time(data['Main time'])
target=main_date.replace(hour=hour,minute=minute,tzinfo=fixed_zone).isoformat(timespec='seconds')
check('Main timestamp independently derived from exact displayed date/time',config['countdownTimestamp']==target,target)
mapping={'Bride':'bride','Groom':'groom','Name order':'nameOrder','Initials':'initials','Main date':'date','Main time':'time','Venue':'venue','Address':'address','Dress code':'dressCode','Maps link':'maps'}
check('CONFIG matches exact source fields',all(config[key]==data[item] for item,key in mapping.items()))
check('Exactly the source functions, in source order',len(config['functions'])==len(functions) and all([event.get(key,'') for key in ['name','date','day','time','venue','dressCode','maps']]==row for event,row in zip(config['functions'],functions)))
rows=[]
for item,value in main:
    display=value or '— omitted —'
    flag='Copied exactly from screenshot or confirmed user reply.' if item in ['Bride','Groom','Main date','Main time','Venue','Address'] else ''
    if item=='Initials':flag='Retained existing derived initials; not supplied in screenshot.'
    if item=='Maps link':flag='Derived exact-address search URL; verify selected place.'
    if item=='RSVP number':flag='Optional, blank: no WhatsApp button or invented contact.'
    if item=='Site URL':flag='Unknown: og:url and og:image omitted.'
    if 'outfit' in item:flag='Fictional SVG portrait; real likeness awaits supplied photos.'
    rows.append([item,value or 'EMPTY',display,'YES' if not value or value in html else 'NO',flag])
rows.append(['Countdown timestamp',data['Main date']+'; '+data['Main time']+'; '+offset,target,'YES','Technical value only; display remains exact.'])
rows.append(['RSVP wa.me href','EMPTY','— omitted —','YES','No personal telephone number fabricated.'])
main_weekday=datetime.strptime(data['Main date'],'%d %B %Y').strftime('%A');check('Main weekday matches the stated day',main_weekday==data['Main day'],main_weekday)
rows.append(['Main computed weekday',data['Main day'],main_weekday,'YES' if main_weekday==data['Main day'] else 'FLAG','Computed with Python; never rewritten.'])
computed_weekdays=[]
for index,event in enumerate(functions,1):
    name,date,day,time,venue,dress,maps=event
    for label,typed,used in [('Name',name,name),('Date',date,date),('Day',day,day),('Time',time,time),('Venue',venue,venue or data['Venue']),('Dress code',dress,dress or data['Dress code']),('Maps link',maps,maps or (data['Maps link'] if not venue else ''))]:
        flag='Inherited main value.' if not typed and used else ''
        if label=='Maps link' and venue and not maps:flag='Own venue has no directions link.'
        rows.append([f'Function {index} {label}',typed or 'EMPTY',used or '— omitted —','YES',flag])
    internal=datetime.fromisoformat(config['functions'][index-1]['iso']);expected_date=parse_date(date,internal.year);hour,minute=parse_time(time)
    expected=expected_date.replace(hour=hour,minute=minute,tzinfo=fixed_zone)
    check(f'{name} internal date/time matches exact displayed values',internal==expected)
    weekday=expected.strftime('%A');computed_weekdays.append(weekday)
    if day:check(f'{name} computed weekday matches {day}',weekday==day,weekday)
    rows.append([f'Function {index} computed weekday',day or 'Not supplied',weekday,'COMPUTED','Unprovided weekdays are not added to the page.'])
    if name=='Wedding':check('Wedding function agrees with main date and time',date==data['Main date'] and time==data['Main time'])
rows.extend([
 ['Calendar end-time rule','Start only supplied','Start + 3 hours','DERIVED','Hidden constant CONFIG.calendarDurationHours = 3; end times never displayed.'],
 ['Event order','Haldi; Sangeet; Wedding','Haldi; Sangeet; Wedding','YES','Source order retained although Sangeet starts earlier than Haldi.'],
 ['Haldi year','31st Dec','2026 internally; display unchanged','DERIVED','Year derived from the confirmed wedding and Sangeet dates.'],
 ['Maps URLs','Supplied addresses','Address-search links','DERIVED','Not supplied place-pin links; verify the selected places.'],
 ['Real photos','None supplied','Three original inline SVG scenes','APPROVED','Temporary illustrations previously approved. Photo EXIF, likeness and crop checks are deferred.'],
 ['OG photograph','None supplied','Omitted','APPROVED','No real photo or published URL yet.'],
])
def escape(value):return str(value).replace('|','\\|').replace('\n',' ')
report='# Data checklist\n\nSource: DETAILS.md, supplied screenshot and user replies on 28 November 2026. Unconfirmed demo details were removed with approval.\n\n| Item | As typed in DETAILS.md | As used in index.html | Match | Flag |\n|---|---|---|---|---|\n'
report+='\n'.join('| '+' | '.join(escape(value) for value in row)+' |' for row in rows)+'\n'
(ROOT/'work/CHECKLIST.md').write_text(report)
check('All populated source data cells also appear verbatim in CHECKLIST.md',all(value in report for value in values))
result={'status':'PASS' if all(item['status']=='PASS' for item in checks) else 'FAIL','checks':checks,'totalPublicBytes':total,'timestamp':target,'computedWeekdays':computed_weekdays,'deferred':['Real photo dimensions/EXIF and face crops await supplied photos.','Maps search links are derived from exact addresses, not supplied place-pin URLs.']}
(ROOT/'work/STATIC_RESULTS.json').write_text(json.dumps(result,indent=2))
if result['status']!='PASS':raise SystemExit(1)
