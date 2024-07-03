import os
import time

import booking.constants as const
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from booking.mail import EmailSend


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Booking(webdriver.Chrome):

    def __init__(self,driver_path=r"/Users/muzeffertagiyev/development",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        # for making the browser to be open all the time
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches',['enable-logging'])

        super(Booking,self).__init__(options=options)

        self.implicitly_wait(15)
        # self.maximize_window()

        # Flags to track whether pop-ups have been dismissed
        self.cookies_popup_dismissed = False
        self.login_popup_dismissed = False

    def dismiss_popups(self):

        if not self.cookies_popup_dismissed:
            try:
                reject_cookies = WebDriverWait(self, 3).until(
                EC.visibility_of_element_located((By.ID, "onetrust-reject-all-handler"))
            )
                reject_cookies.click()
                self.cookies_popup_dismissed = True
            except:
                pass
        if not self.login_popup_dismissed:
            try:
                login_popup_ignoring = WebDriverWait(self, 3).until(
                    EC.element_to_be_clickable((By.XPATH, '//div//button[@aria-label="Dismiss sign-in info."]'))
                )
                login_popup_ignoring.click()
                self.login_popup_dismissed = True
            except:
                pass 


    # when the code see that there is not other steps to go then it runs quit function and close the chrome window
    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)

        
    def change_currency(self,currency):
        self.dismiss_popups()

        currency_element = WebDriverWait(self, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//header//nav//div//button[@data-testid='header-currency-picker-trigger']"))
        )
        currency_element.click()

        if currency:
            selected_currency_element = WebDriverWait(self,20).until(EC.element_to_be_clickable((By.XPATH,f"//li//button//div[contains(text(),'{currency.upper()}')]"))
            )
            selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        self.dismiss_popups()

        select_input_area = WebDriverWait(self,20).until(
            EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Where are you going?']"))
        )
        select_input_area.click()
        select_input_area.clear()
        select_input_area.send_keys(place_to_go)
        time.sleep(2)

        first_result = WebDriverWait(self,20).until(
            EC.presence_of_element_located((By.XPATH,"//li[@id='autocomplete-result-0']"))
        )

        first_result.click()


    def select_dates(self,check_in,check_out):
        self.dismiss_popups()
        
        check_in_selection = WebDriverWait(self,20).until(EC.element_to_be_clickable((By.XPATH,f'//td//span[@data-date="{check_in}"]'))).click()

        check_out_selection = WebDriverWait(self,20).until(EC.element_to_be_clickable((By.XPATH, f'//td//span[@data-date="{check_out}"]'))).click()

    def select_adults_num(self,number):

        WebDriverWait(self,20).until(EC.element_to_be_clickable((By.XPATH,'//button[@data-testid="occupancy-config"]'))).click()

        default_number = int(WebDriverWait(self,20).until(EC.element_to_be_clickable((By.XPATH,'//div[@data-testid="occupancy-popup"]//div//div[1]//div[2]//span[@class="c366165ccc"]'))).text)

        try: 
            button_number = 0
            click_number = 0
            if number > default_number:
                click_number = number - default_number
                button_number = 2
            else:
                click_number = default_number - number 
                button_number = 1

            click_button = WebDriverWait(self,20).until(EC.element_to_be_clickable((By.XPATH,f'//div[@data-testid="occupancy-popup"]//div//div[1]//button[{button_number}]')))

            for _ in range(click_number):
                click_button.click()

        except: 
            pass
        
    
    def click_search(self):
        WebDriverWait(self,20).until(EC.element_to_be_clickable((By.XPATH,'//div[@data-testid="searchbox-layout-wide"]//button[@type="submit"]'))).click()


    def apply_filtration(self):

        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(2,3)
        time.sleep(3)
        filtration.sorting_price_lowest_first()

    def report_results(self,to_email):
        hotel_boxes = self.find_elements(By.XPATH, value='//div[@data-testid="property-card"]')

        print("Creating report...")
        report = BookingReport(hotel_boxes)
        our_data = report.pull_hotel_boxes_attributes()

        print("Preparing to send email...")
        email_send = EmailSend(collection=our_data,to_email=to_email)

        place_input_element = WebDriverWait(self,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@placeholder="Where are you going?"]')))
        place_name = place_input_element.get_attribute('value')

        email_send.send_email(subject=f"Requested hotels data for '{place_name.upper()}'")
        
        print(f"Email sent successfully to the email '{to_email}'")
