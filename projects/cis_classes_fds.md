# Project: Functional Dependencies 

In the previous two projects you've gathered and refined the data on CIS courses taught this semester. In this one you will state the functional dependencies in your data and use them to validate your choice of keys. 

## Important Attributes 

In your previous projects you collected a bunch of attributes regarding courses, sections and instructors from the catalog and SALSA. You've made choices about what attributes are relevant in your schema. For this project you should have *at least* the attributes listed here. You are free to add as many others as you like: 

  1. Instructor Name 
  2. Instructor Title 
  3. Instructor Phone Number 
  4. Course Number
  5. Course Title 
  6. Course Units 
  7. Section Times
  8. Section Room 
  9. Section Instructor 
  10. Section Course
  
## Describing Tables 

As mentioned in class there's a way to describe a table in documentation. In this assignment you are required to use the format. As a reminder a table is described like this: 

TableName ( <u>key1</u>, <u>key2</u>, attr1, attr2, *fk1*, *fk2* )

For example, if you had a `Section` table that looked like this: 

| SectionNumber | Room | Time | Course | Instructor | 
| --- | --- | --- | --- | --- | 
| 1 | 828 | Th 5:30-9:30 | cis-54 | Mike Matera | 

Assuming your `Course` and `Instructor` columns are foreign keys your table definition looks like this: 

Section ( <u>SectionNumber</u>, Room Time, *Course*, *Title* )

## Finding Functional Dependencies 

Start by listing all of the attributes that you track in your schema. Once you have them listed write out the functional dependencies in the "arrow" form shown in class. If you use surrogate keys include them. Watch out for incorrect FDs that don't use a surrogate key. For example, this FD is correct: 

    InstructorID → ( InstructorName, InstructorPhone, InstructorTitle ) 

This FD is **incorrect** because your schema won't support two "John Smiths":

    InstructorName → ( InstructorPhone, InstructorTitle ) 

List your FDs clearly and verify that every attributes is represented in an FD. **Watch out for multivalued dependencies** there are some in there!

## Rebuild your Schema

With FDs in hand describe your schema using the table syntax above. Also, update your schema in SQL. Once your updates are complete export your schema and submit the written part of the assignment. 

## Turn In 

Please turn in the following:

  1. A document with your FDs and Tables called `cis_fds.*` (It can't be text because you need underlines and italics.)
  2. You exported database called `cis_fds.sql`
