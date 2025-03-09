from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
import pushover
import configparser

def send_pushover_notification(configfile, message, title="Global Entry Appointment", sound="pushover"):
    """Sends a push notification to your iPhone using Pushover."""
    try:
        client = pushover.PushoverClient(configfile=configfile)
        client.send_message(message, title=title, sound=sound)
        print("Pushover notification sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def get_popup_text(location, webpage):
    # Set up the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(webpage)

    try:
        wait = WebDriverWait(driver, 5)
        chicago_link = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='centerDetailsUS{location}']/strong/span")))
        chicago_link.click()
        
        time.sleep(2)
        
        popup = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[@id='popoverUS{location}']/div/div/div/strong")))
        popup_text = popup.find_element(By.XPATH, f"ancestor::div[@id='popoverUS{location}']").text

        location_name = popup_text.split('\n')[0]
        availability = " ".join(popup_text.replace('\n',' ').split('Google Map')[-1].strip().split(' ')[:6])
        status = "No Appointments" if "full" in availability else "Appointments Available!"

        output = f"""{status}\n{availability}\nAccessed: {accessed}\nLocation: {location_name}\n{webpage}"""

        return output
    
    finally:
        driver.quit()

if __name__ == "__main__":

    configfile='scheduler_config.ini'
    webpage = "https://ttp.cbp.dhs.gov/schedulerui/schedule-interview/location?lang=en&vo=true&returnUrl=ttp-external&service=up"
    accessed = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    config = configparser.ConfigParser()
    config.read(configfile)
    location = int(config.get('location','location'))

    text = get_popup_text(location=location,webpage=webpage)
    # print(text)

    send_pushover_notification(message=text,configfile=configfile)
