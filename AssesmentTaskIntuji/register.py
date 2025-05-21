from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from faker import Faker
import json
import time

# Initialize browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")

# Generate valid fake data (remove trailing commas)
fake = Faker()
name = fake.name()
email = fake.unique.email()
first_name = fake.first_name()
last_name = fake.last_name()
company = fake.company()
address1 = fake.street_address()
address2 = fake.secondary_address()
state = fake.state()
city = fake.city()
zipcode = fake.zipcode()
mobile = fake.phone_number()

# Click "Signup / Login"
driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()
time.sleep(2)

# Fill name and email
driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys(name)
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)

# Click "Signup"
driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()
time.sleep(3)

# Check if email already exists
try:
    error = driver.find_element(By.XPATH, "//*[contains(text(),'Email Address already exist!')]")
    if error.is_displayed():
        print("[❌] Email already exists.")
        driver.quit()
        exit()
except NoSuchElementException:
    pass  # Continue registration if no error

# Fill registration form
driver.find_element(By.XPATH, "//label[normalize-space()='Mr.']").click()
driver.find_element(By.ID, "password").send_keys("Password@123")
Select(driver.find_element(By.ID, "days")).select_by_value("10")
Select(driver.find_element(By.ID, "months")).select_by_visible_text("May")
Select(driver.find_element(By.ID, "years")).select_by_value("1995")

# Address info
driver.find_element(By.ID, "first_name").send_keys(first_name)
driver.find_element(By.ID, "last_name").send_keys(last_name)
driver.find_element(By.ID, "company").send_keys(company)
driver.find_element(By.ID, "address1").send_keys(address1)
driver.find_element(By.ID, "address2").send_keys(address2)
driver.find_element(By.ID, "state").send_keys(state)
driver.find_element(By.ID, "city").send_keys(city)
driver.find_element(By.ID, "zipcode").send_keys(zipcode)
driver.find_element(By.ID, "mobile_number").send_keys(mobile)

# Submit form
driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()
time.sleep(3)

# Verify user is logged in
try:
    logged_in_text = driver.find_element(By.XPATH, "//i[@class='fa fa-user']").text
    assert name.split()[0] in logged_in_text
    print(f"Registration successful. User is logged in as: {logged_in_text}")
except:
    print(" Login verification failed.")



# Save session cookies
cookies = driver.get_cookies()
with open("session_cookies.json", "w") as f:
    json.dump(cookies, f)
print("[💾] Session cookies saved.")

# Optional: reuse cookies in another test
# driver.delete_all_cookies()
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.get("https://automationexercise.com")

# Cleanup
time.sleep(5)
driver.quit()
