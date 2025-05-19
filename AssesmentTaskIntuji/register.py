from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
import time

# Initialize the browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")

# Generate fake user data
fake = Faker()
name = fake.name(),
email = fake.unique.email(),
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

# Click "Signup" button
driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()
time.sleep(3)

# Fill registration form
driver.find_element(By.XPATH, "//label[normalize-space()='Mr.']").click()  # Gender
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Password@123")
time.sleep(3)

# Select DOB
Select(driver.find_element(By.XPATH, "//select[@id='days']")).select_by_value("10")
time.sleep(3)
Select(driver.find_element(By.XPATH, "//select[@id='months']")).select_by_visible_text("May")
time.sleep(3)
Select(driver.find_element(By.XPATH, "//select[@id='years']")).select_by_value("1995")
time.sleep(3)


# Fill address details
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(first_name)
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys(last_name)
driver.find_element(By.XPATH, "//input[@id='company']").send_keys(company)
driver.find_element(By.XPATH, "//input[@id='address1']").send_keys(address1)
driver.find_element(By.XPATH, "//input[@id='address2']").send_keys(address2)
driver.find_element(By.XPATH, "//input[@id='state']").send_keys(state)
driver.find_element(By.XPATH, "//input[@id='city']").send_keys(city)
driver.find_element(By.XPATH, "//input[@id='zipcode']").send_keys(zipcode)
driver.find_element(By.XPATH, "//input[@id='mobile_number']").send_keys(mobile)
driver.find_element(By.XPATH, "//button[normalize-space()='Create Account']").click()
time.sleep(5)

# Wait and close
time.sleep(5)
driver.quit()
