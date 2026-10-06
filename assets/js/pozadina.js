/* Pozadina: crna podloga s finom bijelom mrežom i nasumičnim ASCII znakovima (Consolas).
   Crta se na <canvas> fiksiranom preko cijelog prozora; bez JS-a ostaje samo CSS mreža. */
(function () {
    'use strict';
    var root = document.documentElement;
    var cfg = {
        cell: 16,          // veličina ćelije mreže (px)
        density: 0.08,     // udio ćelija sa znakom
        alphaMin: 0.12,    // najtamniji znak
        alphaMax: 0.45,    // najsvjetliji znak
        charset: 'all',    // all | symbols | alnum | binary
        twinkle: true,     // povremeno mijenjaj nekoliko znakova
        seedFixed: false   // isti raspored pri svakom učitavanju
    };
    var SETS = {
        all: '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~',
        symbols: '!#$%&*+-/<=>?@[\\]^{|}~;:',
        alnum: '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        binary: '01'
    };
    function readCfg() {
        var cs = getComputedStyle(root);
        var g = function (name, fallback, parse) {
            var v = cs.getPropertyValue(name).trim();
            return v ? (parse ? parse(v) : v) : fallback;
        };
        cfg.cell = g('--pozadina-celija', cfg.cell, parseFloat);
        cfg.density = g('--pozadina-gustoca', cfg.density, parseFloat);
        cfg.alphaMin = g('--pozadina-alfa-min', cfg.alphaMin, parseFloat);
        cfg.alphaMax = g('--pozadina-alfa-max', cfg.alphaMax, parseFloat);
        cfg.charset = g('--pozadina-znakovi', cfg.charset).replace(/["']/g, '');
        cfg.twinkle = g('--pozadina-treptanje', cfg.twinkle ? '1' : '0') !== '0';
    }
    var canvas = document.createElement('canvas');
    canvas.className = 'pozadina-ascii';
    canvas.setAttribute('aria-hidden', 'true');
    var ctx = canvas.getContext('2d');
    var cells = []; // {x,y,ch,a}
    var cols = 0, rows = 0, dpr = 1;

    // Deterministički generator (mulberry32) kad želimo isti raspored na svakoj stranici
    function rng(seed) {
        var t = seed >>> 0;
        return function () {
            t = (t + 0x6D2B79F5) >>> 0;
            var r = Math.imul(t ^ (t >>> 15), 1 | t);
            r ^= r + Math.imul(r ^ (r >>> 7), 61 | r);
            return ((r ^ (r >>> 14)) >>> 0) / 4294967296;
        };
    }
    var rand = Math.random;

    function font() {
        var size = Math.round(cfg.cell * 0.78);
        return size + 'px Consolas, "Liberation Mono", Menlo, "DejaVu Sans Mono", monospace';
    }
    function layout() {
        dpr = Math.min(window.devicePixelRatio || 1, 2);
        var w = window.innerWidth, h = window.innerHeight;
        canvas.width = Math.ceil(w * dpr);
        canvas.height = Math.ceil(h * dpr);
        canvas.style.width = w + 'px';
        canvas.style.height = h + 'px';
        cols = Math.ceil(w / cfg.cell);
        rows = Math.ceil(h / cfg.cell);
        rand = cfg.seedFixed ? rng(20250101) : Math.random;
        var set = SETS[cfg.charset] || SETS.all;
        cells = [];
        for (var y = 0; y < rows; y++) {
            for (var x = 0; x < cols; x++) {
                if (rand() < cfg.density) {
                    cells.push({ x: x, y: y, ch: set[Math.floor(rand() * set.length)],
                                 a: cfg.alphaMin + rand() * (cfg.alphaMax - cfg.alphaMin) });
                }
            }
        }
        draw();
    }
    function draw() {
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.font = font();
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        var half = cfg.cell / 2;
        for (var i = 0; i < cells.length; i++) {
            var c = cells[i];
            ctx.fillStyle = 'rgba(255,255,255,' + c.a.toFixed(3) + ')';
            ctx.fillText(c.ch, c.x * cfg.cell + half, c.y * cfg.cell + half + 1);
        }
    }
    var twinkleTimer = null;
    function startTwinkle() {
        if (twinkleTimer) clearInterval(twinkleTimer);
        twinkleTimer = null;
        if (!cfg.twinkle || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        twinkleTimer = setInterval(function () {
            if (!cells.length || document.hidden) return;
            var set = SETS[cfg.charset] || SETS.all;
            var n = Math.max(1, Math.round(cells.length * 0.02));
            for (var k = 0; k < n; k++) {
                var c = cells[Math.floor(Math.random() * cells.length)];
                c.ch = set[Math.floor(Math.random() * set.length)];
                c.a = cfg.alphaMin + Math.random() * (cfg.alphaMax - cfg.alphaMin);
            }
            draw();
        }, 900);
    }
    var resizeTimer = null;
    function onResize() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(layout, 120);
    }
    function init() {
        readCfg();
        document.body.insertBefore(canvas, document.body.firstChild);
        // Pričekaj da se font učita da se znakovi ne crtaju zamjenskim fontom
        var go = function () { layout(); startTwinkle(); };
        if (document.fonts && document.fonts.load) {
            document.fonts.load(font()).then(go, go);
        } else { go(); }
        window.addEventListener('resize', onResize);
    }
    // Javno sučelje za pregled/varijante
    window.pozadina = {
        refresh: function (extra) {
            readCfg();
            if (extra) for (var k in extra) cfg[k] = extra[k];
            layout();
            startTwinkle();
        },
        config: cfg
    };
    if (document.body) init(); else document.addEventListener('DOMContentLoaded', init);
})();
