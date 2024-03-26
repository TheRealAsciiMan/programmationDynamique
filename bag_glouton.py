s = 30 # taille du sac, ici 30kg
ol = [('A', 700, 13), ('B', 400, 12), ('C', 300, 8), ('D', 300, 10)] # liste des objets


def thief(s:int, ol:list):
    def compare(e):
        return e[3]
    mh = [] # Prix à la masse
    ou = [] # Onjets dans le sac
    w = 0 # Masse utilisée
    p = 0 # Prix dans le sac
    for o in ol:
        omh = o[1] // o[2] # Prix au kilo d'un objet
        mh.append([o[0], o[1], o[2], omh])
    mh.sort(key=compare, reverse=True)
    while w + mh[0][2] < s:
        w += mh[0][2]
        p += mh[0][1]
        ou.append(mh[0][0])
        mh.pop(0)
    return [w, p, ou]

def thief2(s: int, ol: list):
    mh = sorted([(o[0], o[1], o[2], o[1] // o[2]) for o in ol], key=lambda x: x[3])
    ou = []
    w = p = 0
    while w + mh[-1][2] < s:
        w += mh[-1][2]
        p += mh[-1][1]
        ou.append(mh[-1][0])
        mh.pop()
    return [w, p, ou]


print(thief2(s, ol))