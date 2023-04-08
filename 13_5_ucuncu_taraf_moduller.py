import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

response = requests.get("https://www.google.com/custom", {
    "q": "ramazan",
    "sitesearch": "http://teknolojiaihl.meb.k12.tr"
})

print(response.content)

chrome_install = ChromeDriverManager().install()
print(chrome_install)
chrome_service = Service(chrome_install)
browser = webdriver.Chrome(service=chrome_service)

# tam ekran
browser.maximize_window()

# arama sayfasına girelim
browser.get("https://www.google.com/custom?q=ramazan&sitesearch=http://teknolojiaihl.meb.k12.tr")
print(browser.title)

browser.get("https://www.google.com.tr")
browser.find_element(By.XPATH)

time.sleep(5)
