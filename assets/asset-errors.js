(function () {
    var NOTICE_ID = 'asset-error-notice';

    function insertNotice(text) {
        var notice = document.getElementById(NOTICE_ID);
        if (!notice) {
            notice = document.createElement('div');
            notice.id = NOTICE_ID;
            notice.setAttribute('role', 'alert');
            notice.style.cssText = 'margin: 0 0 20px 0; padding: 12px 16px; border: 1px solid #f0c36d;' +
                ' border-left-width: 5px; background-color: #fdf6e3; color: #7a5b00;' +
                ' font-family: Arial, sans-serif; font-size: 15px; line-height: 1.5;';
            document.body.insertBefore(notice, document.body.firstChild);
        }
        var line = document.createElement('p');
        line.style.cssText = 'margin: 0;';
        line.textContent = text;
        notice.appendChild(line);
    }

    // Makes a failed external asset visible in the console and on the page
    // instead of leaving the page silently degraded.
    window.reportAssetError = function (asset, details) {
        var text = asset + ' se nije uspio učitati.' + (details ? ' ' + details : '');
        console.error('[asset-error] ' + asset, details || '');
        if (document.body) {
            insertNotice(text);
        } else {
            document.addEventListener('DOMContentLoaded', function () {
                insertNotice(text);
            });
        }
    };

    window.mathJaxStartup = {
        pageReady: function () {
            return window.MathJax.startup.defaultPageReady().catch(function (err) {
                window.reportAssetError('MathJax', 'Matematički izrazi nisu ispravno prikazani: ' + err.message);
                throw err;
            });
        }
    };
}());
