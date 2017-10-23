#Author Ivan Ferrante
#StudentID: 1563390

import math, numpy

def get_cosine(vec1, vec2):
#This metod take two vectors of number and calculate
#the cosine similarity.
     vec1 = numpy.array(vec1)
     vec2 = numpy.array(vec2)
     numerator = sum(vec1 * vec2)

     sum1 = sum(numpy.power(vec1,2))
     sum2 = sum(numpy.power(vec2,2))
     denominator = numpy.sqrt(sum1) * numpy.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator


def get_sim(doc):
#This metod take a list of document rappresented as
#vectors in m-dimensional array and return the pairs
#of documents that are closest each other using get_cosine(v1,v2)
    coppie = []
    for i in range(len(doc)):
        max = -1
        prov = []
        for j in range(i+1,len(doc)):
            k = get_cosine(doc[i],doc[j])
            if(k>max):
            #Case 1 : k is the new max
                max = k
                prov = [j]
            elif(k==max):
            #Case 2 : k is the same max value finded previously
            #This case handles the same cosine values
                prov.append(j)
        for w in prov:
            # Create the pairs
            coppie.append((i+1,w+1))
    return coppie

# ---------------- INPUT:

S1 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
S2 = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
S3 = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1]
S4 = [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
S5 = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]
S6 = [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
S7 = [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]
S8 = [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0]

d = [S1, S2, S3, S4, S5, S6, S7, S8]

print(get_sim(d))
