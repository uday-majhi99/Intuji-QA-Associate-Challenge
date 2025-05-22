from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Credentials (must already be registered)
email = "umajhi1@gmail.com"
password = "Password@123"

# Start Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/login")
time.sleep(2)

# Fill in login form
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(email)
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

# Click Login
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(3)

# Verify login
try:
    logged_in_text = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]").text
    assert "Logged in as" in logged_in_text
    print(f"[✅] Login successful: {logged_in_text}")
except Exception as e:
    print("[❌] Login failed.")
    print(e)
    driver.quit()
