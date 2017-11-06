import sys

inp = sys.argv[1:sys.argv.index('-l')]
x = sys.argv[sys.argv.index('-l')+1:]

def wordC(car, stringa):
    k = 0
    for i in stringa:
        if i == car:
            k += 1
    return k

def histo(x, stringa):
    v = []
    c = 0
    for i in x:
        c += wordC(i, stringa)
    for i in x:
        v.append(wordC(i,stringa)/c) if c != 0 else v.append(0)
    return v

def euc_distance(t1,t2):
    x = 0
    for i in range(len(t1)):
        x += (t1[i]-t2[i])**2
    return float('%.2f'%x**(1/2))

res = []
for file in inp:
    f = open(file)
    txt = f.read().split()
    for stringa in txt:
        res.append((histo(x,stringa)))

for k in range(len(inp)):
    str = ''
    for w in range(0,k+1):
        str += '%.2f' % euc_distance(res[k],res[w]) + ' '
    print(str)