from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "127.0.0.1:5555"
options.udid = "127.0.0.1:5555"
options.automation_name = "UiAutomator2"

options.set_capability("appPackage", "com.example.android.contactmanager")
options.set_capability("appActivity", ".ContactManager")
options.set_capability("noReset", True)
options.set_capability("enforceAppInstall", False)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
print("🚀 Successfully connected to the Contact Manager app!")

try:
    wait = WebDriverWait(driver, 20)
    
    # 1. 'Add Contact' button clicked
    print("✅ Clicked Add Contact ")
    add_button = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Add Contact']"))
    )
    add_button.click()
    print("✅ Clicked Add Contact ")

    time.sleep(3)

except Exception as e:
    print("❌ An error occurred:", e)

driver.quit()
print("Test completed successfully!")