from logging import handlers
from playwright.sync_api import sync_playwright


# gerando alias, na qual quando gerado o sync_playwright... ele se resume na função P.
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto ("https://www.google.com/")
    #Vou digitar Joydev no imput de text Name="q"
    page.fill("input[name='search_query']", 'joydev')
    #Vou clicar no botão pesquisar cujo name="btnk"
    page.click("input[name='search-icon-legacy']")
    page.click("")
    page.wait_for_timeout(10000)
    print(page.title())
    browser.close()