# Your First Schema

In this lab you will create a schema and some tables two different ways. MySQL Workbench allows you to do many things with little or no knowledge of SQL. That's very helpful for beginners but, as this class progresses I hope that, like me, you'll learn to crave the power of SQL and not depend on the GUI. In this lab we'll create a schema with two tables and add some data to it.  

## Using the GUI

In this part you will create a new schema. Your new schema name must begin with your login ID. For example: 

> matmic54_firstschema

Use the Create Schema button shown below: 

![](https://sites.google.com/a/lifealgorithmic.com/cabrillo-home/_/rsrc/1513330349177/home/cis-154/lab-2---your-first-schema/Create%20Schema.png)

That will bring up the create schema tab. Name your schema and apply as shown:

![](https://sites.google.com/a/lifealgorithmic.com/cabrillo-home/_/rsrc/1454526758030/home/cis-154/lab-2---your-first-schema/Name%20and%20Apply.png)

MySQL Workbench will show you what SQL is about to execute and ask you to confirm:

![](https://sites.google.com/a/lifealgorithmic.com/cabrillo-home/_/rsrc/1513330349177/home/cis-154/lab-2---your-first-schema/Create%20Schema%20Apply.png)

Click Apply. Now you should see your schema on the left hand side of your window: 

![](https://sites.google.com/a/lifealgorithmic.com/cabrillo-home/_/rsrc/1454526758030/home/cis-154/lab-2---your-first-schema/Schema%20Created.png)

Double click the name of your schema to select it as the active one. Then select the "New Table" button. This will bring up the new table tab. Your new table should have the following properties: 

  * Name: actor
  * Columns:
    * id (type INT, PK, NN)
    * name (type VARCHAR(45), NN)
    * birthday (type DATE, NN)
    * hometown (type VARCHAR(45), NN)

You table should look like this: 

![](https://sites.google.com/a/lifealgorithmic.com/cabrillo-home/_/rsrc/1454526758030/home/cis-154/lab-2---your-first-schema/New%20Table.png)

Select apply to create your table and you will see the SQL command that creates your table:

![](https://sites.google.com/a/lifealgorithmic.com/cabrillo-home/_/rsrc/1454526758030/home/cis-154/lab-2---your-first-schema/Apply%20Table.png)

Click "Apply". Next you will add values to the table. Pull open the lab2 schema. When you hover over the actor table you will see a set of icons. The right-most icon looks like a table. Select it and it will bring up the table editor as shown below:

![](https://sites.google.com/a/lifealgorithmic.com/cabrillo-home/_/rsrc/1513330349177/home/cis-154/lab-2---your-first-schema/Add%20Actor%20Data.png)

Add the following people to the actor table as shown in the picture above: 

| ID | Name | Birthday | Hometown |
| --- | --- | --- | --- | 
| 1 | Robert De Niro | 1943-08-17 | New York, NY | 
| 2	| Meryl Streep | 1949-06-22 | Summit, NJ | 

When you're done click Apply and the SQL statements will be shown to you. Select Apply again. You have now populated the actors table. 

## Creating Tables Using SQL

Now you will create tables using SQL. Select the "Query 1" tab in MySQL Workbench. This tab allows you to enter SQL statements. You can load and save SQL files as well as run them step-by-step. In the tab enter the following SQL statements:

```sql
CREATE TABLE oscar (year INT NOT NULL, category VARCHAR(45) NOT NULL, movie VARCHAR(45), actor INT NOT NULL); 

INSERT INTO oscar VALUES (1981, 'Best Actor', 'Raging Bull', 1);
INSERT INTO oscar VALUES (1975, 'Best Suporting Actor', 'The Godfather: Part II', 1);
INSERT INTO oscar VALUES (2012, 'Best Actress', 'The Iron Lady', 2);
INSERT INTO oscar VALUES (1983, 'Best Actress', 'Sophie''s Choice', 2);
INSERT INTO oscar VALUES (1980, 'Best Supporting Actress', 'Kramer vs. Kramer', 2);
```

With the above SQL statements in the editor press the button with the lightning icon to execute them all. It's much faster to create and edit tables when you know SQL. Verify that your table contains the data. It must be turned in with your assignment. 

## Export your Schema 

MySQL workbench can export your schema so you can load it into another DBMS. To export a schema select the server menu item at the top of the window:

    Server -> Data Export

That will bring up the export dialog as shown:

![](https://sites.google.com/a/lifealgorithmic.com/cabrillo-home/_/rsrc/1513330349177/home/cis-154/lab-2---your-first-schema/Export%20Lab%202.png)

Save your schema in a file called `first_schema_export.sql` and submit your file for credit.

## Turn In

  * Your `first_schema_export.sql` file 

Submit your homework on canvas.
