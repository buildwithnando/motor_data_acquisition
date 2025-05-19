# motor_data_acquisition

This project contains a Python script (`wbc.py`) designed to scrape vehicle data from a website using Selenium. The scraped data is then stored in a Supabase database.

## Features

The script performs the following actions:

*   **Data Extraction**:
    *   Extracts counts of vehicles by category (e.g., cars, bakkies, motorbikes).
    *   Extracts vehicle counts per branch.
    *   Extracts vehicle counts per make and model.
    *   Extracts vehicle counts per body type.
    *   Gathers detailed information for each vehicle, including description, year, mileage, rating, location, price, Dekra rating, and auction status.
    *   Extracts stock numbers and prices.
*   **Web Navigation**:
    *   Navigates through paginated search results to collect all available vehicle data.
*   **Database Interaction**:
    *   Connects to a Supabase instance.
    *   Inserts extracted vehicle data into a specified table, checking for duplicates based on stock number.

## Main Script

*   **[`wbc.py`](wbc.py)**: The core script that uses Selenium for web scraping and Supabase for data storage. It includes functions to:
    *   Initialize the Selenium WebDriver and Supabase client.
    *   Populate various data structures with information scraped from web elements (e.g., [`populate_counts_struct`](wbc.py), [`populate_branch_struct`](wbc.py), [`populate_make_struct`](wbc.py)).
    *   Extract specific vehicle details (e.g., [`extract_stock_numbers`](wbc.py), [`get_vehicle_struct_list`](wbc.py)).
    *   Handle pagination (e.g., [`click_next_page`](wbc.py)).
    *   Insert data into the Supabase database (e.g., [`insert_vehicle_into_db`](wbc.py)).
    *   Orchestrate the overall scraping process (e.g., [`populate_all_cars`](wbc.py)).

## Dependencies

*   selenium
*   supabase

## Setup

1.  Ensure Python is installed.
2.  Install the required libraries:
    ```sh
    pip install selenium supabase
    ```
3.  Configure Supabase URL and Key:
    Update the `url` and `key` variables in [`wbc.py`](wbc.py) with your Supabase project credentials.
    ```python
    // filepath: wbc.py
    // ...existing code...
    # Initialize the Supabase client
    url: str = "YOUR_SUPABASE_URL"
    key: str = "YOUR_SUPABASE_KEY"
    supabase: Client = create_client(url, key)
    // ...existing code...
    ```
4.  Ensure you have the appropriate WebDriver (e.g., ChromeDriver) installed and in your system's PATH or specified in the script.
