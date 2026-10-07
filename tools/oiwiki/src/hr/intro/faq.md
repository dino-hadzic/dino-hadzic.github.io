---
title: F.A.Q.
---

Ova stranica odgovara na neka česta pitanja.

## Htio bih pitati nešto o ovom Wikiju

P: Zašto ste uopće htjeli napraviti ovaj Wiki?

O: Ne znam jeste li se, učeći **OI**, pred golemim sustavom znanja ikad osjećali izgubljeno i bespomoćno. Ono što **OI Wiki** želi postići moglo bi se opisati otprilike kao „omogućiti da više učenika koji nemaju dovoljno natjecateljskih resursa lako dođe do materijala za trening”. Naravno, ni taj opis nije potpun; motiv za Wiki možda je i sasvim jednostavan – samo želja da se dade mali doprinos razvoju **OI-ja**. XD

***

P: Zanima me, kako se mogu uključiti?

O: **OI Wiki** se sada nalazi na GitHubu; najnoviji napredak možete pratiti izravno u ovom [repozitoriju](https://github.com/OI-wiki/OI-wiki). Uključiti se možete otvaranjem [Issuea](https://github.com/OI-wiki/OI-wiki/issues) ili [Pull Requesta](https://github.com/OI-wiki/OI-wiki/pulls) na GitHubu, dijeljenjem ideja u grupama za raspravu ili slanjem priloga izravno administratorima. Trenutačno koristimo okvir [MkDocs](https://mkdocs.readthedocs.io), razvijen u Pythonu, koji podržava Markdown (uključujući matematičke formule).

***

P: Ali ja sam prilično slab… ne znam što bih mogao učiniti.

O: Sve kreće od ljubavi. Možete pomoći drugima u pregledu i ispravljanju priloga, pomoći nam u promicanju **OI Wikija** i pridonijeti dobroj atmosferi učenja i razmjene u zajednici!

***

P: Tko trenutačno uglavnom radi na ovome? Čini se kao golem posao – može li to zaista uspjeti?

O: U početku su to uglavnom radili umirovljeni stariji natjecatelji, a poslije smo upoznali mnogo istomišljenika: aktivne natjecatelje, bivše natjecatelje, pa i prijatelje koji nikad nisu sudjelovali u **OI-ju**. Projekt trenutačno uglavnom održava projektni tim **OI Wikija** (u nastavku je zajednička fotografija).

<a href="https://github.com/OI-wiki/OI-wiki/graphs/contributors"><img src="https://opencollective.com/oi-wiki/contributors.svg?width=890&button=false"/></a>

Naravno, samo vlastitim snagama teško bismo projekt doveli do savršenstva, pa vas srdačno pozivamo da zajedno s nama usavršavate **OI Wiki**.

***

P: Kako jamčite da sadržaj koji dodamo neće iznenada nestati?

O: Sadržaj držimo na [GitHubu](https://github.com/OI-wiki/OI-wiki), pa se ni u slučaju pada našeg poslužitelja neće izgubiti. Osim toga, redovito radimo sigurnosne kopije svačijeg truda, pa čak i ako GitHub jednog dana propadne (?), naš sadržaj neće nestati.

***

P: Čini se da **OI Wiki** ima prazne stranice!

O: Da. Zbog ograničenog znanja i vremena članova tima te prazne stranice zasad ne možemo dovršiti. Zato ovdje pozivamo na priloge i tražimo nove suradnike, u nadi da ćemo pronaći prijatelje sličnih ideja i zajedno upotpuniti **OI Wiki**.

***

P: Zašto jednostavno ne pišete na [kinesku Wikipediju](https://zh.wikipedia.org/)?

O: Zato što želimo stvarno pomoći što većem broju natjecatelja i svih koje ovaj sadržaj zanima. Osim toga, zbog općepoznatih razloga sadržaju kineske Wikipedije nije moguće pristupiti bez prepreka.

## Želim se uključiti!

P: Kako mogu stupiti u kontakt s projektnim timom?

O: Možete nas kontaktirati putem [načina komunikacije navedenih u opisu projekta](./about.md#načini-komunikacije).

***

P: Kako mogu pridonijeti kodom ili sadržajem?

Pogledajte stranicu [Kako sudjelovati](./htc.md).

***

P: Gdje je sadržaj (kazalo)?

O: Kazalo se nalazi u datoteci [mkdocs.yml](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml#L17) u korijenu projekta.

***

P: Kako izmijeniti sadržaj neke teme?

O: U gornjem desnom kutu odgovarajuće stranice nalazi se gumb za uređivanje<i class="md-icon">edit</i>; kad ga kliknete i potvrdite da ste pročitali [Kako pridonijeti](./htc.md), bit ćete preusmjereni na odgovarajuću datoteku na GitHubu.

Možete i sami pogledati kazalo [(mkdocs.yml)](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml) i pronaći gdje se datoteka nalazi.

***

P: Kako dodati novu temu?

O: Postoje dvije mogućnosti:

-   Možete otvoriti Issue i navesti sadržaj koji želite dodati.
-   Možete otvoriti Pull Request: u kazalo [(mkdocs.yml)](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml) dodajte novu temu i na odgovarajućem mjestu u mapi [docs](https://github.com/OI-wiki/OI-wiki/tree/master/docs) stvorite praznu `.md` datoteku. Pojedinosti o obliku dokumenata potražite u [priručniku za oblikovanje](./format.md#贡献文档要求).

***

P: Imam poteškoća s pristupom GitHubu.

O: Preporučujemo da u datoteku hosts dodate sljedeće retke[^ref1]:

```text
# GitHub Start
140.82.114.25                 alive.github.com
140.82.113.5                  api.github.com
185.199.110.153               assets-cdn.github.com
185.199.111.133               avatars.githubusercontent.com
185.199.111.133               avatars0.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.111.133               avatars2.githubusercontent.com
185.199.111.133               avatars3.githubusercontent.com
185.199.111.133               avatars4.githubusercontent.com
185.199.111.133               avatars5.githubusercontent.com
185.199.111.133               camo.githubusercontent.com
140.82.112.22                 central.github.com
185.199.111.133               cloud.githubusercontent.com
140.82.114.9                  codeload.github.com
140.82.113.22                 collector.github.com
185.199.111.133               desktop.githubusercontent.com
185.199.111.133               favicons.githubusercontent.com
140.82.112.3                  gist.github.com
52.216.163.147                github-cloud.s3.amazonaws.com
52.217.124.1                  github-com.s3.amazonaws.com
52.216.144.83                 github-production-release-asset-2e65be.s3.amazonaws.com
52.217.121.249                github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.206.57                 github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.114.4                  github.com
140.82.113.18                 github.community
185.199.110.154               github.githubassets.com
151.101.1.194                 github.global.ssl.fastly.net
185.199.110.153               github.io
185.199.111.133               github.map.fastly.net
185.199.110.153               githubstatus.com
140.82.112.25                 live.github.com
185.199.111.133               media.githubusercontent.com
185.199.111.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.111.133               raw.githubusercontent.com
185.199.111.133               user-images.githubusercontent.com
13.107.253.40                 vscode.dev
140.82.112.21                 education.github.com
# GitHub End
```

Najnovije podatke i više informacija naći ćete na [GitHub520](https://gitee.com/klmahuaw/GitHub520).

Korisnici Linuxa i macOS-a mogu isprobati [skriptu gh-check](https://gist.github.com/lilydjwg/93d33ed04547e1b9f7a86b64ef2ed058) autora [依云 (lilydjwg)](https://github.com/lilydjwg/), koja pronalazi IP adresu s najbržim pristupom; parametrom `--hosts` izravno ažurira datoteku hosts, a parametrom `--help` ispisuje upute. Prije upotrebe treba instalirati Python 3 i aiohttp (`pip install aiohttp -i https://pypi.tuna.tsinghua.edu.cn/simple/`). Opis na autorovu blogu: [Traženje najbržeg GitHubova IP-a (kineski)](https://blog.lilydjwg.me/2019/8/16/gh-check.214730.html).

Također, za brže kloniranje možete koristiti uslugu [Gitclone](https://www.gitclone.com/); upute su na njezinoj početnoj stranici.

Ako samo želite klonirati repozitorij **OI Wikija**:

```bash
git clone https://gitclone.com/github.com/OI-wiki/OI-wiki
```

Ako želite pridonositi **OI Wikiju**, najprije forkajte repozitorij **OI Wikija**, a zatim (zamijenite `username` svojim korisničkim imenom); imajte na umu da ćete se prema navedenom primjeru na GitHub spajati putem SSH-a[^only-ssh-connect]:

```bash
git clone https://gitclone.com/github.com/username/OI-wiki
git remote set-url origin git@github.com:username/OI-wiki.git
```

***

P: Meni je pip prespor!

O: Možete prijeći na kinesko zrcalo[^ref2] ili:

```bash
pip install -U -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

***

P: Klonirao sam projekt klijentom i presporo je.

O: Ako imate instaliran `git bash`, možete dodati nekoliko ograničenja da smanjite količinu preuzimanja.[^ref3]

```bash
git clone https://github.com/OI-wiki/OI-wiki.git --depth=1 -b master
```

***

P: Nikad nisam instalirao Python 3.

O: Više informacija naći ćete na [službenoj stranici Pythona](https://www.python.org/downloads/).

***

P: Čini se da mi javlja da je verzija pipa prestara.

O: Otvorite cmd/shell i izvršite sljedeću naredbu:

```bash
python -m pip install --upgrade pip
```

***

P: Instalacija ovisnosti mi nije uspjela.

O: Provjerite: mrežu? dopuštenja? poruku o pogrešci?

***

P: Već sam klonirao, zašto ne mogu pokrenuti stranicu?

O: Provjerite jeste li instalirali ovisnosti.

***

P: Klonirao sam repozitorij jako davno; kako ga ažurirati na novu verziju?

O: Pogledajte službenu GitHubovu stranicu pomoći [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork).

***

P: Kako ažurirati već instalirane starije ovisnosti?

O: Upišite sljedeću naredbu:

```bash
pip install -U -r requirements.txt
```

***

P: Zašto mi se Markdown pokvario?

O: Pogledajte [bilješke korisnika cyent (kineski)](https://web.archive.org/web/20221103014610/https://cyent.github.io/markdown-with-mkdocs-material/) ili [upute za MkDocs (kineski)](https://github.com/ctf-wiki/ctf-wiki/wiki/Mkdocs-%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E).

Trenutačno koristimo [remark-lint](https://github.com/remarkjs/remark-lint) za automatsko ispravljanje oblika; možda u [konfiguraciji](https://github.com/OI-wiki/OI-wiki/blob/master/.remarkrc) još ima nedostataka, pa slobodno ukažite na njih.

***

P: Je li moguće da GitHub ne prikazuje moje matematičke formule?

O: Da, GitHubov pregled ne prikazuje matematičke formule. No bez brige, MkDocs podržava formule i one rade normalno; može se koristiti sve što podržava MathJax.

***

P: Zašto mi je formula iskrivljena?

O: Ako je riječ o formuli u zasebnom retku (s `$$`), poznat je problem da oko `$$` moraju biti prazni redci i da `$$` mora stajati **samostalno** u retku (bez razmaka ispred). Oblik je sljedeći:

```text
// prazan redak
$$
a_i
$$
// prazan redak
```

***

P: Zašto se moja formula ne prikazuje ispravno u sadržaju? Kao da je udvostručena.

O: Da, to je bug u python-markdownu koji bi uskoro mogao biti ispravljen.

Ako želite izbjeći udvostručenu formulu u sadržaju, pogledajte [kako je napisan sadržaj stranice o SAM-u u kategoriji string](https://github.com/OI-wiki/OI-wiki/blame/master/docs/string/sam.md#L73).

```text
结束位置 <script type="math/tex">endpos</script>
```

U sadržaju postaje

```text
结束位置 endpos
```

Napomena: sada molimo da u naslovima koji ulaze u sadržaj po mogućnosti izbjegavate MathJax formule.

***

P: Kako za pojedinu stranicu zasebno navesti podatke o autorskim pravima?

O: Dovoljno je dodati jedan redak na početak stranice.[^ref4]

Na primjer:

```text
copyright: SATA
```

Napomena: zadano je CC BY-SA 4.0 i SATA.

***

P: Zašto mog imena nema u statistici autora?

O: Ako ste napisali dio sadržaja neke stranice, a niste zabilježeni na popisu autora, dodajte svoj GitHub ID u [polje author](./htc.md#author-字段) u zaglavlju datoteke.

***

Hvala što ste čitali do kraja. Ono što nam je sada najpotrebnije upravo je vaša pomoć.

Projektni tim **OI Wikija**

2018.8

## Literatura i bilješke

[^ref1]: [GitHub520](https://gitee.com/klmahuaw/GitHub520)

[^ref2]: [Promjena pip izvora na kinesko zrcalo - L 瑜 - CSDN blog (kineski)](https://blog.csdn.net/lambert310/article/details/52412059)

[^ref3]: [GIT – korak po korak za početnike (Windows Git Bash) (kineski)](https://blog.csdn.net/FreeApe/article/details/46845555)

[^ref4]: [Metadata - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/extensions/metadata/#usage)

[^only-ssh-connect]: GitHub je ukinuo HTTPS autentifikaciju lozinkom, pa se za spajanje mora koristiti SSH ili Personal Access Token; vidi [Koji udaljeni URL koristiti?](https://docs.github.com/cn/github/using-git/which-remote-url-should-i-use), [Stvaranje osobnog pristupnog tokena](https://docs.github.com/cn/github/authenticating-to-github/creating-a-personal-access-token) i [Spajanje na GitHub putem SSH-a](https://docs.github.com/cn/github/authenticating-to-github/connecting-to-github-with-ssh).
