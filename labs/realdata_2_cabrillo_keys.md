# Keys in Real Data: Cabrillo Courses 

In this lab we will examine some trade-offs when addressing problems with data. This lab builds on the schema that we imported in the [Using Real Data: Cabrillo Courses](realdata_1_cabrillo_import.md) lab. 

## Step 1: Keys in the Program Data 

This query shows the problem with the program data: 

```sql 
select * from ProgramFile
	where `Program Control Number` = '';
```

Some records don't have a control number. What can we do about it? Let's delete the rows and re-create the program table with a key.

```sql 
create table program ( 
    ControlNumber char(5) primary key,
    Title varchar(64),
    TOPCode char(6), 
    AwardType char(1), 
    CreditType char(1), 
    ApprovedDate date, 
    Status varchar(16), 
    InactiveDate date
);

# Truncates some dates that also have time of day. Ignore. 
insert into program (ControlNumber, Title, TOPCode, AwardType, CreditType, ApprovedDate, Status, InactiveDate)
	select `Program Control Number`, `Title`, `TOP Code`, `Program Award`, 
		`Credit Type`, IF (`Approved Date` = '', NULL, `Approved Date`), 
        TRIM(`Proposal Status`), IF (`Inactive Date` = '', NULL, `Inactive Date`)
	from ProgramFile
    where `Program Control Number` != '';
```

Note the `where` clause in the insert/select statement removes rows with empty control numbers.

## Step 2: Keys in the Intersection Table 

Now let's fix the `program_course` table to use our new key. This too will encounter problems with empty control numbers. Run this query to check for bad keys: 

```sql 
select `Program Control Number`, `Course Control Number`, count(*) 
    from ProgramCourseFile 
    group by `Program Control Number`, `Course Control Number`
    having count(*) > 1;
```

There are courses that map to empty programs. Again, we're going to discard this data because it's hard to figure out where these courses belong.

```sql 
create table program_course (
    ProgramControlNumber char(5), 
    CourseControlNumber char(12),
    constraint primary key (ProgramControlNumber, CourseControlNumber),
    constraint prog_course_fk_1 foreign key (ProgramControlNumber) 
        references program (ControlNumber),
    constraint prog_course_fk_2 foreign key (CourseControlNumber) 
        references course (ControlNumber)
);

insert into program_course (ProgramControlNumber, CourseControlNumber)
    select `Program Control Number`, `Course Control Number` 
    from ProgramCourseFile
    where `Program Control Number` != '';    
```

## Turn In 

Export your schema into a file called `cabrillo_datamart_keys.sql` and submit it on Canvas. 
