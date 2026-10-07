from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "K7X250807BD2948"
options.udid = "K7X250807BD2948"
options.automation_name = "UiAutomator2"

# clock app package and activity for Android devices
# to find the package and activity of the clock app, you can use the following adb command:
#& "C:\Users\HP\AndroidSdk\platform-tools\adb.exe" -s K7X250807BD2948 shell "dumpsys window | grep mCurrentFocus"
# mCurrentFocus=Window{e940751 u0 com.google.android.deskclock/com.android.deskclock.DeskClock}-[Surface(name=*Title#1423)/@0xdf01d42]
options.set_capability("appPackage", "com.google.android.deskclock")  # Use the correct package name for the clock app
options.set_capability("appActivity", "com.android.deskclock.DeskClock")
options.set_capability("noReset", True)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
print("🚀 Successfully connected to the Clock app on the tablet!")

try:
    wait = WebDriverWait(driver, 20)
    
    # -------------------------------------------------------------
    # 1. CREATE: Navigate to Alarm tab and add a new alarm
    # -------------------------------------------------------------
    print("⏰ Navigating to the Alarm section...")
    alarm_tab = wait.until(
    EC.presence_of_element_located((AppiumBy.ID, "com.google.android.deskclock:id/tab_menu_alarm"))
    )
    alarm_tab.click()
    time.sleep(1)

    print("➕ Clicking on the 'Add Alarm' button to create a new alarm...")
    add_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.google.android.deskclock:id/fab"))
    )
    add_button.click()

    time.sleep(2)

    print("📌 Clicking on the 'OK' button to save the alarm...")
    ok_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.google.android.deskclock:id/material_timepicker_ok_button"))
    )
    ok_button.click()

    time.sleep(2)
    print("✅ Alarm saved successfully!")

   # -------------------------------------------------------------
    # 2. UPDATE: Toggle or modify the alarm status (Enable/Disable)
    # -------------------------------------------------------------
    print("🔄 Simple Update: Clicking the last alarm...")
    time.sleep(2)

    #click the last alarm card to toggle its status
    print("🔄 Clicking the last alarm card...")
    alarm_cards = wait.until(
        EC.presence_of_all_elements_located((AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.google.android.deskclock:id/alarm_card_layout"]'))
    )
    alarm_cards[-1].click()
    time.sleep(2)

    print("📌 Clicking OK...")
    ok_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@text="OK"]'))
    )
    ok_button.click()
    time.sleep(2)

    print("✅ Update test completed successfully!")
#3 delete the test alarm
    print("🗑️ Deleting the test alarm...")

    alarm_card = wait.until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.google.android.deskclock:id/alarm_card_layout"])[1]'))
    )
    alarm_card.click()

    time.sleep(2)

    print("🗑️ Clicking on the delete button...")
    delete_button = wait.until(
        EC.element_to_be_clickable((AppiumBy.ID, "com.google.android.deskclock:id/delete_button"))
    )
    delete_button.click()

    time.sleep(1)
    print("✅ Test alarm deleted successfully!")
    print("🎉 Complete CRUD operations on the Clock app executed successfully!")
except Exception as e:
    print("❌ An error occurred during execution:", e)

driver.quit()