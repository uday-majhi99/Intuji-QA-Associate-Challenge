from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
email = "umajhi1@gmail.com"
password = "Password@123"

# Initialize browser
driver = webdriver.Chrome()
driver.get("https://automationexercise.com/login")
driver.maximize_window()
time.sleep(2)

# Fill in login form
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(email)
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

# Click Login
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(3)

try:
    logged_in_as = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]").text
    assert "Logged in as" in logged_in_as, "[❌] Login failed."
    print(f"[✅] Login successful. {logged_in_as}")
except Exception as e:
    print("[❌] Login failed.")
    print(e)

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
