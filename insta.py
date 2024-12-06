from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv()
USERNAME = os.getenv("user")
PASSWORD = os.getenv("pass")

if not USERNAME or not PASSWORD:
    raise ValueError("Instagram username or password is missing in the .env file.")

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open Instagram login page
    driver.get("https://www.instagram.com/accounts/login/")
    
    # Wait for the login fields to load and enter credentials
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys(USERNAME)
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    
    # Wait for the homepage to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='feed']"))
    )
    print("Login successful. Liking posts on the home screen...")

    # Scroll and like posts
    for _ in range(5):  # Adjust the range for more posts
        # Find all Like buttons (ensure you don't re-like already liked posts)
        like_buttons = driver.find_elements(
            By.XPATH, "//button//*[name()='svg' and @aria-label='Like']"
        )
        for button in like_buttons:
            try:
                button.click()
                print("Liked a post.")
                time.sleep(2)  # Small delay to mimic human behavior
            except Exception as e:
                print(f"Error while liking a post: {e}")

        # Scroll down to load more posts
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

except Exception as e:
    print("An error occurred:", e)

finally:
    print("")
    # Keep the browser open for debugging purposes
    # Comment or remove the next line if you want the browser to close:
    # driver.quit()
