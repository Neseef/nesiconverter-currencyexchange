
def convert (currency1,currency2,amount):
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
        currency1=currency1.upper()
        currency2=currency2.upper()
        exchange_rates = [['#', 'USD', 'EUR', 'AUD', 'CAD', 'CHF', 'INR ', 'RUB', 'AED', 'SAR', 'KD'], ['USD', '1.0000', '1.2200', '0.7800', '0.7900', '1.1300', '0.0140', '0.0130', '0.2700', '0.2700', '3.2900'], ['EUR', '0.8200', '1.0000', '0.6300', '0.6400', '0.9200', '0.0110', '0.0110', '0.2200', '0.2200', '2.6900'], ['AUD', '1.2900', '1.5800', '1.0000', '1.0100', '1.4600', '0.0180', '0.0170', '0.3500', '0.3400', '4.2400'], ['CAD', '1.2700', '1.5500', '0.9900', '1.0000', '1.4300', '0.0170', '0.0170', '0.3500', '0.3400', '4.1800'], ['CHF', '0.8900', '1.0800', '0.6900', '0.7000', '1.0000', '0.0120', '0.0120', '0.2400', '0.2400', '2.9200'], ['INR', '73.3800', '89.7100', '56.9100', '57.8300', '82.8600', '1.0000', '0.9900', '19.9700', '19.5700', '241.5500'], ['RUB', '74.0800', '90.5700', '57.6900', '58.3800', '83.6600', '1.0100', '1.0000', '20.1700', '19.7600', '243.8700'], ['AED', '3.6700', '4.4900', '2.8500', '2.8900', '4.1500', '0.0500', '0.0500', '1.0000', '0.9800', '12.1000'], ['SAR', '3.7500', '4.5900', '2.9100', '2.9600', '4.2400', '0.0510', '0.0510', '1.0200', '1.0000', '12.3500'], ['KD', '0.3000', '0.3700', '0.2400', '0.2400', '0.3400', '0.0041', '0.0041', '0.0830', '0.0810', '1.0000']]
        currencies= exchange_rates[0]
        index_of_currency1=currencies.index(currency1)
        exchange_rate_of_currency1_to_currency2=0
        for rate in exchange_rates:
            if rate[0] != currency2:
                continue
            else:
                exchange_rate_of_currency1_to_currency2= float(rate[index_of_currency1])

        return round((float(amount) * exchange_rate_of_currency1_to_currency2),2)
