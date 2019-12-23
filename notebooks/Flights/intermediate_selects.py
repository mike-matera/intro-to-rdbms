"""
CIS-54 Course SQL Questions
"""

import sys
import inspect 

from IPython.display import HTML, Markdown, display
import sqlite3
import pandas as pd

conn = sqlite3.connect('../Databases/flights.sqlite3')

class Question01:
  """
## Highest Airports 

Write a query that lists all airports in order from lowest to highest.
"""
  answer = "select * from airports order by altitude limit 5"

class Question02:
  """
## Lowest Airports 

Write a query that lists all airports in order from highest to lowest.
"""
  answer = "select * from airports order by altitude desc limit 5"

class Question03:
  """
## Highest Airport

Write a query that returns just one row: The row with the highest airport.
"""
  answer = "select * from airports order by altitude limit 1"

class Question04:
  """
## Count Airports 

Write a query that counts the number of airports in the `airports` table.
"""
  answer = "select count(*) as count from airports;"

class Question05:
  """
## Airlines Without an ICAO Call Sign 

Write a query that shows the airlines without an ICAO Call Sign (where icao is Null)

> Note: Null values appear as "None" in Jupyter's output.
"""
  answer = """select * from airlines where icao is Null limit 5;"""

class Question06:
  """
## Rename Columns 

Select all routes from the `routes` table. Your output should have the following output columns:

  1. airline -> rename to "Airline"
  2. source -> rename to "Departs"
  3. dest -> rename to "Arrives" 
"""
  answer = """select airline as Airline, source as Departs, dest as Arrives from routes limit 5;"""
  
class Question07:
  """
## Average Altitude 

Write a query that finds the average altitude of all airports. 
"""
  answer = """select avg(altitude) as Average from airports;"""

class Question08:
  """
## Average Altitude of U.S. Airports 

Write a query that finds the average altitude of all airports in the united states. 
"""
  answer = """select avg(altitude) as Average from airports where country = 'United States';"""

class Question09:
  """
## Average Altitude by Country

Write a query that lists all countries and the average altitude of all of the airports in that country. 
"""
  answer = """select country, avg(altitude) as `average altitude` from airports group by country limit 5;"""

class Question10:
  """
## Mile High Countries 

Write a query that lists the countries with an average airport altidue of over 5,200 feet. 
"""
  answer = """select country, avg(altitude) as `average altitude` from airports group by country having avg(altitude) > 5200 limit 5;"""


###########################################
q_num = 0 

def get_question(module, name=None):
    global q_num
    if name is None:
        questions = []
        for name, member in inspect.getmembers(module):
            if inspect.isclass(member) and name.startswith('Question'):
                questions.append(member)
        question = questions[q_num]
        q_num += 1

    else:
        question = getattr(module, name)

    hint = '*This preview is limited to five rows.*'
    df = pd.read_sql_query(question.answer, conn)
    
    return display(Markdown(question.__doc__), df, Markdown(hint))

if __name__ == '__main__':
    get_question(sys.modules[__name__], 'Question1')
    