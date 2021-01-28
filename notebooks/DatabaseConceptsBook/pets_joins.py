"""
# Pet Joins

The Pets database from the book has data that isn't cleanly related. This is an chance to see how outer joins work. For reference the pet schema is defined below:

BREED ( <u>BreedName</u>, MinWeight, MaxWeight, AverageLifeExpectancy ) 
<br>PET ( <u>PetID</u>, PetName, PetType, *PetBreed*, PetDOB, *OwnerID* ) 
<br>PET_3" ( <u>PetID</u>, PetName, PetType, PetBreed, PetDOB, PetWeight, OwnerID )
<br>PET_OWNER ( <u>OwnerID</u>, OwnerLastName, OwnerFirstName, OwnerPhone, OwnerEmail )
"""

db_url = 'http://www.lifealgorithmic.com/_static/databases/pets.sqlite3'
#db_url = ('sqlite:///pets.sqlite3')

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
"""
