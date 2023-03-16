### THIS IS A COMMAND LINE APPLICATION TO FETCH THE DATA FROM SWAPI.DEV

#### This is a Mini-project that pulls the data(resources) of starwars-Movie series.

In star_warsAPI there are following resources:
  1) People
  2) Vehicles 
  3) Starships
  4) Planets 
  5) Species
  6) Films
#### Tasks to do in this project: 
````
# TASK - 1 
    
- The Star Wars API lists 82 main characters in the Star Wars saga. For the first task, we would like you to use a 
       random number generator that picks a number between 1-82. Using these random numbers you will be pulling 15 
       characters from the API using Python.
````

````
# TASK - 2

- **Main Task:**
  - We have to fetch the data of first film from swapi.dev
  - After pulling out the data write json data in `output.txt`
  - Convert the script into CLI Application.


- **Sub-Task:** 
  - Then we have to list down only first name and last name of the character who worked in 1st film [ LIST FORMAT]
  - Also we have to list down the names of planets and vehicles which are in 1st film in [ LIST FORMAT]
  
````

````
# TASK - 3

- **Main Task:** 
  - Create Package called resources and define resouce accessing class for each resouce seperatly to get data.
  - Create Package called models and define pydantic class for each resource and validate data.
  - Get singular resource URL from each resource.
  - Pull data from random 3 "singular" resource URLs and Print them in pprint format.
  - Convert the script into CLI Application.
        
````

````
# Task - 4
- **Main Task:**
  - Create MySQL Queries for each resources
  - Create Database named as starwar_db using MySQL Workbench.
  - Push all resouces data on starwar_db database.
        
````
    
## Project Structure

```
├── Starwars-API (project root)
│ ├── utils (Custom package)
│ │ ├── __init__.py
│ │ ├── fetch_data.py
│ │ ├── randgen.py
│ │ ├── timing.py
| |
│ ├── models(data validation package)
| | ├── __init__.py
| | ├── basemodel.py
| | ├── datamodels
| | | ├── __init__.py
| | | ├──  Py_Characters.py
| | | ├──  Py_Films.py
| | | ├──  Py_Planets.py
| | | ├──  Py_Species.py
| | | ├──  Py_Starships.py
| | | ├──  Py_Vehicles.pyy
| |
│ ├──resources (resources package)
| | ├── __init__.py
| | ├── base.py
| | ├── R_Characters.py
| | ├── R_Films.py
| | ├── R_Planets.py
| | ├── R_Species.py
| | ├── R_Starships.py
| | ├── R_Vehicles.py
|
├── task_one.py (entry-point for task 1)
├── task_two.py (entry-point for task 2)
├── task_three.py (entry-point for task 3
├── task_four.py (entry-point for task 4
├── requirements.txt (package requirements)
├── database.sql (creating database tables)
├── SWAPI_Flask.py (Converting SWAPI project to Flask Application)
├── README.md (your documentation on project)
```
