import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the HTML file
# Update the URL to the path of your local HTML file
driver.get("file:///C:/Users/Lenovo/Documents/New%20folder/Ocean-AI-Assignment-QA/assets/checkout.html")

# Wait for the discount code input field to be visible
discount_code_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "discount-code"))
)

# Enter the discount code
discount_code_input.send_keys("SAVE15")

# Click the apply discount button
apply_discount_button = driver.find_element(By.ID, "apply-discount")
apply_discount_button.click()

# Wait for the discount message to be visible
discount_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "discount-message"))
)

# Verify the discount message
assert "15% Discount Applied!" in discount_message.text
assert "green" in discount_message.get_attribute("style")

# Get the total price element
total_price_element = driver.find_element(By.ID, "total-price")

# Calculate the expected total price after discount
expected_total_price = round(248.00 * 0.85, 2)

# Verify the total price
assert float(total_price_element.text) == expected_total_price

print("✅ Test Passed!")
time.sleep(5)
driver.quit()