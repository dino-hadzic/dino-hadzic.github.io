---
title: Mo algoritam uz bitset
---

Bitset se često koristi za probleme odlučivanja i prebrojavanja koje je uobičajenim strukturama podataka teško održavati, a Mo algoritam (Mo's algorithm) može održavati informacije o intervalima koje je uobičajenim strukturama podataka teško održavati. Kombiniranjem jednog i drugog istodobno iskorištavamo prednosti obaju.

## Primjer zadatka [「Ynoi2016」掉进兔子洞 (Pad u zečju rupu)](https://www.luogu.com.cn/problem/P4688)

Ovaj zadatak točno odgovara gore opisanim obilježjima Mo algoritma uz bitset. Lako je dosjetiti se da za svaki interval možemo u zasebnom bitsetu pohraniti sve vrijednosti koje se u njemu pojavljuju; odgovor na jedan upit tada je zbroj duljina svih intervala umanjen za broj elemenata u presjeku triju bitseta $\times 3$.

No kad bitset koristimo u Mo algoritmu, algoritam treba prilagoditi osobitostima bitseta:

1.  Bitset se ne snalazi dobro kad se ista vrijednost pojavi više puta. Možemo kao objekt koji umećemo u bitset uzeti zbroj diskretizirane vrijednosti trenutnog elementa i broja njegovih dosadašnjih pojavljivanja u trenutnom intervalu.
2.  Kad inače koristimo Mo algoritam, možda ne pazimo na redoslijed 4 načina pomicanja pokazivača, pa se tijekom pomicanja može dogoditi da lijevi kraj intervala bude desno od desnog kraja, tj. da duljina intervala bude negativna, zbog čega broj elemenata postaje negativan. U drugim situacijama to ne smeta, ali u ovom zadatku element koji umećemo u bitset ovisi o broju elemenata, pa moramo paziti na redoslijed 4 načina pomicanja pokazivača: naredbe koje lijevi pokazivač pomiču ulijevo i desni pokazivač udesno pišemo prve, kako u bitset ne bismo umetali negativne brojeve.
3.  Iako bitset troši malo memorije, ipak ne može podnijeti podatke veličine $10 ^ 5 \times 10 ^ 5$. Zato upite moramo podijeliti na konstantan broj dijelova i obraditi ih zasebno, čime memorija postaje upravo dovoljna, a vremenska složenost ostaje nepromijenjena.

??? note "Referentni kôd"
    ```cpp
    --8<-- "docs/misc/code/mo-algo-with-bitset/mo-algo-with-bitset_1.cpp"
    ```

## Zadaci za vježbu

-   [小清新人渣的本愿 (Skromna želja jednog nitkova)](https://www.luogu.com.cn/problem/P3674)
-   [「Ynoi2017」由乃的玉米田 (Yunino kukuruzno polje)](https://www.luogu.com.cn/problem/P5355)
-   [「Ynoi2011」WBLT](https://www.luogu.com.cn/problem/P5313)
