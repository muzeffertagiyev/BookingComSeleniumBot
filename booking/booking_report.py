# that file will get specific data as per found hotel after we get from the website as per user's needs

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BookingReport:

    def __init__(self,hotel_boxes:WebElement):
        self.hotel_boxes = hotel_boxes

    def pull_hotel_boxes_attributes(self):
        collection = []
        for hotel in self.hotel_boxes:
            hotel_name = hotel.find_element(By.XPATH,value='.//h3//div[@data-testid="title"]').text
            
            title_section = hotel.find_element(By.XPATH,value='.//h3//a')
            link_to_hotel = title_section.get_attribute('href')

            hotel_price = hotel.find_element(By.XPATH,value='.//div[@data-testid="availability-rate-information"]//span[@data-testid="price-and-discounted-price"]').text
            
            try: 
                hotel_score_element = WebDriverWait(hotel,20).until(EC.presence_of_element_located((By.XPATH,'.//div[@data-testid="review-score"]//div[contains(text(), "Scored")]')))
                
                hotel_score = hotel_score_element.text.replace("Scored",'').strip()
            except:
                hotel_score = 'N/A'  # Handle the case where the score is not found

            hotel_info = {
                "name": hotel_name,
                "price": hotel_price,
                "score": hotel_score,
                "link": link_to_hotel
            }

            collection.append(hotel_info)

        return collection

        
            
            
