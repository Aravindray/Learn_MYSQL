myres = session.sql("SELECT actor, COUNT(movie) as movies, GROUP_CONCAT(year SEPARATOR ', ') AS years_string, COUNT(year) AS years FROM movies_actors GROUP BY actor ORDER BY movies DESC").execute().fetch_all()

for myrow in myres:
    print(myrow[0] + " was featured in " + str(myrow[1]) + (" movies" if (myrow[1] > 1) else " movie") + " in " + ("years " if (myrow[3] > 1) else "the year ") + myrow[2] + ".")
