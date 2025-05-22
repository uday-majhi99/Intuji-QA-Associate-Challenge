from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to handle login
def login_site(email, password):
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

    # ✅ Verify login success
    try:
        logged_in_as = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]").text
        assert "Logged in as" in logged_in_as, "[❌] Login failed."
        print(f"[✅] Login successful. {logged_in_as}")
    except Exception as e:
        print("[❌] Login failed.")
        print(e)

    # Return driver instance to allow further actions if necessary
    return driver
