# Project: Keys and Constraints 

In the [CIS Course Schema](cis_classes_schema.md) you gathered information about the CIS department and this semester's classes. In this project you will further the construction of your schema by ensuring it follows relational rules. Remember the eight relational rules are: 

  1. Each row holds information about one entity. 
  2. Each column holds information about one attribute. 
  3. Each cell holds a single value. 
  4. All entries in a column have the same type. 
  5. Each column has a unique name. 
  6. The column order is unimportant. 
  7. The row order is unimportant. 
  8. Each row is unique. 
  
You may or may not have organized your data according to rules like #3. MySQL (and all SQL) forces you to obey rule #4, for example.

> Do the [Referential Integrity Lab](../labs/referential_integrity.md) before you begin.
 
## Split Courses and Sections

Your first schema may have captured all of the spring catalog course data into one table. That was okay last week, but your database stores two entities, courses and sections, which will cause modification problems if you only use one table. Your database should store information about a course (e.g. title and units) and information about a section (e.g. section number, semester and times) in separate tables. Update your schema to separate courses and sections. 

Before you create your new tables consider the following questions? 

  1. What are the *attributes* of a course? 
  2. What are the *attributes* of a section? 
  
Think about the attributes and write them down. Remember attributes should belong to the entity that they describe. Again, ask yourself which of the attributes above are *keys*. 

Your new schema should have three tables: 

  1. Course
  2. Section
  3. Instructor
  
Use a foreign key constraint to ensure that all sections have a corresponding course. 

## Select your Keys

MySQL forces you to have primary keys. The name is a bit misleading because you can have **multiple** columns as primary keys. These are knows as *composite keys*. For each table think about the attribute or attributes you will use for a key. Separately, turn in answers to the following questions:

  1. What is the key of your Course table? What kind of key is it (e.g. a surrogate key, composite key or a single-value key)
  2. What is the key of your Section table? What kind of key it it? 
  3. What is the key of your Instructor table? What kind of key is it?
  
Turn in the answers to these questions in a document called `keys_and_constraints`.
  
## Add Constraints to Section and Instructor

Add a referential integrity constraint between Section and Instructor. The constraint should ensure that the instructor of a section is present in the instructor table. You may have to change your data to make this work. *At least one section is currently being taught by staff*. That's what happens when there is no instructor identified by the time the schedule goes to print. Divise a strategy for handling that in your schema (we'll discuss this next week).

## Chapter Questions 

Answer the following questions and add them to your `keys_and_constraints` document.

  1. Define the term *entity* and give and example of an entity. 
  2. Define the term *unique key* and give an example. 
  3. What is a *surrogate key* and why would you use one? 
  
## Turn In 

When you're finished in MySQL Workbench, export your database into a file called `keys_and_constraints.sql`. Submit the following on Canvas:

  * `keys_and_constraints.sql` - The SQL export 
  * `keys_and_constraints.xxx` - A document with answers to the questions (it can be any kind of document).
  