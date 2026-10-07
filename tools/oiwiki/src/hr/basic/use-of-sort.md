---
title: Primjene sortiranja
---

Ova stranica kratko predstavlja primjene sortiranja.

## Razumijevanje svojstava podataka

Obrada podataka sortiranjem pomaže razumjeti njihova svojstva i olakšava kasniju analizu i vizualizaciju. Primjeri iz svakodnevnog života su rječnik ili jelovnik: kad ne bi bili poredani po nekom redu, vrijeme potrebno da se pronađe ono što tražimo znatno bi se povećalo.

Računala moraju obrađivati velike količine podataka; nakon sortiranja čovjek može, prema svojstvima podataka i potrebama, oblikovati daljnji tijek obrade.

## Smanjenje vremenske složenosti

Sortiranje kao predobrada može smanjiti vremensku složenost potrebnu za rješavanje problema; obično je to kompromis u kojem se prostor mijenja za vrijeme. Ako sortirani popis treba analizirati više puta, vrlo se isplati jednom potrošiti resurse na sortiranje, jer se svaka sljedeća analiza znatno ubrzava.

???+ note "Primjer: provjeri postoje li u zadanom nizu jednaki elementi"
    Zadan je niz brojeva; treba provjeriti postoje li u njemu dva jednaka elementa.
    
    Naivni pristup provjerava svaki par brojeva i ispituje jesu li jednaki. Vremenska složenost je $O(n^2)$.
    
    Umjesto toga, najprije sortirajmo niz; tada nije teško primijetiti: ako postoje dva jednaka broja, u novom nizu oni su nužno na susjednim mjestima. Sad je dovoljno jednom proći novim nizom u $O(n)$.
    
    Ukupna vremenska složenost jednaka je složenosti sortiranja, $O(n\log n)$.

## Predobrada za pretraživanje

Sortiranje je predobrada koju zahtijeva [binarno pretraživanje](./binary.md). Binarnim pretraživanjem nakon sortiranja zadani se element u nizu može pronaći u vremenu $O(\log n)$.
