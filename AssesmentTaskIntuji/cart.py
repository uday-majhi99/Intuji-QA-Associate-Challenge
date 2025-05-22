from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# User credentials (must already be registered)
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

# ✅ Verify login success
try:
    logged_in_as = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]").text
    assert "Logged in as" in logged_in_as, "[❌] Login failed."
    print(f"[✅] Login successful. {logged_in_as}")
except Exception as e:
    print("[❌] Login failed.")
    print(e)

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
