// Detaljno rješenje – globalna postavka stranice (uz Trenerski način).
//
// Stanje se čuva u localStorage i preslikava na atribut data-detaljno ("on"/"off")
// korijenskog <html> elementa. Sadržaj koji ovisi o postavci označen je u HTML-u
// isključivo klasama "rjesenje-sazeto" / "rjesenje-detaljno" (statični tekst);
// prikaz i skrivanje rješava CSS u assets/css/trener.css, a ova skripta upravlja
// samo stanjem i prekidačem. Učitava se u <head> (bez defer), nakon coach-mode.js,
// kako bi se atribut postavio prije prvog iscrtavanja.
(function () {
    var STORAGE_KEY = 'detaljnoRjesenje';
    var EVENT_NAME = 'detailedmodechange';
    var TOGGLE_ID = 'detaljno-prekidac';

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
        document.documentElement.setAttribute('data-detaljno', enabled ? 'on' : 'off');
        var toggle = document.getElementById(TOGGLE_ID);
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
        if (document.getElementById(TOGGLE_ID)) {
            return;
        }
        var wrap = document.querySelector('.postavke');
        if (!wrap) {
            wrap = document.createElement('div');
            wrap.className = 'postavke';
            wrap.setAttribute('role', 'group');
            wrap.setAttribute('aria-label', 'Postavke stranice');
            document.body.insertBefore(wrap, document.body.firstChild);
        }

        var label = document.createElement('label');
        label.className = 'prekidac prekidac-detaljno';
        label.title = 'Kad je uključen, u rješenju se umjesto sažetog prijevoda prikazuje detaljno ' +
            'objašnjenje svakog koraka te lokalno testiran C++ kod.';

        var input = document.createElement('input');
        input.type = 'checkbox';
        input.id = TOGGLE_ID;
        input.setAttribute('role', 'switch');

        var slider = document.createElement('span');
        slider.className = 'prekidac-klizac';
        slider.setAttribute('aria-hidden', 'true');

        var text = document.createElement('span');
        text.className = 'prekidac-tekst';
        text.textContent = 'Detaljno rješenje';

        input.addEventListener('change', function () {
            setEnabled(input.checked);
        });

        label.appendChild(input);
        label.appendChild(slider);
        label.appendChild(text);
        wrap.appendChild(label);
        apply(window.DetailedMode.isEnabled());
    }

    window.DetailedMode = {
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
