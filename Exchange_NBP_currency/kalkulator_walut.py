from requests import get

currency_dict = {'currency_cod':['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CLP', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'RON', 'SEK', 'SGD', 'THB', 'TRY', 'UAH', 'USD', 'XDR', 'ZAR']}

def description():
    print("Check the historical rate of the selected currency.")

def choose_currency():
    currency = input("Select a currency code:")
    while currency not in currency_dict['currency_cod'] and currency.upper() not in currency_dict['currency_cod']:
        print("Invalid currency")
        currency = input("Select a currency code:")
    print("correct currency")
    return currency


def present_rate_on_selected_date(currency):
    print("Use date format: YYYY-MM-DD where:")
    print("                   R means year")
    print("                   M means month")
    print("                   D means day")
    date = input("For day:")
    link=f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/'
    inputed_data = get(link)
    tab = inputed_data.json()

    rate = tab['rates'][0]['mid']
    print(f"1 {currency.upper()} = {rate} PLN on day {date}")

def main():
    description()
    present_rate_on_selected_date(currency = choose_currency())

main()