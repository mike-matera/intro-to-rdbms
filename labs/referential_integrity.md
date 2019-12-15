# Referential Integrity 

In this lab you'll use a *foreign key constraint* to have MySQL enforce rules in your database. A foreign key constraint causes MySQL (and other relational DBMSes) to guarantee that rows in one table match rows in another table. In your first schema you entered actors and Oscar wins. What happens if you enter an oscar for an actor that's not in your database? 

> You must have completed last week's lab [Your First Schema](mysql_first_schema.md). 

## Step 0: Update the Oscar Table 

In this lab you'll have to enter data into the Oscar table. In order to be able to edit a table in MySQL Workbench the table must have a primary key column (or columns). Copy this query into an editor window in MySQL Workbench and execute it by placing the cursor over the query and pressing the lightning bolt with cursor button. 

```sql
ALTER TABLE oscar ADD PRIMARY KEY (`year`, `category`);
```

> Note: Step 2 will only be possible after running this query. 

## Step 1: A Join Query

A *join* is an SQL query that operates on more than one table. Copy this query into the SQL editor window:

```sql
select name, category, movie from oscar, actor where oscar.actor = actor.id; 
```

Execute the query by placing the cursor over the query and pressing the lightning bolt with cursor button in MySQL worbench. You should see this output:

|name | category | movie |
| --- | --- | --- | 
| Robert De Niro | Best Actor | Raging Bull | 
| Robert De Niro | Best Suporting Actor | The Godfather: Part II | 
| Meryl Streep | Best Actress | The Iron Lady | 
| Meryl Streep | Best Actress | Sophie's Choice | 
| Meryl Streep | Best Supporting Actress | Kramer vs. Kramer | 

## Step 2: Corrupt the Data

What happens when you add an Oscar but don't have a record of the actor? Add the following information to your oscar table:

  * Year: 2018
  * Category: Best Actor
  * Movie: Darkest Hour
  * Actor: 3

> Be sure to apply your changes.

Notice a problem? There is no actor #3 because we haven't entered Gary Oldman. Rerun the join query in Step 1 and you'll notice that even though you have a record of the 2018 Best Actor award it's not shown. 

> Delete the 2018 best actor row before moving ahead. 

## Step 4: Add a Constraint 

The DBMS should prevent the update we made in step 2 until there's a matching actor. In this step we'll create a foreign key constraint for the purpose. In class I did a walkthrough of this process. The summary is: 

  1. Edit the oscar table by clicking the wrench icon next to the table name. 
  2. Select the "Foreign Keys" tab at the bottom of the editor pane. 
  3. Select the "Foreigh Key Name" field in the list, a default name of "fk_oscar_1" will appear. Keep that name and press "Enter" while editing that field.
  4. In the "Referenced Table" field select your actor table. 
  5. In the "Foreign Key Columns" pane check the box next to "actor".  A value will appear in the "Referenced Column" field.
  6. Select "id" in the referenced column field.
  7. Click "Apply", then "Apply" again in the popup. 
  
> If you see this error:
>
> ERROR 1452: Cannot add or update a child row: a foreign key constraint fails
>
> You must delete the 2018 oscar row and repeat Step 4 from the start.

Test your constraint by attempting to execute the following SQL: 

```sql
insert into oscar values ('2018', 'Best Actor', 'Darkest Hour', 3); 
```

You will see an error in the bottom pane. The error is: 

```
Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`matera_MikesFirstSchema`.`oscar`, CONSTRAINT `fk_oscar_1` FOREIGN KEY (`actor`) REFERENCES `actor` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION)
```

An oscar winner must be in the actor table!

## Step 5: Add Gary Oldman 

Add Gary Oldman's information:

  * ID: 3
  * Name: Gary Oldman 
  * Birthday: 1958-03-21
  * Hometown: London, England
  
After Gary has been added re-run the insert query from the previous step and the join query from Step 1. They work! 

## Turn In 

Export your data into a file called `referential_integrity.sql` and submit the file on Canvas. 


