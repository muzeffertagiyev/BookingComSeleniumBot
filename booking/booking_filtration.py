# This file will include a class with instance methods.
# That will be responsible filtrating of the result after we get the results


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import time

class BookingFiltration:

    def __init__(self,driver:WebDriver):
        # it is our webdriver
        self.driver = driver
        
    def apply_star_rating(self,*star_values):
        time.sleep(3)
        for star_value in star_values:
            star = self.driver.find_element(By.XPATH,f'//div[@data-testid="filters-sidebar"]//h3[contains(text(),"Property rating")]/ancestor::div[2]//input[@value="class={star_value}"]')
            if not star.is_selected():  # Check if the star rating is already selected
                star.click()
                time.sleep(1)  # Small delay to ensure the click is registered and the page is updated

    def sorting_price_lowest_first(self):

        self.driver.find_element(By.XPATH,'//button[@data-testid="sorters-dropdown-trigger"]').click()

        time.sleep(2)
        from_lowest_element = self.driver.find_element(By.XPATH,'//div[@data-testid="sorters-dropdown"]//button[@data-id="price"]')
        
        from_lowest_element.click()
        
    