---
title: Uvod u tokove u mrežama
---

Ova stranica uvodi osnovne pojmove vezane uz tokove u mrežama (network flow).

## Pregled

**Mreža** (network) je poseban usmjereni graf $G=(V,E)$ koji se od običnog usmjerenog grafa razlikuje po tome što ima kapacitete te izvor i ponor.

-   Svaki brid $(u, v)$ iz $E$ ima težinu koja se zove **kapacitet** (capacity) i označava $c(u, v)$. Kad $(u,v)\notin E$, možemo uzeti $c(u,v)=0$.

-   U $V$ postoje dva posebna vrha: **izvor** (source) $s$ i **ponor** (sink) $t$ ($s \neq t$).

Za mrežu $G=(V, E)$, **tok** (flow) je funkcija sa skupa bridova $E$ u skup cijelih ili realnih brojeva koja zadovoljava sljedeća svojstva.

1.  Ograničenje kapaciteta: za svaki brid tok kroz njega ne smije premašiti njegov kapacitet, tj. $0 \leq f(u,v) \leq c(u,v)$;
2.  Očuvanje toka: za svaki vrh $u$ osim izvora i ponora neto tok je $0$. Pritom neto tok vrha $u$ definiramo kao $f(u) = \sum_{x \in V} f(u, x) - \sum_{x \in V} f(x, u)$.

Za mrežu $G = (V, E)$ i tok $f$ na njoj, **vrijednost toka** $|f|$ definiramo kao neto tok izvora $f(s)$. Kao posljedica očuvanja toka, to je jednako i suprotnoj vrijednosti neto toka ponora, $-f(t)$.

Za mrežu $G = (V, E)$, ako je $\{S, T\}$ particija skupa $V$ (tj. $S \cup T = V$ i $S \cap T = \varnothing$) takva da je $s \in S, t \in T$, kažemo da je $\{S, T\}$ **$s$-$t$ rez** (cut) grafa $G$. Kapacitet $s$-$t$ reza $\{S, T\}$ definiramo kao $||S, T|| = \sum_{u \in S} \sum_{v \in T} c(u, v)$.

## Uobičajeni problemi

Uobičajeni problemi s tokovima u mrežama uključuju, između ostalog, sljedeće tipove.

-   Problem maksimalnog toka: za mrežu $G = (V, E)$ svakom bridu dodijeliti tok tako da dobijemo tok $f$ čija je vrijednost što veća. Takav $f$ zovemo **maksimalni tok** mreže $G$.
-   Problem minimalnog reza: za mrežu $G = (V, E)$ pronaći $s$-$t$ rez $\{S, T\}$ čiji je ukupni kapacitet što manji. Taj ukupni kapacitet zovemo **minimalni rez** mreže $G$.
-   Problem maksimalnog toka minimalne cijene: u mreži $G = (V, E)$ svakom je bridu zadana i težina $w(u, v)$ koja se zove **cijena** (cost) i označava koliko stoji jedinica toka koja prolazi bridom $(u, v)$. Među svim maksimalnim tokovima mreže $G$ onaj s najmanjom ukupnom cijenom zovemo **maksimalni tok minimalne cijene** (min-cost max-flow).

Sve ćemo ih detaljno obraditi u kasnijim poglavljima.

## Primjer: „24 zadatka o tokovima u mrežama”

„24 zadatka o tokovima u mrežama” (网络流 24 题) popis je zadataka koji se naširoko dijeli na kineskom internetu ([LibreOJ](https://loj.ac/problems/tag/30)/[Luogu](https://www.luogu.com.cn/problem/list?tag=332)) i postoji barem od oko 2010. godine. Popis uvodi neke klasične tehnike modeliranja drugih problema kao problema toka u mreži. Zbog ograničenja vremena u kojem je nastao, ti zadaci nisu nužno najreprezentativniji problemi o tokovima, ali ih se čitateljima koji se ozbiljno bave algoritamskim natjecanjima i dalje isplati pogledati.
