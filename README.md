# NesiConverter for Currencies.
This module will calculate the exchange amount of two currencies.  
There are two version of this module.  
`nesiconverter` and `nesiconverter2`  

(Static values are used for exchange rates. Rates as per 10/01/2021)  
  
### supported currencies:  
USD - United Stated Doller  
EUR - Euro  
AUD - Australian Doller  
CAD - Canadian Doller 
CHF - Swiss Franc  
INR - Indian Rupees  
RUB - Russian Rubles  
AED - United Arab Emirated - Dinar  
SAR - Saudi Riyal  
KD - Kuwait Dinar

## Files:
1. nesiconverter.py : This is a standalone module. Conversion table is manually created as a list.
1. nesiconverter2.py : This module uses a CSV file to create conversion table.
1. e_rates.csv : conversion rates of 10 currencies as per 10-01-2021 is stored inside this csv file.
  
  
## Installation and usage:
In case you are using the first module `nesiconverter.py` Downalod the the module to program folder.  
If you are using the second module `nesiconverter2.py` Download both `nesiconverter2.py` and `e_rates.csv`  
    
    
After downloading the module, import module to your program.
```python
import nesiconverter
```
nesiconverter module takes 3 arguments. Currency1, Currency2, and Amount.  
to call the function we can use ` nesiconverter.convert` "convert" is the function name.  
  
for example if you want to convert 2000 riyal to indian rupees,  
arguments to pass are : currency1 = SAR, currency2 = INR, amount = 2000  
lets print the result,
```python
print(nesiconverter.convert("sar","inr",2000))
```
