
import urllib.request
import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

url = 'https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat'
u = urllib.request.urlopen(url)
rawdata = u.read()
localFile = open("Airport.csv", 'wb')
localFile.write(rawdata)
localFile.close()



f = open('Airport.csv', encoding='utf8')
airports = []
for row in csv.reader(f, delimiter=','):
    thisline = []
    try:
        thisline.append(int(row[0])) # ID
        thisline.append(row[1]) # Airport Name
        thisline.append(row[2]) # City
        thisline.append(row[3]) # Country
        thisline.append(row[4])
        thisline.append(row[5])
        thisline.append(float(row[6]))
        thisline.append(float(row[7]))
        thisline.append(float(row[8])) #Altitude
        thisline.append(float(row[9])) #Timezone
        thisline.append(row[10])
        thisline.append(row[11])
        thisline.append(row[12])
        thisline.append(row[13])
    except:
        print("Error")
    else:
        airports.append(thisline)
    


plt.figure()
plt.hist([row[8] for row in airports]) #Altitude
plt.show()
plt.hist([row[9] for row in airports]) #Timezone
plt.show()
plt.scatter([row[7] for row in airports], [row[6] for row in airports], s=0.2)
plt.show()





kmeans = KMeans(n_clusters=5, init='random')
kmeans.fit([row[6:8] for row in airports])



c = kmeans.predict([row[6:8] for row in airports])



data= []
for row in range(0,len(airports)):
    line = []
    line.append(airports[row][6])
    line.append(airports[row][7])
    line.append(c[row])
    data.append(line) 


plt.figure()
for c in range(0,5): # c = cluster number
    plt.scatter([row[1] for row in data if row[2]==c],
               [row[0] for row in data if row[2]==c], s=0.3)
plt.show()


