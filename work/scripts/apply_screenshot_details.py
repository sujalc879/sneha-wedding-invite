from pathlib import Path
from html import escape
import json
import re

ROOT=Path(__file__).resolve().parents[2]
source=json.loads((ROOT/'work/CONFIRMED_DETAILS.json').read_text())
v=source['values'];events=source['functions']
p=ROOT/'public/index.html';s=p.read_text()

def patch(old,new):
    global s
    if old not in s:raise ValueError('Expected source fragment is absent: '+old[:100])
    s=s.replace(old,new)

bride=escape(v['Bride']);groom=escape(v['Groom']);venue=escape(v['Venue']);address=escape(v['Address'])
names=bride+' &amp; '+groom
old_map='https://www.google.com/maps/search/?api=1&amp;query=Rambagh+Palace+Jaipur'
new_map=escape(v['Maps link'],quote=True)
s=re.sub(r'<!--\n===== DETAILS.md[\s\S]*?-->',lambda _: '<!--\n===== DETAILS.md — EXACT CONTENT =====\n'+(ROOT/'DETAILS.md').read_text()+'\n-->',s,count=1)
patch('<title>sneha &amp; sanghpal | Wedding Invitation</title>','<title>'+names+' | Wedding Invitation</title>')
patch('1 January 2027 · Rambagh Palace. Fictional wedding invitation demonstration.','1 January 2027 · '+venue)
patch('sneha &amp; sanghpal · Wedding Invitation',names+' · Wedding Invitation')
patch('1 January 2027 · Rambagh Palace','1 January 2027 · '+venue)
patch('<span class="envelope-card-names">sneha &amp; sanghpal</span>','<span class="envelope-card-names"><span>'+bride+'</span><span> &amp; </span><span>'+groom+'</span></span>')
patch('<span>Rambagh Palace</span></p>','<span>'+venue+'</span></p>')
patch('aria-label="sneha and sanghpal, back to top"','aria-label="'+bride+' and '+groom+', back to top"')
patch('<span class="demo-label">Fictional invitation</span>','<span class="demo-label">'+escape(v['Demo label'])+'</span>')
patch('<p class="blessing">Shree Ganeshaya Namah</p><p class="hero-subtitle">Wedding Invitation</p><p class="hero-intro">Together with our families</p>','<p class="hero-subtitle">Wedding Invitation</p>')
patch('<h1 class="names" id="couple-names"><span>sneha</span><span class="amp">&amp;</span><span>sanghpal</span></h1>','<h1 class="names" id="couple-names"><span class="person-name">'+bride+'</span><span class="amp">&amp;</span><span class="person-name">'+groom+'</span></h1>')
patch('<p class="hero-venue">Rambagh Palace · Jaipur</p>','<p class="hero-venue">'+venue+'</p>')
patch('id="couple-title">Two hearts, one beginning.</h2>','id="couple-title">The couple</h2>')
patch('<h3>sneha</h3><p>A little sunshine, a lot of heart.</p>','<h3>'+bride+'</h3>')
patch('<h3>sanghpal</h3><p>A steady hand, a joyful soul.</p>','<h3>'+groom+'</h3>')
patch('Illustrated portraits · Fictional invitation','Illustrated portraits')
patch('<p class="sr-only">Wedding date: 1 January 2027. Wedding time is pending.</p><p class="countdown-foot">Friday · 1 January 2027</p>','<p class="sr-only">Countdown to 1 January 2027 at 1:35 pm, fixed UTC offset +05:30.</p><p class="countdown-foot">Friday · 1 January 2027 · 1:35 pm</p>')
patch('<p class="subtitle reveal">A wedding, in four beautiful moments.</p>','<p class="subtitle reveal">Wedding functions</p>')
fact_start=s.index('        <div class="venue-facts">')
fact_end=s.index('\n        <div class="venue-layout">',fact_start)
facts=[('Date',v['Main date']),('Time',v['Main time']),('Venue',v['Venue'])]
s=s[:fact_start]+'        <div class="venue-facts">'+''.join('<div class="venue-fact reveal"><span class="fact-label">'+key+'</span><span class="fact-value">'+escape(value)+'</span></div>' for key,value in facts)+'</div>'+s[fact_end:]
patch('<h3>Rambagh Palace</h3><address>Bhawani Singh Road, Jaipur, Rajasthan 302 005</address>','<h3>'+venue+'</h3><address>'+address+'</address>')
patch(old_map,new_map)
patch('type="button" disabled aria-describedby="calendar-pending"','type="button"')
patch('<p id="calendar-pending" style="font-size:14px;margin-top:14px">Calendar download awaits the wedding time.</p>','')
patch('aria-label="Open directions to Rambagh Palace in Google Maps"','aria-label="Open directions to '+venue+' in Google Maps"')
patch('aria-label="Decorative illustrated map with roads and a pin for Rambagh Palace"','aria-label="Decorative illustrated map with roads and a pin for '+venue+'"')
patch('<strong>Rambagh Palace</strong>','<strong>'+venue+'</strong>')
patch('font-size="20">Rambagh Palace</text>','font-size="22">'+venue+'</text>')
patch('<p class="footer-message reveal">Your presence is our most beautiful gift.</p>','')
patch('<p class="footer-names reveal">sneha &amp; sanghpal</p>','<p class="footer-names reveal"><span>'+bride+'</span><span class="footer-amp"> &amp; </span><span>'+groom+'</span></p>')
patch('<p>Rambagh Palace</p>','<p>'+venue+'</p>')
patch('<p class="families reveal">With love, our families</p>','')
patch('Fictional wedding details. Original illustrations stand in for real photos.',escape(v['Demo notice']))

config={'bride':v['Bride'],'groom':v['Groom'],'nameOrder':v['Name order'],'initials':v['Initials'],'blessing':v['Blessing'],'subtitle':v['Hero subtitle'],'date':v['Main date'],'day':v['Main day'],'time':v['Main time'],'offset':v['Time zone offset'],'countdownTimestamp':source['countdownTimestamp'],'venue':v['Venue'],'address':v['Address'],'dressCode':v['Dress code'],'maps':v['Maps link'],'rsvp':'','siteUrl':'','calendarDurationHours':3}
start=s.index('    bride:',s.index('  const CONFIG = {'))
end=s.index('    // Replace illustration entries',start)
serialized=json.dumps(config,ensure_ascii=False,indent=4)[2:-2]
serialized+='\n    ,"functions":'+json.dumps(events,ensure_ascii=False,indent=4)+',\n'
s=s[:start]+serialized+s[end:]
old="function renderEvents(){CONFIG.functions.forEach((event,index)=>{const li=element('li','event reveal');li.style.setProperty('--delay',(index%2)*90+'ms');li.append(element('span','event-number',String(index+1).padStart(2,'0')));const top=element('div','event-top');top.append(element('h3','',event.name),svgUse(event.icon,'event-icon'));li.append(top,element('p','event-date',event.date));const when=element('p','event-day-time');when.append(element('span','',event.day),element('span','',event.time));li.append(when,element('p','event-venue',event.venue||CONFIG.venue),element('p','event-dress',event.dressCode||CONFIG.dressCode));const link=eventMap(event);if(link){const a=element('a','line-link','Get Directions');a.href=link;a.target='_blank';a.rel='noopener noreferrer';const icon=svgUse('icon-pin');icon.setAttribute('viewBox','0 0 24 24');a.prepend(icon);li.append(a);}$('events-list').append(li);});}"
new="function renderEvents(){CONFIG.functions.forEach((event,index)=>{const li=element('li','event reveal');li.style.setProperty('--delay',(index%2)*90+'ms');li.append(element('span','event-number',String(index+1).padStart(2,'0')));const top=element('div','event-top');top.append(element('h3','',event.name),svgUse(event.icon,'event-icon'));li.append(top);if(event.date)li.append(element('p','event-date',event.date));if(event.day||event.time){const when=element('p','event-day-time');if(event.day)when.append(element('span','',event.day));if(event.time)when.append(element('span','',event.time));li.append(when);}const venue=event.venue||CONFIG.venue,dress=event.dressCode||CONFIG.dressCode;if(venue)li.append(element('p','event-venue',venue));if(dress)li.append(element('p','event-dress',dress));const link=eventMap(event);if(link){const a=element('a','line-link','Get Directions');a.href=link;a.target='_blank';a.rel='noopener noreferrer';const icon=svgUse('icon-pin');icon.setAttribute('viewBox','0 0 24 24');a.prepend(icon);li.append(a);}$('events-list').append(li);});}"
patch(old,new)
patch("const location=venue+(event.venue?'':', '+CONFIG.address);","const location=event.venue||CONFIG.address||CONFIG.venue;")
patch("anchor.download='sneha-and-sanghpal.ics'","anchor.download='Sneha-Parmeshwar-Landge-and-Sanghpal-Ramdas-sawale.ics'")

css='''    /* ===== FULL NAMES AND CONFIRMED DETAILS ===== */
    .hero-copy{width:100%;min-width:0;max-width:860px}
    .names{font-size:clamp(52px,7.5vw,108px);letter-spacing:-.035em;line-height:1.02;max-width:100%}
    .names .person-name{display:block;max-width:100%;white-space:normal}
    .hero-arch{width:min(1000px,calc(100% - 36px))}
    .envelope-card-names{font-size:clamp(20px,2.8vw,32px);line-height:1.05;max-width:95%}
    .envelope-card-names span{display:block}.envelope-card-names span:nth-child(2){font-size:18px;line-height:1}
    .opening-meta{max-width:100%;row-gap:8px}
    .portrait-card h3{font-size:38px;max-width:330px;margin-inline:auto;line-height:1.1}
    .venue-layout>*,.venue-fact{min-width:0}
    .venue-facts{grid-template-columns:repeat(3,minmax(0,1fr))}
    .venue-fact:nth-child(3){border-left:1px solid rgba(183,157,102,.65)}
    .venue-copy h3{font-size:clamp(42px,5vw,61px);line-height:1.05}
    .footer-names{font-size:clamp(36px,4.5vw,48px);line-height:1.15;max-width:800px;margin-inline:auto}
    .footer-names span{display:block}.footer-names .footer-amp{font-size:27px;margin-block:6px}
    @media(max-width:599px){.couple-grid{grid-template-columns:1fr;gap:34px}.couple-amp{position:static;transform:none;grid-row:2;text-align:center;font-size:40px}.portrait-card{width:100%}.portrait-frame{height:330px;max-width:270px}.portrait-card h3{font-size:38px}.names .amp{font-size:34px;margin-block:11px}.venue-facts{grid-template-columns:1fr 1fr}.venue-fact:nth-child(3){grid-column:1/-1;border-left:0;border-top:1px solid rgba(183,157,102,.55);padding-top:22px}.opening-meta{max-width:290px}.hero-venue{max-width:260px;margin-inline:auto}.hero .names{margin-top:30px}}
'''
patch('  </style>',css+'  </style>')
patch('const edge=Math.max(34,w*.09);','const edge=innerWidth<600?24:Math.max(34,w*.09);')
patch('const center=Math.max(35,Math.min(document.documentElement.clientWidth-35,point.x));','const center=Math.max(innerWidth<600?24:35,Math.min(document.documentElement.clientWidth-35,point.x));')
assert 'Rambagh' not in s and 'Jaipur' not in s
assert (ROOT/'DETAILS.md').read_text() in s
next_file=ROOT/'work/index.next.html';next_file.write_text(s);next_file.replace(p)
print('Patched exact names, venues, event formats and confirmed time; HTML bytes:',p.stat().st_size)
