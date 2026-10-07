---
title: Uvod u heap
---

Heap (hrpa, gomila) je stablo u kojem svaki čvor ima ključ, pri čemu je ključ svakog čvora veći ili jednak / manji ili jednak ključu njegova roditelja.

Heap u kojem je ključ svakog čvora veći ili jednak ključu roditelja zove se min-heap, a inače max-heap. [`priority_queue` iz STL-a](../lang/csl/container-adapter.md#优先队列) zapravo je max-heap.

Glavne operacije koje (min-)heap podržava jesu: umetanje broja, upit za minimum, brisanje minimuma, spajanje dvaju heapova i smanjivanje vrijednosti elementa.

Neki moćniji heapovi (spojivi heapovi, mergeable heaps) (učinkovito) podržavaju i operacije poput merge.

Neki još moćniji heapovi podržavaju i perzistentnost, tj. upite ili operacije nad bilo kojom prijašnjom inačicom, pri čemu nastaje nova inačica.

## Vrste heapova

|    Operacija `\` struktura podataka[^ref4]   |                                      Pairing heap                                     |      Binarni heap     |      Leftist tree     |          Binomni heap         |        Fibonaccijev heap       |
| :---------------------: | :--------------------------------------------------------------------------: | :----------: | :----------: | :------------------: | :----------------: |
|        umetanje (insert)       |                                    $O(1)$                                    |  $O(\log n)$ |  $O(\log n)$ |  $O(\log n)$[^ref1]  |       $O(1)$       |
|     upit za minimum (find-min)     |                                    $O(1)$                                    |    $O(1)$    |    $O(1)$    | $O(1)$[^ref2][^ref3] |       $O(1)$       |
|    brisanje minimuma (delete-min)    |                              $O(\log n)$[^ref3]                              |  $O(\log n)$ |  $O(\log n)$ |      $O(\log n)$     | $O(\log n)$[^ref3] |
|        spajanje (merge)       |                                    $O(1)$                                    |    $O(n)$    |  $O(\log n)$ |      $O(\log n)$     |       $O(1)$       |
| smanjivanje vrijednosti elementa (decrease-key) | $o(\log n)$ (donja granica $\Omega(\log \log n)$, gornja granica $O(2^{2\sqrt{\log \log n}})$)[^ref3] |  $O(\log n)$ |  $O(\log n)$ |      $O(\log n)$     |    $O(1)$[^ref3]   |
|         podržava perzistentnost        |                                   $\times$                                   | $\checkmark$ | $\checkmark$ |     $\checkmark$     |      $\times$      |

[^ref1]: Složenost jednog umetanja je $O(\log n)$, ali pri $k$ uzastopnih umetanja može se napraviti binomni heap samo od elemenata koji se umeću i zatim spojiti s izvornim binomnim heapom, uz amortiziranu složenost $O(1)$

[^ref2]: Može se čuvati pokazivač na najmanji element i ažurirati ga pri ostalim operacijama, pa je upit moguć u složenosti $O(1)$

[^ref3]: Složenost je amortizirana

[^ref4]: Tablica je preuzeta s [Wikipedije](https://en.wikipedia.org/wiki/Priority_queue#Summary_of_running_times)

Po običaju, kad se „heap” spominje bez pobliže oznake, obično se misli na binarni heap.
