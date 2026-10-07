---
title: Vezana lista
---

Ova stranica kratko predstavlja vezane liste (linked list).

## Uvod

Vezana lista je struktura podataka za pohranu podataka u kojoj su elementi povezani pokazivačima, poput karika lanca. Odlikuje se vrlo jednostavnim umetanjem i brisanjem podataka, ali lošijim pronalaženjem i čitanjem podataka.

## Razlika u odnosu na niz

I vezana lista i niz služe za pohranu podataka. Za razliku od vezane liste, niz sve elemente pohranjuje redom, jedan za drugim. Različiti načini pohrane daju im različite prednosti:

Vezana lista zbog svoje lančane strukture omogućuje jednostavno brisanje i umetanje podataka s $O(1)$ operacija. No upravo zbog toga pronalaženje i čitanje podataka nije tako učinkovito kao kod niza: za nasumični pristup podatku treba $O(n)$ operacija.

Niz omogućuje jednostavno pronalaženje i čitanje podataka, s $O(1)$ operacija za nasumični pristup. No brisanje i umetanje zahtijevaju $O(n)$ operacija.

## Izgradnja vezane liste

???+ tip "Savjet"
    Pri izgradnji vezane liste dio s pokazivačima prilično je apstraktan i teško ga je razumjeti samo iz opisa i koda; preporučujemo da si pritom crtate slike.

### Jednostruko vezana lista

Čvor jednostruko vezane liste sadrži podatkovno polje i pokazivačko polje: podatkovno polje čuva podatak, a pokazivačko polje povezuje trenutni čvor sa sljedećim.

![](images/list.svg)

???+ note "Implementacija"
    === "C++"
        ```cpp
        struct Node {
          int value;
          Node *next;
        };
        ```
    
    === "Python"
        ```python
        class Node:
            def __init__(self, value=None, next=None):
                self.value = value
                self.next = next
        ```

### Dvostruko vezana lista

Dvostruko vezana lista također ima podatkovno i pokazivačko polje. Razlika je u tome što pokazivačko polje ima lijevi i desni (odnosno prethodni i sljedeći) pokazivač, kojima se povezuju prethodni, trenutni i sljedeći čvor.

![](images/double-list.svg)

???+ note "Implementacija"
    === "C++"
        ```cpp
        struct Node {
          int value;
          Node *left;
          Node *right;
        };
        ```
    
    === "Python"
        ```python
        class Node:
            def __init__(self, value=None, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right
        ```

## Umetanje (upisivanje) podataka u vezanu listu

### Jednostruko vezana lista

Postupak je otprilike ovakav:

1.  inicijaliziraj podatak `node` koji se umeće;
2.  pokazivač `next` čvora `node` usmjeri na čvor koji slijedi iza `p`;
3.  pokazivač `next` čvora `p` usmjeri na `node`.

Konkretan tijek prikazuju sljedeće slike:

1.  ![](./images/list-insert-1.svg)
2.  ![](./images/list-insert-2.svg)
3.  ![](./images/list-insert-3.svg)

Implementacija u kodu:

???+ note "Implementacija"
    === "C++"
        ```cpp
        void insertNode(int i, Node *p) {
          Node *node = new Node;
          node->value = i;
          node->next = p->next;
          p->next = node;
        }
        ```
    
    === "Python"
        ```python
        def insertNode(i, p):
            node = Node()
            node.value = i
            node.next = p.next
            p.next = node
        ```

### Jednostruko vezana kružna lista

Ako spojimo početak i kraj liste, lista postaje kružna. Budući da su početak i kraj spojeni, pri umetanju treba provjeriti je li izvorna lista prazna: ako jest, čvor pokazuje sam na sebe, a ako nije, podatak se umeće uobičajeno.

Postupak je otprilike ovakav:

1.  inicijaliziraj podatak `node` koji se umeće;
2.  provjeri je li zadana lista `p` prazna;
3.  ako jest, pokazivač `next` čvora `node` i `p` usmjeri na sam `node`;
4.  inače pokazivač `next` čvora `node` usmjeri na čvor koji slijedi iza `p`;
5.  pokazivač `next` čvora `p` usmjeri na `node`.

Konkretan tijek prikazuju sljedeće slike:

1.  ![](./images/list-insert-cyclic-1.svg)
2.  ![](./images/list-insert-cyclic-2.svg)
3.  ![](./images/list-insert-cyclic-3.svg)

Implementacija u kodu:

???+ note "Implementacija"
    === "C++"
        ```cpp
        void insertNode(int i, Node *p) {
          Node *node = new Node;
          node->value = i;
          node->next = NULL;
          if (p == NULL) {
            p = node;
            node->next = node;
          } else {
            node->next = p->next;
            p->next = node;
          }
        }
        ```
    
    === "Python"
        ```python
        def insertNode(i, p):
            node = Node()
            node.value = i
            node.next = None
            if p == None:
                p = node
                node.next = node
            else:
                node.next = p.next
                p.next = node
        ```

### Dvostruko vezana kružna lista

Pri umetanju u dvostruko vezanu kružnu listu, osim provjere je li zadana lista prazna, treba istodobno ažurirati i lijevi i desni pokazivač.

Postupak je otprilike ovakav:

1.  inicijaliziraj podatak `node` koji se umeće;
2.  provjeri je li zadana lista `p` prazna;
3.  ako jest, pokazivače `left` i `right` čvora `node`, kao i `p`, usmjeri na sam `node`;
4.  inače pokazivač `left` čvora `node` usmjeri na `p`;
5.  pokazivač `right` čvora `node` usmjeri na desni čvor od `p`;
6.  pokazivač `left` desnog čvora od `p` usmjeri na `node`;
7.  pokazivač `right` čvora `p` usmjeri na `node`.

Implementacija u kodu:

???+ note "Implementacija"
    === "C++"
        ```cpp
        void insertNode(int i, Node *p) {
          Node *node = new Node;
          node->value = i;
          if (p == NULL) {
            p = node;
            node->left = node;
            node->right = node;
          } else {
            node->left = p;
            node->right = p->right;
            p->right->left = node;
            p->right = node;
          }
        }
        ```
    
    === "Python"
        ```python
        def insertNode(i, p):
            node = Node()
            node.value = i
            if p == None:
                p = node
                node.left = node
                node.right = node
            else:
                node.left = p
                node.right = p.right
                p.right.left = node
                p.right = node
        ```

## Brisanje podataka iz vezane liste

### Jednostruko vezana (kružna) lista

Neka je `p` čvor koji treba izbrisati. Da bismo ga uklonili iz liste, dovoljno je vrijednost sljedećeg čvora `p->next` prepisati u `p` i istodobno ažurirati pokazivač na čvor iza sljedećeg.

Postupak je otprilike ovakav:

1.  vrijednost sljedećeg čvora od `p` pridruži čvoru `p`, čime se briše `p->value`;
2.  napravi privremeni čvor `t` koji čuva adresu `p->next`;
3.  pokazivač `next` čvora `p` usmjeri na čvor iza sljedećeg, čime se briše `p->next`;
4.  izbriši `t`. Iako je adresa izvornog čvora `p` i dalje u uporabi, a obrisana je adresa izvornog `p->next`, podaci čvora `p` prepisani su podacima iz `p->next`, pa `p` postoji samo još po imenu.

Konkretan tijek prikazuju sljedeće slike:

1.  ![](./images/list-delete-1.svg)
2.  ![](./images/list-delete-2.svg)
3.  ![](./images/list-delete-3.svg)

Implementacija u kodu:

???+ note "Implementacija"
    === "C++"
        ```cpp
        void deleteNode(Node *p) {
          p->value = p->next->value;
          Node *t = p->next;
          p->next = p->next->next;
          delete t;
        }
        ```
    
    === "Python"
        ```python
        def deleteNode(p):
            p.value = p.next.value
            p.next = p.next.next
        ```

### Dvostruko vezana kružna lista

Postupak je otprilike ovakav:

1.  desni pokazivač lijevog čvora od `p` usmjeri na desni čvor od `p`;
2.  lijevi pokazivač desnog čvora od `p` usmjeri na lijevi čvor od `p`;
3.  napravi privremeni čvor `t` koji čuva adresu `p`;
4.  adresu desnog čvora od `p` pridruži čvoru `p`, da `p` ne bi postao viseći pokazivač;
5.  izbriši `t`.

Implementacija u kodu:

???+ note "Implementacija"
    === "C++"
        ```cpp
        void deleteNode(Node *&p) {
          p->left->right = p->right;
          p->right->left = p->left;
          Node *t = p;
          p = p->right;
          delete t;
        }
        ```
    
    === "Python"
        ```python
        def deleteNode(p):
            p.left.right = p.right
            p.right.left = p.left
            p = p.right
        ```

## Trikovi

### XOR lista

XOR lista (XOR linked list) u biti je i dalje **dvostruko vezana lista**, ali uz pomoć vrijednosti bitovnog XOR-a ostvaruje funkcionalnost dvostruko vezane liste koristeći memoriju samo jednog pokazivača.

U strukturi `Node` definiramo `lr = left ^ right`, tj. **bitovni XOR** adresa prethodnog i sljedećeg elementa. Pri obilasku prema naprijed XOR-om adrese prethodnog elementa i `lr` trenutnog čvora dobivamo adresu sljedećeg elementa, a pri obilasku unatrag XOR-om adrese sljedećeg elementa i `lr` trenutnog čvora dobivamo adresu prethodnog elementa.
Tako se s upola manje memorije ostvaruje ista funkcionalnost kao kod dvostruko vezane liste.
