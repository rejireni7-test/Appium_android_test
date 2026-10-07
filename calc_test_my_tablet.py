from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "K7X250807BD2948"  # Tablet serial number
options.udid = "K7X250807BD2948"          # Tablet serial number
options.automation_name = "UiAutomator2"

# നിങ്ങളുടെ ടാബിൽ നിന്നും കണ്ടെത്തിയ പാക്കേജും ആക്റ്റിവിറ്റിയും
options.set_capability("appPackage", "com.android.calculator2")
options.set_capability("appActivity", "com.android.calculator2.Calculator")
options.set_capability("noReset", True)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
print("🚀 Successfully connected to the Calculator app on the tablet!")

try:
    wait = WebDriverWait(driver, 15)
    
    # 1. '7' എന്ന നമ്പർ ക്ലിക്ക് ചെയ്യുന്നു
    print("🔢 '7' clicked...")
    seven_btn = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='7']"))
    )
    seven_btn.click()
    time.sleep(2)

    # 2. '+' ബട്ടൺ ക്ലിക്ക് ചെയ്യുന്നു
    print("➕ '+' clicked...")
    plus_btn = driver.find_element(AppiumBy.XPATH, "//*[@text='+']")
    plus_btn.click()
    time.sleep(2)

    # 3. '8' എന്ന നമ്പർ ക്ലിക്ക് ചെയ്യുന്നു
    print("🔢 '8' clicked...")
    eight_btn = driver.find_element(AppiumBy.XPATH, "//*[@text='8']")
    eight_btn.click()
    time.sleep(2)

    # 4. '=' ബട്ടൺ ക്ലിക്ക് ചെയ്യുന്നു
    print("🟰 '=' clicked...")
    equals_btn = driver.find_element(AppiumBy.XPATH, "//*[@text='=']")
    equals_btn.click()
    time.sleep(3)

    print("✅ Calculation completed successfully!")

except Exception as e:
    print("❌ An error occurred:", e)

driver.quit()