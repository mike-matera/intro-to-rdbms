"""
# More Selects 

This notebook will help give you practice writing selects that use the 
`order by` and `limit` clauses and the `avg()` function. 
"""

db_url = 'sqlite:///flights.sqlite3'

class Question01:
  """
## 1. Highest Airports 

Write a query that lists all airports in order from lowest to highest.
"""
  answer = "select * from airports order by altitude"

class Question02:
  """
## 2. Lowest Airports 

Write a query that lists all airports in order from highest to lowest.
"""
  answer = "select * from airports order by altitude desc"

class Question03:
  """
## 3. Highest Airport

Write a query that returns just one row: The row with the highest airport.
"""
  answer = "select * from airports order by altitude limit 1"

class Question04:
  """
## 4. Count Airports 

Write a query that counts the number of airports in the `airports` table.
"""
  answer = "select count(*) as count from airports;"

class Question05:
  """
## 5. Airlines Without an ICAO Call Sign 

Write a query that shows the airlines without an ICAO Call Sign (where icao is Null)

> Note: Null values appear as "None" in Jupyter's output.
"""
  answer = """select * from airlines where icao is Null;"""

class Question06:
  """
## 6. Rename Columns 

Select all routes from the `routes` table. Your output should have the following output columns:

  1. airline -> rename to "Airline"
  2. source -> rename to "Departs"
  3. dest -> rename to "Arrives" 
"""
  answer = """select airline as Airline, source as Departs, dest as Arrives from routes;"""
  
class Question07:
  """
## 7. Average Altitude 

Write a query that finds the average altitude of all airports. 
"""
  answer = """select avg(altitude) as Average from airports;"""

class Question08:
  """
## 8. Average Altitude of U.S. Airports 

Write a query that finds the average altitude of all airports in the united states. 
"""
  answer = """select avg(altitude) as Average from airports where country = 'United States';"""

class Question09:
  """
## 9. Average Altitude by Country

Write a query that lists all countries and the average altitude of all of the airports in that country. 
"""
  answer = """select country, avg(altitude) as `average altitude` from airports group by country;"""

class Question10:
  """
## 10. Mile High Countries 

Write a query that lists the countries with an average airport altitude of over 5,200 feet. 
"""
  answer = """select country, avg(altitude) as `average altitude` from airports group by country having avg(altitude) > 5200;"""

