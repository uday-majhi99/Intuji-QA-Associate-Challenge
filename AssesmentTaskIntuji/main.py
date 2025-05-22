from register import register_new_user
import time
from product import dress_site
from cart import add_product_to_cart

# Call the function to register and log in
driver, email = register_new_user()

# Now navigate and verify product details
dress_site(driver)

# Now navigate to cart
add_product_to_cart(driver)

 # Pause if needed and quit
time.sleep(5)
driver.quit()

