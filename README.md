Case Study: Crime Analysis and Reporting System (C.A.R.S.)

The primary objective of this project is to develop a comprehensive Crime Analysis and Reporting
System (CARS) that addresses the above-mentioned challenges and provides law enforcement agencies
with a robust, user-friendly, and secure platform for crime data management and reporting.

Directory Structure Overview:

o entity

▪ Entity classes are created in this package. All entity class are created without any
business logic.

o dao

▪ Here we have created Service Provider interface to showcase functionalities.

▪ Also we have create the implementation class for the above interface with db interaction.

o exception
▪ The user defined exceptions are created in this package 

o util
▪ Created a DBPropertyUtil class with a static function which takes properties(user, host, database, password) as parameter and returns connection string.

▪ Created a DBConnUtil class which holds static method which takes connection
string as parameters and returns connection object(Using method defined in
DBPropertyUtil class to get the connection String).

o main

▪ Here a class MainModule is created and demonstrated the functionalities in a menu
driven application.
