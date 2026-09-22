// Lekcije kurikuluma: inline formula koja je šira od svog odlomka (uski zasloni)
// dobiva klasu "preduga" pa klizi vodoravno sama, umjesto da širi cijeli članak.
// Mora se učitati nakon mathjax-config.js, a prije MathJax skripte.
(function () {
    var KLASA = 'preduga';
    var timer = null;

    function blokRoditelj(el) {
        var r = el.parentElement;
        while (r && window.getComputedStyle(r).display.indexOf('inline') === 0) {
            r = r.parentElement;
        }
        return r;
    }

    function oznaci() {
        var formule = document.querySelectorAll('.analiza.lekcija mjx-container:not([display="true"])');
        for (var i = 0; i < formule.length; i++) {
            var f = formule[i];
            var roditelj = blokRoditelj(f);
            if (!roditelj) {
                continue;
            }
            f.classList.remove(KLASA);
            if (f.getBoundingClientRect().width > roditelj.clientWidth + 1) {
                f.classList.add(KLASA);
            }
        }
    }

    function zakazi() {
        window.clearTimeout(timer);
        timer = window.setTimeout(oznaci, 150);
    }

    if (!window.MathJax) {
        return;
    }
    var startup = window.MathJax.startup || {};
    var prijasnjiPageReady = startup.pageReady;
    startup.pageReady = function () {
        var gotovo = prijasnjiPageReady ? prijasnjiPageReady() : window.MathJax.startup.defaultPageReady();
        return gotovo.then(function (rezultat) {
            oznaci();
            window.addEventListener('resize', zakazi);
            return rezultat;
        });
    };
    window.MathJax.startup = startup;
}());
