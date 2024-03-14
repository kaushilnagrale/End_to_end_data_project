from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
from selenium.webdriver.chrome.options import Options
import zipfile


class Browser:
    def __init__(self, driver_path, chrome_options=None):
        # Create a new instance of the ChromeOptions class if options are provided
        self.chrome_options = chrome_options if chrome_options else webdriver.ChromeOptions()
        # Add the path to ChromeDriver executable to the 'executable_path' option
        self.chrome_options.add_argument(f"webdriver.chrome.driver={driver_path}")

        # Create a new instance of the Chrome driver with ChromeOptions
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def open_url(self, url):
        self.driver.get(url)
        
    def click(self, button_selector):
            # Wait for the button to be clickable
             go_button = WebDriverWait(self.driver, 15).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
            )
             
    def insert_text_by_id(self,textbox,text):
        #this method will put a respect text in the passed ID
        location_element = self.driver.find_element(By.ID, textbox)
        location_element.clear()  # Clear any existing value
        location_element.send_keys(text) #searchboxinput
        
    def close_browser(self):
        self.driver.quit()

# Calling the class:
if __name__ == "__main__":
    # Set the path to your webdriver executable For organising the code make this dynamic so that the driver can be called as per the 
    # the user custom path
    webdriver_path = r"C:\Users\kaush\chromedriver-win64\chromedriver.exe"
    # Instantiate the Browser class, can pass a key word arugment of Chrome Options to customize any chrome options we want
    browser = Browser(webdriver_path)

    # Open a URL
    browser.open_url("https://www.google.com/maps")
    browser.driver.maximize_window()
    # Do Selenium operations like finding elements, clicking, etc.
    time.sleep(5)
    # #searchbox-searchbutton > span
    browser.insert_text_by_id("searchboxinput","test")

    time.sleep(5)
    # Close the browser when done
    browser.close_browser()
    



