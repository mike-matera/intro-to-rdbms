# Lab: Actors and Movie Functional Dependencies 

This lab takes you through the process of creating an *intersection table* to handle a Multivalued Dependency. 

> You must have completed last week's lab [Referential Integrity](referential_integrity.md). 

## Step 1: Add Movies 

Create a table to store movies. The table should have the following definition:

movie ( <u>title</u>, year )

Add the following information to your movie table (it's the movies from the Oscar table:

  1. The Godfather: Part II, 1975 
  2. Kramer vs. Kramer: 1980
  3. Raging Bull: 1981 
  4. Sophie's Choice: 1983 
  5. The Iron Lady: 2012
  6. Darkest Hour: 2018

Now add another actor to your table: 

  1. Al Pacino, April 25 1940, New York, NY
   
## Step 2: Create an Intersection Table Between Actor and Move 

Intersection tables sometimes have funny names like `actor_has_movie` because they form a bridge between two tables when there's an MVD. In this case we have a better name for our intersection table. We will call it `starring` and the definition should look like this:

starring ( <i><u>ActorID</u></i>, <i><u>Movie</u></i>)

> Notice! Both attributes are primary keys **and** foreign keys. 

Intersection tables will always have at least two foreign keys becasue they join two tables together. 

## Step 3: Populate the Intersection Table 

Populate the intersection table with the movies that actors have appeared in:

  1. Meryl Streep - Kramer vs. Kramer and The Iron Lady 
  2. Robert DeNiro - The Godfather: Part II and Raging Bull 
  3. Gary Oldman - The Darkest Hour 
  4. Al Pacino - The Godfather: Part II 
  
## Step 4: Replace Columns in the Oscar Table 

The oscar table now refers to data that's in the `movie` table. Place a foreign key constraint in the `oscar` table that ensures an oscar is given to a movie that's in the `movie` table. 

## Step 5: Run Some Queries 

You now have an intersection table that satisfies the MVDs:

    ActorName → → MovieTitle
    MovieTitle → → ActorName
    
You can query actors and movies with the following SQL. 

```sql
select * 
  from actor, starring, movie
  where
    actor.id = starring.ActorID
    AND starring.Movie = movie.title; 
```
  
## Turn In 

  1. Export your schema to a file called `actors_fds.sql`.
