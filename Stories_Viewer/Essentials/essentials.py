#Import Selenium Dependencies
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")# ---- MUTE AUDIO FROM STORIES
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'./Driver/chromedriver', chrome_options=chrome_options)




#login-page

