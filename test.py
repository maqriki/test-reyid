# Test failed cause pokemon's website using imperva protection

import time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

driver = uc.Chrome()  
driver.maximize_window()  
driver.get("https://www.pokemon.com/us")  
time.sleep(5)  
driver.find_element(By.CSS_SELECTOR,'#onetrust-accept-btn-handler').click()  
time.sleep(5)  
driver.find_element(By.CSS_SELECTOR,'.explore a').click()  
time.sleep(5)  
driver.save_screenshot('.\pokemon\protected-web-using-undetected-chromedriver.png')  
driver.quit()  