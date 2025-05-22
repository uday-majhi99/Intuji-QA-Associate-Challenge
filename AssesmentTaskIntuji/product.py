from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from login import login_site

# Start Chrome WebDriver (no options used)
driver = webdriver.Chrome()
driver.maximize_window()

email = "umajhi1@gmail.com"
password = "Password@123"

driver = login_site(email, password)

driver.find_element(By.XPATH, "(//i[@class='fa fa-plus'])[1]").click() #Clicke on women button
time.sleep(2)

driver.find_element(By.XPATH, "(//a[contains(text(),'Dress')])[1]").click() #Clicked on dress button
time.sleep(2)

header = driver.find_element(By.XPATH, "//h2[normalize-space()='Women - Dress Products']").text
assert "WOMEN - DRESS PRODUCTS" in header.upper(), "Expected heading not found."
print("Women dress page : Expected Value for women dress page Found")

driver.find_element(By.XPATH, "//body[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/a[1]").click() #Clicked on product details
time.sleep(2)

# Verify Product name
product_name = driver.find_element(By.XPATH, "//h2[normalize-space()='Sleeveless Dress']").text
assert product_name != "", "[❌] Product name not found"
print(f" Product Name: {product_name}")

# Verify Product Price
price = driver.find_element(By.XPATH, "//span[normalize-space()='Rs. 1000']").text
assert price.startswith("Rs."), "[❌] Product price not found or invalid"
print(f" Product Price: {price}")

#  Verify Availability
availability = driver.find_element(By.CSS_SELECTOR, "body > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > p:nth-child(6)").text
assert "In Stock" in availability, "[❌] Product availability not confirmed"
print(f" Availability: {availability}")


# Close the browser
driver.quit()
