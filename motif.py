def naif(chaine, motif):
    occurrences = []
    for i in range(len(chaine)-len(motif)+1):
        match = True
        for j in range(len(motif)):
            if chaine[i+j] != motif[j]:
                match = False
        if match:
            occurrences.append(i)
    return occurrences, len(occurrences)

def BoyerMoore(txt, motif):
    m = len(motif)
    n = len(txt)
    tab_car = [-1]*256
    for i in range(m):
        tab_car[ord(motif[i])] = i
    decalage = 0
    res = []
    while(decalage <= n-m):
        j = m-1
        while j>=0 and motif[j] == txt[decalage+j]:
            j = j - 1
        if j<0:
            res.append(decalage)
            if decalage+m<n :
                decalage = decalage + m-tab_car[ord(txt[decalage+m])]
            else :
                decalage = decalage + 1
        else:
            decalage = decalage + max(1, j-tab_car[ord(txt[decalage+j])])
    return res

