from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from login import login_site

# User credentials (must already be registered)
email = "umajhi1@gmail.com"
password = "Password@123"

driver = login_site(email, password)

driver.find_element(By.XPATH, "(//i[@class='fa fa-plus'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//a[contains(text(),'Dress')])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//body/section/div[@class='container']/div[@class='row']/div[@class='col-sm-9 padding-right']/div[@class='features_items']/div[2]/div[1]/div[1]/div[1]/a[1]").click() #Clicked on dress button
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='Continue Shopping']").click()

driver.find_element(By.XPATH, "(//span[@class='badge pull-right'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//span[@class='badge pull-right'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//body[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/a[1]").click() #Clicked on dress button

driver.find_element(By.XPATH, "//input[@id='quantity']").click()
input_field = driver.find_element(By.XPATH, "//input[@id='quantity']")
input_field.clear()
driver.find_element(By.XPATH, "//input[@id='quantity']").send_keys(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']").click()
time.sleep(2)




driver.quit()
