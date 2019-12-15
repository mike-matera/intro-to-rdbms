# Using Real Data: Cabrillo Courses 

In this lab you will examine some of the issues and trade-offs when you begin to use real data in a schema. The data that we will use comes from the [State of California's Data Mart](https://datamart.cccco.edu/), which has many other interesting data sets. I've downloaded data for Cabrillo College from this page: 

[https://datamart.cccco.edu/Courses/College_MCF.aspx](https://datamart.cccco.edu/Courses/College_MCF.aspx)

The data was downloaded in Microsoft Excel format, fixed up an exported to CSV format. 

## Step 1: Import the CSV Files 

Complete instructions on importing table data can be found here:

[https://dev.mysql.com/doc/workbench/en/wb-admin-export-import-table.html](https://dev.mysql.com/doc/workbench/en/wb-admin-export-import-table.html)

The dataset has three files: 

  - [MasterCourseFile.csv](../../_static/cis-54/MasterCourseFile.csv) - The list of all Cabrillo courses. 
  - [ProgramFile.csv](../../_static/cis-54/ProgramFile.csv) - The list of Cabrillo programs. (A program is a degree or certificate.)
  - [ProgramCourseFile.csv](../../_static/cis-54/ProgramCourseFile.csv) - The intersection table that maps courses into programs. 
  
The Excel files have been slightly modified to remove problems that will break the CSV import. I have deleted extra rows and columns that make the formatting nice but mess up imports. 

Create a schema in MySQL (use your local computer if you can because it's faster). In the tables element in the schema tree view on the left select the "Table Data Import Wizard". Follow the steps to import each CSV file. **Leave all settings at their defaults.**

## Step 2: Import Course Data

Public datasets often have problems that prevent imported CSV data from being used easily. Common problems include:

 - Undefined or unknown columns. (e.g. what does "Funding Category" mean?)
 - Columns that have no useful data (e.g. "Total Units" is always 0)
 - Multiple candidate keys (e.g. "Control Number" and "Course ID")
 - Non-normalized data. The ProgramCourseFile.csv contains data from MasterCourseFile.csv and ProgramFile.csv. That makes the data easier to work with in Excel but is not great for SQL. 
 - Bad Data. In a spredsheet it's hard to find rows with confusing data or that have NULL keys. 
 
In this step we'll create tables to hold our data. Our new tables will have the column names and data types we want. 

```sql
create table course (
    ControlNumber char(12) primary key,
    CourseID char(12),
    TOPCode char(6), 
    CreditStatus char(1), 
    MaximumUnits float,
    MinimumUnits float, 
    SAMCode char(1), 
    Date date
);
```


Now let's insert the data: 

```sql
insert into course (ControlNumber, CourseID, TOPCode,
        CreditStatus, MaximumUnits, MinimumUnits, 
        SAMCode, Date)
	select `Control Number`, `Course ID`, `TOP Code`, 
		`Credit Status`, `Maximum Units`, `Minimum Units`, 
		`SAM Status`, `Issue/Update Date`
	from MasterCourseFile;
```

## Step 3: Create the Program Table

The course data imported easily, using exactly the key we'd hoped for. The program data is a bit more problematic. Let's inspect the source data to look for candidate keys. This query shows you if `Program Control Number` is a workable key:

```sql
select `Program Control Number`, count(*)  
	from ProgramFile
    group by `Program Control Number`
    having count(*) > 1; 
```

It's not! Let's drill down to see why:

```sql
select * from ProgramFile
	where `Program Control Number` = '';
```

Notice that all of the results have "Draft", "Revision", "Deleted" or "Review" in the `Proposal Status` column. This might be the reason that they don't have a control number yet. We cannot simply ignore this data so our table needs a surrogate key.

```sql
create table program ( 
    ID int primary key auto_increment,
    ControlNumber char(5), 
    Title varchar(64),
    TOPCode char(6), 
    AwardType char(1), 
    CreditType char(1), 
    ApprovedDate date, 
    Status varchar(16), 
    InactiveDate date
);
```

## Step 4: Import Program Data 

Now let's bring in the data from the `ProgramFile` table. This query inserts data, excluding the `ID` field which will automatically number itself because of the `auto_increment` satetement. 

```sql
insert into program (ControlNumber, Title, TOPCode, AwardType, CreditType, ApprovedDate, Status, InactiveDate)
	select `Program Control Number`, `Title`, `TOP Code`, `Program Award`, 
		`Credit Type`, IF (`Approved Date` = '', NULL, `Approved Date`), 
        TRIM(`Proposal Status`), IF (`Inactive Date` = '', NULL, `Inactive Date`)
	from ProgramFile; 
```

Notice the select alters some of the data in the `ProgramFile` table using SQL functions. The insert would fail otherswise. Here's what's done: 

```sql
TRIM(`Proposal Status`)
```

The `Proposal Status` field has extraneous spaces at the end. The `TRIM` function removes whitespace from the beginning and the end of the data. 

```sql
IF (`Approved Date` = '', NULL, `Approved Date`)
```

This statement says, *If the row contains an empty Approved Date replace it with NULL otherwise use the Approved Date from the row.* This statement fixes the situation where NULL values in the spreadsheet are represented by an empty cell. 

> You can find all of the functions available to MySQL here: 
>
> [https://dev.mysql.com/doc/refman/5.7/en/functions.html](https://dev.mysql.com/doc/refman/5.7/en/functions.html)

## Step 5: Create the Intersection Table 

Finally, let's create the intersection table. Note, this table does not have foreign keys, attempting to set an FK constraint in this table will fail because there are problems with the data and becuasue `ControlNumber` is not a key in the foreign tables. We'll address those problems next week.

```sql
create table program_course (
    ID int primary key auto_increment, 
    ProgramControlNumber char(5), 
    CourseControlNumber char(12)
);

insert into program_course (ProgramControlNumber, CourseControlNumber)
	select `Program Control Number`, `Course Control Number` 
    from ProgramCourseFile; 
```

## Turn In 

Export your schema into a file called `cabrillo_datamart.sql` and submit it on Canvas. 
