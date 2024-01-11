''' This module provides a reusable byline for the author's services. Re write this so it describes the code and whats it doing'''

import math
import statistics

''' Define at least one variable of each of these types: str, int, float, bool, list of strings, list of numbers. The following example
uses optional type hints. Follow naming conventions for variable names, but create your own names and values. Note boolean values are typically named as a question, e.g., has_international_presence.'''


company_name: str = "Nolan's European Government Analytics"
current_customers: int = 67
trades_with_united_states: bool = True
average_inflation_rate: float = 3.3
services_offered: list = ["Data Analysis", "Python Scripting", "Insider trading"]
inflation_of_countries: list = [4.8, 4.6, 4.9, 5.0, 4.7, 12.1, 4.9]

#Use f-strings to create formatted strings for non-string variables. For example:

current_customers_string: str = f"Active Projects: {current_customers}"
trades_with_united_states_string: str = f"Trade with the United Stated: {trades_with_united_states}"
average_inflation_rate_string: str = f"Average Inflation Rate: {average_inflation_rate}"


"""Use built-in Python functions and the statistics module to calculate descriptive statistics for your numeric list. 
Python has built-in functions for calculating min(), max(), sum(), and len(). The statistics module provides additional functions for mean(), mode(), median(), and stdev()."""


smallest= min(inflation_of_countries)
largest= max(inflation_of_countries)
total= sum(inflation_of_countries)
count= len(inflation_of_countries)
mean= statistics.mean(inflation_of_countries)
mode= statistics.mode(inflation_of_countries)
median= statistics.median(inflation_of_countries)
standard_deviation=statistics.stdev(inflation_of_countries)

stats_string: str = f"""
Descriptive Statistics for European Country's inflation rate:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}

  6. Define Byline String
Create a multiline string to display your formatted information. For example:
"""

byline: str = f"""
Company Name: {company_name}
Current customers: {current_customers}
Trades with USA: {international_presence_string}
{client_satisfaction_string}
{services_offered_string}
{stats_string}
"""

Define a main() function that we can call to test our code and display all information.

def main():
    ''' Display all output'''
    print(company_name)
    print(active_projects_string)
    print(international_presence_string)
    print(client_satisfaction_string)
    print(services_offered_string)
    print(numbers_string)
    print(stats_string)

    # If all of the above works, then the byline should work too:
    print(byline)


  if __name__ == '__main__':
    main()

