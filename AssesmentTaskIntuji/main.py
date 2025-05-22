from register import register_new_user
import time
from product import dress_site
from cart import add_product_to_cart
from checkoutAndPayment import complete_checkout
from LogoutLogin import login_site
from selenium.webdriver.common.by import By

email = "umajhi1@gmail.com"
password = "Password@123"

# Call the function to register and log in
driver, email = register_new_user()

# Now navigate and verify product details
dress_site(driver)

# Now navigate to cart
add_product_to_cart(driver)

# Checkout
complete_checkout(driver)

#LogOut
driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
time.sleep(2)

#Relogin
driver = login_site(email, password)

 # Pause if needed and quit
time.sleep(5)
driver.quit()

