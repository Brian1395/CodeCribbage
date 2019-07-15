def deckProcess(a,b,c,d):
    new = []
    new.append(b[0])
    new.append(b[1])
    return new

def playCard(a,b,c,d):
    total = 0
    for x in b:
        total += int(x[1:len(x)])
    for i in a:
        if(total + int(i[1:len(i)]) <= 31):
            return i
    return "GO"
