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

    function naslovi(jezik) {
        var sel = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'].map(function (t) { return '.jezik-' + jezik + ' ' + t + '[id]'; }).join(', ');
        return document.querySelectorAll(sel);
    }

    // Vrati element za #kotvu u aktivnom jeziku. Ako slug ne postoji (naslovi su različito
    // prevedeni), traži isti naslov po rednom broju u drugom jeziku – struktura je 1:1.
    function ciljKotve(h) {
        var sad = trenutni(), drugi = sad === 'en' ? 'hr' : 'en';
        var osnovna = h.replace(/^en-/, '');
        var el = document.getElementById(sad === 'en' ? 'en-' + osnovna : osnovna);
        if (el) return el;
        var izvor = document.getElementById(drugi === 'en' ? 'en-' + osnovna : osnovna) || document.getElementById(h);
        if (!izvor) return null;
        var a = naslovi(drugi), b = naslovi(sad);
        for (var i = 0; i < a.length && i < b.length; i++) {
            if (a[i] === izvor) return b[i];
        }
        return null;
    }

    function skociNaKotvu() {
        var h;
        try { h = decodeURIComponent(location.hash.slice(1)); } catch (e) { h = location.hash.slice(1); }
        if (!h) return;
        var el = ciljKotve(h);
        if (!el) return;
        if (el.id !== h && history.replaceState) {
            try { history.replaceState(null, '', '#' + el.id); } catch (e) { /* file:// */ }
        }
        el.scrollIntoView();
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
