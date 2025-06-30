import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

# Initialize Twitter URL and other variables
url = "https://x.com/i/flow/login"
email = 'peachyymiah'
password = "Twitter24Miah"
# File path to save cookies
cookies_file = r"C:\Users\Haseeb\Desktop\twitter\twitter_cookies.txt"

# Function to save cookies
def save_cookies(driver, cookies_file):
    with open(cookies_file, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)

# Function to load cookies
def load_cookies(driver, cookies_file):
    with open(cookies_file, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)

# Initialize the WebDriver
driver = uc.Chrome()


driver.get(url)
sleep(20)

    # Enter email
email_input = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
email_input.send_keys(email)
email_input.send_keys(Keys.ENTER)
sleep(200)

# password_input = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
# password_input.send_keys(password)
# password_input.send_keys(Keys.ENTER)
# sleep(10)
# while True:
#     current_url = driver.current_url
#     if current_url != "https://x.com/home":
#         try:
#             verificationcode_input = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
#             verificationcode_input.send_keys(Keys.ENTER)
#         except Exception as e:
#             pass
                
#         sleep(20)
#     # Save cookies after login
#     if current_url == "https://x.com/home":
#         save_cookies(driver, cookies_file)
#         break
save_cookies(driver, cookies_file)
# Now you can interact with Twitter as a logged-in user
# Optional: Close the browser after operations
# driver.quit()
