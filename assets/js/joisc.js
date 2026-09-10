// JOISC arhiva: tabovi na stranici zadatka i interaktivni prikaz slajdova.
//
// Bez JavaScripta stranica je i dalje potpuno čitljiva: tabovi su obične
// poveznice na sidra, a slajdovi su prikazani jedan pod drugim. Ova skripta
// samo nadograđuje ponašanje (klasa "js" na <html> uključuje odgovarajući CSS).
(function () {
    document.documentElement.classList.add('js');

    var reducedMotion = window.matchMedia &&
        window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function reportBrokenImage(event) {
        var img = event.target;
        if (img && img.tagName === 'IMG' && typeof window.reportAssetError === 'function') {
            window.reportAssetError('Slika', img.getAttribute('src'));
        }
    }
    document.addEventListener('error', reportBrokenImage, true);

    /* ---------- Tabovi ---------- */

    function initTabs(root) {
        var tabs = Array.prototype.slice.call(root.querySelectorAll('a[role="tab"]'));
        var panels = tabs.map(function (tab) {
            return document.getElementById(tab.getAttribute('href').slice(1));
        });
        if (!tabs.length || panels.indexOf(null) !== -1) {
            return;
        }

        function select(index, focus) {
            tabs.forEach(function (tab, i) {
                var active = i === index;
                tab.setAttribute('aria-selected', active ? 'true' : 'false');
                tab.setAttribute('tabindex', active ? '0' : '-1');
                panels[i].setAttribute('data-aktivan', active ? 'da' : 'ne');
            });
            if (focus) {
                tabs[index].focus();
            }
        }

        tabs.forEach(function (tab, i) {
            tab.addEventListener('click', function (event) {
                event.preventDefault();
                select(i, false);
                if (window.history && window.history.replaceState) {
                    window.history.replaceState(null, '', tab.getAttribute('href'));
                }
            });
            tab.addEventListener('keydown', function (event) {
                var next = null;
                if (event.key === 'ArrowRight') {
                    next = (i + 1) % tabs.length;
                } else if (event.key === 'ArrowLeft') {
                    next = (i - 1 + tabs.length) % tabs.length;
                } else if (event.key === 'Home') {
                    next = 0;
                } else if (event.key === 'End') {
                    next = tabs.length - 1;
                }
                if (next !== null) {
                    event.preventDefault();
                    select(next, true);
                }
            });
        });

        function fromHash() {
            var hash = window.location.hash;
            for (var i = 0; i < tabs.length; i++) {
                if (tabs[i].getAttribute('href') === hash) {
                    return i;
                }
            }
            return -1;
        }

        var initial = fromHash();
        if (initial === -1) {
            // Kad je trenerski način uključen, prvo se otvara trenerski tab.
            var coachOn = document.documentElement.getAttribute('data-coach') === 'on';
            initial = 0;
            if (coachOn) {
                tabs.forEach(function (tab, i) {
                    if (tab.classList.contains('tab-trener')) {
                        initial = i;
                    }
                });
            }
        }
        select(initial, false);

        window.addEventListener('hashchange', function () {
            var idx = fromHash();
            if (idx !== -1) {
                select(idx, false);
            }
        });
    }

    /* ---------- Slajdovi ---------- */

    function initSlides(root) {
        var slides = Array.prototype.slice.call(root.querySelectorAll('.slajd'));
        if (slides.length < 2) {
            root.setAttribute('data-jedan', 'da');
            return;
        }
        var current = 0;
        var timer = null;
        var counter = root.querySelector('.brojac');
        var controls = root.querySelector('.kontrole');
        var prev = controls.querySelector('.prethodni');
        var next = controls.querySelector('.sljedeci');
        var range = controls.querySelector('input[type="range"]');
        var play = controls.querySelector('.animiraj');

        var sourceLabel = counter ? counter.textContent : '';
        range.min = '0';
        range.max = String(slides.length - 1);

        function show(index) {
            current = Math.max(0, Math.min(slides.length - 1, index));
            slides.forEach(function (slide, i) {
                slide.setAttribute('data-aktivan', i === current ? 'da' : 'ne');
            });
            counter.textContent = (current + 1) + ' / ' + slides.length +
                (sourceLabel ? ' \u00b7 ' + sourceLabel : '');
            range.value = String(current);
            prev.disabled = current === 0;
            next.disabled = current === slides.length - 1;
            if (current === slides.length - 1) {
                stop();
            }
        }

        function stop() {
            if (timer !== null) {
                window.clearInterval(timer);
                timer = null;
            }
            if (play) {
                play.setAttribute('aria-pressed', 'false');
                play.textContent = '▶ Animiraj';
            }
        }

        function start() {
            if (current === slides.length - 1) {
                show(0);
            }
            timer = window.setInterval(function () {
                show(current + 1);
            }, reducedMotion ? 3500 : 1800);
            play.setAttribute('aria-pressed', 'true');
            play.textContent = '❚❚ Zaustavi';
        }

        prev.addEventListener('click', function () { stop(); show(current - 1); });
        next.addEventListener('click', function () { stop(); show(current + 1); });
        range.addEventListener('input', function () { stop(); show(parseInt(range.value, 10)); });
        if (play) {
            play.addEventListener('click', function () {
                if (timer !== null) {
                    stop();
                } else {
                    start();
                }
            });
        }

        root.setAttribute('tabindex', '0');
        root.addEventListener('keydown', function (event) {
            if (event.target.tagName === 'INPUT') {
                return;
            }
            if (event.key === 'ArrowRight' || event.key === 'PageDown') {
                event.preventDefault();
                stop();
                show(current + 1);
            } else if (event.key === 'ArrowLeft' || event.key === 'PageUp') {
                event.preventDefault();
                stop();
                show(current - 1);
            } else if (event.key === 'Home') {
                event.preventDefault();
                stop();
                show(0);
            } else if (event.key === 'End') {
                event.preventDefault();
                stop();
                show(slides.length - 1);
            }
        });

        // Klik na sliku = sljedeći slajd (kao u prezentaciji).
        slides.forEach(function (slide) {
            var img = slide.querySelector('img');
            if (img) {
                img.style.cursor = 'pointer';
                img.addEventListener('click', function () { stop(); show(current + 1); });
            }
        });

        // Slike koje nisu prikazane učitavaju se lijeno da stranica bude brza.
        slides.forEach(function (slide, i) {
            var img = slide.querySelector('img');
            if (img && i > 1) {
                img.setAttribute('loading', 'lazy');
            }
        });

        show(0);
    }

    function init() {
        Array.prototype.forEach.call(document.querySelectorAll('.tabovi'), initTabs);
        Array.prototype.forEach.call(document.querySelectorAll('.slajdovi'), initSlides);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
}());
