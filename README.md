# CS50 Final Project Flask
 A SQL/Flask based webpage that stores information and reviews about TV Series.
 
 **This project uses the web track technologies - Flask(Python), HTML/CSS and SQLITE3.**

The goal of the Serie Review webpage is to store information and reviews about tv series that the user inputs. It shows the average rate of each show and the commentarys about them.

Technically, it uses two interconnected databases TABLES, "series" (that have a PRIMARY KEY) and "reviews", who uses the series primary key to store each review from a TV serie.

Each show has their own page, that is determined by the query string in the URL, wich shows their gender, average note, past reviews and let you do a review for that show.

The list of shows is available in the index page ('/' route), where you can see a description about them and their average rate.

**Important: the db folder was not uploaded to git, so, you need to create a new database and tables by the SQL files**
