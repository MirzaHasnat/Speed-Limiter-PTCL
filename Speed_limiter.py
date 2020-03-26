from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyautogui import press,typewrite
import time

print("Dukan:08:b3:af:df:5f:8f")
print("Abdulqadir:d0:77:14:bf:24:70")
print("Ayesha:a0:4c:5b:3b:bf:e8")
print("Api:68:c4:4d:96:e3:81")
print("Husnain:14:9d:09:b5:5e:22")
print("Husnain Laptop:08:b3:af:df:5f:8f")
print("--------------------------------------")

mac = input("Enter The Mac Address:")
speed = input(f"Enter The Speed To Limit for This {mac}:")

driver = webdriver.Chrome("driver.exe")
def login_to_host(): #login to ptcl server
    username = "admin"
    password = "crowcrow"
    driver.get("http://192.168.10.1")
    typewrite(username)
    press("tab")
    typewrite(password)
    press("enter")
    
def add_speed_limit(mac_address,speed_limit):
    login_to_host()
    driver.get("http://192.168.10.1/ratelimit.cmd?action=view")
    time.sleep(1)
    remove_if_already_exist(mac_address)
    time.sleep(1)
    new_limits(mac_address,speed_limit)
    
def remove_if_already_exist(this_mac):
    for rows in driver.find_elements_by_tag_name("tr")[1:]:
        td = rows.find_elements_by_tag_name("td")
        if this_mac == td[3].text.strip():
            td[5].find_element_by_tag_name("input").click() # Select All Already Exist person for new speed limit
    driver.find_element_by_xpath("/html/body/blockquote/form/center/input[2]").click() # Click on Remove Button

def new_limits(mac,limit):
    add_new = driver.find_element_by_xpath("/html/body/blockquote/form/center/input[1]")
    add_new.click()
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[1]/td[2]/select/option[5]").click() #click on walan in select
    driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[5]/td[1]/input").click() #click on mac address to enter to set speed limit
    driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[3]/td[2]/input").send_keys(limit)
    driver.find_element_by_xpath("/html/body/blockquote/form/table/tbody/tr[5]/td[2]/input").send_keys(mac) # mac address for speed limit
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/blockquote/form/center/input").click()

add_speed_limit(mac,speed)
    
    
