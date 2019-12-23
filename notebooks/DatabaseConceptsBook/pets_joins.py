"""
CIS-54 Course SQL Questions
"""

import sys
import inspect 

from IPython.display import HTML, Markdown, display
import sqlite3
import pandas as pd

conn = sqlite3.connect('../Databases/pets.sqlite3')

class Question01:
  """
## 1. Pets and Breed

Write a join query that joins PET_3 and BREED to output a table with the following attributes: 

  - PET_3.PetName
  - PET_3.PetBreed
  - PET_3.PetDOB
  - PET_3.PetWeight
  - BREED.MinWeight
  - BREED.MaxWeight
  - BREED.AverageLifeExpectancy
"""
  answer = """
select
  pet_3.PetName, pet_3.petbreed, pet_3.petdob, pet_3.petweight, 
  breed.minweight, breed.maxweight, breed.averagelifeexpectancy
from pet_3 join breed 
on pet_3.petbreed = breed.breedname
limit 5;
"""

class Question02:
  """
## 2. Unknown Breeds

Update the last query to include the pets with an unknown breed. 
"""
  answer = """
select
  pet_3.PetName, pet_3.petbreed, pet_3.petdob, pet_3.petweight, 
  breed.minweight, breed.maxweight, breed.averagelifeexpectancy
from pet_3 left join breed 
on pet_3.petbreed = breed.breedname
limit 5;
"""

class Question03:
  """
## 3. Average Breed Weight

Update query #1 to include a calculated column that is the average weight of the breed as defined by (MinWeight + MaxWeight) / 2. 
"""
  answer = """
select
  pet_3.PetName, pet_3.petbreed, pet_3.petdob, pet_3.petweight, 
  breed.minweight, breed.maxweight, breed.averagelifeexpectancy,
  (breed.minweight + breed.maxweight) / 2 as `Average Weight`
from pet_3 join breed 
on pet_3.petbreed = breed.breedname
limit 5;
"""

class Question04:
  """
## 4. Fatties

Filter query #3 to show only pets that are above average weight. 
"""
  answer = """
select
  pet_3.PetName, pet_3.petbreed, pet_3.petdob, pet_3.petweight, 
  breed.minweight, breed.maxweight, breed.averagelifeexpectancy,
  (breed.minweight + breed.maxweight) / 2 as `Average Weight`
from pet_3 join breed 
on pet_3.petbreed = breed.breedname
where pet_3.petweight > `Average Weight`
limit 5;
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
    