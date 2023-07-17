from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import schedule

def send_msg():
    driver = webdriver.Chrome(Service(ChromeDriverManager().install()))

    # QR code will be displayed when you hit this URL, you have to scan this QR from your phone to access the WhatsApp web
    driver.get("https://web.whatsapp.com/")  
    time.sleep(20)  # 20 seconds to scan the QR code

    # replace 'Friend's Name' with your friend's name as saved in your contacts
    receiver = driver.find_element(By.XPATH, '//span[@title = "Friend\'s Name"]')
    receiver.click()

    # replace 'Your Message' with the message you want to send
    input_box = driver.find_element(By.XPATH, '//div[@data-tab = "6"]')
    input_box.send_keys('Your Message' + Keys.ENTER)

    driver.quit()

# Replace '10:30' with your desired time
schedule.every().day.at("10:30").do(send_msg)

while True:
    schedule.run_pending()
    time.sleep(1)
