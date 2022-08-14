import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()
user_name = os.getenv("User_Name")
password = os.getenv("Password")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://eduserve.karunya.edu/Login.aspx")
time.sleep(1)

driver.find_element(By.ID, "mainContent_Login1_UserName").send_keys(user_name)
driver.find_element(By.ID, 'mainContent_Login1_Password').send_keys(password)
driver.find_element(By.ID, 'mainContent_Login1_LoginButton').click()
time.sleep(1)
if(driver.title == "Hourly Feedback"):
    try:
        for i in range(1,10):
            driver.find_element(By.XPATH,  f'/html/body/form/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/table/tbody/tr[{i}]/td[5]/div/ul/li[4]').click()
    except:
        driver.find_element(By.ID, "mainContent_btnSave").click()
