"# Neo4j-Recommendation" 

Data Load:
bin\neo4j-admin import --database=<database-name>.db --mode=csv --nodes=import\customers3.csv --nodes=import\taskers.csv --relationships=import\transaction3.csv


CSV Format for Customers3.csv:
username:ID, firstName,	lastName, passportNumber, region, educationLevel, :LABEL
Sample values:
ccalhoun, Caleb, Calhoun, 81EItsodl, Nou Barris, High School, graduate, Customer


CSV Format for Taskers.csv
| username:ID	firstName	lastName	passportNumber	region	educationLevel	profession	:LABEL|
|ahendrix	Adrian	Hendrix	YHK2yTIcV	el Poblenou	University studies	plumber	Tasker|
Sample values:
username:ID	firstName	lastName	passportNumber	region	educationLevel	profession	:LABEL
ahendrix	Adrian	Hendrix	YHK2yTIcV	el Poblenou	University studies	plumber	Tasker

CSV Format for Transactions.csv
|:START_ID	| priceRating:int |	qualityRating:int |	flexScheduleRating:int	| overAll:int	| :END_ID	| :TYPE
|ccalhoun  |	5	          | 9	     |6	   |9   |	ahendrix	|Booked|
|
Sample values:


| username:ID   | firstName     | lastName | passportNumber  | region       | :LABEL   |
| ------------- |:-------------:| -----:   | -----:          | -----:       | -----:   |
| ahendrix      |Adrian| Hendrix   | 81EItsodl              | el Poblenou  | Customer |
