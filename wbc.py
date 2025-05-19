from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from supabase import create_client, Client

# Initialize the Supabase client
url: str = ""
key: str = ""
supabase: Client = create_client(url, key)

def insert_vehicle_into_db(table, data, stocknumber):
    existing_records = supabase.table(table).select('*').eq('stocknumber', stocknumber).execute()
 
    if existing_records.data != []:
        print("Supabase reply")
        print(existing_records)
        print(type(existing_records))
        response, count = "Already exists", None 
    else:
        response, count = supabase.table(table).insert(data).execute()
    return response, count

def populate_counts_struct(driver):
    all_count = 0
    car_count = 0
    bakkie_count = 0
    bike_count = 0
    leisure_count = 0
    commercial_count = 0
    
    element = driver.find_element(By.CLASS_NAME, 'search-count')
    all_count = int(element.text.replace('(', '').replace(')', ''))
    
    elements = driver.find_elements(By.CLASS_NAME, 'top-bar-category-item')
    
    print("Different categories: ")
    for e in elements:
        label_element = e.find_element(By.CLASS_NAME, 'category-label')
        count_element = e.find_element(By.CLASS_NAME, 'category-count')
        
        label = label_element.text
        count = int(count_element.text.strip('() '))
        
        if "Vehicle" in label:
            car_count = count
        elif "Bakkie" in label:
            bakkie_count = count
        elif "Motorbike" in label:
            bike_count = count
        elif "Leisure" in label:
            leisure_count = count
        elif "Commercial" in label:
            commercial_count = count
        
        print(f"Label: {label}, Count: {count}")
        
    counts_summary = {
        "all_count": all_count,
        "car_count": car_count,
        "bakkie_count": bakkie_count,
        "bike_count": bike_count,
        "leisure_count": leisure_count,
        "commercial_count": commercial_count
    }

    return counts_summary

def populate_branch_struct(driver):
    filter_button_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/div')
    filter_button_element.click()
    time.sleep(2)
    
    sort_button_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/button')
    sort_button_element.click()
    time.sleep(2)
    
    branch_button_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[10]/div[1]')
    branch_button_element.click()
    time.sleep(2)
    
    print("Different Branches: ")
    
    data_dict = {}

    elements = driver.find_elements(By.CSS_SELECTOR, '.filter-chip-container.open .check-chip-block')
    for e in elements:
     try:
        # Extract the entire text of the div, including the name and count
        full_text = driver.execute_script("return arguments[0].innerText;", e)
        
        # Split the text into name and count
        parts = full_text.split(')')
        name = parts[0].strip() + ')'
        count_element = e.find_element(By.CLASS_NAME, 'check-chip-count')
        count = count_element.text.strip('() ')

        allowed_branches = [
                'Brackenfell (WC)',
                'Dome (GP)',
                'East London (EC)',
                'Epping (WC)',
                'George (WC)',
                'Germiston (GP)',
                'Gqeberha (EC)',
                'JHB South (GP)',
                'Mbombela (MP)',
                'Midstream (GP)',
                'Pietermaritzburg (KZN)',
                'Polokwane (L)',
                'Richmond (WC)',
                'Riverhorse (KZN)',
                'Silver Lakes (GP)',
                'Springfield (KZN)'
            ]
        
        if name != "" and name in allowed_branches:
            # Store the name and count in the dictionary
            data_dict[name] = int(count)
     finally:
        z = 9
    
    return data_dict


def populate_make_struct(driver):
    
    make_button_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[6]/div[1]')
    make_button_element.click()
    time.sleep(2)
    
    print("Different Makes: ")
    
    data_dict = {}

    elements = driver.find_elements(By.CSS_SELECTOR, '.filter-chip-container.open .check-chip-block')
    for e in elements:
     try:
        # Extract the entire text of the div, including the name and count
        full_text = driver.execute_script("return arguments[0].innerText;", e)
        
        # Split the text into name and count
        parts = full_text.split('(')
        name = parts[0].strip() 
        count_element = e.find_element(By.CLASS_NAME, 'check-chip-count')
        count = count_element.text.strip('() ')
        
        if name != "":
            # Store the name and count in the dictionary
            data_dict[name] = int(count)
     finally:
        z = 9
    
    return data_dict

def populate_model_struct(driver):
    
    model_button_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[7]/div[1]')
    model_button_element.click()
    time.sleep(2)
    
    print("Different Models: ")
    
    data_dict = {}

    elements = driver.find_elements(By.CSS_SELECTOR, '.filter-chip-container.open .check-chip-block')
    for e in elements:
     try:
        # Extract the entire text of the div, including the name and count
        full_text = driver.execute_script("return arguments[0].innerText;", e)
        
        # Split the text into name and count
        parts = full_text.split('(')
        name = parts[0].strip() 
        count_element = e.find_element(By.CLASS_NAME, 'check-chip-count')
        count = count_element.text.strip('() ')
        
        if name != "":
            # Store the name and count in the dictionary
            data_dict[name] = int(count)
     finally:
        z = 9
    
    return data_dict

def populate_body_struct(driver):
    
    body_button_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/div/div[1]/div/div/div[2]/div/div/div[11]/div[1]')
    body_button_element.click()
    time.sleep(2)
    
    print("Different Bodies: ")
    
    data_dict = {}

    elements = driver.find_elements(By.CSS_SELECTOR, '.filter-chip-container.open .check-chip-block')
    for e in elements:
     try:
        # Extract the entire text of the div, including the name and count
        full_text = driver.execute_script("return arguments[0].innerText;", e)
        
        # Split the text into name and count
        parts = full_text.split('(')
        name = parts[0].strip() 
        count_element = e.find_element(By.CLASS_NAME, 'check-chip-count')
        count = count_element.text.strip('() ')
        
        if name != "":
            # Store the name and count in the dictionary
            data_dict[name] = int(count)
     finally:
        z = 9
    
    return data_dict

def extract_stock_numbers(driver):
    # Find all elements with the class "btn btn-link" and aria-label "Add Favourite"
    stock_buttons = driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-link[aria-label='Add Favourite']")
    
    stock_numbers = []
    
    # Extract the stock number from each element's "data-stocknumber" attribute
    for button in stock_buttons:
        stock_number = button.get_attribute("data-stocknumber")
        stock_numbers.append(stock_number)
        
    return stock_numbers

def extract_prices(driver):
   # Find all elements with the class "price-text"
   elements = driver.find_elements(By.CLASS_NAME, 'price-text')

   # Initialize an empty list to store the prices
   prices = []

   # Loop through each element
   for e in elements:
       # Extract the text from the element and strip leading and trailing whitespace
       price_text = e.text.strip().replace(' ', '').replace('R', '')
       # Remove the currency symbol and convert the remaining string to an integer
       price = int(price_text)
       # Append the price to the list
       prices.append(price)

   # Return the list of prices
   return prices

def get_vehicle_struct_list(driver):
    
    # Find all elements with the class "grid-card-body"
    grid_card_bodies = driver.find_elements(By.CLASS_NAME, "grid-card-body")

    vehicle_list = []

    for grid_card_body in grid_card_bodies:

        
        description = grid_card_body.find_element(By.CLASS_NAME, "description").text
        chip_texts = grid_card_body.find_elements(By.CLASS_NAME, "chip-text")

        km = "-1"
        rating = ""
        location = ""
        found_location = False
        year = ""  # Initialize year variable
        price = 0  # Initialize price variable
        dekra = ""  # Initialize Dekra rating variable
        auction = False  # Initialize auction flag
        time_left = ""  # Initialize time-left field
        
        sale_in_progress = False
        try:
            sale_in_progress_banner = driver.find_element(By.CLASS_NAME, "image-banner")
            sale_in_progress = True
        except:
            sale_in_progress = False
        

        # Extract year from description
        words = description.split()
        for word in words:
            if word.isdigit() and len(word) == 4:  # Check for 4-digit year
                year = word
                break

        # Check for auction and extract price if applicable
        auction_chip_texts = grid_card_body.find_elements(By.CLASS_NAME, "auction-chip-text")
        if auction_chip_texts:
            auction = True
            try:
                # Try extracting price from "Current Bid" if it's an auction
                price_text_element = grid_card_body.find_element(By.CLASS_NAME, "auction-description")
                current_bid_text = price_text_element.text.strip()
                price = float(current_bid_text.replace("R ", "").replace(",", "").replace(' ', ''))  # Format price
            except:
                # Fall back to original price extraction if "Current Bid" is not found
                try:
                    price_text_element = grid_card_body.find_element(By.CLASS_NAME, "price-text")
                    price_text = price_text_element.text.strip()
                    price = float(price_text.replace("R ", "").replace(",", "").replace(' ', ''))
                except:
                    price = -1  # Set price to -1 if element not found

        # Extract other details for both auction and non-auction cars
        else:
            try:
                price_text_element = grid_card_body.find_element(By.CLASS_NAME, "price-text")
                price_text = price_text_element.text.strip()
                price = float(price_text.replace("R ", "").replace(",", "").replace(' ', ''))
            except :
                price = -1

       
        
            
        
        for chip_text in chip_texts:
            text = chip_text.text.strip()
            if "KM" in text:
                km = text.replace("KM", "").strip()
            elif "Rated" in text:
                rating = text
            elif not found_location and "Dekra" not in text and "Auction" not in text:
                location = text
                found_location = True

            if "Platinum" in text:
                dekra = "Platinum"
            elif "Gold" in text:
                dekra = "Gold"
            elif "Green" in text:
                dekra = "Green"
            
  

        # Create vehicle information dictionary
        vehicle_info = {
            "description": description.replace(year, '').lstrip(),
            "year": year,
            "km": km.replace(' ', ''),
            "rating": rating.replace('Rated', '').replace(' ', ''),
            "location": location,
            "price": price,
            "dekra": dekra.replace(' ', '').strip().replace('Dekra', ''),
            "auction": auction,
            "time_left": time_left,
            "sale_in_progess": sale_in_progress,
            "stocknumber": "",  # Add stocknumber if available
            "make": description.split()[1]
        }

        vehicle_list.append(vehicle_info)

    return vehicle_list

def click_next_page(count, driver):
    temp = ''
    if count==0:
        temp = '//*[@id="main"]/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/ul/li[6]/a'
    else:
        temp = '//*[@id="main"]/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/ul/li[8]/a'
        
    button_element = driver.find_element(By.XPATH, temp)
    button_element.click()
    print("Clicked next page button.")
    
def populate_all_cars(driver):
    global very_short_wait
    very_short_wait = WebDriverWait(driver, 0.05)  # 20 seconds timeout
    global wait
    wait = WebDriverWait(driver, 20)  # 20 seconds timeout
    global short_wait
    short_wait = WebDriverWait(driver, 10)
    global long_wait
    long_wait = WebDriverWait(driver, 60)
    
    all_vehicle_list = []
    
    on_last_page = False
    execute_one_more_time = False
    count = 0
    
    while (not(on_last_page)):
        
        if execute_one_more_time:
           on_last_page = True 
    
        list_of_stock_numbers = extract_stock_numbers(driver)
        print(len(list_of_stock_numbers))
        # list_of_prices = extract_prices()
        # print(len(list_of_prices))
        list_of_vehicles = get_vehicle_struct_list(driver)
        print(len(list_of_vehicles))
        
        for i in range(len(list_of_vehicles)):
            # list_of_vehicles[i]["price"] = list_of_prices[i]
            list_of_vehicles[i]["stocknumber"] = list_of_stock_numbers[i]

            print(insert_vehicle_into_db('all_vehicles', list_of_vehicles[i], list_of_vehicles[i]["stocknumber"] )) # here 
            
            print(list_of_vehicles[i])
            
        all_vehicle_list = all_vehicle_list + list_of_vehicles
        if not(on_last_page):
            click_next_page(count, driver)
            count += 1
            path = '//*[@id="main"]/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/ul/li[2]/a'
            wait.until(EC.presence_of_element_located((By.XPATH, path)))
            time.sleep(0.2)
            
            path = '//*[@id="main"]/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/ul/li[8]/a'
            
            try:
                short_wait.until(EC.presence_of_element_located((By.XPATH, path)))
            except:
                execute_one_more_time = True
        
    print("Here is the final list: ")
    print(all_vehicle_list)
    return all_vehicle_list
