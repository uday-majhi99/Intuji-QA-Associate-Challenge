from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_site(email, password):
    # Start Chrome browser
    driver = webdriver.Chrome()

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
        return driver  # Return the driver for further use
    except Exception as e:
        print("[❌] Login failed.")
        print(e)
        driver.quit()
        return None
