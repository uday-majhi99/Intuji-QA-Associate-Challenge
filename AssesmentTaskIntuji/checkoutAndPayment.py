from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from login import login_site

driver = webdriver.Chrome()
email = "umajhi1@gmail.com"
password = "Password@123"

# User credentials (must already be registered)
email = "umajhi1@gmail.com"
password = "Password@123"

driver = login_site(email, password)

driver.find_element(By.XPATH, "//a[normalize-space()='Cart']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//a[normalize-space()='Proceed To Checkout']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//a[normalize-space()='Place Order']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//input[@name='name_on_card']").send_keys("Uday Majhi")
time.sleep(3)

driver.find_element(By.XPATH, "//input[@name='card_number']").send_keys("4242424242424242")
time.sleep(3)

driver.find_element(By.XPATH, "//input[@placeholder='ex. 311']").send_keys("311")
time.sleep(3)

driver.find_element(By.XPATH, "//input[@placeholder='MM']").send_keys("12")
time.sleep(3)

driver.find_element(By.XPATH, "//input[@placeholder='YYYY']").send_keys("2029")
time.sleep(3)

driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(3)

# Find the element containing the confirmation message
confirmation_message = driver.find_element(By.XPATH, "//p[normalize-space(text())='Congratulations! Your order has been confirmed!']")

# Assert the message is correct
assert "Congratulations! Your order has been confirmed!" in confirmation_message.text, "Confirmation message not found."
print("[✅] Order confirmed!")

driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
time.sleep(3)



driver.quit()
