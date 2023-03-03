from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:/Users/Acids/Documents/chromedriver.exe')
driver.get("https://www.pokemon.com/us")  
time.sleep(5)  
driver.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler').click()  
time.sleep(5)  
driver.find_element(By.CSS_SELECTOR,'.explore a').click()  
time.sleep(5)  
driver.save_screenshot('.\pokemon\protected-web-using-user-agent.png')  
driver.quit()