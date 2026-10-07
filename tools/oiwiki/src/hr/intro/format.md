---
title: Priručnik za oblikovanje
---

Prije početka članka, svi članovi projektnog tima **OI Wiki** srdačno vas pozdravljaju i pozivaju da doprinesete stranicama ovog projekta. Upravo zahvaljujući stotinama ljudi poput vas **OI Wiki** postao je ono što je danas!

Ova stranica navodi preporučena pravila oblikovanja i uređivačke smjernice za pisanje **OI Wikija**. Prije pisanja ili ispravljanja wiki stranica pažljivo pročitajte sljedeći tekst kako biste pripremili što kvalitetniji sadržaj.

Ako jedva čekate početi, preporučujemo da najprije pročitate odjeljke [Ukratko](#ukratko) i [Ilustrirani primjeri](#ilustrirani-primjeri).

??? abstract "Povijest izmjena"
    **Napomena**: bilježe se samo promjene vezane uz pisanje, recenziranje i slično, a ne ispravci oblikovanja.
    
    | Datum | Glavni sadržaj | Poveznice na povezane issuee/pull requestove |
    | ---------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
    | 2026-02-22 | Dopunjena pravila uporabe navodnika | [#6793](https://github.com/OI-wiki/OI-wiki/pull/6793)                                                       |
    | 2026-01-07 | Propisana točka pune širine umjesto kineske kružne točke | [#6746](https://github.com/OI-wiki/OI-wiki/pull/6746)                                                       |
    | 2025-08-10 | Dodani zahtjevi oblikovanja samog priručnika;<br>kôd: dopunjeni zahtjevi za isječke koda | [#6412](https://github.com/OI-wiki/OI-wiki/pull/6412)                                                       |
    | 2025-08-10 | Dodani povijest izmjena i sažetak | [#6409](https://github.com/OI-wiki/OI-wiki/pull/6409)                                                       |
    | 2024-10-08 | Kôd: dopunjeni zahtjevi oblikovanja za testiranje na svim platformama | [#5912](https://github.com/OI-wiki/OI-wiki/pull/5912), [#5924](https://github.com/OI-wiki/OI-wiki/pull/5924) |
    | 2024-03-26 | Za zadatke na OJ-ovima koristiti izvornu poveznicu umjesto zrcalne | [#5482](https://github.com/OI-wiki/OI-wiki/pull/5482)                                                       |
    | 2023-10-09 | Dodaci teme: dodani zahtjevi oblikovanja kartica[^note6] | [#5152](https://github.com/OI-wiki/OI-wiki/pull/5152)                                                       |
    | 2023-07-23 | Za preuzimanje i instalaciju alata upućivati na službenu dokumentaciju | [#5023](https://github.com/OI-wiki/OI-wiki/pull/5023)                                                       |
    | 2023-04-15 | Dopunjena pravila uporabe navodnika | [#4792](https://github.com/OI-wiki/OI-wiki/pull/4792)                                                       |
    | 2023-03-28 | LaTeX: tablica matematičkih simbola | [#4587](https://github.com/OI-wiki/OI-wiki/pull/4587)                                                       |
    | 2023-03-02 | Dopunjena pravila interpunkcije pune i polovične širine te spojnica i crta | [#4726](https://github.com/OI-wiki/OI-wiki/pull/4726)                                                       |
    | 2022-12-13 | Dodaci teme: uklonjen zahtjev za stil sjene ugniježđenih sklopivih okvira | [#4500](https://github.com/OI-wiki/OI-wiki/pull/4500)                                                       |
    | 2022-08-09 | Pri povezivanju odjeljaka internih stranica koristiti kineske naslove | [#4057](https://github.com/OI-wiki/OI-wiki/pull/4057)                                                       |
    | 2022-06-12 | Dopunjeni zahtjevi za promjene navigacije[^note4] | [#4043](https://github.com/OI-wiki/OI-wiki/pull/4043)                                                       |
    | 2021-09-09 | Dodaci teme: dopunjeni zahtjevi za sklopive okvire | [#3517](https://github.com/OI-wiki/OI-wiki/pull/3517)                                                       |
    | 2021-09-03 | LaTeX: `\Leftrightarrow` $\to$ `\iff` | [#3499](https://github.com/OI-wiki/OI-wiki/pull/3499)                                                       |
    | 2021-08-18 | Kôd: dodani zahtjevi oblikovanja koda oglednih zadataka | [#3447](https://github.com/OI-wiki/OI-wiki/pull/3447)                                                       |
    | 2021-08-12 | Slike: za animacije prednost dati APNG-u | [#3422](https://github.com/OI-wiki/OI-wiki/pull/3422)                                                       |
    | 2021-06-29 | Slike: preporučeno istodobno slanje izvornih datoteka | [#3255](https://github.com/OI-wiki/OI-wiki/pull/3255)                                                       |
    | 2021-05-29 | Kôd: uklonjen zahtjev da vitičaste zagrade ne budu u novom retku, dodani zahtjevi čitljivosti | [#3197](https://github.com/OI-wiki/OI-wiki/pull/3197)                                                       |
    | 2021-03-15 | Održavanje stranice: standardiziran način spajanja pull requestova[^note5] | [#3061](https://github.com/OI-wiki/OI-wiki/pull/3061)                                                       |
    | 2021-02-01 | LaTeX: `\lt` $\to$ `<`, `\gt` $\to$ `>` | [#2950](https://github.com/OI-wiki/OI-wiki/pull/2950)                                                       |
    | 2021-01-27 | Preporučeno spremanje vanjskih poveznica u [Internet Archive](https://web.archive.org/) | [#2918](https://github.com/OI-wiki/OI-wiki/pull/2918)                                                       |
    | 2020-09-19 | Održavanje stranice: zahtjevi za commit poruke i naslove pull requestova[^note4] | [#2744](https://github.com/OI-wiki/OI-wiki/pull/2744)                                                       |
    | 2020-10-18 | Slike: prednost dati SVG-u | [#2215](https://github.com/OI-wiki/OI-wiki/pull/2215)                                                       |
    | 2020-08-05 | LaTeX: dodani zahtjevi oblikovanja višeslovnih varijabli | [#2502](https://github.com/OI-wiki/OI-wiki/pull/2502)                                                       |
    | 2020-07-28 | LaTeX: zabranjeno više od dva stupca u okruženju `cases` | [#2466](https://github.com/OI-wiki/OI-wiki/pull/2466)                                                       |
    | 2020-07-24 | LaTeX: `{n \choose m}`$\to$ `\dbinom{n}{m}` | [#2442](https://github.com/OI-wiki/OI-wiki/pull/2442)                                                       |
    | 2020-07-20 | Markdown: zabranjena sintaksa precrtanog teksta | [#2422](https://github.com/OI-wiki/OI-wiki/pull/2422)                                                       |
    | 2020-07-19 | Dodaci teme: obvezno očuvanje uvlačenja praznih redaka u sklopivim okvirima[^note3];<br>LaTeX: dodatni zahtjevi oblikovanja matematičkih formula | [#2412](https://github.com/OI-wiki/OI-wiki/pull/2412)                                                       |
    | 2020-07-11 | Početna verzija | [#2350](https://github.com/OI-wiki/OI-wiki/pull/2350)                                                       |

## Ukratko

Kako bismo olakšali prvo čitanje ovog dokumenta, u ovom odjeljku izdvajamo nekoliko važnih točaka priručnika:

-   Pohrana datoteka:

    -   Koristite mala slova u nazivima datoteka i `-` umjesto razmaka. Pogledajte [SAVE-1](#SAVE-1).

    -   Nemojte umetati slike s vanjskih poveznica. Pogledajte [SAVE-2](#SAVE-2).

    -   Kad god je moguće, koristite SVG slike, i to samo standard SVG 1.1. Pogledajte [SAVE-3](#SAVE-3).

    -   Animacije trebaju biti u formatu SVG ili APNG. Pogledajte [SAVE-4](#SAVE-4).

    -   Ako slika ima izvornu datoteku, preporučuje se poslati i nju. Pogledajte [SAVE-5](#SAVE-5).

    -   Uz vanjsku poveznicu preporučuje se dodati poveznicu na arhiviranu snimku. Pogledajte [SAVE-6](#SAVE-6).

    -   Nemojte pisati interne poveznice kao vanjske. Pogledajte [SAVE-7](#SAVE-7).

-   Interpunkcija:

    -   Pravilno koristite interpunkciju. Svaku rečenicu završite **točkom**. Pogledajte [PUNC-1](#PUNC-1) do [PUNC-7](#PUNC-7).

    -   Razlikujte spojnicu, kratku crtu i dugu crtu (hyphen, en dash, em dash). Pogledajte [PUNC-8](#PUNC-8).

-   Sintaksa Markdowna i proširenja teme:

    -   Koristite samo naslove druge, treće i četvrte razine. Ne zamjenjujte podebljani tekst naslovima. Ne pišite LaTeX formule u naslovima. Pogledajte [LINT-1](#LINT-1), [MDFM-1](#MDFM-1), [CONT-4](#CONT-4), [CONT-9](#CONT-9).

    -   U sklopivim okvirima[^note3] i karticama[^note6] održavajte jednako uvlačenje, **čak i na praznim redcima**. **Nemojte izostaviti** razmake za uvlačenje praznih redaka. Pogledajte [LINT-6](#LINT-6), [MDFM-6](#MDFM-6).

    -   Nemojte koristiti sintaksu precrtanog teksta `~~foo~~`. Pogledajte [LINT-3](#LINT-3).

    -   Izdvojene formule pišite ovako

        ```text
        $$
        a^{2}=b^{2}+c^{2}
        $$
        ```

        umjesto `$$a^{2}=b^{2}+c^{2}$$`. Pogledajte [LINT-5](#LINT-5).

    -   Koristite sklopive okvire umjesto blokova citata (Blockquotes). Pogledajte [MDFM-5](#MDFM-5).

    -   Za blokove koda koristite samo sintaksu ` ``` ` i obvezno navedite jezik. Pogledajte [LINT-7](#LINT-7), [MDFM-3](#MDFM-3).

-   LaTeX formule:
    -   Ne smiju biti u suprotnosti s [tablicom matematičkih simbola](./symbol.md). Pogledajte [MATH-1.1](#MATH-1.1).

    -   Pazite na uporabu fontova. Pogledajte [MATH-1.2](#MATH-1.2), [MATH-1.15](#MATH-1.15), [MATH-2.6](#MATH-2.6), [MATH-2.7](#MATH-2.7).

    -   Nemojte pretjerivati s LaTeX formulama. Pogledajte [MATH-1.14](#MATH-1.14).

    -   U LaTeX formulama nemojte koristiti zapise iz programskih jezika (primjerice $a==b$, $a<<1$, $a\%b$). Ne nižite uglate zagrade ($a[i][j]$). Pogledajte [MATH-1.9](#MATH-1.9), [MATH-1.10](#MATH-1.10).

-   Kôd:

    -   Pišite što jednostavnije i razumljivije te izbjegavajte loše navike poput zbijanja koda u premalo redaka. Pazite na čitljivost i istaknite ideju algoritma. Pogledajte [CONT-10](#CONT-10).

    -   Ne preporučuje se umetati kôd izravno u Markdown dokument. Pogledajte [CODE-1.1](#CODE-1.1), [CODE-1.2](#CODE-1.2).

## Zahtjevi oblikovanja ovog dokumenta

-   <span id="FREQ-1">FREQ-1</span>: pri izmjeni pravila priručnika dopunite i povijest izmjena. Ako samo ispravljate oblikovanje, to nije potrebno.
-   <span id="FREQ-2">FREQ-2</span>: osim u odjeljku [Ukratko](#ukratko), svako pravilo priručnika mora imati jedinstvenu oznaku koja odgovara regularnom izrazu `(?<category>[A-Z]{4})-(?<id>[1-9][0-9]*(?:\.[1-9][0-9]*)*)`, pri čemu `category` treba imati intuitivno značenje. Objašnjenjima nisu potrebne oznake.
-   <span id="FREQ-3">FREQ-3</span>: stavke odjeljka [Ukratko](#ukratko) moraju potjecati iz drugih odjeljaka priručnika i na kraju sadržavati poveznice na odgovarajuće oznake pravila.
-   <span id="FREQ-4">FREQ-4</span>: jednom dodijeljene oznake pravila ne treba mijenjati. Ako je promjena nužna (primjerice pri brisanju ili spajanju pravila), označite je tekstom poput „Ukinuto” ili „Premješteno u XXXX-id”.

## Zahtjevi za doprinos dokumentaciji

Kada namjeravate doprinijeti sadržaju, upoznajte se koliko je moguće sa sljedećim trima područjima:

-   oblik pohrane dokumenata
-   smislenost dokumenata
-   zahtjevi oblikovanja remark-linta i $\rm{\LaTeX}$ formula

### Oblik poveznica i pohrane dokumenata

-   <span id="SAVE-1">SAVE-1</span>: **nazivi datoteka moraju biti malim slovima, a riječi odvojene znakom `-`.** Primjer: `file-name.md`.

-   <span id="SAVE-2">SAVE-2</span>: sve **vanjske** slike koje dokument koristi pohranite u odgovarajuću mapu `images` **unutar ovog repozitorija** (kako biste izbjegli zaštitu od izravnog povezivanja na nekim stranicama). Preporučuje se oblik naziva `naziv MD dokumenta + broj` (pogledajte slike u postojećim dokumentima). Primjerice, naziv datoteke ovog dokumenta je format, pa se prva slika u njemu zove `format1.png`.

-   <span id="SAVE-3">SAVE-3</span>: preporučuje se format SVG[^ref4] radi bolje oštrine i skaliranja. Budući da komponente **OI Wikija** različito podržavaju SVG standarde, slike trebaju slijediti standard [SVG 1.1](http://www.w3.org/TR/SVG11/).

-   <span id="SAVE-4">SAVE-4</span>: ako animaciju ne možete ili ne znate izraditi u SVG-u, preporučuje se APNG[^apng]. Korisnici Windowsa mogu snimati alatom [ScreenToGif](https://www.screentogif.com), a korisnici Linuxa alatom [Peek](https://github.com/phw/peek); u postavkama odaberite APNG. U ostalim slučajevima preporučuje se prvo izraditi video, primjerice MP4, i pretvoriti ga u APNG. U ffmpegu to možete učiniti naredbom `ffmpeg -i filename.mp4 -f apng filename.apng -plays 0`.[^intro-apng]

-   <span id="SAVE-5">SAVE-5</span>: ako slika ima i izvornu datoteku i izvezeni prikaz (primjerice JPG i PSD ili SVG i izvorni TikZ TeX kôd), preporučuje se spremiti izvornu datoteku u isti direktorij s istim osnovnim nazivom kao slika.

-   <span id="SAVE-6">SAVE-6</span>: provjerite trajnost poveznica u dokumentu. **Ne preporučuje se** povezivanje resursa s **vlastitih** servisa (primjerice zadataka s vlastitog OJ-a). Pri dodavanju vanjske poveznice preporučuje se pohraniti je i u Internet Archive[^webarchive] kako nezamjenjive poveznice ne bi postale nedostupne.

-   <span id="SAVE-7">SAVE-7</span>: u internim poveznicama izostavite domenu i relativnom putanjom povežite odgovarajuću `.md` datoteku. Primjerice, na ovoj stranici (`intro/format`) uvod u razne teme (`misc`) povezuje se zapisom `[Uvod u razne teme](../misc/index.md)`. Dodavanjem fragmenta možete povezati određeni odjeljak, primjerice [`[Pravila oblikovanja pull requestova](./htc.md#pravila-oblikovanja-pull-requestova)`](./htc.md#pravila-oblikovanja-pull-requestova). Vrijednost fragmenta možete dobiti gumbom desno od svakog naslova ili iz poveznica u sadržaju na desnoj strani web-stranice.

### Smislenost dokumenata

**Smislenost** znači da napisani **sadržaj** mora imati sljedeća svojstva:

-   <span id="STRC-1">STRC-1</span>: od jednostavnoga prema složenome; težina sadržaja treba postupno rasti.
-   <span id="STRC-2">STRC-2</span>: logičnost.

    -   <span id="STRC-2.1">STRC-2.1</span>: tekstovi o algoritmima ili matematičkim pojmovima trebaju, koliko je moguće, sadržavati:

        1.  načelo: objasnite pripadajuće načelo;
        2.  primjere: dajte 1 \~ 2 tipična primjera;
        3.  zadatke: pod tim naslovom **navedite samo nazive zadataka i poveznice na njih**. Za algoritamske zadatke prioritet OJ-ova je: izvorni OJ (strani OJ mora biti lako dostupan iz Kine) > UOJ > LOJ > Luogu.

        Primjer stranice: [IDA\*](../search/idastar.md)

    -   <span id="STRC-2.2">STRC-2.2</span>: tekstovi o alatima trebaju, koliko je moguće, sadržavati:

        1.  uvod: objasnite pozadinu i namjenu alata.
        2.  postavljanje: detaljno opišite postavljanje okruženja i uporabu. Za preuzimanje i instalaciju po mogućnosti uputite na službenu dokumentaciju.

        Primjer stranice: [WSL (Windows 10)](../tools/wsl.md)

Osim kada je postojeći sadržaj loše kvalitete, preporučuje se doprinijeti **dopunjavanjem**, a ne izravnim prepisivanjem preko postojećeg sadržaja. Ako niste sigurni, pogledajte odjeljak [Načini komunikacije o projektu](./about.md#načini-komunikacije) i obratite se timu **OI Wikija**.

### Osnovni zahtjevi oblikovanja dokumenata

#### Zahtjevi oblikovanja remark-linta

[remark-lint](https://github.com/remarkjs/remark-lint) može automatski ujednačiti stil datoteka u projektu. Trenutačna konfiguracija **OI Wikija** nalazi se u [.remarkrc](https://github.com/OI-wiki/OI-wiki/blob/master/.remarkrc).

Pri postavljanju konfiguracije tim **OI Wikija** naišao je i na probleme koje remark-lint ne obrađuje dobro. Stoga pri uređivanju dokumenata strogo slijedite ove zahtjeve:

-   <span id="LINT-1">LINT-1</span>: nemojte koristiti naslove prve razine, poput `<h1>` ili `# Naslov`.

-   <span id="LINT-2">LINT-2</span>: nakon oznake naslova stavite jedan obični razmak, primjerice `## Uvod`.

-   <span id="LINT-3">LINT-3</span>: nemojte koristiti sintaksu precrtanog teksta jer je remark-lint ne obrađuje dobro (drugi je razlog što su precrtani dijelovi uglavnom dosjetke koje čitatelju ne pomažu razumjeti sadržaj i ne zadovoljavaju [zahtjeve izražavanja](#CONT-5) iz odjeljka „Zahtjevi oblikovanja tekstualnog sadržaja” u nastavku).

-   <span id="LINT-4">LINT-4</span>: popisi:
    -   <span id="LINT-4.1">LINT-4.1</span>: prije popisa ostavite prazan redak i započnite novi odlomak.
    -   <span id="LINT-4.2">LINT-4.2</span>: u numeriranim popisima (primjerice `1. Primjer`) nakon točke stavite razmak.

-   <span id="LINT-5">LINT-5</span>: prije i poslije izdvojene formule ostavite po jedan prazan redak; inače će se tumačiti kao formula unutar retka.

-   <span id="LINT-6">LINT-6</span>: pri uporabi sintakse Details koja počinje s `???` ili `!!!`, svaki redak koji pripada okviru mora počinjati s najmanje 4 razmaka.

    **Čak i prazni redci moraju imati jednako uvlačenje kao ostali. Nemojte uključivati automatsko uklanjanje završnih razmaka u uređivaču.**

    ???+ success "Primjer"
        U sljedećem kodu `␣` predstavlja razmak ` `.
        
        ```text
        ???+ warning
        ␣␣␣␣Ne zaboravite dodati 4 razmaka ispred teksta. Ostala je sintaksa jednaka Markdownovoj.
        ␣␣␣␣
        ␣␣␣␣Bez 4 razmaka tekst se neće pojaviti unutar okvira Details.
        ␣␣␣␣
        ␣␣␣␣Što znači `???` objašnjeno je [u nastavku](#MDFM-5).
        ```
        
        ???+ warning "Upozorenje"
            Ne zaboravite dodati 4 razmaka ispred teksta. Ostala je sintaksa jednaka Markdownovoj.
            
            Bez 4 razmaka tekst se neće pojaviti unutar okvira Details.
            
            Što znači `???` objašnjeno je [u nastavku](#MDFM-5).

-   <span id="LINT-7">LINT-7</span>: za blok običnog teksta oblikovan kao kôd koristite ` ```text`. Ako koristite samo ` ``` ` bez navođenja jezika, sadržaj može biti pogrešno uvučen.

#### Uporaba interpunkcije

-   <span id="PUNC-1">PUNC-1</span>: svaku rečenicu završite **točkom**.

<!-- scripts.linter.postprocess.fix_full_stop off -->

-   <span id="PUNC-2">PUNC-2</span>: pravilno koristite interpunkciju **pune širine** i **polovične širine**. U kineskom koristite punu širinu, a u engleskom polovičnu. Pri miješanju kineskog i engleskog pogledajte [Uređivačka pravila za engleski tekst u kineskim publikacijama](https://www.nppa.gov.cn/xxgk/fdzdgknr/hybz/202210/t20221004_445147.html). Posebno, koristite točku pune širine „．” umjesto kineske kružne točke „。”.

<!-- scripts.linter.postprocess.fix_full_stop on -->

<!-- scripts.linter.postprocess.fix_quotation off -->

-   <span id="PUNC-3">PUNC-3</span>: budući da `“……”` i `‘……’` ne razlikuju punu i polovičnu širinu, koristite `「……」` za dvostruke navodnike pune širine, `"..."` za dvostruke navodnike polovične širine, `『……』` za jednostruke navodnike pune širine, a `'...'` za jednostruke navodnike polovične širine.

<!-- scripts.linter.postprocess.fix_quotation on -->

-   <span id="PUNC-4">PUNC-4</span>: razlikujte **kineski zarez za nabrajanje** i **obični zarez**.
-   <span id="PUNC-5">PUNC-5</span>: pazite na položaj **zagrada**. Zagrade unutar rečenice i one koje obuhvaćaju cijelu rečenicu stoje na različitim mjestima.
-   <span id="PUNC-6">PUNC-6</span>: za odnos složenih rečenica u popisu obično koristite **točku sa zarezom**.
-   <span id="PUNC-7">PUNC-7</span>: u numeriranom popisu preporučuje se svaku stavku završiti **točkom sa zarezom**, a posljednju **točkom**; u nenumeriranom popisu preporučuje se svaku stavku završiti **točkom**.
-   <span id="PUNC-8">PUNC-8</span>: razlikujte spojnicu (hyphen, obično zamijenjenu znakom U+002D hyphen-minus (-), odnosno „minusom” na tipkovnici), kratku crtu U+2013 en dash (–) i dugu crtu U+2014 em dash (—). (Pri povezivanju više osobnih imena u engleskom treba koristiti en dash, iako se vrlo često pogrešno koristi spojnica. Druge su pogreške rjeđe, pa je najvažnije zapamtiti ovo pravilo.) Pogledajte [Crtu na Wikipediji](https://en.wikipedia.org/wiki/Dash).

    ???+ success "Primjer"
        -   中学生学科竞赛主要包括信息学奥林匹克竞赛、信息学奥林匹克竞赛、信息学奥林匹克竞赛、信息学奥林匹克竞赛和信息学奥林匹克竞赛（谁写的这个示例，建议抬走）． (Predmetna natjecanja za srednjoškolce uglavnom uključuju informatičku olimpijadu, informatičku olimpijadu, informatičku olimpijadu, informatičku olimpijadu i informatičku olimpijadu (tko god je napisao ovaj primjer, neka ga odvedu).)
        -   「你吃了吗？」李四问张三． („Jesi li jeo?” upitao je Li Si Zhanga Sana.)
        -   我想对你说：「我真是太喜欢你了．」 (Želim ti reći: „Zaista mi se jako sviđaš.”)
        -   「苟利国家生死以，岂因祸福避趋之！」 („Ako to koristi zemlji, dat ću i život; zar da biram prema vlastitoj sreći ili nesreći!”)
        -   张华考上了大学；李萍进了技校；我当了工人：我们都有美好的前途．[^note1] (Zhang Hua upisao je fakultet; Li Ping krenula je u strukovnu školu; ja sam postao radnik: svi imamo svijetlu budućnost.)
        -   以下是这个算法的基本流程： (Osnovni je postupak algoritma sljedeći:)
            1.  初始化到各点的距离为无穷大，将所有点设置为未被访问过，初始化一个队列； (postavite udaljenosti do svih vrhova na beskonačno, označite sve vrhove neposjećenima i inicijalizirajte red;)
            2.  将起点放入队列，将起点设置为已被访问过，更新到起点的距离为 $0$； (dodajte početni vrh u red, označite ga posjećenim i postavite njegovu udaljenost na 0;)
            3.  取出队首元素，将该元素设置为未被访问过； (izvadite prvi element reda i označite ga neposjećenim;)
            4.  遍历所有与此元素相连的边，若到这个点存在更短的距离，则进行松弛操作； (prođite svim bridovima povezanima s tim elementom i provedite relaksaciju ako postoji kraći put do vrha;)
            5.  若这个点未被访问过，则将这个点放入队列，且设置这个点为已经访问过； (ako vrh nije posjećen, dodajte ga u red i označite posjećenim;)
            6.  回到第三步，直到队列为空． (vratite se na treći korak dok red ne bude prazan.)
        -   KMP 算法（Knuth–Morris–Pratt algorithm, KMP algorithm）由 Knuth、Pratt 和 Morris 在 1977 年共同发布．[^note2] (KMP algoritam (Knuth–Morris–Pratt algorithm, KMP algorithm) zajednički su objavili Knuth, Pratt i Morris 1977. godine.)

#### Zahtjevi oblikovanja Markdowna i proširenja teme

-   <span id="MDFM-1">MDFM-1</span>: za isticanje koristite `**SOMETHING**` i navodnike, a ne naslove bilo koje razine, jer naslovi narušavaju hijerarhiju članka i/ili uzrokuju probleme sa sadržajem.

-   <span id="MDFM-2">MDFM-2</span>: pri povezivanju zadataka, kad god je moguće, koristite poveznicu na izvorni OJ umjesto zrcalne poveznice.

-   <span id="MDFM-3">MDFM-3</span>: pravilno koristite Markdownove blokove. Kôd unutar retka omeđite parom obrnutih apostrofa, a izdvojeni kôd parom oznaka ` ``` `. Obrnuti apostrof je znak ispod tilde u gornjem lijevom dijelu tipkovnice. Za izdvojeni kôd nakon prvog ` ``` ` navedite jezik (primjerice ` ```cpp`).

    ???+ success "Primjer"
        ````text
        ```cpp
        // #include<stdio.h>    //Loš način
        #include <cstdio>  //Dobar način
        ```
        ````
        
        ```cpp
        // #include<stdio.h>    //Loš način
        #include <cstdio>  //Dobar način
        ```

-   <span id="MDFM-4">MDFM-4</span>: odjeljak „Literatura i napomene” pišite Markdownovim fusnotama. Oblik je:

    ```markdown
    Tekst.[^naziv-fusnote]
    [^naziv-fusnote]: Sadržaj izvora. Napomena: koristite običnu dvotočku, iza koje slijedi razmak.
    ```

    Nazivi fusnota mogu biti brojevi ili tekst. Položaj oznake fusnote slijedi pravila za zagrade. Radi urednosti koristite isti obrazac naziva na cijeloj stranici, primjerice ref1, ref2, note1…

    Sadržaj svih fusnota stavite pod naslov druge razine `## Literatura i napomene`.

    ???+ success "Primjer"
        ```markdown
        Kada `#include <cxxxx>` može zamijeniti `#include <xxxx.h>`, koristite prvi oblik.[^ref1]
        
        CCF je 21. siječnja 2020. objavio povratak NOIP-a.[^ref2]
        
        ## Literatura i napomene
        
        [^ref1]: [cstdio stdio.h namespace](https://stackoverflow.com/questions/10460250/cstdio-stdio-h-namespace)
        
        [^ref2]: [CCF-ova obavijest o povratku natjecanja NOIP - China Computer Federation](https://www.ccf.org.cn/c/2020-01-21/694716.shtml)
        ```
        
        Kada `#include <cxxxx>` može zamijeniti `#include <xxxx.h>`, koristite prvi oblik.[^ref1]
        
        CCF je 21. siječnja 2020. objavio povratak NOIP-a.[^ref2]

-   <span id="MDFM-5">MDFM-5</span>: za tekstove zadataka i referentni kôd preporučuje se proširena sintaksa teme `???+note` (odnosno [Collapsible Blocks](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#collapsible-blocks)). Možete je koristiti i za druge dodatne sadržaje koje treba predstaviti.

    Primjer koda (u nastavku `␣` predstavlja razmak ` `):

    ```text
    ??? note "Naslov"
    ␣␣␣␣Ovaj je okvir zadano sklopljen.
    ␣␣␣␣
    ␣␣␣␣Preporučuje se staviti **kôd rješenja** u sklopivi okvir.

    ???+note "[HDOJ-ov zadatak „A + B Problem”](https://acm.hdu.edu.cn/showproblem.php?pid=1000)"
    ␣␣␣␣Naslov može sadržavati Markdown poveznicu. Ovdje poveznica vodi na HDOJ-ov zadatak „A + B Problem”.
    ␣␣␣␣
    ␣␣␣␣Preporučuje se tako **navesti poveznicu na izvorni zadatak**.
    ␣␣␣␣
    ␣␣␣␣Pazite na položaj dvostrukih navodnika.
    ```

    Prikaz:

    ??? note "Naslov"
        Ovaj je okvir zadano sklopljen.
        
        Preporučuje se staviti **kôd rješenja** u sklopivi okvir.

    ???+ note "[HDOJ-ov zadatak „A + B Problem”](https://acm.hdu.edu.cn/showproblem.php?pid=1000)"
        Naslov može sadržavati Markdown poveznicu. Ovdje poveznica vodi na HDOJ-ov zadatak „A + B Problem”.
        
        Preporučuje se tako **navesti poveznicu na izvorni zadatak**.
        
        Pazite na položaj dvostrukih navodnika.

    Razlika je u tome što je okvir s `+` zadano otvoren, a okvir bez `+` zadano sklopljen.

    Naslov sklopivog okvira, odnosno sadržaj iza `note` u `???+note`, treba omeđiti znakovima `"`. U njemu je podržana Markdown sintaksa. Pogledajte [Admonition - Changing the title](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#changing-the-title). (Okviri bez mogućnosti sklapanja obični su Admonitions; pogledajte [Admonitions - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/admonitions).)

-   <span id="MDFM-6">MDFM-6</span>: za kôd u više programskih jezika preporučuju se kartice sadržaja (Content tabs), koje omogućuju prebacivanje između jezika. Kartice imaju i druge namjene; pogledajte [Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#usage). Njihova uporaba i prikaz navedeni su ispod.

    ???+ success "Primjer"
        Ispred teksta dodajte 4 razmaka (u nastavku prikazana kao `␣`). Ostala je sintaksa jednaka Markdownovoj.
        
        ````text
        === "C"
        ␣␣␣␣```c
        ␣␣␣␣#include <stdio.h>
        ␣␣␣␣
        ␣␣␣␣int main(void) {
        ␣␣␣␣  printf("Hello world!\n");
        ␣␣␣␣  return 0;
        ␣␣␣␣}
        ␣␣␣␣```
        
        === "C++"
        ␣␣␣␣```cpp
        ␣␣␣␣#include <iostream>
        ␣␣␣␣
        ␣␣␣␣int main(void) {
        ␣␣␣␣  std::cout << "Hello world!" << std::endl;
        ␣␣␣␣  return 0;
        ␣␣␣␣}
        ␣␣␣␣```
        ````
        
        === "C"
            ```c
            #include <stdio.h>
            
            int main(void) {
              printf("Hello world!\n");
              return 0;
            }
            ```
        
        === "C++"
            ```cpp
            #include <iostream>
            
            int main(void) {
              std::cout << "Hello world!" << std::endl;
              return 0;
            }
            ```

Ako imate dodatnih pitanja o mkdocs-materialu (temi koju koristimo), pogledajte [Upute za MkDocs](https://github.com/ctf-wiki/ctf-wiki/wiki/Mkdocs-%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E), gdje je objašnjena uporaba dodataka te teme.

#### Zahtjevi oblikovanja tekstualnog sadržaja

-   <span id="CONT-1">CONT-1</span>: svako pojavljivanje naziva **OI Wiki** treba biti podebljano.

-   <span id="CONT-2">CONT-2</span>: na početku stranice napišite kratak tekst koji sažima njezin sadržaj (primjerice „Ova stranica predstavlja…”).

    ???+ success "Primjer"
        Ova stranica navodi preporučena pravila oblikovanja i uređivačke smjernice za pisanje **OI Wikija**.

-   <span id="CONT-3">CONT-3</span>: ako stranica zahtijeva predznanje, na početak, prije sažetka sadržaja, dodajte redak **Predznanje: …**. Oblik je:

    `Predznanje: [Interna stranica 1](url1), [Interna stranica 2](url2) i [Interna stranica 3](url3)`

    ???+ success "Primjer"
        Predznanje: [Vremenska složenost](../basic/complexity.md)
        
        Ova stranica predstavlja osnove teorije izračunljivosti.

-   <span id="CONT-4">CONT-4</span>: pazite na strukturu dokumenta. Mora biti uredna i imati jasnu hijerarhiju. Nemojte ponovno koristiti „naslove pete razine”; običnom članku nije potrebna toliko složena struktura.

-   <span id="CONT-5">CONT-5</span>: pazite na izražavanje. Kao enciklopedijska stranica, **OI Wiki** treba koristiti formalan i objektivan jezik. Dosjetke i drugi sadržaji koji čitatelju ne pomažu razumjeti temu ne pripadaju **OI Wikiju**.

-   <span id="CONT-6">CONT-6</span>: poveznicama dajte potpune naslove ili prepoznatljive opise. Izbjegavajte gole adrese i nejasne opise poput „ovo” ili „ovdje”. Svaku poveznicu opišite što jasnije kako bi čitatelji znali kamo vodi.

    Preporučuje se naslov izvornog članka ili kartice preglednika.

    ???+ failure "Nepreporučeni oblik"
        ```markdown
        Pogledajte [ovu stranicu](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
        
        Pogledajte <https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork>
        ```
        
        Pogledajte [ovu stranicu](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
        
        Pogledajte <https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork>

    ???+ success "Preporučeni oblik"
        ```markdown
        Pogledajte službenu GitHubovu stranicu pomoći [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
        ```
        
        Pogledajte službenu GitHubovu stranicu pomoći [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)

-   <span id="CONT-7">CONT-7</span>: zbog ograničenja Markdowna naslov druge razine `## Literatura i napomene` mora biti na kraju dokumenta.

-   <span id="CONT-8">CONT-8</span>: redne brojeve preporučuje se pisati kineskim riječima. Primjeri:
    -   Prvi član niza.
    -   Prvi redak ulazne datoteke.

-   <span id="CONT-9">CONT-9</span>: izbjegavajte MathJax formule u naslovima bilo koje razine jer mogu uzrokovati pogrešan prikaz sadržaja.[^ref3]

-   <span id="CONT-10">CONT-10</span>: pazite na čitljivost koda.

    -   <span id="CONT-10.1.1">CONT-10.1.1</span>: kôd treba imati jasnu logiku i biti što jednostavniji i razumljiviji. Nemojte ga pretjerano zbijati u retke ni dodavati previše nepovezanog koda. Izbjegavajte sadržaje koji nisu povezani s idejom algoritma.
    -   <span id="CONT-10.1.2">CONT-10.1.2</span>: preporučuje se dodati prikladne komentare u referentni kôd radi lakšeg razumijevanja.

    Za jezike poput C-a i C++-a:

    -   <span id="CONT-10.2.1">CONT-10.2.1</span>: izbjegavajte pretprocesorske direktive i makronaredbe koje otežavaju čitanje.

    -   <span id="CONT-10.2.2">CONT-10.2.2</span>: nemojte koristiti `0` umjesto `false`/`NULL`/`nullptr` i sličnoga, ni `1` umjesto `true` i sličnoga.

    -   <span id="CONT-10.2.3">CONT-10.2.3</span>: pri deklariranju [aliasa tipa](https://en.cppreference.com/w/cpp/language/type_alias) preporučuje se `using`, a ne `typedef`.

    -   <span id="CONT-10.2.4">CONT-10.2.4</span>: ne preporučuje se definirati konstante makronaredbama; izravno koristite ključne riječi poput `constexpr`/`const`.

    -   <span id="CONT-10.2.5">CONT-10.2.5</span>: za funkcije se ne preporučuje ključna riječ `inline`; pogledajte [Optimizacije prevoditelja](../lang/optimizations.md#inline---内联).

    -   <span id="CONT-10.2.6">CONT-10.2.6</span>: izbjegavajte složene tehnike metaprogramiranja predlošcima poput type traitsa i djelomične specijalizacije. Ako su nužne, objasnite ih komentarima.

        ???+ failure "Nepreporučeni oblik"
            ```cpp
            --8<-- "docs/intro/code/format/format_1.cpp:not-recommended"
            ```
            
            Ovaj kôd daje složenu implementaciju izračuna [najvećega zajedničkog djelitelja](../math/number-theory/gcd.md), u kojoj:
            
            -   prvi `gcd` prima dva cijela broja bez predznaka `x`, `y` i vraća njihov najveći zajednički djelitelj; raspon povratnog tipa sigurno obuhvaća i `x` i `y`.
            -   Drugi `gcd` prima dva cijela broja `x`, `y`, od kojih je barem jedan s predznakom, i vraća njihov najveći zajednički djelitelj.
            -   Treći `gcd` prima više od dva cijela broja i vraća njihov najveći zajednički djelitelj.
            -   Četvrti `gcd` prima spremnik i vraća najveći zajednički djelitelj svih brojeva u njemu.
            
            Na **OI Wikiju** zanima nas samo ideja algoritma za najveći zajednički djelitelj. Ovaj kôd sadrži previše nepovezanih i složenih tehničkih pojedinosti te ga treba izbjegavati.

        ???+ success "Preporučeni oblik"
            ```cpp
            --8<-- "docs/intro/code/format/format_1.cpp:recommended"
            ```
            
            „Dodavanje provjere tipova”, „obrada negativnog ulaza” i „podrška funkcije za više argumenata” više su inženjerske teme; naš naglasak uvijek treba biti na ideji algoritma.

#### Zahtjevi oblikovanja LaTeX formula

LaTeX je prvi izbor za slaganje formula i treba ga pravilno koristiti. Stoga imamo stroge zahtjeve za njegovu uporabu. Za brz početak možete pročitati tablicu na kraju ovog odjeljka.

-   <span id="MATH-1.1">MATH-1.1</span>: simboli koje koristite ne smiju biti u suprotnosti s [tablicom matematičkih simbola](./symbol.md).

-   <span id="MATH-1.2">MATH-1.2</span>: koristite uspravni slog (Roman) za brojeve, konstante, operatore i funkcije, a kurziv (Italic) za varijable i indekse. LaTeX već definira neke česte konstante, funkcije, operatore i slično, koje možemo izravno koristiti, uključujući, ali ne ograničavajući se na:

    ```latex
    \log, \ln, \lg, \sin, \cos, \tan, \sec, \csc, \cot, \gcd, \min, \max, \exp, \inf, \mod, \bmod, \pmod
    ```

    Zato pri unosu konstanti, naziva funkcija, operatora i sličnoga prvo provjerite treba li koristiti uspravni slog ili neki drugi font. Za zapis LaTeX simbola pogledajte [KaTeXovu stranicu Supported Functions](https://katex.org/docs/supported.html) (nije potpun popis) ili potražite odgovor pretragom.

    Budući da je u LaTeXu teško dobiti uspravna mala grčka slova, konstante, operatori i funkcije s takvim slovima mogu biti u kurzivu, primjerice $\pi$ te $\delta x$ s oznakom $\delta$.

    Za **naziv funkcije** koji nije unaprijed definiran, a treba biti uspravan, koristite `$\operatorname{something}$`; primjerice `$\operatorname{lcm}$` daje uspravnu oznaku (funkcije) najmanjega zajedničkog višekratnika. Slično, za uspravne **konstante** koristite `$\mathrm{}$`, za podebljane uspravne simbole `$\mathbf{}$`, a za podebljane simbole u kurzivu `$\boldsymbol{}$` (primjerice vektor $\boldsymbol{a}$). Za višeslovne varijable koristite `$\textit{}$`. Sav ostali nematematički sadržaj, uključujući engleski tekst i posebne znakove, pišite s `$\text{}$`. Kineski tekst preporučujemo ne stavljati u LaTeX formule.

-   <span id="MATH-1.3">MATH-1.3</span>: ako izraz treba prelomiti u više redaka (često kod dugih izdvojenih formula), slijedite ova pravila:

    -   <span id="MATH-1.3.1">MATH-1.3.1</span>: prijelom retka stavite prije $=$, $+$, $-$, $\pm$, $\mp$, a po potrebi i prije $\times$, $\cdot$, $/$, primjerice:

        $$
        \begin{aligned}
            \mathrm{e}^x &= \sum\limits_{n=0}^{\infty} \frac{x^n}{n!} \\
            &= \phantom{+} 1 + x + \frac{x^2}{2} \\
            & \phantom{=} + \frac{x^3}{6} + \frac{x^4}{24} + \dots \\
        \end{aligned}
        $$

    -   <span id="MATH-1.3.2">MATH-1.3.2</span>: isti se operator ne smije pojaviti i prije i poslije prijeloma retka,

    -   <span id="MATH-1.3.3">MATH-1.3.3</span>: izbjegavajte prijelome retka unutar izraza u zagradama.

-   <span id="MATH-1.4">MATH-1.4</span>: za razlomke unutar retka koristite `$\dfrac{}{}$`. Primjerice, `$\dfrac{1}{2}$` daje $\dfrac{1}{2}$, umjesto `$\frac{1}{2}$`, što daje $\frac{1}{2}$.

-   <span id="MATH-1.5">MATH-1.5</span>: za binomne koeficijente koristite `\dbinom{n}{m}`, što daje $\dbinom{n}{m}$, umjesto `{n \choose m}` (taj se oblik u LaTeXu više ne preporučuje). Kao kod prethodnog pravila o razlomcima, nemojte koristiti `\binom{n}{m}`, što daje $\binom{n}{m}$.

-   <span id="MATH-1.6">MATH-1.6</span>: izbjegavajte velike operatore unutar retka (poput $\sum$, $\prod$, $\int$).

-   <span id="MATH-1.7">MATH-1.7</span>: kada nema dvosmislenosti, umjesto zvjezdice koristite `$\times$`; za vektorski produkt koristite `$\times$`, a za skalarni `$\cdot$`. Primjerice $a\times b$, $a\cdot b$, a ne $a\ast b$.

-   <span id="MATH-1.8">MATH-1.8</span>: umjesto `$...$` koristite `$\cdots$` (na srednjoj visini), `$\ldots$` (na osnovnoj crti) ili `$\vdots$` (okomita trotočka). Primjerice $a_1,a_2,\cdots a_n$, a ne $a_1,a_2,... a_n$.

-   <span id="MATH-1.9">MATH-1.9</span>: izvan koda nemojte koristiti zapise programskih jezika, nego LaTeX formule. Primjerice, koristite `$=$`, a ne `$==$` ($a=b$, a ne $a==b$); `` `a<<1` `` ili `$a\times 2$`, a ne `$a<<1$`; `$a\bmod b$`, a ne `$a\%b$` ($a\bmod b$, a ne $a\%b$).

-   <span id="MATH-1.10">MATH-1.10</span>: u formulama nemojte nizati uglate zagrade (zapis višedimenzionalnih polja u C++-u), nego koristite indekse: $a_{i,j,k}$, a ne $a[i][j][k]$. Za složenije indekse preporučuje se viševarijabilna funkcija ($f(i,j,k)$) ili zapis koda unutar retka. Za jednostavne funkcije jedne varijable prihvatljivi su `$f_i$`, `$f(i)$` i `$f[i]$`.

-   <span id="MATH-1.11">MATH-1.11</span>: radi dosljednosti i jednostavnijeg pisanja, u analizi složenosti veliko $O$ pišite kao `$O()$`, a ne `$\mathcal O()$`.

-   <span id="MATH-1.12">MATH-1.12</span>: za ekvivalenciju koristite `$\iff$`, što daje $\iff$, a ne `$\Leftrightarrow$`, što daje $\Leftrightarrow$.

-   <span id="MATH-1.13">MATH-1.13</span>: okruženje `cases` za funkcije zadane po dijelovima **smije imati samo dva stupca** (jedan razdjelnik `&`).

-   <span id="MATH-1.14">MATH-1.14</span>: nemojte pretjerivati s LaTeX formulama. Time se stranica sporije učitava (MathJax je poznat po neučinkovitosti), a raspored može postati neuredan. LaTeX matematički font obično koristimo za nazive varijabli. Preporučujemo izbjegavati nepotrebno **učestalo** miješanje formula i običnog teksta te formule koje nisu nužne. Primjerice:

    ```LaTeX
    我们将要学习 $Network-flow$ 中的 $SPFA$ 最小费用流，需要使用 $Edmonds–Karp$ 算法进行增广．
    ```

    To je tipičan primjer **zlouporabe matematičkog fonta**. (Za kurziv na stranici koristite `*tekst*`.) (Učit ćemo SPFA za tok najmanje cijene iz područja Network-flow, koristeći algoritam Edmonds–Karp za povećavanje toka.)

-   <span id="MATH-1.15">MATH-1.15</span>: koristite odgovarajuće LaTeX simbole, osobito grčka slova i druge posebne simbole u formulama. Primjerice, za Eulerovu funkciju koristite `$\varphi$`, za promjer kružnice `$\Phi$`, a za zlatni rez `$\phi$`. Iako svi označavaju grčko slovo fi, imaju različita značenja u različitim kontekstima. **Nemojte ih umetati funkcijom za posebne znakove svog načina unosa.**

    Zbog povijesnih razloga u LaTeXu, prazni skup označava se s `$\varnothing$`, a ne `$\emptyset$`; ostale simbole pišite prema [tablici matematičkih simbola](./symbol.md).

Prethodna pravila možemo sažeti tablicom. Ona ne prikazuje uporabu svih simbola, nego samo česte pogreške. Na slične situacije primijenite ista načela.

| Neispravan zapis | Prikaz | Ispravan zapis | Prikaz |
| ---------------------------- | ----------------- | ---------------------------------------- | ----------------------------------- |
| `$log, ln, lg$`              | $log, ln, lg$     | `$\log$, $\ln$, $\lg$`                   | $\log$, $\ln$, $\lg$                  |
| `$sin, cos, tan$`            | $sin, cos, tan$   | `$\sin$, $\cos$, $\tan$`                 | $\sin$, $\cos$, $\tan$                |
| `$gcd, lcm$`                 | $gcd, lcm$        | `$\gcd$, $\operatorname{lcm}$`           | $\gcd$, $\operatorname{lcm}$         |
| `$e$, $\text{e}$, e` (baza prirodnog logaritma) | $e$, $\text{e}$, e | `$\mathrm{e}$` | $\mathrm{e}$ |
| `$i$, $\text{i}$, i` (imaginarna jedinica) | $i$, $\text{i}$, i | `$\mathrm{i}$` | $\mathrm{i}$ |
| `$ 小于 a 的质数 $`               | $小于 a 的质数$        | `小于 $a$ 的质数`                             | 小于 $a$ 的质数 (prosti brojevi manji od a) |
| `$...$`                      | $...$             | `$\cdots$, $\ldots$, $\vdots$, $\ddots$` | $\cdots$, $\ldots$, $\vdots$, $\ddots$ |
| `$a*b$` (množenje dvaju brojeva) | $a*b$ | `$a\times b$, $a\cdot b$` | $a\times b$, $a\cdot b$ |
| `$SPFA$` (engleski naziv) | $SPFA$ | `SPFA` | SPFA |
| `$a==b$`                     | $a==b$            | `$a=b$`                                  | $a=b$                               |
| `$f[i][j][k]$`               | $f[i][j][k]$      | `$f_{i,j,k}$, $f(i,j,k)$`                | $f_{i,j,k}$, $f(i,j,k)$              |
| `$R,N^*$` (skupovi) | $R,N^*$ | `$\mathbf{R}$, $\mathbf{N}^*$` | $\mathbf{R}$, $\mathbf{N}^*$ |
| `$\emptyset$`                | $\emptyset$       | `$\varnothing$`                          | $\varnothing$                       |
| `$size$`                     | $size$            | `$\textit{size}$`                        | $\textit{size}$                     |

#### Dodatni zahtjevi oblikovanja matematičkih formula

Iako je navedena sintaksa formula vrlo slična pravom LaTeX sustavu za slaganje teksta, **MathJax i LaTeX dva su potpuno nepovezana sustava**. MathJax koristi samo dio sintakse vrlo slične LaTeXu. U detaljima postoje brojne razlike zbog kojih formule često nisu prenosive između njih.

Budući da je **OI Wiki** razvio alat za izvoz PDF-a s LaTeXovim mehanizmom slaganja, važno je naglasiti kompatibilnost formula između MathJaxa i LaTeXa. **Pri pisanju matematičkih formula na wikiju obratite pozornost na sljedeće.**

Ova su pravila već što više prilagođena MathJaxu. Alat za izvoz podržava i neke zapise koji su izvorno ispravno radili samo u MathJaxu.

-   <span id="MATH-2.1">MATH-2.1</span>: za višeredne poravnate formule koristite `\begin{aligned} ... \end{aligned}`;

-   <span id="MATH-2.2">MATH-2.2</span>: ako te formule trebaju biti **numerirane**, koristite okruženje `align` ili `equation`;

-   <span id="MATH-2.3">MATH-2.3</span>: nemojte koristiti okruženja `split` i `eqnarray`;

-   <span id="MATH-2.4">MATH-2.4</span>: za znakove manje i veće nemojte koristiti `\lt`, `\gt`, nego izravno `<`, `>`;

-   <span id="MATH-2.5">MATH-2.5</span>: nemojte izravno koristiti `\\` za novi redak (formule koje treba prelomiti stavite u `aligned` ili drugo višeredno okruženje);

-   <span id="MATH-2.6">MATH-2.6</span>: za LaTeXov logotip $\rm{\LaTeX}$ koristite `$\rm{\LaTeX}$`, a ne `mathrm`; (`\LaTeX` u TeXu nije dopušten u matematičkom načinu, dok `\mathrm` nije dopušten u običnom načinu; premda `\text` ispravno radi u TeXu, MathJax argument naredbe `\text` ispisuje doslovno umjesto da obradi naredbe);

-   <span id="MATH-2.7">MATH-2.7</span>: kineski tekst u matematičkim formulama **mora biti unutar naredbe `\text{}`**, dok varijable, brojevi, operatori i nazivi funkcija moraju biti izvan nje. **Nemojte ugnježđivati matematičke formule u `\text{}`**;

-   <span id="MATH-2.8">MATH-2.8</span>: u okruženju `array` **broj stvarnih stupaca mora odgovarati broju oznaka poravnanja**. Primjerice, u sljedećoj formuli podaci imaju 3 stupca (`&` je razdjelnik stupaca), pa trebaju 3 oznake poravnanja (`l`/`r`/`c` znače lijevo/desno/središnje poravnanje).

    ```latex
    $$
    \begin{array}{lll}
    F_1=\{\frac{0}{1},&&\frac{1}{1}\}\\
    F_2=\{\frac{0}{1},&\frac{1}{2},&\frac{1}{1}\}\\
    \end{array}
    $$
    ```

#### Oblik pseudokoda

Nema strogih zahtjeva za konkretan oblik pseudokoda; pogledajte Uvod u algoritme (Introduction to Algorithms) ili znanstvene radove. Nemojte ga pisati kao Python.

<span id="PCOD-1">PCOD-1</span>: na Wikiju pseudokod pišemo u LaTeXu, cijeli unutar okruženja array. Za uvlačenje koristite `$\qquad$`, za tekstualne opise `$\text$`, za ključne riječi `$\textbf$`, za višeslovne varijable `$\textit$`, a za pridruživanje `$\gets$`.

Primjer:

$$
\begin{array}{l}
\textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v, w) \\
\text{ denoting that there is an edge between } u \text{ and } v \text{ weighted } w . \\
\textbf{Output. } \text{The edges of the MST of the input graph}. \\
\textbf{Method. } \\
\begin{array}{ll} 
1 &  \textit{result} \gets \varnothing \\
2 &  \text{sort } e \text{ into nondecreasing order by weight } w \\ 
3 &  \textbf{for} \text{ each } (u, v, w) \text{ in the sorted } e \\ 
4 &  \qquad \textbf{if } u \text{ and } v \text{ are not connected in the union-find set } \\
5 &  \qquad\qquad \text{connect } u \text{ and } v \text{ in the union-find set} \\
6 &  \qquad\qquad \textit{result} \gets \textit{result}\;\bigcup\ \{(u, v, w)\} \\
7 &  \textbf{return } \textit{result}
\end{array}
\end{array}
$$

```latex
$$
\begin{array}{l}
\textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v, w) \\
\text{ denoting that there is an edge between } u \text{ and } v \text{ weighted } w . \\
\textbf{Output. } \text{The edges of the MST of the input graph}. \\
\textbf{Method. } \\
\begin{array}{ll} 
1 &  \textit{result} \gets \varnothing \\
2 &  \text{sort } e \text{ into nondecreasing order by weight } w \\ 
3 &  \textbf{for} \text{ each } (u, v, w) \text{ in the sorted } e \\ 
4 &  \qquad \textbf{if } u \text{ and } v \text{ are not connected in the union-find set } \\
5 &  \qquad\qquad \text{connect } u \text{ and } v \text{ in the union-find set} \\
6 &  \qquad\qquad \textit{result} \gets \textit{result}\;\bigcup\ \{(u, v, w)\} \\
7 &  \textbf{return } \textit{result}
\end{array}
\end{array}
$$
```

#### Zahtjevi oblikovanja blokova koda

Trenutačno postoje dvije vrste blokova koda: isječci i primjeri zadataka.

O isječcima koda:

-   <span id="CODE-1.1">CODE-1.1</span>: ako je isječak dovoljno kratak i nije ga potrebno testirati, možete ga izravno mijenjati u Markdown dokumentu.
-   <span id="CODE-1.2">CODE-1.2</span>: budući da je teško automatizirati testiranje koda ugrađenog u Markdown dokumente, preporučuje se umetati isječke u obliku koda za primjere zadataka. Možete koristiti [kompiliranje više datoteka](https://github.com/OI-wiki/OI-wiki/pull/5729) ili sintaksu [Snippet Sections](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippet-sections):

    Primjer kompiliranja više datoteka: [bubble sort](https://github.com/OI-wiki/OI-wiki/blob/c35defebff6cea072d6cfeb359642f6fd84e66c7/docs/basic/bubble-sort.md?plain=1#L48). U tekst je uključen [bubble-sort\_1.cpp](https://github.com/OI-wiki/OI-wiki/blob/c35defebff6cea072d6cfeb359642f6fd84e66c7/docs/basic/code/bubble-sort/bubble-sort_1.cpp), a testni kôd nalazi se u [bubble-sort\_1.aux1.cpp](https://github.com/OI-wiki/OI-wiki/blob/c35defebff6cea072d6cfeb359642f6fd84e66c7/docs/basic/code/bubble-sort/bubble-sort_1.aux1.cpp).

    Primjer sintakse Snippet Sections: [prefiksne sume](https://github.com/OI-wiki/OI-wiki/blob/c7cf6d6de13b44757f1d0528e952349beb921f8a/docs/basic/prefix-sum.md?plain=1#L37). U tekst nije potrebno uključiti testni dio datoteke [prefix-sum\_1.cpp](https://github.com/OI-wiki/OI-wiki/blob/c7cf6d6de13b44757f1d0528e952349beb921f8a/docs/basic/code/prefix-sum/prefix-sum_1.cpp), pa se umeće samo glavni isječak koda.

    **Napomena**: nemojte koristiti sintaksu [Snippet Lines](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippet-lines).

    Za bolju ponovnu uporabu koda možete ga razdvojiti u datoteke zaglavlja, koje zatim uključujete u različite testne programe. Ako tekst treba sadržavati potpun testni program kao referentnu implementaciju za primjer zadatka, u tekstu dodatno sastavite kôd u jednu datoteku sintaksom Snippet Sections radi lakšeg čitanja. Primjer: [crveno-crno stablo](https://github.com/OI-wiki/OI-wiki/blob/3b721e22ea60d59a2687a9b10555263de7bdc2f0/docs/ds/rbtree.md?plain=1#L218-L231).

O kodu za primjere zadataka:

-   <span id="CODE-2.1">CODE-2.1</span>: kôd primjera zadatka uključuje se kao `--8<-- "path"`, pri čemu je sav kôd pohranjen na putanji `path`. Putanja je obično `docs/主题/code/内容/内容_编号.cpp` (tema/sadržaj/sadržaj_broj).

-   <span id="CODE-2.2">CODE-2.2</span>: pri izmjeni koda primjera zadatka provjerite da je kôd ispravan. Svaki takav primjer ima skup testnih podataka pohranjen u `/docs/主题/examples/内容/内容_编号.in/ans` (tema/sadržaj/sadržaj_broj).

Ako trebate dodati primjer zadatka:

-   Dodajte kôd primjera u `docs/主题/code/内容` i dodijelite mu broj. U toj mapi `内容` (sadržaj) obično već postoji jedan ili više primjera koda. Na primjer, za izmjenu koda za `dag.md` putanja je `docs/dp/code/dag`, gdje je `dp` tema, a `dag` sadržaj.

-   Ako želite dodati kôd primjera nakon svih postojećih primjera, nastavite trenutačno numeriranje. Primjerice, ako već postoji `code/prefix-sum/prefix-sum_3.cpp`, za primjer nakon posljednjega nazovite svoj kôd `prefix-sum_4.cpp` i dodajte ga u `docs/basic/code/prefix-sum`.

-   Ako želite dodati kôd primjera usred članka, umetnite ga i promijenite postojeće brojeve. Primjerice, ako postoje `prefix-sum_2.cpp` i `prefix-sum_3.cpp`, a želite umetnuti primjer između drugoga i trećega, nazovite svoj kôd `prefix-sum_3.cpp`, preimenujte stari `prefix-sum_3.cpp` u `prefix-sum_4.cpp` te **istodobno promijenite brojeve u Markdown dokumentu i mapi s testnim podacima**.

-   **Ne zaboravite dodati i skup testnih podataka za svoj kôd kako biste provjerili da se uspješno izvršava.** Dodajte ih u mapu `docs/主题/examples/内容`, ulaz spremite kao `内容_编号.in`, a očekivani odgovor kao `内容_编号.ans`.

-   Na kraju možete uključiti kôd u dokument. Dodajte blok koda i u njega izravno napišite `--8<-- "你的代码路径"` (putanja vašega koda).

**OI Wiki** testira kôd primjera zadataka na svim platformama. Da bi vaš kôd prošao testove, slijedite ova pravila:

-   <span id="CODE-3.1">CODE-3.1</span>: vaš se kôd mora moći prevesti i izvršiti prema standardima C++14, C++17 i C++20.
-   <span id="CODE-3.2">CODE-3.2</span>: nemojte koristiti nestandardna zaglavlja poput `<bits/stdc++.h>` i `<bits/extc++.h>`.
-   <span id="CODE-3.3">CODE-3.3</span>: datoteke očekivanih odgovora ne smiju sadržavati suvišne razmake.
-   <span id="CODE-3.4">CODE-3.4</span>: nemojte koristiti [alternativne tokene](https://en.cppreference.com/w/cpp/language/operator_alternative#Alternative_tokens).
-   <span id="CODE-3.5">CODE-3.5</span>: pri [agregatnoj inicijalizaciji](https://en.cppreference.com/w/cpp/language/aggregate_initialization) zapis `object{args}` ne smijete zamijeniti s `(object){args}`.
-   <span id="CODE-3.6">CODE-3.6</span>: pri [preopterećenju operatora](https://en.cppreference.com/w/cpp/language/operators) pazite na oblik; primjerice, kod preopterećenja operatora usporedbe članskom funkcijom ne smijete izostaviti kvalifikator `const`.
-   <span id="CODE-3.7">CODE-3.7</span>: nemojte koristiti makronaredbe poput `#define int long long`.
-   <span id="CODE-3.8">CODE-3.8</span>: ako trebate C-ov [formatirani ulaz/izlaz](https://en.cppreference.com/w/cpp/io/c#Formatted_input.2Foutput), posebno pazite na specifikatore formata: za `size_t` koristite `%zu`, a za `ptrdiff_t` `%td`. Primjerice, veličinu STL spremnika ispišite kodom poput `printf("%zu", container.size());`.
-   <span id="CODE-3.9">CODE-3.9</span>: zbog [BUG-a](https://github.com/actions/runner-images/issues/8659) u biblioteci `<chrono>` implementacije libstdc++ u trenutačnom testnom okruženju, izbjegavajte `<chrono>`.
-   <span id="CODE-3.10">CODE-3.10</span>: tipovi `long` i `unsigned long` u nekim su testnim okruženjima 32-bitni, a u drugima 64-bitni. Radi jednakog ponašanja na svim platformama ne preporučuju se ta dva tipa, nego [cjelobrojni tipovi fiksne širine](../lang/var.md#定宽整数类型).
-   <span id="CODE-3.11">CODE-3.11</span>: ne preporučuju se nestandardne značajke poput `__gcd`, `__int128` i funkcija iz obitelji `__builtin_`. Ako su potrebne, morate osigurati prolazak testova na svim platformama. Primjerice, [ovaj kôd](https://github.com/OI-wiki/OI-wiki/blob/4af83d6db6017f4c36db6d4a7583bbc3f6257484/docs/ds/code/tree-decompose/tree-decompose_1.cpp#L24-L47) daje višeplatformsku implementaciju članske funkcije `_Find_first()` za [std::bitset](../lang/csl/bitset.md), specifične za libstdc++.

Za bolju čitljivost koda preporučuje se i poštovanje pravila [CONT-10](#CONT-10).

## Ilustrirani primjeri

Navedene zahtjeve možda nije jednostavno usvojiti, pa ćemo slikama pobliže objasniti koji oblik treba koristiti, a koji izbjegavati:

### Primjer 1

![](./images/format-1.png)

Izdvojene složene LaTeX formule čine raspored stranice skladnijim. No **OI Wiki** prvenstveno je kineski web, pa želimo da ključne informacije (poput naslova) budu na kineskom kad god je moguće, osim engleskih vlastitih naziva.

### Primjer 2

![](./images/format-2.png)

U složenijim LaTeX formulama pazite na poravnanje znakova jednakosti. Sadržaj možete dopuniti i prikladnim **poveznicama** na druge stranice Wikija.

### Primjer 3

![](./images/format-3.png)

U pravilu preporučujemo navesti izvore na kraju članka u odjeljku `## Literatura i napomene` te uz izvornu rečenicu dodati fusnotu, umjesto izravne poveznice. Svakako izbjegavajte izražavati kôd LaTeX formulama: dvije uglate zagrade na slici nisu ispravan zapis. Preporučujemo `dp(i,j)` ili `dp_{i,j}`.

### Primjer 4

![](./images/format-4.png)

Za **množenje** obično koristimo `\times` ili `\cdot`; u posebnim slučajevima (poput konvolucije) koristimo `*` (ili `\ast`). Naslovi su kratke sintagme, ali glavni tekst ne bi se trebao sastojati od naslaganih sintagmi. Izraz „dva elementa” na slici preporučujemo zamijeniti s „načelo dinamičkog programiranja ima sljedeća dva elementa” radi povezanosti teksta. Dobro je što se prikladnom uporabom **uređenog** popisa sadržaj prikazuje preglednije. Još jednom: ako je stavka popisa rečenica, na kraju mora imati **interpunkcijski znak**. Uređeni popisi obično imaju točku sa zarezom, a posljednja stavka točku; sve stavke neuređenih popisa imaju točku.

### Primjer 5

![](./images/format-5.png)

Prikladne **slike** poboljšavaju čitljivost članka. **Pseudokod** jednostavno i sažeto opisuje tijek algoritma te je razumljiviji od izravnog navođenja predloška koda.

### Primjer 6

![](./images/format-6.png)

Ponovno isti problem: naslov je na engleskom. Nakon zagrade nema točke. Osim toga, izdvojena formula na slici nema zagrada, ali zbog previše ugniježđenih indeksa najdublji je indeks vrlo sitan, pa formula ne izgleda lijepo. Preporučujemo zamijeniti `son_{now,i}` s `son(now,i)` ili `f_{now}` s `f(now)`. Nastojte ograničiti ugnježđivanje indeksa i eksponenata na najviše dvije razine (za višestruko ugniježđene eksponente preporučujemo Knuthove strelice, primjerice $2 \uparrow (2 \uparrow (2 \uparrow (2 \uparrow \cdots)))$ umjesto $2^{2^{2^{2^{\cdots}}}}$, kao u zadatku „Sedam minuta u kojima je Bog sastavljao zadatke”).

### Primjer 7

![](./images/format-7.png)

Proširenom sintaksom MkDocsa odvojite tekst primjera zadatka od opisa algoritma. Sklapanjem koda članak postaje sažetiji. (Uostalom, većina čitatelja Wikija želi razumjeti ideju; osim predložaka koje treba pročitati, većina koda za zadatke može se sklopiti.) Pri opisu rada funkcija dobar su izbor i kôd unutar retka i LaTeX formule.

### Primjer 8

![](./images/format-8.png)

Navođenjem literature na kraju članka sadržaj postaje utemeljeniji i vjerodostojniji.

## Vanjske poveznice

-   [Uporaba interpunkcijskih znakova (GB/T 15834—2011)](http://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201001/W020190128580990138234.pdf)
-   [Wikipedija: priručnik stila/interpunkcija](https://zh.wikipedia.org/wiki/Wikipedia:%E6%A0%BC%E5%BC%8F%E6%89%8B%E5%86%8C/%E6%A0%87%E7%82%B9%E7%AC%A6%E5%8F%B7)
-   [Vodič za tipografiju kineskog teksta (pojednostavnjeno kinesko izdanje)](https://mazhuang.org/wiki/chinese-copywriting-guidelines/)
-   [Stilski vodič za kineski tekst - PDFE GUIDELINE](https://pdfe.github.io/GUIDELINE/#/others/copywriter)
-   [(Ne baš) kratak uvod u LATEX2ε ili LATEX2ε u 106 minuta](https://github.com/CTeX-org/lshort-zh-cn/releases)
-   [Uredničke smjernice za engleski tekst u kineskim publikacijama](https://www.nppa.gov.cn/xxgk/fdzdgknr/hybz/202210/t20221004_445147.html)

## Literatura i napomene

[^note1]: Dvotočka ovdje sažima prethodni tekst.

[^note2]: Između punog engleskog naziva znanstvenog ili tehničkog pojma i njegove kratice treba biti engleski zarez. Engleska rečenica ili odlomak umetnut u kinesku rečenicu kao napomena, dopuna ili objašnjenje treba biti u kineskim okruglim zagradama.

[^note3]: Sklopivi okviri: pogledajte [Collapsible Blocks](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#collapsible-blocks). Ponekad ih nazivamo i „sintaksom Details” jer im funkcionalnost odgovara HTML [elementu `<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details).

[^note4]: Premješteno na [Kako sudjelovati](./htc.md).

[^note5]: Ovo je pravilo dodano na stranicu [Prije uređivanja](../edit-landing.md) i javno objavljeno, ali nije dodano u ovaj dokument.

[^note6]: Kartice: pogledajte [Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs).

[^ref1]: [cstdio stdio.h namespace](https://stackoverflow.com/questions/10460250/cstdio-stdio-h-namespace)

[^ref2]: [CCF-ova objava o povratku natjecanja NOIP - China Computer Federation](https://www.ccf.org.cn/c/2020-01-21/694716.shtml)

[^ref3]: [Zašto se moja formula ne prikazuje ispravno u sadržaju? Izgleda udvostručeno](faq.md)

[^ref4]: [SVG|MDN](https://developer.mozilla.org/zh-CN/docs/Web/SVG)

[^webarchive]: [Save Page in Internet Archive](https://web.archive.org/save/)

[^apng]: [APNG](https://en.wikipedia.org/wiki/APNG)

[^intro-apng]: [OI-wiki/OI-wiki#3422](https://github.com/OI-wiki/OI-wiki/issues/3422)
