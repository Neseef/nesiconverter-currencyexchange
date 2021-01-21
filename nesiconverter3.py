def convert(cur1, cur2, amt):
    '''This module will calculate the exchange amount of two currencies.

    supported currencies:
    USD - United Stated Doller
    EUR - Euro
    AUD - Australian Doller
    CAD - Canadian Doller CHF - Swiss Franc
    INR - Indian Rupees
    RUB - Russian Rubles
    AED - United Arab Emirated - Dinar
    SAR - Saudi Riyal
    KD - Kuwait Dinar

    USAGE:
    nesiconverter.convert(currency1,currency2,amount)

    example:
    convert 2000 SAR to INR
    print(nesiconverter.convert("sar","inr",2000))

    Returns:
    This function return the converted amount.
    '''
    cur1 = cur1.upper()
    cur2 = cur2.upper()
    e_rates = {
        'USD': {
            "EUR":	0.82,
            "AUD":	1.29,
            "CAD":	1.27,
            "CHF":	0.89,
            "INR":	73.38,
            "RUB":	74.08,
            "AED":	3.67,
            "SAR":	3.75,
            "KD":	0.3,
        },
        'EUR': {
            "USD": 1.22,
            "AUD": 1.58,
            "CAD": 1.55,
            "CHF": 1.08,
            "INR": 89.71,
            "RUB": 90.57,
            "AED": 4.49,
            "SAR": 4.59,
            "KD": 0.37,
        },
        'AUD': {
            "USD": 0.78,
            "EUR": 0.63,
            "CAD": 0.99,
            "CHF": 0.69,
            "INR": 56.91,
            "RUB": 57.69,
            "AED": 2.85,
            "SAR": 2.91,
            "KD": 0.24,
        },
        'CAD': {
            "USD": 0.79,
            "EUR": 0.64,
            "AUD": 1.01,
            "CHF": 0.7,
            "INR": 57.83,
            "RUB": 58.38,
            "AED": 2.89,
            "SAR": 2.96,
            "KD": 0.24,
        },
        'CHF': {
            "USD": 1.13,
            "EUR": 0.92,
            "AUD": 1.46,
            "CAD": 1.43,
            "INR": 82.86,
            "RUB": 83.66,
            "AED": 4.15,
            "SAR": 4.24,
            "KD": 0.34,
        },
        'INR': {
            "USD": 0.014,
            "EUR": 0.011,
            "AUD": 0.018,
            "CAD": 0.017,
            "CHF": 0.012,
            "RUB": 1.01,
            "AED": 0.05,
            "SAR": 0.051,
            "KD": 0.0041,
        },
        'RUB': {
            "USD": 0.013,
            "EUR": 0.011,
            "AUD": 0.017,
            "CAD": 0.017,
            "CHF": 0.012,
            "INR": 0.99,
            "RUB": 1,
            "AED": 0.05,
            "SAR": 0.051,
            "KD": 0.0041,
        },
        'AED': {
            "USD": 0.27,
            "EUR": 0.22,
            "AUD": 0.35,
            "CAD": 0.35,
            "CHF": 0.24,
            "INR": 19.97,
            "RUB": 20.17,
            "SAR": 1.02,
            "KD": 0.083,
        },
        'SAR': {
            "USD": 0.27,
            "EUR": 0.22,
            "AUD": 0.34,
            "CAD": 0.34,
            "CHF": 0.24,
            "INR": 19.57,
            "RUB": 19.76,
            "AED": 0.98,
            "KD": 0.081,
        },
        'KD': {
            "USD": 3.29,
            "EUR": 2.69,
            "AUD": 4.24,
            "CAD": 4.18,
            "CHF": 2.92,
            "INR": 241.55,
            "RUB": 243.87,
            "AED": 12.1,
            "SAR": 12.35,
            "KD": 1,
        }}
    for i in e_rates:
        if cur1 == i:
            return float(e_rates[cur1][cur2])*amt
