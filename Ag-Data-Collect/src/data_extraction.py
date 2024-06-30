import os
import requests
import pandas as pd
import logging

# Ensure the logs directory exists
os.makedirs('logs', exist_ok=True)

# Configure logging
logging.basicConfig(
    filename='logs/data_extraction.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Function to fetch the data
def fetch_data(api_url, params):
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        logger.info(f'Response from {api_url}: {response.text}')
        data = response.json()
        if 'data' in data:
            logger.info(f'Data fetched successfully from {api_url}.')
            return pd.DataFrame(data['data'])
        else:
            logger.error(f'No data found in response from {api_url}.')
            logger.error(f'Response content: {data}')
            return pd.DataFrame()
    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching data from {api_url}: {e}')
        return pd.DataFrame()
    # All the responses would be displayed on the log file
def fetch_industry_sales_data(config):
    return fetch_data(config['commodity_prices_api']['url'], config['commodity_prices_api']['params'])

def fetch_crop_data(config):
    return fetch_data(config['crop_data_url'], config['crop_data_params'])

# For every data table you would like to fetch, just make sure to make it corresponds to what .yaml file has.
