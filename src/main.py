import time
from src.driver_setup import WebDriverFactory
from src.config import BASE_URL, OUTPUT_FILE, TIMEOUT
from src.utils import save_to_csv, clean_text, logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_quotes():
    driver = WebDriverFactory.getdriver(headless=False)
    wait = WebDriverWait(driver, TIMEOUT)   
    scraped_data = []
    
    
    try:
        logging.info(f"starting scraping at {BASE_URL}")
        driver.get(BASE_URL)
        
        quotes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))
        
        for quote in quotes:
            
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            
            scraped_data.append({
                "quote": clean_text(text),
                "author": author
            })
            
            if scraped_data:
                save_to_csv(scraped_data, OUTPUT_FILE)
                logging.info(f"Scraping completed. Total quotes scraped: {len(scraped_data)}")
                
    except Exception as e:
        driver.quit()
        logging.error(f"An error occurred: {e}")
        
    finally:
        driver.quit()
        logging.info("WebDriver closed.")
        
if __name__ == "__main__":
    scrape_quotes()