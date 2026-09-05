// Trenerski način (Coach Mode) – globalna postavka stranice.
//
// Stanje se čuva u localStorage i preslikava na atribut data-coach ("on"/"off")
// korijenskog <html> elementa. Sav sadržaj koji ovisi o postavci označen je
// u HTML-u isključivo klasom "trener" (statični tekst); prikaz i skrivanje
// rješava CSS u assets/css/trener.css, a ova skripta upravlja samo stanjem
// i prekidačem. Skripta se mora učitati u <head> (bez defer) kako bi se
// atribut postavio prije prvog iscrtavanja.
(function () {
    var STORAGE_KEY = 'trenerskiNacin';
    var EVENT_NAME = 'coachmodechange';

    function readStored() {
        try {
            return window.localStorage.getItem(STORAGE_KEY) === 'on';
        } catch (e) {
            return false;
        }
    }

    function writeStored(enabled) {
        try {
            window.localStorage.setItem(STORAGE_KEY, enabled ? 'on' : 'off');
        } catch (e) {
            // Privatni način rada ili blokirana pohrana: postavka vrijedi samo za ovu stranicu.
        }
    }

    function apply(enabled) {
        document.documentElement.setAttribute('data-coach', enabled ? 'on' : 'off');
        var toggle = document.getElementById('trener-prekidac');
        if (toggle) {
            toggle.checked = enabled;
            toggle.setAttribute('aria-checked', enabled ? 'true' : 'false');
        }
    }

    function setEnabled(enabled) {
        writeStored(enabled);
        apply(enabled);
        document.dispatchEvent(new CustomEvent(EVENT_NAME, { detail: { enabled: enabled } }));
    }

    function buildToggle() {
        if (document.getElementById('trener-prekidac')) {
            return;
        }
        var wrap = document.createElement('div');
        wrap.className = 'postavke';
        wrap.setAttribute('role', 'group');
        wrap.setAttribute('aria-label', 'Postavke stranice');

        var label = document.createElement('label');
        label.className = 'prekidac';
        label.title = 'Kad je uključen, uz svaki zadatak prikazuje se vođeni tok razmišljanja ' +
            '(opažanja, redukcije, odabir algoritma) prije konačnog rješenja.';

        var input = document.createElement('input');
        input.type = 'checkbox';
        input.id = 'trener-prekidac';
        input.setAttribute('role', 'switch');

        var slider = document.createElement('span');
        slider.className = 'prekidac-klizac';
        slider.setAttribute('aria-hidden', 'true');

        var text = document.createElement('span');
        text.className = 'prekidac-tekst';
        text.textContent = 'Trenerski način';

        input.addEventListener('change', function () {
            setEnabled(input.checked);
        });

        label.appendChild(input);
        label.appendChild(slider);
        label.appendChild(text);
        wrap.appendChild(label);
        document.body.insertBefore(wrap, document.body.firstChild);
        apply(window.CoachMode.isEnabled());
    }

    window.CoachMode = {
        STORAGE_KEY: STORAGE_KEY,
        EVENT_NAME: EVENT_NAME,
        isEnabled: readStored,
        setEnabled: setEnabled,
        toggle: function () {
            setEnabled(!readStored());
        }
    };

    apply(readStored());

    // Ako je postavka promijenjena u drugoj kartici, uskladi i ovu stranicu.
    window.addEventListener('storage', function (event) {
        if (event.key === STORAGE_KEY) {
            apply(event.newValue === 'on');
        }
    });

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', buildToggle);
    } else {
        buildToggle();
    }
}());
