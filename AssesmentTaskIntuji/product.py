from selenium.webdriver.common.by import By
import time

def dress_site(driver):


    # Click on 'Women' category
    driver.find_element(By.XPATH, "(//i[@class='fa fa-plus'])[1]").click()
    time.sleep(2)

    # Click on 'Dress' under Women
    driver.find_element(By.XPATH, "(//a[contains(text(),'Dress')])[1]").click()
    time.sleep(2)

    # Verify category heading
    header = driver.find_element(By.XPATH, "//h2[normalize-space()='Women - Dress Products']").text
    assert "WOMEN - DRESS PRODUCTS" in header.upper(), "[❌] Expected heading not found."
    print("[✅] Women dress page loaded correctly.")

    # Click on the first product's 'View Product' link
    driver.find_element(By.XPATH, "//ul/li[1]/a[contains(text(),'View Product')]").click()
    time.sleep(2)

    # Verify Product Name
    product_name = driver.find_element(By.XPATH, "//h2[normalize-space()='Sleeveless Dress']").text
    assert product_name != "", "[❌] Product name not found"
    print(f"[🛍️] Product Name: {product_name}")

    # Verify Product Price
    price = driver.find_element(By.XPATH, "//span[normalize-space()='Rs. 1000']").text
    assert price.startswith("Rs."), "[❌] Product price not found or invalid"
    print(f"[💰] Product Price: {price}")

    # Verify Availability
    availability = driver.find_element(By.CSS_SELECTOR,"body > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > p:nth-child(6)").text
    assert "In Stock" in availability, "[❌] Product availability not confirmed"
    print(f"[📦] Availability: {availability}")
