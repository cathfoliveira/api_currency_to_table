# Currency API: How to read from an exchange rate API to a table

This is an initial project to examine how to read exchange rate conversions from an API and save them into a final table. From this project, you'll have the opportunity to customize the way you need, by adding cloud configurations or changing to historical readings.

Primarily, I established an array of initial currencies to search, but you can run all the existing currencies directly from the [API](https://www.exchangerate-api.com/docs/supported-currencies).

The API chosen was [Exchange Rate API](https://www.exchangerate-api.com/) because is easy to use, and if you need the historical, is possible you'll need upgrade to a paid plan. See the full documentation [here](https://www.exchangerate-api.com/docs/historical-data-requests).


__

### How to start

* Access the website above and create a free key
* Substitute in the code the `Your-Key` for this new generated key (ex.:96cba03d251a29cdd8877fff)
* Save the code and run it!

__

### Running the solution

* Clone de project into a local folder
* Initiate the virtual environment in the Scripts directory (`api_currency_to_table/Scripts/activate.bat`)
* Execute the `api_currency.py` file

__

### Possible outputs for the code

|currency_from|currency_to|exchange_rate|exchange_date|
|---|---|---|---|
|MXN|MXN|1.0000|2021-11-06|
|MXN|AED|0.1792|2021-11-06|
|MXN|AFN|4.4114|2021-11-06|
|MXN|ALL|5.1391|2021-11-06|
|MXN|AMD|23.0900|2021-11-06|
|EUR|XOF|655.9570|2021-11-06|
|EUR|XPF|119.3320|2021-11-06|
|EUR|YER|289.1527|2021-11-06|
|EUR|ZAR|17.5107|2021-11-06|
|EUR|ZMW|20.0094|2021-11-06|