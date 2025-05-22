from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login_site(email, password):
    try:
        # Initialize WebDriver
        driver = webdriver.Chrome()

        # Fill in login credentials
        driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)

        # Click Login
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)

        # Verify login
        logged_in_text = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]").text
        assert "Logged in as" in logged_in_text, "[❌] Login failed."
        print(f"[✅] Login successful. {logged_in_text}")

        return driver  # Return driver for further use

    except Exception as e:
        print(f"[❌] Login failed: {e}")
        if 'driver' in locals():
            driver.quit()
        return None
