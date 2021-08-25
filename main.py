from selenium import webdriver
import time

#Get usrname and passwd
with open('config.yaml','r') as f:
    myList = f.readlines()
    username = myList[0].split(' ')[-1]
    username = username.replace('\n','')
    password = myList[1].split(' ')[-1]

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get('https://www.my.ucla.edu')

#go to the sign in page
driver.find_element_by_id("ctl00_signInLink").click()
time.sleep(2)

#sign in
driver.find_element_by_id("logon").send_keys(username)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("_eventId_proceed").click()
time.sleep(10)

#Get current window    
current_handles=driver.current_window_handle

#go to DARS page
driver.find_element_by_xpath('//*[@id="main-nav"]/li[4]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="main-nav"]/li[4]/ul/li/ul[1]/li[4]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="main-content"]/p/a').click()
time.sleep(6)

#Switch to the new window
window = driver.window_handles
for i in window:
    driver.switch_to.window(window[-1])
time.sleep(30)

#Run audit
driver.find_element_by_id('pageAddButton').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="auditRequest"]/div[2]/p/input').click()
time.sleep(15)

#View audit
driver.find_element_by_xpath('//*[@id="pageMasterViewDeleteForm"]/div[3]/table/tbody/tr[2]/td[8]/a').click()
time.sleep(10)

print('*' * 10 + 'PLEASE VIEW YOUR AUDIT NOW' + '*' * 10)
