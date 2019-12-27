"""
# Population Queries 
"""

db_url = 'sqlite:///population.sqlite3'

class Question01:
  """
## 1. Population Data

Write a query that select all rows from the `population` table.

"""
  answer = "select * from population limit 5;"

class Question02:
  """
## 2. Exploring the Population

Write a query that shows how many 20-year-olds lived in Santa Cruz county in 1996.

"""
  answer = "select * from population where county = 'SANTA CRUZ' and age = 20 and year = 1996;"

class Question03:
    """
## 3. Total Population in a Year 

Write a query that shows the **total** population (all ages) of Santa Cruz county in 1996.
"""
    answer = "select county, sum(pop_total) as total from population where county = 'SANTA CRUZ' and year = 1996"

class Question04:
    """
## 4. Total Population by Year

Write a query that shows the **total** population of Santa Cruz county from 1996 to 2000.
"""
    answer = """select county, year, sum(pop_total) as total from population where county = 'SANTA CRUZ' and year >= 1996 and year <= 2000 group by year;"""

class Question05:
    """
## 5. Demographics: Women and Men 

Write a query that shows what counties have more women than men in 2018. 
"""
    answer = """select county, sum(pop_male) as men, sum(pop_female) as women from population where year = 2018 group by county having women > men"""

class Question06:
    """
## 6. Demographics: Ratio of Men and Women  

Write a query that shows the ratio of men and women (`pop_male` divided by `pop_female`) over the age of 18 by county in 2018. Order the results from the most female to the most male counties.

*Problems with your ratio? Look at the first answer here: https://stackoverflow.com/questions/8305613/converting-int-to-real-in-sqlite*
"""
    answer = """select county, 1.0 * sum(pop_male) / sum(pop_female) as ratio from population where year = 2018 and age >= 18 group by county order by ratio"""

class Question07:
    """
## 7. California Demographics

Write a query that combines the data on each county to show the population of California by age in 2018. 
"""
    answer = """select age, sum(pop_total) from population where year = 2018 group by age""" 
    
class Question08:
    r"""
## 8. Average Age 

Write a query that shows the average age of a person in California in 2018. 

*The formula for the average age is shown below.*

\begin{equation*}
{Average} = \frac{\sum{ \left(Age + 0.5\right) * People}} {\sum{People}}
\end{equation*}
"""
    answer = """select 1.0 * sum((0.5 + age) * pop_total) / sum(pop_total) as average from population where year = 2018;""" 
    
class Question09:
    """
## 9. Oldest Counties

Write a query that shows the average age of a person in each county in 2018. Order the query from oldest to youngest counties.
"""
    answer = """select county, 1.0 * sum((0.5 + age) * pop_total) / sum(pop_total) as average from population where year = 2018 group by county order by average desc; """ 
    
class Question10:
    """
## 10. Big Counties

Write a query showing counties with a total population greater than one million people in 2018.
"""
    answer = """select county, sum(pop_total) as total from population where year = 2018 group by county having total > 1000000;""" 
