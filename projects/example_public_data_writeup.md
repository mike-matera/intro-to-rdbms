# Cabrillo Courses Example Project 

This project uses data about Cabrillo College gathered from California's [Data Mart](https://datamart.cccco.edu/). The data contains information about all Cabrillo programs and courses. 

## Data 

This project will contain data from the following CSV files, that are turned in with this document. 

  - MasterCourseFile.csv - The list of all Cabrillo courses. 
  - ProgramFile.csv - The list of Cabrillo programs. (A program is a degree or certificate.)
  - ProgramCourseFile.csv - The intersection table that maps courses into programs. 

I would like to use this data to better understand Cabrillo's certificates and degrees. 

## Entities and Relationships

The data is about the following entities:

  - Courses 
  - Programs (a certificate or degree)
  
A program contains required courses. 

## Functional Dependencies and Tables

Though I have not yet analyzed the data, these are the functional dependencies that I *expect* will be true of this data. Since CSVs cannot enforce functional dependencies the data may need to be manipulated. 

CourseControlNumber -> (CourseID, TOPCode, CreditStatus, MaximumUnits, MinimumUnits, SAMCode, Date)

ProgramControlNumber -> (Title, TOPCode, AwardType, CreditType, ApprovedDate, Status, InactiveDate) 

ProgramControlNumber ->-> CourseControlNumber

Based on these functional dependencies I will create the following tables: 

course (<u>CourseControlNumber</u>, CourseID, TOPCode, CreditStatus, MaximumUnits, MinimumUnits, SAMCode, Date))

program (<u>ProgramControlNumber</u>, Title, TOPCode, AwardType, CreditType, ApprovedDate, Status, InactiveDate) 

program_course (<u><i>CourseControlNumber</i></u>, <u><i>ProgramControlNumber</i></u>)
