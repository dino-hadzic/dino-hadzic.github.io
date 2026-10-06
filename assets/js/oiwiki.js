// OI Wiki prijevod: gumb Hrvatski/English. Odabir se pamti u localStorage ('oiwiki-jezik');
// stranica sadrži oba jezika, a <html data-jezik> određuje koji je vidljiv (CSS u oiwiki.css).
// Kotve engleskog teksta imaju prefiks "en-", pa #kotva iz hrvatske inačice preusmjeravamo kad je engleski aktivan.
(function () {
    'use strict';
    var KLJUC = 'oiwiki-jezik';
    var root = document.documentElement;

    function trenutni() {
        return root.getAttribute('data-jezik') === 'en' ? 'en' : 'hr';
    }

    function postavi(jezik, pamti) {
        root.setAttribute('data-jezik', jezik);
        root.lang = jezik;
        var gumbi = document.querySelectorAll('.oiwiki-prebaci button');
        for (var i = 0; i < gumbi.length; i++) {
            gumbi[i].setAttribute('aria-pressed', gumbi[i].getAttribute('data-jezik') === jezik ? 'true' : 'false');
        }
        if (pamti) {
            try { localStorage.setItem(KLJUC, jezik); } catch (e) { /* privatni način rada */ }
        }
        skociNaKotvu();
    }

    function skociNaKotvu() {
        var h = decodeURIComponent(location.hash.slice(1));
        if (!h) return;
        var osnovna = h.replace(/^en-/, '');
        var cilj = trenutni() === 'en' ? 'en-' + osnovna : osnovna;
        var el = document.getElementById(cilj);
        if (el) el.scrollIntoView();
    }

    document.addEventListener('click', function (e) {
        var b = e.target.closest ? e.target.closest('.oiwiki-prebaci button') : null;
        if (!b) return;
        postavi(b.getAttribute('data-jezik'), true);
    });

    window.addEventListener('hashchange', skociNaKotvu);

    var pocetni = 'hr';
    try { pocetni = localStorage.getItem(KLJUC) === 'en' ? 'en' : 'hr'; } catch (e) { /* nema localStorage */ }
    postavi(pocetni, false);
})();
