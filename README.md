"# Neo4j-Recommendation" 

Data Load:
bin\neo4j-admin import --database=<database-name>.db --mode=csv --nodes=import\customers3.csv --nodes=import\taskers.csv --relationships=import\transaction3.csv


CSV Format for Customers3.csv:

| username:ID   | firstName     | lastName | passportNumber  | region       | :LABEL   |
| ------------- |:-------------:| -----:   | -----:          | -----:       | -----:   |
| ccalhoun      |Leanordo | Hendy  | 81EItsodl              | el Poblenou  | Customer  |


CSV Format for Taskers.csv:

| username:ID   | firstName     | lastName | passportNumber  | region       |  profession    |:LABEL   |
| ------------- |:-------------:| -----:   | -----:          | -----:       | -----:   |  -----:   |
| ahendrix      |Adrian| Hendrix   | YHK2yTIcV              | el Raval      | plumber | Tasker |

CSV Format for Transactions.csv:

| :START_ID	 | priceRating:int |	qualityRating:int |	flexScheduleRating:int	| overAll:int	| :END_ID	| :TYPE   |
| -----------|:-------------: | -----:               | -----:                 | -----:        | -----:   |  -----: |
|ccalhoun  |	5	          | 9	     |6	   |9   |	ahendrix	|Booked|



