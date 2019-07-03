# First test using Selenium
# User enters info and enters Fantasy Premier League website
# Code works with Firefox

from selenium import webdriver
from time import sleep

print("Please write your FPL e-mail")
fplEmail = input()

print("Please write your FPL password")
fplPassword = input()

driver = webdriver.Firefox()
driver.get("https://fantasy.premierleague.com/")
print("Opened Fantasy Premier League")
sleep(1)

emailBox = driver.find_element_by_id('loginUsername')
emailBox.send_keys(fplEmail)
print("Email entered")
sleep(1)

passwordBox = driver.find_element_by_id('loginPassword')
passwordBox.send_keys(fplPassword)
print("Password entered")
sleep(1)

loginBox = driver.find_element_by_class_name('ArrowButton-thcy3w-0')
loginBox.click()

print("Done")
input('Press anything to quit')
driver.quit()
print('Finished')
