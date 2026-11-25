from pathlib import Path
import html,re,unicodedata,json
from urllib.parse import quote
root=Path(__file__).resolve().parents[2]
batch="2026-11-25-elite"
E=lambda s:html.escape(str(s),quote=True)
rows=[x.split("|") for x in (root/".github/alik6-elite-1125.txt").read_text(encoding="utf8").strip().splitlines()]
assert len(rows)==65
def slug(s):return re.sub("[^a-z0-9]+","-",unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode().lower()).strip("-")
imgs={"cafe":["photo-1501339847302-ac426a4a7cbb","photo-1554118811-1e0d58224f24","photo-1442512595331-e89e73853f31"],"sweet":["photo-1578985545062-69928b1d9587","photo-1488477181946-6428a0291777","photo-1563729784474-d77dbb933a9e"],"food":["photo-1517248135467-4c7edcad34c4","photo-1543353071-873f17a7a088","photo-1552566626-52f8b828add9"]}
palettes=[("#f0e7db","#fffaf3","#352820","#9b6240"),("#e7ebe4","#f8faf6","#29362b","#57765e"),("#f3e8e8","#fff8f5","#382c30","#a96779"),("#ede7dc","#f8f5ee","#2d2a24","#927348"),("#e5e9ea","#f7f9fa","#27373d","#537d88")]
features={"akce":"Akce a oslavy","objednavky":"Objednávky","rozvoz":"Rozvoz","rezervace":"Rezervace","poukazy":"Dárkové poukazy","pobyty":"Pobyty"}
manifest=[]
for id,name,city,email,phone,sector in rows:
    low=sector.lower()
    group="sweet" if re.search("cukrář|cukrár|dort",low) else "cafe" if re.search("kavár|coffee|café",low) else "food"
    fs=[key for key,pattern in [("akce","svat|oslav|akce|catering|raut|sál|hostin|seminář|event|koncert|workshop|kvíz|skupin"),("rozvoz","rozvoz"),("objednavky","dort|cukrář|sezonní|předobjednáv"),("pobyty","ubytování|pobyt"),("poukazy","poukaz")] if re.search(pattern,low)]
    if group=="cafe" or id=="070":fs.insert(0,"rezervace")
    fs=list(dict.fromkeys(fs)) or ["rezervace"]
    folder=slug(name)+"-"+id
    base="/"+batch+"/"+folder+"/"
    pages=[("","Úvod"),("nabidka","Nabídka"),("o-nas","O nás")]+[(f,features[f]) for f in fs]+[("kontakt","Kontakt")]
    bg,paper,ink,accent=palettes[int(id)%5]
    services=[s.strip() for s in sector.split(",") if s.strip()]
    title=("Dvě pobočky, jeden přehled zážitků." if id=="070" else "Sladké chvíle na objednávku." if group=="sweet" else "Káva a chvíle, které patří vám." if group=="cafe" else "Dobré jídlo. Výjimečné příležitosti." if "akce" in fs else "Oběd jednoduše a s chutí." if "rozvoz" in fs else "Pro chvíle u společného stolu.")
    def link(s):return base+(s+"/" if s else "")
    def btn(s,t):return f'<a class="button" href="{link(s)}"><span>{E(t)}</span><span>↗</span></a>'
    def pic(i,c="",w=1200):return f'<img class="{c}" src="https://images.unsplash.com/{imgs[group][(int(id)+i)%3]}?auto=format&amp;fit=crop&amp;w={w}&amp;q=83" alt="Ilustrační fotografie" loading="{"eager" if i==0 else "lazy"}">'
    def nav(active):return "".join(f'<a {"aria-current=page" if s==active else ""} href="{link(s)}">{E(l)}</a>' for s,l in pages)
    def sub(t,d):return f'<section class="subhero"><div class="shell"><span class="overline">{E(name+" · "+city)}</span><h1>{E(t)}</h1><p>{E(d)}</p></div></section>'
    def cards(items):return '<div class="service-grid">'+''.join(f'<a class="service-card {"is-featured" if i==0 else ""}" href="{link(s)}"><span class="card-top"><em>{i+1:02}</em><span>↗</span></span><h3>{E(t)}</h3><p>Podrobnosti a dostupnost ověřte přímo.</p></a>' for i,(s,t) in enumerate(items))+'</div>'
    def section(t,body):return f'<section class="section services-section"><div class="shell"><div class="section-title"><div><span class="overline">{E(name)}</span><h2>{E(t)}</h2></div></div>{body}</div></section>'
    def about():return f'<section class="section"><div class="shell editorial-grid"><div class="editorial-photos">{pic(1,"image-first")}{pic(2,"image-second",700)}<div class="image-note">ILUSTRAČNÍ FOTOGRAFIE</div></div><div class="editorial-copy"><span class="overline">{E(city)}</span><h2>{E(name)}</h2><p>{E(sector)}.</p><p>Aktuální nabídku a podmínky vám potvrdí přímo provozovna.</p>{btn("kontakt","Domluvit se")}</div></div></section>'
    def form(t,s):
        fields=""
        if id in ("070","005"):
            opts=["Ostrava","Olomouc"] if id=="070" else ["Štěpánovice","České Budějovice"]
            fields+='<label>Pobočka</label><select name="Pobočka">'+''.join(f'<option>{E(x)}</option>' for x in opts)+'</select>'
        if s in fs:fields+='<label>Požadovaný termín</label><input type="date" name="Termín" required><label>Počet osob / kusů</label><input type="number" name="Počet" min="1" required>'
        if s=="akce":fields+='<label>Typ akce a orientační rozpočet</label><input name="Typ akce a rozpočet">'
        if s=="rozvoz":fields+='<label>Adresa rozvozu / vyzvednutí</label><input name="Adresa">'
        return f'<div class="form-panel"><h2>{E(t)}</h2><p>Formulář připraví zprávu ve vaší e-mailové aplikaci. Nejde o potvrzenou rezervaci.</p><form data-email="{E(email)}" data-subject="{E(t+" – "+name)}">{fields}<label>Jméno</label><input name="Jméno" required><label>Kontakt</label><input name="Kontakt" required><label>Podrobnosti</label><textarea name="Podrobnosti" rows="4"></textarea><button class="button">Připravit e-mail ↗</button><p class="form-note">Údaje se neukládají. Zprávu odešlete sami.</p></form></div>'
    def contact(t,s):return sub(t,sector)+f'<section class="section"><div class="shell contact-grid"><div class="contact-info"><span class="overline">{E(city)}</span><h2>{E(name)}</h2><div class="contact-point"><span>ZAVOLEJTE</span><a href="tel:{E(phone)}">{E(phone)}</a></div><div class="contact-point"><span>NAPIŠTE</span><a href="mailto:{E(email)}">{E(email)}</a></div><a class="text-cta" href="https://www.google.com/maps/search/?api=1&amp;query={quote(name+" "+city)}">Najít na mapě ↗</a></div>{form(t,s)}</div></section>'
    hero=f'<section class="hero full"><div class="shell hero-grid"><div class="hero-copy"><div class="hero-index"><span class="dot"></span>{E(city)}</div><p class="hero-pre">{E(name)}</p><h1>{E(title)}</h1><p class="hero-description">{E(sector)} — {E(city)}.</p><div class="hero-actions">{btn(fs[0],features[fs[0]])}<a class="subtle-link" href="{link("nabidka")}">Prohlédnout nabídku ↘</a></div></div><div class="hero-visual">{pic(0,"cover-photo",1600)}<div class="hero-caption"><strong>{E(city)}</strong><span>Ilustrační fotografie</span></div></div></div><div class="hero-edge"><span>{E(name)}</span><span>DESIGN STUDY / DIGITORY</span></div></section>'
    for s,l in pages:
        body=hero+section("Na co se můžete těšit.",cards([("nabidka",x) for x in services]))+section("Naplánujte si návštěvu.",cards([(f,features[f]) for f in fs]))+about() if s=="" else sub("Naše nabídka",sector)+section("Služby",cards([("kontakt",x) for x in services])+"<p>Aktuální ceny, nabídku a dostupnost ověřte u provozovny.</p>") if s=="nabidka" else sub(name,sector)+about() if s=="o-nas" else contact(l,s)
        doc=f'<!doctype html><html lang="cs"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{E(l+" | "+name)}</title><link rel="stylesheet" href="/assets/alik-v4.css"><link rel="stylesheet" href="/assets/alik-elite-1125.css"><style>:root{{--bg:{bg};--paper:{paper};--text:{ink};--muted:#776b63;--line:#ccc3b8;--accent:{accent};--ink:{ink};--accentText:white}}</style><script defer src="/assets/alik-v4.js"></script><script defer src="/assets/alik-elite-1125.js"></script></head><body data-genre="cafe"><div class="mockline"><span>Digitory / webový koncept</span><span>Neoficiální návrh · 2026</span></div><header class="header"><div class="shell nav-wrap"><a class="identity" href="{base}"><span class="identity-mark">{E(name[0])}</span><span class="identity-name">{E(name)}<small>{E(city)}</small></span></a><button class="menu-toggle" aria-label="Otevřít navigaci" aria-controls="mainmenu" aria-expanded="false">☰</button><nav class="mainmenu" id="mainmenu">{nav(s)}</nav></div></header><main id="main">{body}</main><footer class="footer"><div class="shell footer-top"><div><div class="footer-super">{E(name)}</div><p>{E(sector)} · {E(city)}</p></div><div><strong>Prozkoumat</strong>{nav(s)}</div><div><strong>Kontakt</strong><a href="tel:{E(phone)}">{E(phone)}</a><a href="mailto:{E(email)}">{E(email)}</a></div></div><div class="shell footer-fine"><span>Neoficiální koncept Digitory, nikoli oficiální web firmy.</span><span>Fotografie jsou ilustrační. Formuláře pouze připravují e-mail.</span></div></footer></body></html>'
        path=root/batch/folder/s/"index.html";path.parent.mkdir(parents=True,exist_ok=True);path.write_text(doc,encoding="utf8")
    manifest.append(dict(name=name,id=id,slug=folder,pages=[s for s,l in pages],url="https://navrhy.digitory.cz"+base))
(root/"assets/alik-elite-1125.css").write_text(".hero.full .hero-copy{max-width:850px}.hero.full .hero-visual img{filter:brightness(.44)}.hero.full h1{font-size:clamp(65px,8vw,116px);overflow-wrap:break-word}.mainmenu{gap:16px}.mainmenu a{white-space:normal}.identity-name{max-width:245px}.form-panel select{width:100%;padding:16px;background:var(--bg);color:var(--text);border:1px solid var(--line)}.contact-point a{overflow-wrap:anywhere}@media(max-width:760px){.hero.full h1{font-size:clamp(50px,12vw,82px)}.hero.full .hero-copy{padding:95px 0 160px}.mainmenu{gap:0}}",encoding="utf8")
(root/"assets/alik-elite-1125.js").write_text("document.querySelectorAll('form[data-email]').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();if(!f.reportValidity())return;location.href='mailto:'+f.dataset.email+'?subject='+encodeURIComponent(f.dataset.subject)+'&body='+encodeURIComponent([...new FormData(f)].map(([k,v])=>k+': '+v).join('\\n'))}));",encoding="utf8")
(root/batch/"index.html").write_text('<!doctype html><html lang="cs"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><meta name="robots" content="noindex,nofollow"><title>Alík 6.0</title><style>body{font:16px/1.6 system-ui;max-width:900px;margin:45px auto;padding:20px}li{padding:7px;border-bottom:1px solid #ddd}</style><h1>Alík 6.0 — 65 návrhů</h1><ol>'+''.join(f'<li><a href="{E(x["url"])}">{E(x["name"])}</a></li>' for x in manifest)+'</ol></html>',encoding="utf8")
(root/".github/alik6-elite-1125-result.json").write_text(json.dumps(manifest,ensure_ascii=False),encoding="utf8")
print("BUILT",len(manifest),sum(len(x["pages"]) for x in manifest))
