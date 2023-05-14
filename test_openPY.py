from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Users/Дарья/Downloads/Chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qahacking.guru/")
driver.set_window_size(1050, 708)
driver.find_element(By.CSS_SELECTOR, ".uk-navbar-nav > li:nth-child(1) > a").click()
time.sleep(10)
driver.find_element(By.ID, "firstName").click()
driver.find_element(By.ID, "firstName").send_keys("Дарья")
driver.find_element(By.ID, "lastName").send_keys("Яворовская")
driver.find_element(By.ID, "userEmail").send_keys("yavorovskayadasha@gmail.com")
driver.find_element(By.ID, "sex-radio-2").click()
driver.find_element(By.ID, "userNumber").click()
driver.find_element(By.ID, "userNumber").send_keys("9627770133")
driver.find_element(By.ID, "date").send_keys("01/06/2023")
driver.find_element(By.ID, "hobbies-checkbox-1").click()
driver.find_element(By.CSS_SELECTOR, ".col-md-9:nth-child(6) #hobbies-checkbox-1").click()
driver.find_element(By.ID, "currentAddress").send_keys("Томск ул.Ленская 45 кв.18")
driver.find_element(By.ID, "submit").click()
time.sleep (5)


