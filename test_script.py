from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ===== SETUP =====
driver = webdriver.Chrome()
driver.maximize_window()

# ===== OPEN WEBSITE =====
driver.get("https://grabdocs.com")
time.sleep(3)

# ===== LOGIN =====
# ⚠️ REPLACE WITH YOUR REAL LOGIN
driver.find_element(By.NAME, "email").send_keys("your_email_here")
driver.find_element(By.NAME, "password").send_keys("your_password_here")
driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

time.sleep(5)

# ===== FILE UPLOAD =====
try:
    driver.find_element(By.XPATH, "//button[contains(text(),'Upload')]").click()
    time.sleep(2)

    upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
    upload_input.send_keys("C:/Users/YourName/Documents/testfile.pdf")  # CHANGE PATH

    print("✅ File upload test passed")
except:
    print("❌ File upload test failed")

time.sleep(5)

# ===== CREATE WORKSPACE =====
try:
    driver.find_element(By.XPATH, "//a[contains(text(),'Workspace')]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(),'Create')]").click()
    driver.find_element(By.NAME, "workspace_name").send_keys("Test Workspace")
    driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()

    print("✅ Workspace test passed")
except:
    print("❌ Workspace test failed")

time.sleep(5)

# ===== SEND MESSAGE =====
try:
    driver.find_element(By.XPATH, "//a[contains(text(),'Messages')]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Type a message']").send_keys("Hello Test" + Keys.ENTER)

    print("✅ Message test passed")
except:
    print("❌ Message test failed")

time.sleep(5)

# ===== CLOSE =====
driver.quit()
