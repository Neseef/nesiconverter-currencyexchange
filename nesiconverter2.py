import csv

def convert (currency1,currency2,amount):
        currency1=currency1.upper()
        currency2=currency2.upper()
        exchange_rates = []

        with open ("e_rates.csv", "r") as f:# r read, w write, a append.
            f_read = csv.reader(f)
            for row in f_read:
                exchange_rates.append(row)
        f.close()

        currencies= exchange_rates[0]
        index_of_currency1=currencies.index(currency1)
        exchange_rate_of_currency1_to_currency2=0
        for rate in exchange_rates:
            if rate[0] != currency2:
                continue
            else:
                exchange_rate_of_currency1_to_currency2= float(rate[index_of_currency1])
        return float(amount) * exchange_rate_of_currency1_to_currency2
