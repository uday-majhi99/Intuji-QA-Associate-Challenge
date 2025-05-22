# checkout.py

from selenium.webdriver.common.by import By
import time

def complete_checkout(driver):
    try:
        # Go to cart
        driver.find_element(By.XPATH, "//a[normalize-space()='Cart']").click()
        time.sleep(2)

        # Proceed to checkout
        driver.find_element(By.XPATH, "//a[normalize-space()='Proceed To Checkout']").click()
        time.sleep(2)

        # Place order
        driver.find_element(By.XPATH, "//a[normalize-space()='Place Order']").click()
        time.sleep(2)

        # Fill in fake payment details
        driver.find_element(By.NAME, "name_on_card").send_keys("Uday Majhi")
        driver.find_element(By.NAME, "card_number").send_keys("4242424242424242")
        driver.find_element(By.NAME, "cvc").send_keys("311")
        driver.find_element(By.NAME, "expiry_month").send_keys("12")
        driver.find_element(By.NAME, "expiry_year").send_keys("2029")
        time.sleep(2)

        # Submit the order
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

        # Confirm success message
        confirmation_message = driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations! Your order has been confirmed!')]").text
        assert "Congratulations! Your order has been confirmed!" in confirmation_message
        print("[✅] Order confirmed!")

        # Logout
        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        time.sleep(2)

    except Exception as e:
        print(f"[❌] Checkout failed: {e}")
