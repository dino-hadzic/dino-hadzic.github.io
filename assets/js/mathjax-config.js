// Zajednička MathJax 3 konfiguracija za sve stranice.
// Mora se učitati PRIJE MathJax skripte (tex-chtml.js / tex-mml-chtml.js / tex-svg.js).
window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true
    },
    svg: {
        fontCache: 'global'
    }
};
