''' This module provides a reusable byline for the author's services. Re write this so it describes the code and whats it doing'''

import math
import statistics

''' Define at least one variable of each of these types: str, int, float, bool, list of strings, list of numbers. The following example
uses optional type hints. Follow naming conventions for variable names, but create your own names and values. Note boolean values are typically named as a question, e.g., has_international_presence.'''

#change these names
company_name: str = "Stellar Analytics Inc."
count_active_projects: int = 5
has_international_presence: bool = False
average_client_satisfaction: float = 4.7
services_offered: list = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#Use f-strings to create formatted strings for non-string variables. For example:

active_projects_string: str = f"Active Projects: {count_active_projects}"
international_presence_string: str = f"International Presence: {has_international_presence}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"


"""Use built-in Python functions and the statistics module to calculate descriptive statistics for your numeric list. 
Python has built-in functions for calculating min(), max(), sum(), and len(). The statistics module provides additional functions for mean(), mode(), median(), and stdev()."""
import statistics

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""
