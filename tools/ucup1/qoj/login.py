"""Prijava na qoj.ac (samo čitanje). Lozinka iz env QOJ_PASS, korisnik iz QOJ_USER."""
import os, re, time
from playwright.sync_api import sync_playwright
user, pw = os.environ['QOJ_USER'], os.environ['QOJ_PASS']
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp('http://localhost:29229')
    pg = b.contexts[0].new_page()
    pg.goto('https://qoj.ac/login', wait_until='domcontentloaded', timeout=60000)
    for _ in range(40):
        if 'Just a moment' not in pg.title(): break
        time.sleep(1)
    print('title', pg.title())
    print([ (i.get_attribute('name'), i.get_attribute('type'), i.get_attribute('id')) for i in pg.query_selector_all('input')])
    pg.fill('#input-username', user)
    pg.fill('#input-password', pw)
    pg.click('#button-submit')
    pg.wait_for_timeout(4000)
    print('after login:', pg.url, pg.title())
    pg.goto('https://qoj.ac/submissions?problem_id=6558', wait_until='domcontentloaded', timeout=60000)
    time.sleep(2)
    h = pg.content()
    print('subs page:', pg.title(), 'links', len(set(re.findall(r'/submission/(\d+)', h))))
    pg.close()
