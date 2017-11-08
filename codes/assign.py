import numpy as np
import numpy.random as nr

names = np.array(["Clement Bonnerot", "Maria Charisi", "Andre da Silva Schneider", \
         "Shea Garrison-Kimmel", "Davide Gerosa", "Francois Hebert", \
         "Cameron Hummels", "Astrid Lamberts", "Eve Lee", \
         "Yiqiu Ma", "Christine Corbett Moran", "Hiroki Nagakura", \
         "Robyn Sanderson", "Jono Squire", "Leo Stein", "Natalia Storch", "Stephen Taylor", \
         "Coral Wheeler", "Jess McIver", "Alex Urban", \
         "TJ Massinger", "Brittany Kamai", "Andrew Wade", \
         "Johannes Eichholz", "Michael Coughlin"])

dates = np.array(["Nov 09 17","Nov 16 17","Nov 30 17","Dec 07 17",\
                  "Jan 11 18","Jan 18 18", "Jan 25 18", \
                  "Feb 01 18", "Feb 08 18", "Feb 15 18", "Feb 22 18", \
                  "Mar 01 18", "Mar 08 18", "Mar 15 18", "Mar 22 18", "Mar 29 18", \
                  "Apr 05 18", "Apr 12 18", "Apr 19 18", "Apr 26 18", \
                  "May 03 18", "May 10 18", "May 17 18", "May 24 18", "May 31 18"])

speaker = np.copy(names)
food = np.copy(names)

nr.shuffle(speaker)
nr.shuffle(food)

f = open("assignment.txt", 'w')
for d, s, o in zip(dates, speaker, food):
    f.write("<tr> <td> %s </td> <td> %s </td> <td> %s </td> </tr>\n"%(d, s, o))
f.close()




