from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
s=Service('C:/Users/Дарья/Downloads/Chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
driver.set_window_size(1366, 768)
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "login-otp-button").click()
exitbutton = driver.find_element(By.ID, "logout-button")

driver.find_element(By.XPATH, "//*[@id='representee-list']/div/button").click()
driver.find_element(By.XPATH,"//*[@id='representee-list']/div/div/ul/li[2]/a/span").click()
time.sleep(15)
driver.find_element(By.ID, "close-alerts-dialog").click()
time.sleep(5)