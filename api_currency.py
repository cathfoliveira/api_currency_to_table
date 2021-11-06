import pandas as pd
import requests
from datetime import date

conversion_rate = []
# url = 'https://v6.exchangerate-api.com/v6/Your-Key/latest/BRL'
# url_hist = 'https://v6.exchangerate-api.com/v6/Your-Key/history/BRL/2021/09/01'

currencies = [
        [0,'MXN'],
        [1,'USD'],
        [2,'GBP'],
        [3,'AUD'],
        [4,'JPY'],
        [5,'CNY'],
        [6,'RUB'],
        [7,'SEK'],
        [8,'INR'],
        [9,'BRL'],
        [10,'EUR']
]

for currency in currencies:
    url = f'https://v6.exchangerate-api.com/v6/Your-Key/latest/{currency[1]}'
    
    # Making our request
    response = requests.get(url)
    response_data = response.json()

    # Show message indicating if the connection was a success
    if response_data['result']=='success':
        # print(f'Data successfully retrieved to {currency[1]}\n')
        
        # Go through the return to read the data and save in a organized structure
        for key, value in response_data['conversion_rates'].items():
            # print(f'item: {key}, rate:{value}')

            conversion_rate.append({
                'currency_from': response_data['base_code'],
                'currency_to': key,
                'exchange_rate': value,
                'exchange_date': date.today().strftime("%Y-%m-%d")
            })

        conversion_rate_df = pd.DataFrame(conversion_rate, columns=['currency_from', 'currency_to', 'exchange_rate', 'exchange_date'])    
        print(conversion_rate_df)

    else:
        error_message = response_data['result'] + f' - Exchange response failed. The currency {currency[1]} did not connect. '
        
        if response_data['error-type']=='invalid-key':
            error_message += "API key is not valid."     
        elif response_data['error-type']=='inactive-account':
            error_message += "E-mail address was not confirmed."
        elif response_data['error-type']=='quota-reached':
            error_message += "Account has reached the the number of requests allowed by your plan."
        else:
            error_message += "Unknown"
        
        print(error_message)