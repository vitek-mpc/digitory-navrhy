#!/usr/bin/env python3
"""Regenerate personalized sections against original ALIK-v4 designs.
Never fabricate booking integration, prices, real photos, named staff, or reviews.
"""
import html, json, re, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEADS = json.loads((ROOT / "assets/premium3-leads-2026-10-19.json").read_text(encoding="utf-8"))["firms"]
SPECS = json.loads((ROOT / ".github/digitory-email-alignment.json").read_text(encoding="utf-8"))["requirements"]
assert len(LEADS) == len(SPECS) == 68, (len(LEADS), len(SPECS))

LABELS = {
 "R": "Rezervace a objednání", "G": "Galerie a inspirace",
 "T": "Tým a přístup", "K": "Kurzy a workshopy",
 "W": "Dárkové poukazy", "C": "Ceník a služby",
 "M": "Nabídka a menu", "E": "Akce a spolupráce",
 "V": "Reference a ohlasy", "P": "Postupy a procedury",
 "D": "Rozvoz a objednávky", "X": "Produkty a další možnosti",
 "L": "Provozovny"
}
IMGS = {
 "beauty": ["photo-1570172619644-dfd03ed5d881","photo-1512290923902-8a9f81dc236c","photo-1616683693504-3ea7e9ad6fec"],
 "hair": ["photo-1560066984-138dadb4c035","photo-1521590832167-7bcbfaa6381f","photo-1599351431202-1e0f0137899a"],
 "wellness": ["photo-1570172619644-dfd03ed5d881","photo-1616683693504-3ea7e9ad6fec","photo-1512290923902-8a9f81dc236c"],
 "food": ["photo-1517248135467-4c7edcad34c4","photo-1552566626-52f8b828add9","photo-1543353071-873f17a7a088"],
 "cafe": ["photo-1501339847302-ac426a4a7cbb","photo-1442512595331-e89e73853f31","photo-1511920170033-f8396924c348"],
 "pet": ["photo-1517849845537-4d257902454a","photo-1583511655857-d19b40a7a54e","photo-1516734212186-a967f81ad0d7"],
 "fitness": ["photo-1534438327276-14e5300c3a48","photo-1517836357463-d25dfeac3438","photo-1518611012118-696072aa579a"],
}
CSS = r"""
<style id="mail-alignment-style">
.mail-focus{background:var(--paper);padding:105px 0;border-bottom:1px solid var(--line)}
.mail-focus-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:9%;align-items:center}
.mail-focus h2{font-size:clamp(42px,5.4vw,74px);margin:20px 0 25px}
.mail-focus p{color:var(--muted);font-size:16px;line-height:1.7}
.mail-chips{display:flex;flex-wrap:wrap;gap:8px;margin:25px 0}
.mail-chip{font-size:11px;border:1px solid var(--line);border-radius:60px;padding:7px 12px;color:var(--text);font-weight:700}
.mail-side{position:relative;height:410px}
.mail-side img{width:100%;height:100%;object-fit:cover}
.mail-side span{position:absolute;left:15px;bottom:15px;padding:10px 12px;background:#000b;color:#fff;font-size:10px;font-weight:700}
.mail-detail-header{background:var(--paper);padding:100px 0 82px}
.mail-detail-header .breadcrumb{margin-bottom:35px}
.mail-detail-header h1{font-size:clamp(53px,8vw,104px);margin:20px 0 25px;overflow-wrap:break-word}
.mail-detail-header p{font-size:18px;max-width:750px;color:var(--muted)}
.mail-subsection{padding:84px 0;border-top:1px solid var(--line)}
.mail-subsection h2{font-size:clamp(40px,5vw,68px);margin:18px 0 22px;max-width:880px}
.mail-subsection>p{font-size:15px;color:var(--muted);max-width:900px;margin-bottom:24px}
.mail-gallery{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:13px;margin-top:31px}
.mail-gallery figure{margin:0}.mail-gallery img{width:100%;height:290px;object-fit:cover}
.mail-gallery figcaption{font-size:11px;color:var(--muted);padding-top:10px}
.mail-panels{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:28px 0}
.mail-panels article{background:var(--paper);border:1px solid var(--line);min-height:145px;padding:26px}
.mail-panels article strong{display:block;font-size:18px;line-height:1.25}
.mail-panels article p{font-size:13px;color:var(--muted);margin-top:14px}
.mail-panels article small{color:var(--accent);display:block;margin-bottom:12px}
.mail-price-list{border-top:1px solid var(--line);margin:28px 0}
.mail-price-list>div{display:flex;justify-content:space-between;gap:20px;border-bottom:1px solid var(--line);padding:17px 5px}
.mail-price-list strong{white-space:nowrap;font-size:12px;color:var(--accent)}
.mail-textlink{text-decoration:underline;text-underline-offset:5px;color:var(--accent);font-size:13px;font-weight:800}
.mail-booking{display:flex;align-items:center;gap:25px;flex-wrap:wrap;margin:27px 0}
.mail-navlink{background:var(--soft);padding:10px 14px!important;border-radius:99px;font-size:11px!important}
.mail-cta-block{background:var(--bg);padding:35px;border:1px solid var(--line);margin:30px 0}
.mail-cta-block h3{font-size:30px;margin:0 0 12px}
.mail-cta-block p{color:var(--muted);margin-bottom:22px}
.mail-modules{background:var(--bg)}
@media(max-width:1230px){.mainmenu{gap:14px}.mail-navlink{padding:9px 11px!important}.identity-name{max-width:180px}}
@media(max-width:760px){.mail-focus{padding:66px 0}.mail-focus-grid{grid-template-columns:1fr}
.mail-side{height:310px;order:-1}.mail-focus h2{font-size:clamp(43px,10vw,67px)}
.mail-detail-header{padding:70px 0}.mail-detail-header h1{font-size:clamp(46px,11vw,78px)}
.mail-subsection{padding:62px 0}.mail-gallery{grid-template-columns:1fr 1fr}
.mail-gallery img{height:200px}.mail-panels{grid-template-columns:1fr}
.mail-navlink{background:transparent;padding:15px 0!important;font-size:15px!important}
.mail-price-list>div{flex-direction:column;gap:6px}}
@media(max-width:460px){.mail-gallery{grid-template-columns:1fr}.mail-gallery img{height:290px}}
</style>
"""
ARROW='<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>'
def e(x): return html.escape(str(x or ""), quote=True)
def base(p): return f"/2026-10-19-premium/{p['slug']}/"
def phone(p): return "tel:"+re.sub(r"[^+0-9]","",p["phone"] or "")
def mail(p,subject):
    return "mailto:"+p["email"]+"?subject="+urllib.parse.quote(subject)
def site_map(p):
    return p.get("map_url") if (p.get("map_url") or "").startswith("https://") else "https://www.google.com/maps/search/?api=1&query="+urllib.parse.quote(p["name"]+" "+p["city"])
def btn(p,title="Spojit se s firmou"):return f'<a class="button" href="{base(p)}kontakt/"><span>{e(title)}</span>{ARROW}</a>'
def picture(p,idx=0,w=1000):
    pics=IMGS.get(p["sector"],IMGS["beauty"])
    link=f"https://images.unsplash.com/{pics[idx%len(pics)]}?auto=format&fit=crop&w={w}&q=83"
    return f'<img src="{link}" loading="lazy" decoding="async" alt="Ilustrační fotografie zaměření firmy {e(p["name"])}">'
def panel(title,desc):
    return f'<article><strong>{e(title)}</strong><p>{e(desc)}</p></article>'
def config(p,s):
    f=s["flags"]
    if p["sector"] in ("cafe","food") or "M" in f:return ("nabidka","Naše nabídka")
    if "K" in f:return ("kurzy-a-inspirace","Kurzy a inspirace")
    if "G" in f:return ("galerie-a-nabidka","Galerie a nabídka")
    if "P" in f:return ("procedury","Procedury")
    if "C" in f:return ("cenik-a-sluzby","Ceník a služby")
    return ("vice-informaci","Více informací")
def module(p,s,k):
    focus=e(s["focus"]); who=e(p["name"])
    if k=="G":
        imgs="".join(f"<figure>{picture(p,i,850)}<figcaption>Ilustrační fotografie · místo pro skutečné portfolio</figcaption></figure>" for i in range(3))
        return f'<section class="mail-subsection" id="galerie"><span class="overline">Vizuální inspirace</span><h2>Galerie a výsledky práce</h2><p>{who} zde může představit vlastní výsledky, proměny a fotografie práce. Zatím jde pouze o jasně označené ilustrační obrázky – skutečné reference ani realizace si nevymýšlíme.</p><div class="mail-gallery">{imgs}</div></section>'
    if k=="T":
        return f'<section class="mail-subsection" id="tym"><span class="overline">Lidé za značkou</span><h2>Poznejte tým</h2><p>Samostatná část pro prezentaci jednotlivých specialistů, jejich zaměření a fotografií. Bez podkladů nevymýšlíme jména zaměstnanců.</p><div class="mail-panels">{panel("Specializace",p["industry"])}{panel("Osobní domluva","Konkrétního specialistu a vhodný termín lze ověřit přímo u provozovatele.")}</div>{btn(p,"Zeptat se na tým")}</section>'
    if k=="K":
        return f'<section class="mail-subsection" id="kurzy"><span class="overline">Možnosti vzdělávání</span><h2>Kurzy a workshopy</h2><p>Prostor pro aktuální nabídku kurzů, program výuky, kapacitu a termíny. Žádné neověřené ceny ani volná místa nejsou v tomto návrhu uváděny.</p><div class="mail-panels">{panel("Témata a zaměření",s["focus"])}{panel("Přihlášení a informace","Konkrétní možnosti účasti a termín potvrdí přímo pořadatel.")}</div>{btn(p,"Poptat kurz")}</section>'
    if k=="W":
        return f'<section class="mail-subsection" id="poukazy"><span class="overline">Dárek s osobním přesahem</span><h2>Dárkové poukazy</h2><p>Chcete darovat službu? U {who} si ověřte aktuální nabídku poukazů, hodnotu a předání. Jde o design návrhu; online platba ani elektronický nákup poukazu zatím nejsou aktivní.</p>{btn(p,"Zeptat se na poukaz")}</section>'
    if k=="C":
        rows="".join(f'<div><span>{e(x.strip())}</span><strong>Cena na dotaz</strong></div>' for x in re.split(r"[,;]",p["industry"]) if x.strip())
        return f'<section class="mail-subsection" id="cenik"><span class="overline">Ceny a podmínky</span><h2>Ceník služeb</h2><p>Přehled kategorií je připravený pro skutečné ceny, ale v podkladech nejsou bezpečně ověřené. Místo vymyšlených částek uvádíme cenu na dotaz.</p><div class="mail-price-list">{rows}</div>{btn(p,"Ověřit cenu")}</section>'
    if k=="M":
        cards="".join(panel(x.strip(),"Aktuální položky, cenu a dostupnost prosím ověřte u provozovny.") for x in re.split(r"[,;]",p["industry"]) if x.strip())
        return f'<section class="mail-subsection" id="menu"><span class="overline">Co je v nabídce</span><h2>Nabídka a menu</h2><p>{focus}. Zatím jde o návrh přehledu jídel a služeb; platnou denní nabídku, položky, otevírací dobu a ceny potvrzuje provozovna.</p><div class="mail-panels">{cards}</div>{btn(p,"Zeptat se na nabídku")}</section>'
    if k=="E":
        return f'<section class="mail-subsection" id="akce"><span class="overline">Setkání a zážitky</span><h2>Akce, oslavy a spolupráce</h2><p>Na tomto místě může být program akcí nebo nabídka pronájmů, cateringu a dalších spoluprací. Přesnou kapacitu a aktuální možnosti ověřte přímo s provozovnou.</p>{btn(p,"Poptat akci")}</section>'
    if k=="V":
        return f'<section class="mail-subsection" id="reference"><span class="overline">Důvěra zákazníků</span><h2>Reference a hodnocení</h2><p>Koncept počítá s prostorem pro skutečné ohlasy a výsledky zákazníků. Bez výslovného podkladu zde nevytváříme zákaznické citace, recenze ani neověřená hodnocení.</p><a class="mail-textlink" href="{e(site_map(p))}" target="_blank" rel="noopener noreferrer">Otevřít veřejný profil nebo mapu ↗</a></section>'
    if k=="P":
        return f'<section class="mail-subsection" id="procedury"><span class="overline">Jak probíhá péče</span><h2>Procedury a jejich možnosti</h2><p>{focus}. Detailní postup, očekávaný průběh, omezení a případné kontraindikace poskytne odborník. Tento návrh neslouží jako zdravotní doporučení.</p><div class="mail-panels">{panel("Před procedurou","Ověřte vhodnost konkrétní služby a očekávání.")}{panel("Průběh ošetření","Postup a délka záleží na prováděné metodě.")}{panel("Následná péče","Podrobnosti sdělí kvalifikovaný poskytovatel.")}</div>{btn(p,"Poptat proceduru")}</section>'
    if k=="D":
        return f'<section class="mail-subsection" id="rozvoz"><span class="overline">Objednávka a rozvoz</span><h2>Objednejte si přímo</h2><p>{focus}. Pro aktuální nabídku a rozvoz volejte provozovnu. Online košík, platba nebo napojení na pokladnu zatím nejsou součástí tohoto návrhu.</p><a class="button" href="{phone(p)}"><span>Zavolat a ověřit rozvoz</span>{ARROW}</a></section>'
    if k=="X":
        return f'<section class="mail-subsection" id="produkty"><span class="overline">Co dalšího nabízíme</span><h2>Produkty a možnosti</h2><p>{focus}. Na produkty, materiály a jejich aktuální dostupnost se zeptejte přímo. Zobrazený koncept není internetový obchod a nemá ověřené skladové zásoby.</p>{btn(p,"Poptat dostupnost")}</section>'
    if k=="R":
        mail_link=f'<a class="mail-textlink" href="{e(mail(p,"Poptávka rezervace – "+p["name"]))}">Napsat e-mail ↗</a>' if p["email"] else ""
        return f'<section class="mail-subsection" id="rezervace"><span class="overline">Domluva termínu</span><h2>Rezervace a objednání</h2><p>Termín lze začít řešit přímo z tohoto webu telefonicky{" nebo připraveným e-mailem" if p["email"] else ""}. Samostatný online kalendář s potvrzením termínů vyžaduje napojení na skutečný rezervační systém a není zatím aktivní.</p><div class="mail-booking"><a class="button" href="{phone(p)}"><span>Zavolat {e(p["phone"])}</span>{ARROW}</a>{mail_link}</div></section>'
    if k=="L":
        return f'<section class="mail-subsection" id="pobocky"><span class="overline">Provozovny</span><h2>Kde nás navštívit</h2><p>V e-mailu se zmiňuje více provozoven. Z podkladové tabulky je zde možné bezpečně uvést následující kontaktní adresu. Další pobočky a jejich adresy nechceme domýšlet.</p><div class="mail-panels">{panel(p["city"],p.get("address",""))}</div><a class="mail-textlink" href="{e(site_map(p))}" target="_blank" rel="noopener noreferrer">Otevřít navigaci ↗</a></section>'
    raise ValueError("Bad tag "+k)

def focus_section(p,s,kind):
    slug,label=kind
    chips="".join(f'<span class="mail-chip">{e(LABELS[t])}</span>' for t in dict.fromkeys(s["flags"]) if t in LABELS)
    return f'<section class="mail-focus" id="na-miru"><div class="shell mail-focus-grid"><div><span class="overline">Na míru pro {e(p["name"])}</span><h2>To podstatné na jednom místě.</h2><p><strong>{e(s["focus"])}.</strong> Podívejte se na nabídku a související informace přesně k tomu, co vás zajímá.</p><div class="mail-chips">{chips}</div><a class="button" href="{base(p)}{slug}/"><span>{e(label)}</span>{ARROW}</a></div><div class="mail-side">{picture(p,1,1150)}<span>Ilustrační fotografie oboru</span></div></div></section>'

def amend(p,s,kind,path,content):
    slug,label=kind
    assert "<main id=\"main\">" in content and 'class="mainmenu"' in content, (p["id"],path)
    assert "<head>" in content and "</head>" in content
    # Keep the original 2026-10-19 ALIK v4 CSS/JS/hero and add 1 custom navigation entry.
    content=content.replace("</head>",CSS+"</head>",1)
    new_link=f'<a class="mail-navlink" href="{base(p)}{slug}/">{e(label)}</a>'
    assert '<a class="topcta"' in content
    content=content.replace('<a class="topcta"',new_link+'<a class="topcta"',1)
    foot=f'<a href="{base(p)}kontakt/">Kontakt</a></div>'
    assert foot in content
    content=content.replace(foot,f'<a href="{base(p)}kontakt/">Kontakt</a><a href="{base(p)}{slug}/">{e(label)}</a></div>',1)
    insert=f'<section class="section faq-section">'
    extra=f'<div class="shell"><div class="mail-cta-block"><h3>{e(label)}</h3><p>{e(s["focus"])}. Další informace najdete v samostatné části návrhu.</p><a class="button" href="{base(p)}{slug}/"><span>Prohlédnout nabídku</span>{ARROW}</a></div></div>'
    if path=="index.html":
        assert insert in content
        content=content.replace(insert,focus_section(p,s,kind)+insert,1)
    elif path=="sluzby/index.html":
        assert insert in content
        content=content.replace(insert,extra+insert,1)
    elif path=="o-firme/index.html":
        assert '<section class="outro">' in content
        content=content.replace('<section class="outro">',extra+'<section class="outro">',1)
    elif path=="kontakt/index.html":
        assert insert in content
        content=content.replace(insert,extra+insert,1)
    return content

def detail(p,s,kind,home):
    slug,label=kind
    assert '<main id="main">' in home and "</main>" in home
    prefix=home.split('<main id="main">')[0]
    footer=home.split("</main>",1)[1]
    # The source page is Home; reset active-nav selection on the detail page.
    prefix=prefix.replace('aria-current="page"','',1)
    focus=e(s["focus"])
    modules="".join(module(p,s,t) for t in dict.fromkeys(s["flags"]) if t in LABELS)
    main=f'<main id="main"><section class="mail-detail-header"><div class="shell"><div class="breadcrumb"><a href="{base(p)}">Úvod</a><span> / </span>{e(label)}</div><span class="overline">{e(p["name"])} · {e(p["city"])}</span><h1>{e(label)}</h1><p>{focus}. Přehled služeb a možností odpovídající tomu, na co se zákazníci nejčastěji ptají.</p></div></section><div class="mail-modules"><div class="shell">{modules}<div class="mail-cta-block"><h3>Domluva je jednoduchá</h3><p>Máte konkrétní dotaz? Pro aktuální dostupnost a ceny se spojte přímo s {e(p["name"])}.</p>{btn(p,"Kontaktovat firmu")}</div></div></div></main>'
    return prefix+main+footer

processed=[]
for p in LEADS:
    s=SPECS[p["id"]]
    kind=config(p,s)
    folder=ROOT / "2026-10-19-premium" / p["slug"]
    homepage=""
    for path in ("index.html","sluzby/index.html","o-firme/index.html","kontakt/index.html"):
        f=folder/path
        original=f.read_text(encoding="utf-8")
        assert "mail-alignment-style" not in original, (p["id"],path,"already aligned")
        updated=amend(p,s,kind,path,original)
        f.write_text(updated,encoding="utf-8")
        if path=="index.html":homepage=updated
    dest=folder/kind[0]/"index.html"
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(detail(p,s,kind,homepage),encoding="utf-8")
    processed.append({"id":p["id"],"name":p["name"],"slug":p["slug"],"detail_slug":kind[0],
                      "detail_name":kind[1],"tags":s["flags"],"focus":s["focus"],
                      "page_count":5,"website":"https://navrhy.digitory.cz"+base(p)})
assert len(processed)==68
(ROOT/".github/email-alignment-result.json").write_text(json.dumps(processed,ensure_ascii=False,indent=2),encoding="utf-8")
print("ALIGNED_SITES",len(processed),"MODIFIED_PAGES",len(processed)*4,"ADDED_PAGES",len(processed))
