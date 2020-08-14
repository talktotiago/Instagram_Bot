from Credentials.credentials import *
from Essentials.essentials import *
from Xpaths.xpaths import *
from Classes.classes import *

""" username_field_1 = driver.find_element_by_xpath(username_field_xpath)
username_field_2 = driver.find_element_by_class_name(username_field_class)
password_field_1 = driver.find_element_by_xpath(password_field_xpath)
password_field_2 = driver.find_element_by_class_name(password_field_class)
login_btn_1 = driver.find_element_by_xpath(login_btn_xpath)
login_btn_2 = driver.find_element_by_xpath(login_btn_class)
logo_instagram_1 = driver.find_element_by_xpath(logo_instagram_xpath)
logo_instagram_2 = driver.find_element_by_class_name(logo_instagram_class) """


#Login Page Elements - www.instagram.com
def Username_Field_IG():
    try:
        print("Username Field - Trying to find xpath - Attempt 1")
        username_field_1 = driver.find_element_by_xpath(username_field_xpath).send_keys(username_ig)
        print("Success!")
    except:
        print("Username Field - Trying to find class name - Attempt 2")
        username_field_2 = driver.find_element_by_class_name(username_field_class).send_keys(username_ig)
        print("Success!")

def Password_Field_IG():
    try:
        print("Password Field - Trying to find xpath - Attempt 1")
        password_field_1 = driver.find_element_by_xpath(password_field_xpath).send_keys(password_ig)
        print("Success!")
    except:
        print("Password Field - Trying to find class name - Attempt 2")
        password_field_2 = driver.find_element_by_class_name(password_field_class).send_keys(password_ig)
        print("Success!")

def Login_Btn_IG():
    try:
        print('Login Btn via xpath - Attempt 1')
        login_btn_1 = driver.find_element_by_xpath(login_btn_xpath).click()
        print('Success!')
    except:
        print('Login Btn via Class - Attempt 2')
        login_btn_2 = driver.find_element_by_class_name(login_btn_class).click()
        print('Success!')

def Logo_Instagram():
    try:
        print('Clicking Logo via xpath - Attempt 1')
        logo_instagram_1 = driver.find_element_by_xpath(logo_instagram_xpath).click()
        print('Success!')
    except:
        print('Clicking Logo via class - Attempt 2')
        logo_instagram_2 = driver.find_element_by_class_name(logo_instagram_class).click()
        print ('Success!')

def Not_Now_Btn():
    try:
        print('Clicking Not Now Btn from modal window - Attempt 1')
        not_now_btn_1 = driver.find_element_by_xpath(not_now_btn_xpath).click()
        print('Success!')
    except:
        print('Now Now Btn Click by class - Attempt 2')
        not_now_btn_2 = driver.find_element_by_class_name(not_now_btn_class).click()