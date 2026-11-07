---
title: Uvod u teoriju igara
---

**Teorija igara** (game theory) grana je ekonomije koja uglavnom proučava ponašanje pojedinaca u natjecateljskim ili suparničkim odnosima pod određenim pravilima. Teorija igara bavi se očekivanim i stvarnim ponašanjem sudionika u igri te proučava njihove optimalne strategije.

Jednostavno rečeno, teorija igara uglavnom proučava sljedeće: kako više igrača koji sudjeluju u nekoj igri bira svoje strategije.

## Osnovni pojmovi

U ovom odjeljku kratko predstavljamo neke uobičajene pojmove iz teorije igara.

### Kooperativne i nekooperativne igre

**Kooperativna igra** (cooperative game) jest igra u kojoj sudionici mogu sklapati saveze i međusobno surađivati. U takvim igrama nekooperativno ponašanje pojedinca obično kažnjava neki vanjski mehanizam. Nasuprot tome, u **nekooperativnoj igri** (noncooperative game) takav mehanizam ne postoji, pa sudionici ili uopće ne mogu sklapati saveze ili suradnju mogu održavati samo pomoću vjerodostojnih prijetnji.

U usporedbi s kooperativnim igrama, nekooperativne igre proučene su sustavnije i zrelije. Sve igre o kojima se govori u ovom članku nekooperativne su igre.

### Simetrične i nesimetrične igre

U **simetričnoj igri** (symmetric game) različiti sudionici za isto ponašanje dobivaju istu isplatu, odnosno isplata ovisi samo o samom potezu, a ne o identitetu onoga tko ga povlači. Igra koja ne zadovoljava taj uvjet naziva se **nesimetrična igra** (asymmetric game).

### Igre nulte i nenulte sume

Glavna stranica: [Igre nulte sume](./zero-sum-game.md)

**Igra nulte sume** (zero-sum game) igra je u kojoj je zbroj isplata svih sudionika uvijek jednak nuli, bez obzira na to kako se strane ponašaju. Igre nulte sume o kojima se obično govori imaju dva sudionika; tada je dobitak jedne strane nužno gubitak druge. Nasuprot tome, **igra nenulte sume** (non-zero-sum game) dopušta da više strana zajedno dobije ili zajedno izgubi; tu spadaju **igre pozitivne sume** (positive-sum game), **igre negativne sume** (negative-sum game) i dr.

### Simultane i sekvencijalne igre

U **simultanoj igri** (simultaneous game) svi sudionici odlučuju istodobno, ne znajući što su odabrali drugi. Tipičan primjer simultane igre jest kamen-škare-papir. Takve se igre često prikazuju matricom isplata i u pravilu ne uključuju pojam vremena.

Nasuprot tome stoji **sekvencijalna igra** (sequential game), u kojoj sudionici povlače poteze jedan za drugim. Valja napomenuti da onaj tko igra kasnije mora moći vidjeti barem dio poteza onih koji su igrali prije njega, inače redoslijed poteza ne bi imao nikakva smisla. Sekvencijalne igre obično se opisuju stablom igre.

### Igre sa savršenom i nesavršenom informacijom

**Savršena informacija** (perfect information) znači da sudionik u trenutku donošenja bilo koje odluke u potpunosti poznaje sve što se dotad dogodilo, uključujući početno stanje igre. Primjerice, šah i go igre su sa savršenom informacijom, dok su mahjong i poker igre s nesavršenom informacijom jer igrači ne znaju koje karte (pločice) drže drugi. Savršena informacija obično se koristi za opis sekvencijalnih igara; budući da u simultanoj igri igrači ne mogu znati koji će potez protivnik upravo povući, obično se smatra da simultane igre nisu igre sa savršenom informacijom.

### Igre s potpunom i nepotpunom informacijom

**Potpuna informacija** (complete information) znači da svi sudionici u potpunosti poznaju samu strukturu igre (uključujući dostupne odluke svih strana i konačne isplate) i da je ta informacija opće znanje (common knowledge). Nasuprot tome stoje igre s nepotpunom informacijom, u kojima su neki elementi igre (npr. protivnikove dostupne odluke ili funkcija isplate) sudionicima nepoznati.

Valja istaknuti da su „potpuna informacija” i „savršena informacija” dva nezavisna pojma koji jedan drugoga ne uključuju. Primjerice, mahjong je igra s potpunom, ali nesavršenom informacijom, jer su pravila i isplate javni, ali pločice nisu vidljive; s druge strane, neke igre sa skrivenim ciljevima, ali potpuno javnim potezima, igre su sa savršenom, ali nepotpunom informacijom.

## Kombinatorna teorija igara

U algoritamskim natjecanjima najčešća je vrsta igre **kombinatorna igra** (combinatorial game). Taj se naziv obično odnosi na igre koje je teško riješiti zbog golemog broja stanja. Upravo zato što su opće kombinatorne igre prilično složene, kombinatorna teorija igara uglavnom se bavi sljedećom vrstom igara: igrama za dva igrača koji naizmjence povlače poteze, sa savršenom informacijom i bez slučajnih elemenata. Šah, go i slične igre tipične su kombinatorne igre.

### Nepristrane kombinatorne igre

Glavna stranica: [Nepristrane kombinatorne igre](./impartial-game.md)

**Nepristrana igra** (impartial game) kombinatorna je igra koja zadovoljava sljedeće uvjete:

-   u svakom određenom stanju svi sudionici imaju na raspolaganju potpuno iste poteze, koji ovise samo o trenutačnom stanju, a ne o identitetu igrača;
-   isto stanje igre ne može se dosegnuti više puta, igra završava kad sudionik ne može povući potez, a igra uvijek završava nakon konačno mnogo poteza i to bez neriješenog ishoda.

Nepristrane igre uvijek su simetrične igre.

### Pristrane kombinatorne igre

Glavna stranica: [Pristrane kombinatorne igre](./partizan-game.md)

Pojam suprotan nepristranoj igri jest **pristrana (partizanska) igra** (partizan game), u kojoj potezi koje sudionik može povući u nekom stanju ovise o njegovu identitetu. Većina igara na ploči (npr. šah, kineski šah, go, gomoku) pristrane su igre jer sudionici mogu pomicati samo vlastite figure.

### Normalne igre i igre misère

U kombinatornim igrama pobjednik je obično sudionik koji je posljednji povukao potez prije završetka igre. To se naziva **normalna igra** (normal game). Nasuprot tome stoji **igra misère** (misère game), u kojoj sudionik koji posljednji povuče potez prije završetka igre gubi.

I nepristrane i pristrane kombinatorne igre mogu biti normalne igre ili igre misère.

## Literatura

-   [Game theory - Wikipedia](https://en.wikipedia.org/wiki/Game_theory)
-   [Combinatorial game theory - Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_game_theory)
-   [Impartial game - Wikipedia](https://en.wikipedia.org/wiki/Impartial_game)
-   [Misère - Wikipedia](https://en.wikipedia.org/wiki/Mis%C3%A8re)
