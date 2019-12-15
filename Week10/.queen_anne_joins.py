"""
CIS-54 Course SQL Questions
"""

import sys
import inspect 

from IPython.display import HTML, Markdown, display
import sqlite3
import pandas as pd

conn = sqlite3.connect('../Databases/queen_anne.sqlite3')

class Question01:
  """
## 1. Vendors and Items

Join the table ITEM and VENDOR so that all items are listed with the following columns:

  - Description
  - Item Cost
  - Vendor Company Name
  
"""
  answer = "select item.itemdescription, item.itemcost, vendor.companyname from item, vendor where item.vendorid = vendor.vendorid limit 5"

class Question02:
  """
## 2. Corporate Vendor Items

Update the last query to only include vendors that have a non-NULL company name. 
"""
  answer = "select item.itemdescription, item.itemcost, vendor.companyname from item, vendor where item.vendorid = vendor.vendorid and vendor.companyname is not NULL limit 5"

class Question03:
  """
## 3. Employee Sales 

Write a query that lists all sales with the name of the salesperson that made them. 
"""
  answer = "select * from sale, employee where sale.employeeid = employee.employeeid limit 5"

class Question04:
  """
## 4. Sales Goals

Update the last query to show the total sales by each employee.
"""
  answer = "select FirstName, LastName, sum(Total) as Total from sale, employee where sale.employeeid = employee.employeeid group by FirstName, LastName limit 5"

class Question05:
  """
## 5. Customer Sales 

Write a query that shows the names of the top customers in terms of sales.  
"""
  answer = """
select FirstName, LastName, sum(Total) as Total
from customer, sale 
where customer.customerid = sale.customerid
group by FirstName, LastName
order by total desc
limit 5;
"""

class Question06:
  """
## 6. Unsold Items

Write a query that shows all **unsold** items. 
"""
  answer = """select * from item where itemid not in (select itemid from sale_item) limit 5;"""
  
class Question07:
  """
## 7. Customer Vendors 

Write a query that lists the customers who are also vendors. 
"""
  answer = """
select firstname, lastname from customer
intersect 
select contactfirstname, contactlastname from vendor
limit 5;
"""

class Question08:
  """
## 8. Email List

Write a query that lists all the names and email addresses in the database.
"""
  answer = """
select firstname, lastname, email from employee 
union
select contactfirstname, contactlastname, email from vendor 
union
select firstname, lastname, email from customer 
limit 5;
"""

class Question09:
  """
## 9. The Whole Enchilada 

Write a join that joins all the tables in the schema and produces and output table of every sale with:

  - The full name of the salesperson
  - The full name of the customer 
  - The company name of the vendor 
  - The full contact name of the vendor 
  - The cost of the item 
  - The item's sale price 
"""
  answer = """
select employee.firstname, employee.lastname, customer.firstname, customer.lastname, 
  vendor.companyname, vendor.contactlastname, vendor.contactfirstname, 
  item.itemcost, item.itemprice 
from employee, customer, vendor, item, sale, sale_item 
where sale.employeeid = employee.employeeid
  and sale.customerid = customer.customerid 
  and sale.saleid = sale_item.saleid 
  and sale_item.itemid = item.itemid 
  limit 5
;  
"""

class Question10:
  """
## 10. Sales by Employee and Customer

Write a query that shows salesdata by salesperson and customer. Show the following: 

  - The first and last name of the salesperson 
  - The customer's first and last name
  - The total sales from that salesperson to that customer
  
"""
  answer = """
select employee.firstname, employee.lastname, customer.firstname, customer.lastname, sum(Total) as Total
from employee, customer, sale 
where employee.employeeid = sale.employeeid 
  and customer.customerid = sale.customerid
group by employee.employeeid, customer.customerid
limit 5
;
"""


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
    