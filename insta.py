from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define your Instagram credentials
INSTAGRAM_USERNAME = "your_username"
INSTAGRAM_PASSWORD = "your_password"
HASHTAG = "nature"  # Change this to your desired hashtag

# Set up the Selenium WebDriver
driver = webdriver.Chrome(executable_path="path_to_chromedriver")

try:
    # Open Instagram
    driver.get("https://www.instagram.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    # Log in to Instagram
    driver.find_element(By.NAME, "username").send_keys(INSTAGRAM_USERNAME)
    driver.find_element(By.NAME, "password").send_keys(INSTAGRAM_PASSWORD, Keys.RETURN)

    # Wait for the login to complete
    WebDriverWait(driver, 20).until(EC.url_contains("https://www.instagram.com/"))

    # Search for the hashtag
    driver.get(f"https://www.instagram.com/explore/tags/{HASHTAG}/")
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "v1Nh3")))

    # Find and interact with posts
    posts = driver.find_elements(By.CLASS_NAME, "v1Nh3")
    for post in posts[:10]:  # Limit to the first 10 posts
        post.click()
        time.sleep(2)

        # Like the post
        try:
            like_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='Like']"))
            )
            like_button.click()
        except:
            print("Post already liked or an error occurred.")
        
        # Close the post
        close_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
        close_button.click()
        time.sleep(1)

finally:
    driver.quit()
