---
title: Kako sudjelovati
---

Prije početka članka, svi članovi projektnog tima **OI Wiki** srdačno vas pozdravljaju i pozivaju da doprinesete stranicama ovog projekta. Upravo zahvaljujući stotinama ljudi poput vas **OI Wiki** postao je ono što je danas!

Ovaj članak uglavnom opisuje postupak pisanja pri sudjelovanju u izradi **OI Wikija**. Prije pisanja ili ispravljanja wiki stranica pažljivo pročitajte sljedeći tekst kako biste pripremili što kvalitetniji sadržaj.

## Smjernice za doprinos

Prije uređivanja pročitajte [Smjernice za doprinos OI Wikiju](https://github.com/OI-wiki/OI-wiki/blob/master/.github/CONTRIBUTING.md) i [smjernice projekta](./about.md#smjernice-projekta) kako biste lakše surađivali i komunicirali s drugim doprinositeljima iz zajednice.

## Suradnja

???+ warning "Upozorenje"
    Prije nego što počnete pisati neki sadržaj, pregledajte [Issues](https://github.com/OI-wiki/OI-wiki/issues), provjerite da nitko već ne radi isto te otvorite [novi issue](https://github.com/OI-wiki/OI-wiki/issues/new) u kojem ćete zabilježiti što namjeravate napisati.

???+ tip "Savjet"
    Među issueima ima mnogo problema koje treba ispraviti ili riješiti, osobito u našem planu iteracije (Iteration Plan). Odabir zadatka odande odličan je početak!

Kako bismo osigurali stručnost i točnost članaka, preporučujemo da prije uređivanja razmotrite sljedeće:

1.  **Odaberite područje koje poznajete**: dajte prednost člancima povezanima s vašim stručnim znanjem, obrazovanjem ili interesima. Tako ćete lakše napisati kvalitetan sadržaj.
2.  **Budite oprezni s novim područjima**: ako tek počinjete učiti o nekoj temi ili je slabo poznajete, preporučujemo da prvo produbite razumijevanje čitanjem i učenjem, a uređivati počnete tek kada ste dovoljno sigurni u znanje.
3.  **Proučite relevantne izvore**: pri dodavanju ili izmjeni sadržaja preporučujemo da najprije proučite mjerodavnu literaturu i izvore kako biste osigurali točnost informacija. Slobodno postavite pitanja u komentarima na stranici ili u našoj zajednici i raspravite ih s drugim urednicima.

Cijenimo entuzijazam i trud svakog doprinositelja te razumijemo da nemaju svi jednaku razinu stručnosti. Surađujmo i zajedno njegujmo ovo mjesto znanja, pomažući većem broju čitatelja točnim i stručnim sadržajem. Veselimo se vašem doprinosu! Ovdje ćemo citirati Wikipediju:

> Ne bojte se uređivati, odvažno ažurirajte stranice![^ref1]

### Uređivanje na GitHubu

Za sudjelovanje u pisanju **OI Wikija** **potreban je** GitHub račun (možete ga otvoriti na [GitHubovoj stranici za registraciju](https://github.com/signup)), ali **nisu potrebne** napredne vještine rada s GitHubom. Čak i kao početnik možete **izvrsno** urediti sadržaj slijedeći postupak u nastavku.

???+ tip "Savjet"
    Dok se vaše promjene ne spoje u glavni repozitorij **OI Wikija**, nijedna vaša izmjena sadržaja neće se pojaviti na glavnoj stranici **OI Wikija**. Stoga se ne morate brinuti da ćete pokvariti sadržaj koji se trenutačno prikazuje na **OI Wikiju**.
    
    Ako ste i dalje zabrinuti, možete proučiti [službene GitHubove vodiče](https://skills.github.com/).

#### Uređivanje sadržaja jedne stranice

1.  Pronađite odgovarajuću stranicu na **OI Wikiju**;
2.  kliknite gumb **„Uredi ovu stranicu”** (<i class="md-icon">edit</i>) u gornjem desnom kutu sadržaja (lijevo od sadržaja članka). Nakon potvrde da ste pročitali ovu stranicu i [Priručnik za oblikovanje](./format.md), kliknite gumb i slijedite upute za prelazak na GitHub radi uređivanja;
3.  u okviru za uređivanje napišite željene izmjene. Tijekom uređivanja i slanja promjena **isključite softver za automatsko prevođenje** jer može uzrokovati nepotrebne probleme (primjerice, katkad pogrešno preimenuje datoteku koju uređujete i tako naruši strukturu direktorija);
4.  nakon pisanja pomaknite se na dno stranice i unesite commit poruku prema odjeljku [Pravila oblikovanja commit poruka](#pravila-oblikovanja-commit-poruka), a zatim kliknite **Propose changes** kako biste poslali izmjene. GitHub će automatski stvoriti vaš fork repozitorija **OI Wiki** i dodati mu vaš commit.
5.  GitHub će automatski otvoriti stranicu vašeg forka. Pri vrhu stranice pojavit će se zeleni gumb **Create pull request**. Kliknite ga kako biste otvorili stranicu za stvaranje pull requesta. Pomaknite se dolje, provjerite da u izmjenama nema pogrešaka, unesite opis prema odjeljku [Pravila oblikovanja pull requestova](#pravila-oblikovanja-pull-requestova), a zatim kliknite zeleni gumb **Create pull request** kako biste stvorili pull request.
6.  Ako sve prođe kako treba, vaš je pull request uspješno poslan u repozitorij. Preostaje pričekati da ga administratori pregledaju i spoje u glavni repozitorij.

Dok čekate spajanje, možete komentirati tuđe pull requestove ili glasati za njih ili protiv njih. Ako stignu nove poruke, u gornjem desnom kutu stranice pojavit će se obavijest, a dobit ćete i obavijest e-poštom (ovisno o načinu obavještavanja u osobnim postavkama).

#### Uređivanje sadržaja više stranica

Ako istodobno trebate urediti više međusobno nepovezanih stranica, slijedite prethodni odjeljak [Uređivanje sadržaja jedne stranice](#uređivanje-sadržaja-jedne-stranice) i uredite sve stranice u jednom prolazu.

1.  Otvorite repozitorij [OI-Wiki/OI-Wiki](https://github.com/OI-Wiki/OI-Wiki), pritisnite tipku <kbd>.</kbd> (ili zamijenite `github.com` u URL-u s `github.dev`)[^ref2] kako biste otvorili GitHubov web-uređivač VS Code;
2.  u uređivaču izmijenite izvorne datoteke stranica. Gumbom za pregled u gornjem desnom kutu (ili prečacem <kbd>Ctrl+K</kbd><kbd>V</kbd>) možete otvoriti pregled s desne strane;
3.  nakon izmjena otvorite karticu Source Control s lijeve strane, unesite commit poruku prema odjeljku [Pravila oblikovanja commit poruka](#pravila-oblikovanja-commit-poruka) i napravite commit. Kad vas sustav upita želite li stvoriti fork repozitorija, kliknite zeleni gumb **Fork Repository**.
4.  Nakon commita pri vrhu stranice u sredini pojavit će se dijaloški okvir. U prvi okvir unesite naslov, a u drugi naziv grane odredišnog repozitorija. Zatim će se u donjem desnom kutu pojaviti obavijest poput `Created Pull Request #1 for OI-Wiki/OI-Wiki.`. Klikom na plavu poveznicu možete otvoriti taj pull request.

#### Dodavanje izmjena pull requestu

1.  Otvorite [popis pull requestova OI Wikija](https://github.com/OI-wiki/OI-wiki/pulls), pronađite svoj pull request i kliknite ga.
2.  Ispod naslova pull requesta vidjet ćete tekst poput `<vašID> wants to merge x commits into OI-wiki:master from <vašID>:patch-1`. Kliknite dio `<vašID>:patch-1`.
3.  Bit ćete preusmjereni na svoj fork, a naziv grane u gornjem lijevom kutu popisa datoteka bit će naziv grane iz koje ste poslali pull request (u ovom primjeru `patch-1`).
4.  Napravite potrebne izmjene.
    -   Ako trebate urediti jednu datoteku ili više međusobno nepovezanih stranica, pronađite željenu datoteku i izmijenite je. Zatim se pomaknite na dno stranice, unesite commit poruku prema odjeljku [Pravila oblikovanja commit poruka](#pravila-oblikovanja-commit-poruka) i kliknite **Commit changes** kako biste poslali izmjene.
    -   Ako trebate urediti više datoteka, pritisnite <kbd>.</kbd> (ili zamijenite `github.com` u URL-u s `github.dev`)[^ref2] kako biste otvorili GitHubov web-uređivač VS Code i napravili izmjene. Zatim na kartici Source Control s lijeve strane unesite commit poruku prema odjeljku [Pravila oblikovanja commit poruka](#pravila-oblikovanja-commit-poruka) i napravite commit.
5.  Vaše će se izmjene automatski dodati pull requestu.

### Lokalno uređivanje Gitom

???+ warning "Upozorenje"
    Većini korisnika preporučujemo uređivanje u GitHubovu web-uređivaču opisanom gore.

Iako u većini slučajeva možete uređivati izravno na GitHubu, za posebne slučajeve (primjerice kada trebate potpisivanje GPG-om) preporučujemo lokalno uređivanje Gitom.

Okvirni je postupak sljedeći:

1.  napravite fork glavnog repozitorija na svojem računu;
2.  klonirajte (clone) svoj fork lokalno;
3.  napravite lokalne izmjene i zabilježite ih commitom;
4.  pošaljite (push) izmjene u fork koji ste klonirali;
5.  pošaljite pull request glavnom repozitoriju.

Detaljne upute možete pronaći na stranici [Git](../tools/git.md).

#### Dodavanje izmjena pull requestu

Nastavite uređivati u lokalno kloniranom forku, napravite commit i pošaljite ga naredbom push. Izmjene će se automatski dodati pull requestu.

### Pregled izmjena na izgrađenoj web-stranici

Pri dnu stranice pull requesta možete pronaći testnu stranicu. Kliknite poveznicu Details uz stavku netlify/oi-wiki/deploy-preview (kao na slici ispod) kako biste otvorili automatski izgrađen pregled stranice s vašim izmjenama.

![deploy\_preview](./images/deploy_preview.png)

### Promjene navigacije i poveznica

Ako želite dodati novu stranicu ili promijeniti poveznicu na postojeću stranicu u navigaciji, obično trebate izmijeniti datoteku [`mkdocs.yml`](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml).

Pri dodavanju nove stranice slijedite postojeći oblik. Međutim, osim pri preustroju ili ispravljanju naziva, **ne preporučujemo mijenjanje poveznica na postojeće stranice**. Nepotrebne izmjene u pull requestovima bit će odbijene.

Ako ipak želite promijeniti poveznicu, ažurirajte polje author i datoteku preusmjeravanja.

### Polje author

GitHub API ne može pratiti statistiku nakon promjene putanje datoteke, pa radi toga ručno održavamo popis autora na početku datoteke. Polje author nalazi se na samom početku Markdown datoteke i izgleda poput `author: Ir1d, cjsoft`; susjedni ID-jevi odvojeni su zarezom i razmakom. ID je korisničko ime na GitHubu, odnosno dio adrese GitHub profila (primjerice `Ir1d` u <https://github.com/Ir1d>).

Pri promjeni poveznice unesite sve doprinositelje trenutačne stranice u polje author.

### Datoteka preusmjeravanja

Pri promjeni poveznica potrebno je izmijeniti datoteku preusmjeravanja kako vanjske poveznice na stranicu ne bi prestale raditi.

Datoteka [`_redirects`](https://github.com/OI-wiki/OI-wiki/blob/master/docs/_redirects) služi za generiranje [konfiguracije Netlifyja](https://docs.netlify.com/routing/redirects/#syntax-for-the-redirects-file) i [datoteka za preusmjeravanje](https://github.com/OI-wiki/OI-wiki/blob/master/scripts/gen_redirect.py).

Svaki redak predstavlja jedno pravilo preusmjeravanja: početni i odredišni URL (bez naziva domene):

```text
/path/to/src /path/to/desc
```

Napomena: sva su preusmjeravanja tipa 301. Izmjene su potrebne samo kada promjene URL-ova u navigaciji uzrokuju neispravne poveznice.

### Pravila oblikovanja commit poruka

Pri pisanju commit poruke slijedite ova osnovna pravila:

1.  u sažetku kratko opišite promjene iz tog commita. Sažetak ne smije biti dulji od 50 znakova; višak će se automatski premjestiti u tijelo poruke.
2.  Ako sadržaj commita treba dodatno opisati, učinite to detaljno u tijelu poruke.

Za sažetak commita preporučuje se sljedeći oblik:

```text
<vrsta promjene>(<naziv datoteke>): <opis promjene>
```

Vrste promjena dijele se ovako:

-   `feat`: dodavanje sadržaja.
-   `fix`: ispravljanje pogrešaka u postojećem sadržaju.
-   `refactor`: preustroj stranice (veće izmjene).
-   `revert`: poništavanje prethodnih izmjena.

### Pravila oblikovanja pull requestova

Za pull requestove slijedite ova pravila:

1.  u naslovu jasno navedite svrhu PR-a (**što** je napravljeno, **koji** je problem ispravljen).
2.  U opisu ukratko navedite izmjene. Ako rješavate neki issue, dodajte `fix #xxxx`, gdje je `xxxx` broj issuea.
3.  Pažljivo pročitajte [Smjernice za doprinos](https://github.com/OI-wiki/OI-wiki/blob/master/.github/CONTRIBUTING.md) i [Kodeks ponašanja](https://github.com/OI-wiki/OI-wiki/blob/master/CODE_OF_CONDUCT.md). Ako se slažete s njima, označite kućice u predlošku PR-a kako biste potvrdili pristanak.

Za naslov pull requesta preporučuje se sljedeći oblik:

```plain
<vrsta promjene>(<naziv datoteke>): <opis promjene> (<broj odgovarajućeg issuea>)
```

Vrste promjena dijele se ovako:

-   `feat`: dodavanje sadržaja.
-   `fix`: ispravljanje pogrešaka u postojećem sadržaju.
-   `refactor`: preustroj stranice (veće izmjene).
-   `revert`: poništavanje prethodnih izmjena.

Primjeri:

-   `fix(ds/persistent-seg): jasniji opis u komentarima koda`
-   `fix: tools/judger/index nedostaje u navigaciji (#3709)`
-   `feat(math/poly/fft): better proof`
-   `refactor(ds/stack): sređivanje sadržaja stranice`

### Tijek suradnje

1.  Nakon primitka novog pull requesta GitHub šalje e-poruku recenzentima;
2.  istodobno se na [GitHub Actionsu](https://github.com/OI-wiki/OI-wiki/actions) i [Netlifyju](https://app.netlify.com/sites/oi-wiki) pokreću dvije skupine testova, čiji se napredak prikazuje pri dnu stranice PR-a. GitHub Actions uglavnom provjerava da promjene u PR-u ne ometaju izgradnju web-stranice; Netlify gradi pregled izmjena iz PR-a radi lakšeg pregleda (nakon testova kliknite Details za više informacija);
3.  recenzenti mogu pronaći probleme i ostaviti `review` ili `suggested changes` (predložene izmjene, prikazane sivom ikonom) / `requested changes` (obvezne izmjene, prikazane crvenom ikonom, dostupne samo recenzentima s pravom pisanja u repozitorij). Obično će priložiti prijedloge i potrebne izmjene pa ćete trebati dodati nove promjene pull requestu. Postupak je opisan pod „Dodavanje izmjena pull requestu” u odjeljcima „Uređivanje na GitHubu” i „Lokalno uređivanje Gitom”.
4.  Tek kada dovoljno recenzenata odobri PR, on se može spojiti u granu master;
5.  nakon spajanja u master GitHub Actions ponovno gradi sadržaj web-stranice i ažurira granu gh-pages;
6.  tek tada poslužitelj preuzima izmjene iz grane gh-pages i ponovno objavljuje najnoviju verziju sadržaja.

## Literatura i napomene

[^ref1]: [Wikipedia: Uvod/uređivanje](https://zh.wikipedia.org/wiki/Wikipedia:%E6%96%B0%E6%89%8B%E5%85%A5%E9%96%80/%E7%B7%A8%E8%BC%AF)

[^ref2]: [Web-based editor - GitHub Codespaces - GitHub Docs](https://docs.github.com/en/codespaces/developing-in-codespaces/web-based-editor)
