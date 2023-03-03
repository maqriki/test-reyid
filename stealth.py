from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:/Users/Acids/Documents/chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://www.pokemon.com/us"
driver.get(url)
time.sleep(5)  
driver.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler').click()  
time.sleep(5)  
driver.find_element(By.CSS_SELECTOR,'.explore a').click()  
time.sleep(5)  
driver.save_screenshot('.\pokemon\protected-web-using-stealth.png')  
driver.quit()