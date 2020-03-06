"""
# Beginning Selects 

This assignment will get you started writing select statements in SQL. 
"""

db_url = "sqlite:///flights.sqlite3"

class Question01:
    """
## 1. Select Airports

Write an SQL query that selects all rows from the `airports` table. 
    """
    answer = "select * from airports;"
    
class Question02:
    """
## 2. Select Airlines

Write an SQL query that selects all rows from the `airlines` table. 
    """
    answer = "select * from airlines;"

class Question03:
    """
## 3. Select Routes

Write an SQL query that selects all rows from the `routes` table. 
    """
    answer = "select * from routes;"

class Question04:
    """
## 4. Select Specific Columns 

Write an SQL query that selects the following columns from the `airports` table.

  - code
  """
    
    answer = 'select code from airports;'
  
class Question05:
    """
## 5. Select Specific Columns 

Write an SQL query that selects the following columns from the `airports` table.

  - code
  - city
  """
    
    answer = 'select code, city from airports;'

class Question06:
    """
## 6. Select Specific Columns 

Write an SQL query that selects the following columns from the `airports` table.

  - code
  - city
  - latitude
  - longitude
  
  """
    
    answer = 'select code, city, latitude, longitude from airports;'

class Question07:
    """
## 7. Airports in South Africa

Write a query that shows every airport in South Africa
  """
    answer = "select * from airports where country = 'South Africa';"

class Question08:
    """
## 8. Airports in Springfield

Write a query that shows every airport in a city called Springfield
  """
    answer = "select * from airports where city = 'Springfield';"

class Question09:
    """
## 9. Mile High Airports

Write a query that shows every airport that has an altitude higher than 5,200 feet.
  """
    answer = "select * from airports where altitude > 5200"

class Question10:
    """
## 10. Airports Ending in X 

Write a query that shows every airport that has a three-letter code ending in 'X'.
  """
    answer = "select * from airports where code like '__X'"

class Question11:
    """
## 11. High Airports Ending in X 

Write a query that shows every airport that has a three-letter code ending in 
'X' **and** has an altitude of greater than 5,200 feet. 
  """
    answer = "select * from airports where code like '__X' and altitude > 5200"

class Question12:
    """
## 12. Equatorial Airports

Write a query that shows every airport that has has a latitude 5 degrees from the 
equator (latitude is less than 5 and greater than -5).
  """
    answer = "select * from airports where latitude < 5 and latitude > -5"

class Question13:
    """
## 13. Polar Airports

Write a query that shows every airport that has has a latitude above or below 80 degrees.
  """
    answer = "select * from airports where latitude > 80 or latitude < -80"

class Question14:
    """
## 14. Airlines Without a Callsign

Write a query that shows every airline with a callsign that is not 'None'
  """
    answer = "select * from airlines where callsign <> 'None'"

class Question15:
    """
## 15. Foreign San Joses

Write a query that shows airports in a city called San Jose that are **not** in the United States
  """
    answer = "select * from airports where city = 'San Jose' and not country = 'United States'"

class Question16:
    """
## 16. Countries with Airports

Write a query that shows the distinct countries in the airports table.
  """
    answer = "select distinct(country) from airports"

class Question17:
    """
## 17. Types of Planes

Write a query that shows planes (equipment) listed in the routes table.
  """
    answer = "select distinct(equipment) from routes"

class Question18:
    """
## 18. Planes from LAX

Write a query that shows planes (equipment) that fly from LAX.
  """
    answer = "select distinct(equipment) from routes where source = 'LAX'"

class Question19:
    """
## 19. Planes to or from LAX

Write a query that shows planes (equipment) that flies to or from LAX. Sort the answer. 
"""
    answer = "select distinct(equipment) from routes where source = 'LAX' or dest = 'LAX' order by equipment"

class Question20:
    """
## 20. Low Airport Countries

Write a query that shows countries that have an airport below sea level.
"""
    answer = "select distinct(country) from airports where altitude < 0"

class Question21:
    """
## 21. Rename columns

Rewrite the query in Question 19 to rename the ouput column to `planes`.
"""
    answer = "select distinct(equipment) as planes from routes where source = 'LAX' or dest = 'LAX'"

class Question22:
    """
## 22. Rename columns

Rewrite the query in Question 20 to rename the output column to `low_country`.
"""
    answer = "select distinct(country) as low_country from airports where altitude < 0"
