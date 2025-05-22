from selenium.webdriver.common.by import By
import time

def add_product_to_cart(driver):
    try:
        # Navigate to Women > Dress
        driver.find_element(By.XPATH, "(//i[@class='fa fa-plus'])[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "(//a[contains(text(),'Dress')])[1]").click()
        time.sleep(2)

        # Click on a specific dress
        driver.find_element(By.XPATH, "//div[@class='features_items']/div[2]//a").click()
        time.sleep(2)

        # Click "Continue Shopping"
        driver.find_element(By.XPATH, "//button[normalize-space()='Continue Shopping']").click()

        # Open cart
        driver.find_element(By.XPATH, "(//span[@class='badge pull-right'])[2]").click()
        time.sleep(2)

        # # Click on the product again
        driver.find_element(By.CSS_SELECTOR, "a[href='/category_products/3']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[2]//ul[1]//li[1]//a[1]").click()
        time.sleep(2)

        # Set quantity
        quantity_input = driver.find_element(By.XPATH, "//input[@id='quantity']")
        quantity_input.click()
        quantity_input.clear()
        quantity_input.send_keys("3")

        # Add to cart
        driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "(//button[normalize-space()='Continue Shopping'])[1]").click()
        time.sleep(2)

        print("[✅] Product added to cart successfully.")

    except Exception as e:
        print(f"[❌] Failed to add product to cart: {e}")
