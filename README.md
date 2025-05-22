automation-test-suite/
│
├── main.py                     # Main test runner script
├── login.py                   # Contains reusable login function
├── register.py                # Handles user registration
├── product.py                 # Product browsing and detail verification
├── cart.py                    # Cart management functions
├── checkout.py                # Checkout and fake payment flow
├── cookies.py                 # Cookie saving and loading logic
├── utils/                     # Common utilities (optional)
├── session_cookies.json       # Stored browser session cookies
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
✅ Features Covered
User Registration

Register with random user using faker

Check for email uniqueness

Validate post-registration login

Session Management

Save and reuse session cookies

Product Browsing

Navigate through categories (e.g., Women > Dress)

Validate filtered product results

Verify product detail (name, price, availability)

Cart Management

Add products from multiple categories

Change item quantity and validate cart totals

Remove item from cart

Checkout Flow

Proceed to checkout

Fill fake payment details

Confirm order and assert confirmation message

Logout and Re-login

Logout user

Login again and verify session persistence

Only run main.py and all the processing is there

🛠️ Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourname/automation-test-suite.git
cd automation-test-suite
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the main test:

bash
Copy
Edit
python main.py
🧾 Requirements
Python 3.7+

Google Chrome & ChromeDriver

selenium

faker

Install ChromeDriver and ensure it matches your Chrome version. Add it to your system PATH.

📄 Test Cases
All test cases are documented in test_cases.xlsx which includes:

Steps

Expected Results

Status (Pass/Fail)

Notes

🔄 Reusability
All functions (e.g., login_site(), register_new_user(), add_product_to_cart()) are designed to be importable and reusable across test flows.
