# RDT-Django-round
--> STOCK FINANCE

    This is the source code repository for the Google Finance.nibinsha.pythonanywhere.com so if you want to read it, please go there. If you want to contribute please do go further with this file

--> How to contribute

    This Application is free everyone cann access this App.


--> What's in it?

    It's a simple management system that contains 2 models:

   
    StockName   - it have stockname and the dates
    StockPrices - a list of events relates on stocknames.

--> How to manage your website?

    The Admin section is mainly manage the entire the application Fields.
 
    Here you can change:

    -> Meta tags - title and description of the website
    -> Main color - main color on the website  (default is Green)
    -> Custom CSS - customize CSS on the website
    -> ADMIN interface - we can add delete update the fileds through admin interface
    

--> What are advantages in this Application

    -> It can Calculate the stock closing percentage.
    -> It can See the top stock name of google finance company.
    -> It can also see top 5 stock name of a individual company
    -> It can be see About page about Google Finance
    -> It can be also see List of stock companies

--> How to use this APPLICATION

    -> Introduction page showing simple detail of the application. And some important Buttons that are
       
       * Home button :- Its going into Home page of application
       * About Google Finance :- Its showing a brief detail about google finance
       * Click here To view top 5 stock names generally :- Top 5 stock names showing in totally
       * CLICK HERE:- List of stocks company Names and the check the percentage :- Its first showing the list of volumes 
    -> List Page
        
       * List of stock names 
       * Each stock names inside showing a detailed table . 
    -> Tables Showing 
       
       * First Table is showing the stock name and its created date, stock open , stock close . And calculation result stock change %.
       * second Table showing the top 5 volume of the that selected stock name


--> Setting up a development environment

    ->First, clone the repository:

    git clone 

    -> Step into newly created djangogirls directory:

    cd Stock exchange

    -> Create a new virtual environment if needed. Then, install all the required dependencies:

    pip install -r requirements.txt

    -> Start the PostgreSQL database server and enter the psql shell (you need to have PostgreSQL installed):

    psql

    -> Run the migration to create database schema:

    ./manage.py migrate

    -> Create a user so you can login to the admin:

    ./manage.py createsuperuser

    -> Run your local server:

    ./manage.py runserver

You're done.


