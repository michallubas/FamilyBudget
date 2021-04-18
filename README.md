# FamilyBudget

Specification

1.Database
The application with family budget. Inside application is located data base with two tables:
- type of budget, table Budget with columns: 

=>id,
=>name,
=>description

- InOut, consists of income and expenses for specific budget, list of columns: 
=>category(with validators for specific group of spendings),
=>amount (with min / max validators)
Foreign keys/id:
=>Budget(Budget table)
=>User (from django.contrib.auth.models)


2.Admin and users
It’s allow for creating several users using admin profile:

http://127.0.0.1:8000/admin/
Login and password: father

- Every time admin adds new use from administration profile, token is assigned automatically.

Added also username mother, login and password: mother.

3.Endpoints
Available end points GET method on local:

http://127.0.0.1:8000/api/budgets/  , list of all budgets  
http://127.0.0.1:8000/api/inouts/ , list of all inouts   
http://127.0.0.1:8000/api/users , list of all inouts , hidden password to displaying


- Includes the possibility of adding new budgets and inouts using above endpoints

4.Authorizations and tokens

Only log in users can have access to data in the database

To get token need to use url and use username and password, on local:

http://127.0.0.1:8000/auth/


5.Filtering and others

Available end points for filtering on local:

http://127.0.0.1:8000/api/lastinouts/3 , take e.g. 3 last spendings


http://127.0.0.1:8000/api/rangeinouts/1618553806/1618563806 ,take all spendings from e.g. last 3 hours 


- added extra function which calculate balance of each budget during displaying all budgets


Each user can create a list of any number of budgets, all budgets are available for all family.  

6.Basic forms

Below available basic forms to quick check data in database, without any authorization, on local:

http://127.0.0.1:8000/budget_create     - to quick add new budget

http://127.0.0.1:8000/budget_list/      - to list all budgets

http://127.0.0.1:8000/inout_list/       - to list all inouts

http://127.0.0.1:8000/budget_find/      - to find by id specific budget

7.Prepared test for: models, urls, views

