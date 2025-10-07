# Carter-Stancil-Project

## Custom Producer 

My custom producer file reads the NBA Data CSV file and separates them by NBA Season (Excluding any other league). It then aggregates the total amount of fouls called for that season. After separating by season and accumulating the number of fouls called, it produces a message of the season and the total fouls. 

## Custom Consumer 

My custom consumer connects to an SQlite data base to store the messages sent by the producer. This makes it much easier to read for the user. This consumer is different from other projects as I use this solely for seeing the season and the amount of fouls called. When I enhance this project and create more columns, it'll have more use. 

## Custom Analyzer 

My custom analyzer gets the data from the SQLite database and starts plotting. This file plots a line chart of the season on the X axis, and the total amount of fouls called on the Y axis. This makes it easy to see significant drops or increases in fouls called season by season. 

## Main File 

My custom main file brings the whole project together. I recently learning the module "threading", which allows my producer and consumer to run at the same time. This is the reason why I am able to see both the Producer and Consumer messages in the same terminal. Once my producer and consumer files are finished, I start the analyzer file, which generates the chart for further analysis. 
