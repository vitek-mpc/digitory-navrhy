
window.LAB_DATA = [
{
slug:"strechy-efem",name:"STŘECHY eFeM",icon:"⌂",group:"Obchod",accent:"#e3b67b",mode:"pipeline",
hook:"Žádná cenová nabídka bez dalšího kroku.",subtitle:"Obchodní radar poptávek od prvního kontaktu po zaměření a připomenutí nabídky.",
why:"Veřejně uváděné realizační týmy a střechařské zakázky vytvářejí příležitost ke sledování více současných poptávek.",
hypothesis:"Některé rozpracované nabídky mohou čekat bez následného kontaktu. Nejprve ověřit, jestli a jak dnes firma follow-up řeší.",
outcome:"Přehled všech otevřených nabídek a připravená připomínka, kterou schvaluje obchodník.",
teams:["Obchod","Rozpočtář","Zaměření","Realizační tým"],
stages:["Nová poptávka","Podklady","Zaměření","Nabídka","Follow-up"],
tasks:["Typ střechy","Rozloha či půdorys","Fotografie aktuálního stavu","Adresa realizace","Požadovaný termín","Kontakt pro zaměření","Podklady pro rozpočtáře"],
scenarios:[
{title:"Nová střecha rodinného domu",tag:"Nová realizace",priority:"standard",age:2,team:"Rozpočtář",message:"Dobrý den, stavíme rodinný dům u Frýdku-Místku. Potřebujeme nacenit sedlovou střechu, projekt máme. Kdy byste mohli poslat nabídku?",missing:["Přibližná plocha střechy","Výkresy projektu","Telefon"],next:"Vyžádat projekt a přibližnou plochu; po kontrole předat rozpočtáři."},
{title:"Zatékání střechy po dešti",tag:"Oprava",priority:"high",age:0,team:"Zaměření",message:"Dobrý den, po včerejším dešti nám zatéká do podkroví. Potřebovali bychom, aby se na to někdo co nejdříve podíval.",missing:["Přesné místo závady","Fotografie","Adresa","Telefon"],next:"Urgentně předat člověku k posouzení a získat adresu s fotografiemi."},
{title:"Střecha firemní haly",tag:"B2B",priority:"standard",age:6,team:"Obchod",message:"Poptáváme rekonstrukci střechy skladové haly. Máme připravenou dokumentaci a rádi bychom se domluvili na obhlídce.",missing:["Rozloha haly","Technický rozsah","Lokalita"],next:"Předat obchodníkovi, ověřit rozsah a domluvit nezávazné zaměření."}
]},
{
slug:"vitasolar",name:"Vitasolar",icon:"☀",group:"Servis",accent:"#b6dd89",mode:"onboarding",
hook:"Nový servisní zákazník bez chaosu v dokumentaci.",subtitle:"Převzetí fotovoltaické elektrárny do pravidelné péče, krok za krokem.",
why:"Společnost uvádí také převzetí servisu FVE instalovaných jinými dodavateli. Takové případy mohou mít různě úplnou dokumentaci.",
hypothesis:"Shromažďování revizí, výrobních údajů a servisní historie může administrativu zpomalovat.",
outcome:"Přehled chybějících dokumentů a připravený předávací balíček pro servisního technika.",
teams:["Příjem servisu","Technik FVE","Revizní technik","Obchod"],
stages:["Poptávka","Identifikace FVE","Dokumentace","Technické posouzení","Převzetí"],
tasks:["Model a výkon instalace","Výrobce střídače","Datum instalace","Poslední revizní zpráva","Schéma zapojení","Servisní historie","Kontaktní osoba","Odborné schválení převzetí"],
scenarios:[
{title:"Původní dodavatel nereaguje",tag:"Převzetí cizí FVE",priority:"standard",age:3,team:"Příjem servisu",message:"Dobrý den, před třemi lety nám jiná firma instalovala fotovoltaiku a už nereaguje. Hledáme servis, který by naši elektrárnu převzal do péče. Máme fakturu a nějaké dokumenty.",missing:["Výrobce a typ střídače","Poslední revize","Dokumentace zapojení"],next:"Vyzvat k zaslání seznamu zařízení a dostupných dokumentů; posouzení technikem."},
{title:"Pravidelná kontrola FVE",tag:"Údržba",priority:"standard",age:4,team:"Technik FVE",message:"Máme solární elektrárnu od vás a chtěli bychom provést pravidelnou kontrolu. Zatím vše funguje bez problémů.",missing:["Identifikace instalace","Poslední kontrola","Telefon"],next:"Dohledat evidenci zařízení a navrhnout postup kontroly ke schválení."},
{title:"Střídač hlásí chybu",tag:"Porucha",priority:"high",age:0,team:"Technik FVE",message:"Dobrý den, náš střídač svítí červeně a výroba dnes nefunguje. Potřebovali bychom servis. Nevíme, co s tím.",missing:["Typ střídače","Kód chyby","Adresa","Kontakt"],next:"Předat technikovi jako poruchu; bez vzdálených zásahů do elektrického zařízení."}
]},
{
slug:"vbs-montaze",name:"VBS montáže",icon:"▥",group:"Montáže",accent:"#a2bdf4",mode:"measurement",
hook:"Od poptávky po montáž bez ztracených informací.",subtitle:"Připravené podklady pro zaměření, nabídku a předání realizačnímu týmu.",
why:"Nabídka vrat, bran, žaluzií a následného servisu znamená několik odlišných způsobů zpracování poptávky.",
hypothesis:"Neúplné podklady mezi administrativou, zaměřením a montáží mohou vytvářet zbytečná kolečka.",
outcome:"Jedno zadání s rozměry, fotkami a schvalovanými kroky pro montáž.",
teams:["Administrativa","Zaměřovací technik","Montážní tým","Servis pohonů"],
stages:["Poptávka","Rozměry a foto","Zaměření","Návrh ceny","Montáž"],
tasks:["Typ produktu","Přibližné rozměry","Fotografie otvoru","Možnosti elektrického připojení","Adresa montáže","Termín zaměření","Schválená specifikace"],
scenarios:[
{title:"Sekční vrata do garáže",tag:"Vrata",priority:"standard",age:1,team:"Zaměřovací technik",message:"Chtěli bychom sekční garážová vrata s elektrickým pohonem. Šířka otvoru je přibližně 260 cm. Prosím o informaci, co potřebujete k nabídce.",missing:["Výška otvoru","Fotografie nadpraží","Adresa"],next:"Vyžádat chybějící rozměry a fotografii, následně nabídnout zaměření."},
{title:"Venkovní žaluzie na dům",tag:"Stínění",priority:"standard",age:3,team:"Administrativa",message:"Dobrý den, dokončujeme novostavbu a sháníme venkovní žaluzie na osm oken, ideálně s ovládáním na dálku.",missing:["Rozměry oken","Typ řízení","Fáze stavební přípravy"],next:"Připravit checklist podkladů pro stínění a předat technikovi."},
{title:"Brána nereaguje na ovladač",tag:"Servis pohonu",priority:"high",age:0,team:"Servis pohonů",message:"Pohon vjezdové brány od rána nefunguje, ovladač nereaguje. Potřebujeme opravu.",missing:["Model pohonu","Projev závady","Telefon","Adresa"],next:"Nahlásit servisnímu pracovníkovi a vyžádat identifikaci pohonu; žádné návody k zásahům."}
]},
{
slug:"vantuch-klima",name:"Vantuch klima",icon:"❄",group:"Servis",accent:"#8ad9ea",mode:"registry",
hook:"Každá instalace může mít dobře řízený další servis.",subtitle:"Evidence zařízení a automaticky připravené, ale neschválené připomínky údržby.",
why:"Firma uvádí dlouhou historii instalací klimatizací a servisní činnosti.",
hypothesis:"Databáze minulých instalací může být příležitostí k pravidelnému a lépe plánovanému servisu.",
outcome:"Seznam zařízení čekajících na kontrolu a připravené návrhy servisních pozvánek.",
teams:["Servisní koordinátor","Montážní technik","Dispečink","Obchod"],
stages:["Záznam zařízení","Kontrola historie","Servisní plán","Oslovení","Potvrzení člověkem"],
tasks:["Model klimatizace","Datum montáže","Poslední servis","Identifikace zákazníka","Kontaktní souhlas","Doporučený interval","Schválení oslovení"],
scenarios:[
{title:"Sezonní servis domácí klimatizace",tag:"Servis",priority:"standard",age:9,team:"Servisní koordinátor",message:"Dobrý den, loni jste nám instalovali klimatizaci a chtěli bychom si domluvit její pravidelné čištění před sezonou.",missing:["Číslo instalace","Preferovaný termín"],next:"Dohledat servisní kartu a připravit návrh termínu ke schválení."},
{title:"Klimatizace vydává hluk",tag:"Porucha",priority:"high",age:0,team:"Dispečink",message:"Naše klimatizace v kanceláři začala hučet a někdy se vypíná. Potřebujeme odbornou kontrolu.",missing:["Typ jednotky","Popis chování","Adresa"],next:"Založit servisní případ a předat technikovi."},
{title:"Nová split klimatizace do bytu",tag:"Nová montáž",priority:"standard",age:1,team:"Obchod",message:"Prosím o nabídku split klimatizace pro byt 3+1 v Havířově. Potřebujeme poradit s umístěním.",missing:["Plocha místností","Půdorys","Možnost venkovní jednotky"],next:"Doplnit vstupy a připravit konzultaci."}
]},
{
slug:"finis-ostrava",name:"FINIŠ OSTRAVA",icon:"⚙",group:"Servis",accent:"#e8b08f",mode:"dispatch",
hook:"Každá porucha rovnou správnému týmu.",subtitle:"Jednotný přehled poruch chlazení, klimatizací a vzduchotechniky.",
why:"Firma uvádí technické služby ve více oblastech a servisní výjezdy.",
hypothesis:"Rozdělení naléhavých a běžných servisních požadavků může zpřehlednit práci dispečinku.",
outcome:"Rychlejší orientace v hlášeních, jasné lidské převzetí a kontrola zpětného volání.",
teams:["Dispečink","Technik chlazení","Technik klimatizací","Technik VZT"],
stages:["Přijatá porucha","Třídění priority","Přidělení týmu","Kontakt zákazníka","Technik potvrzuje"],
tasks:["Typ zařízení","Lokalita","Popis poruchy","Dopad na provoz","Kontaktní osoba","Přiřazený servisní tým","Potvrzení výjezdu člověkem"],
scenarios:[
{title:"Chlazení provozovny nefunguje",tag:"Provozní porucha",priority:"high",age:0,team:"Dispečink",message:"Dobrý den, v prodejně nám od rána nefunguje chlazení a teplota stoupá. Potřebujeme co nejdříve servis.",missing:["Lokalita","Typ zařízení","Kontaktní telefon"],next:"Označit vysokou prioritu k posouzení dispečerem; neautorizovat výjezd automaticky."},
{title:"Kancelářská klimatizace nejde",tag:"Klimatizace",priority:"standard",age:1,team:"Technik klimatizací",message:"Naše klimatizace v zasedací místnosti nereaguje na ovladač. Budeme rádi za servisní termín.",missing:["Typ jednotky","Adresa","Telefon"],next:"Předat specialistovi na klimatizace a zajistit potvrzení dostupnosti."},
{title:"Pravidelná kontrola rekuperace",tag:"VZT",priority:"standard",age:5,team:"Technik VZT",message:"Chceme objednat pravidelnou servisní prohlídku rekuperace ve firmě. Poslední byla před rokem.",missing:["Inventární označení","Předchozí protokol"],next:"Dohledat historii a připravit návrh termínu."}
]},
{
slug:"pecka-dvere",name:"Pecka dveře",icon:"⛨",group:"Servis",accent:"#e7a0bd",mode:"safety",
hook:"Urgentní požadavek nezapadne mezi běžnými.",subtitle:"Bezpečný příjem zámečnického servisu a poptávek bezpečnostních dveří.",
why:"Firma nabízí bezpečnostní dveře, alarmy a také zámečnické služby včetně pohotovosti.",
hypothesis:"Oddělení urgentních servisních případů od běžných nabídek může zkrátit reakční dobu.",
outcome:"Přehled priority, kontaktních údajů a předání člověku bez bezpečnostních rizik.",
teams:["Pohotovost","Servis zámků","Bezpečnostní konzultant","Obchod"],
stages:["Příjem","Urgence","Ověření oprávnění","Lidské schválení","Předání"],
tasks:["Typ požadavku","Telefonní kontakt","Místo požadavku","Ověření oprávnění zákazníka","Přidělený odpovědný člověk","Schválení výjezdu","Záznam komunikace"],
scenarios:[
{title:"Zabouchnuté dveře bytu",tag:"Urgentní zámečník",priority:"high",age:0,team:"Pohotovost",message:"Zabouchly se nám dveře do bytu a jsme venku. Potřebujeme pomoc zámečníka v Ostravě.",missing:["Přesná adresa","Telefon","Ověření oprávnění"],next:"Urgentně předat pohotovosti k ověření situace a oprávnění; bez návodů k otevření."},
{title:"Porucha bezpečnostního zámku",tag:"Servis",priority:"high",age:0,team:"Servis zámků",message:"Klíč se zasekává v bezpečnostním zámku a obáváme se, že se brzy nepůjde zamknout.",missing:["Typ zámku","Adresa","Telefon"],next:"Vyžádat základní údaje a předat servisnímu technikovi."},
{title:"Poptávka bezpečnostních dveří",tag:"Obchod",priority:"standard",age:3,team:"Bezpečnostní konzultant",message:"Rádi bychom pořídili bezpečnostní dveře do bytu v panelovém domě. Můžete nám doporučit variantu a postup?",missing:["Rozměry otvoru","Způsob instalace","Telefon"],next:"Připravit odbornou konzultaci a podklady pro nabídku."}
]},
{
slug:"tepelna-cerpadla-morava",name:"Tepelná čerpadla Morava",icon:"◈",group:"Montáže",accent:"#b4c2f5",mode:"customer",
hook:"Jedna historie zákazníka od poptávky po servis.",subtitle:"Propojení úvodní konzultace, montáže a následné servisní péče.",
why:"Firma se veřejně prezentuje instalacemi tepelných čerpadel a následným servisem.",
hypothesis:"Předávání údajů mezi obchodní a servisní fází může být výhodné vést na jednom místě.",
outcome:"Kompletní časová osa případu včetně potřebných podkladů a budoucího servisu.",
teams:["Obchodní poradce","Technické posouzení","Montážní tým","Servisní koordinátor"],
stages:["Poptávka","Parametry objektu","Technické posouzení","Montáž","Servisní péče"],
tasks:["Typ objektu","Vytápěná plocha","Současný zdroj tepla","Tepelná ztráta / projekt","Lokalita","Fotografie technické místnosti","Předávací dokumentace"],
scenarios:[
{title:"Tepelné čerpadlo pro rekonstrukci",tag:"Rekonstrukce",priority:"standard",age:2,team:"Obchodní poradce",message:"Rekonstruujeme starší dům se současným plynovým kotlem. Rádi bychom věděli, zda je pro nás vhodné tepelné čerpadlo.",missing:["Vytápěná plocha","Tepelná ztráta","Fotografie kotelny"],next:"Připravit seznam vstupů pro technické posouzení, bez závazného návrhu výkonu."},
{title:"Novostavba rodinného domu",tag:"Novostavba",priority:"standard",age:5,team:"Technické posouzení",message:"Potřebujeme poptat tepelné čerpadlo pro novostavbu RD. Máme projekt a stavební povolení.",missing:["Projekt vytápění","Termín realizace"],next:"Vyžádat projekt vytápění a připravit konzultaci."},
{title:"Servis stávajícího čerpadla",tag:"Servis",priority:"high",age:1,team:"Servisní koordinátor",message:"Naše tepelné čerpadlo poslední týden špatně topí. Potřebujeme kontrolu zařízení.",missing:["Výrobce zařízení","Kód závady","Adresa"],next:"Založit servisní tiket a předat kvalifikovanému člověku."}
]},
{
slug:"komenda-strechy",name:"KOMENDA-STŘECHY",icon:"▱",group:"Montáže",accent:"#c7c899",mode:"planner",
hook:"Podklady, rozpočty a realizační týmy pod kontrolou.",subtitle:"Zakázkový plánovač střech od prvních fotografií až po realizaci.",
why:"Firma pokrývá pokrývačské, tesařské, klempířské a hydroizolační práce.",
hypothesis:"Různé druhy střechařských prací mohou vyžadovat různá data při zadání a předávání zakázky.",
outcome:"Jednotný zakázkový list s podklady pro rozpočtáře a plán realizace.",
teams:["Příjem zakázek","Rozpočtář","Tesařský tým","Klempířský tým","Hydroizolační tým"],
stages:["Příjem","Fotodokumentace","Rozpočet","Plán práce","Realizace"],
tasks:["Typ práce","Rozsah a rozměry","Fotodokumentace","Přístup na střechu","Materiál / konstrukce","Lokalita zakázky","Předběžná kapacita týmu"],
scenarios:[
{title:"Hydroizolace ploché střechy",tag:"Hydroizolace",priority:"standard",age:5,team:"Hydroizolační tým",message:"Poptáváme opravu hydroizolace ploché střechy nad garáží. Na několika místech se objevuje vlhkost.",missing:["Plocha střechy","Fotografie","Skladba pláště"],next:"Vyžádat fotky a rozměry pro rozpočet."},
{title:"Oprava oplechování komína",tag:"Klempířské práce",priority:"high",age:0,team:"Klempířský tým",message:"Po silném větru máme poškozené oplechování komína a zatéká kolem něj.",missing:["Fotografie","Přístup na střechu","Adresa"],next:"Označit pro prioritní lidské posouzení a vyžádat fotky."},
{title:"Nové střešní okno",tag:"Montáž",priority:"standard",age:3,team:"Tesařský tým",message:"Chtěli bychom namontovat nové střešní okno do podkroví. Stávající střecha je tašková.",missing:["Rozměry","Typ krytiny","Stavební souvislosti"],next:"Předat pro technické posouzení a připravit podklady."}
]},
{
slug:"kf-klima",name:"KF klima",icon:"◉",group:"Servis",accent:"#8dcde0",mode:"contracts",
hook:"Servisní smlouvy, termíny a dokumentace v jednom.",subtitle:"Přehled evidence zařízení a podkladů ke kontrolám bez administrativního chaosu.",
why:"Firma popisuje servis klimatizací a vzduchotechniky včetně odborných kontrol chladiv.",
hypothesis:"Koordinace různých kontrolních dokumentů a servisních termínů může být časově náročná; je třeba ověřit stávající software.",
outcome:"Servisní kalendář a kontrolní seznam chybějících dokumentů ke schválení technikem.",
teams:["Správce smluv","Servisní koordinátor","Technik chlazení","Odborný kontrolor"],
stages:["Evidence smlouvy","Inventář zařízení","Plán kontrol","Schválení termínu","Servisní záznam"],
tasks:["Zákaznická smlouva","Typ a číslo zařízení","Poslední servisní záznam","Evidence chladiva","Dostupná technická dokumentace","Plán odborné kontroly","Ověření termínu technikem"],
scenarios:[
{title:"Servis klimatizací ve firmě",tag:"Pravidelný servis",priority:"standard",age:8,team:"Servisní koordinátor",message:"V administrativní budově máme několik klimatizačních jednotek. Chceme sjednotit pravidelný servis a plán termínů.",missing:["Soupis jednotek","Poslední protokol","Kontaktní osoba"],next:"Vytvořit inventář zařízení a předat k nacenění servisního plánu."},
{title:"Nová servisní smlouva",tag:"Smlouva",priority:"standard",age:3,team:"Správce smluv",message:"Rádi bychom uzavřeli servisní smlouvu pro naše provozovny v kraji.",missing:["Počet zařízení","Lokality","Servisní rozsah"],next:"Získat soupis zařízení, ověřit požadovaný rozsah smlouvy."},
{title:"Podklady ke kontrole těsnosti",tag:"Odborná kontrola",priority:"standard",age:1,team:"Odborný kontrolor",message:"Potřebovali bychom připravit podklady pro pravidelnou kontrolu zařízení s chladivem.",missing:["Parametry zařízení","Poslední kontrola","Evidence chladiva"],next:"Připravit dokumenty pro odborníka; neurčovat právní povinnost ani výsledek kontroly."}
]},
{
slug:"kibke-klima",name:"KIBKE KLIMA",icon:"❋",group:"Servis",accent:"#dbb4e9",mode:"aftercare",
hook:"Každá instalace má svůj další servisní krok.",subtitle:"Automaticky připravené návazné úkoly a komunikace po montáži.",
why:"Firma nabízí montáže klimatizací a tepelných čerpadel i následné servisní služby.",
hypothesis:"Pravidelná následná péče o zákazníka může být příležitostí k opakovaným zakázkám.",
outcome:"Úkoly pro návazný servis a návrhy zpráv bez automatického odeslání.",
teams:["Zákaznická péče","Montážní tým","Servis","Reklamace"],
stages:["Kontakt","Zjištění typu","Přidělení","Příprava odpovědi","Následná péče"],
tasks:["Typ zařízení","Datum instalace","Údaje zákazníka","Typ požadavku","Servisní historie","Souhlas s oslovením","Odpovědná osoba"],
scenarios:[
{title:"Klimatizace do nového bytu",tag:"Nová montáž",priority:"standard",age:2,team:"Montážní tým",message:"Dobrý den, chceme klimatizaci do nového bytu 2+kk v Ostravě. Rádi bychom měli informace o možnostech.",missing:["Rozloha","Možné umístění venkovní jednotky","Telefon"],next:"Vyžádat základní údaje pro návrh a nabídnout konzultaci."},
{title:"Údržba starší klimatizace",tag:"Pravidelný servis",priority:"standard",age:11,team:"Zákaznická péče",message:"Před dvěma roky jste nám montovali klimatizaci. Chtěli bychom domluvit běžnou údržbu.",missing:["Číslo zakázky","Preferovaný termín"],next:"Dohledat instalaci a připravit servisní kontakt."},
{title:"Tepelné čerpadlo hlásí závadu",tag:"Reklamace / servis",priority:"high",age:0,team:"Reklamace",message:"Tepelné čerpadlo nám dnes přestalo topit a ukazuje chybu. Prosíme o pomoc.",missing:["Model zařízení","Chybový kód","Telefon"],next:"Předat technikovi, ověřit záruční stav a dohodnout další postup."}
]}
];
