import yaml
import os
from src.data_extraction import fetch_industry_sales_data, fetch_crop_data
from src.data_storage import save_to_csv

def main():
    # Load configuration
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Automatically create a directory called "Data" that stores the .csv files
    os.makedirs('data', exist_ok=True)

    # Fetch and save industry sales data
    industry_sales_data = fetch_industry_sales_data(config)
    if not industry_sales_data.empty:
        save_to_csv(industry_sales_data, 'data/commodity_prices.csv')

    # Fetch and save crop data
    crop_data = fetch_crop_data(config)
    if not crop_data.empty:
        save_to_csv(crop_data, 'data/crop_data.csv')

    # If there is a new data, just repeat the above fetch-and-save process

if __name__ == '__main__':
    main()
