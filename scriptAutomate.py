# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:14:48 2024
@author: Kulsoom
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Selenium webdriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()  # You can use any other browser driver as per your choice

# Open the website
website_url = "https://www.ca-oman.com/"  # Replace with the URL of the website you want to open
driver.get(website_url)

# Find the button using XPath and click on it
button = driver.find_element(By.XPATH, "//*[@id='navbar']/ul/li[6]/a")
button.click()

# Find the input field using XPath and fill it with the needed data
# Define a dictionary with input field IDs (or XPaths) and their corresponding values
input_data = {
    "//*[@id='name']": "Kulthoom Kanwal Shoukat Ali",
    "//*[@id='email']": "ksh@example.com",
    "//*[@id='subject']": "Register in TOT Certified course",
    # Add more input fields as needed
}

# Fill each input field with the corresponding value from the dictionary
for xpath, value in input_data.items():
    input_field = driver.find_element(By.XPATH, xpath)
    input_field.clear()  # Clear the input field first to ensure it's empty
    input_field.send_keys(value)

# Fill in the textarea with a specific message
input_field = driver.find_element(By.XPATH, "//*[@id='contact']/div/div[2]/div[2]/form/div[3]/textarea")
input_field.send_keys('Dear sir/madam, I wanted to register in one of the courses, do you provide TOT certified course?')

# Submit the form by clicking the submit button
buttonSubmit = driver.find_element(By.XPATH,'//*[@id="contact"]/div/div[2]/div[2]/form/div[5]/button')
time.sleep(0.2)
buttonSubmit.click()

