from playwright.sync_api import sync_playwright
import time

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page().goto('https://www.saucedemo.com/')


browser.close()
playwright.stop()