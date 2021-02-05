# CIS Course Schema, Part 1: Gather Data

This project will help you become familiar with structuring data into tables and lists. The goal of the project is to get you thinking about the data and metadata that's necessary to organize information. 

## The Data

You will use the data from the Cabrillo Spring 2020 course schedule:

> [Cabrillo's Spring Schedule](https://success.cabrillo.edu/Student/Courses/Search?terms=2021SP)

Your database should contain all of the classes in the CIS department. You don't have to enter classes from other departments. You will also need to get information about all of the CIS instructors from Cabrillo's directory:

> ![](/static/icon_warning_small.png)
> [Cabrillo's Faculty & Staff Directory](https://www.cabrillo.edu/directory)
>
> **The new directory is quite broken!** 
>
> It's not possible to search by department. Please lookup information for the following instructors:
>
> - Michael Matera
> - Irvin Lemus 
> - Rick Graziani
> - Terri Oropeza 
> - Marcelo Nogueira 
> - Jeffrey Bergamini 
> - Ed Parrish 
> - Steve Hodges 
> - Gary Rollinson
>
> Get as much information as you can for each instructor.

## Creating your Schema 

*You should have already completed the [Your First Schema](../labs/mysql_first_schema.md) lab. The lab shows you how to create tables in MySQL. I also did a walk-through in class.*

### Start with Metadata 

You should capture as much information as possible from the the schedule and SALSA. What items of data do you want to capture? How will you name those data items? Some answers are easier than others and you have the flexibility to decide for yourself. For example you could represent in a table like this: 

| Department | Course Number | Section | Title |
| --- | --- | --- | --- | 
| CIS | 54 | 1 | Introduction to Databases | 

Or you could do this: 

| Course | Section | Title |
|  --- | --- | --- | 
| CIS-54 | 1 | Introduction to Databases | 

Using your metadata as columns, create two tables in MySQL. One for courses and one for instructors. 

### Choose a Key 

Your tables must have a key. Choose one of the columns in your schema to be the key for the table. In MySQL Workbench you will select the "PK" checkbox for your key. 

> IMPORTANT: Two rows cannot have the same primary key. Choose your key carefully!

### Enter the Data 

With your tables created go through all the courses and enter the data. Double check your information to be sure the data is complete. The purpose of this project is not data entry but having all the data is essential. 

### Export Your Schema 

Export your schema into an SQL file called `cis_courses.sql`. You will submit the file with this week's assignments.  

## Schema Questions 

Answer the following questions about your schema: 

  1. What are the related columns between your two tables? 
  2. What are the keys in your data? 
  3. Name one modification problem your schema might have and why. 
  
Answer the questions in a file named `cis_courses_answers`. The file can be any document format. 

## Turn In 

  1. The `cis_courses.sql` file.
  2. The `cis_courses_answers` document. 
  
Submit your files on Canvas.
