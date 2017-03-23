sp = open("C:\Users\\furkan\Desktop\A-large-practice.txt","r")
output = open("C:\Users\\furkan\Desktop\output.txt","w")
input = map(int,sp.read().splitlines())

def frkn(n):
    if n == 0:
        return "INSOMNIA"
    sheep = set([])
    numbers = {"0","1","2","3","4","5","6","7","8","9"}
    i = 1
    while sheep != numbers:
        for x in set(str(n*i)):
            sheep.add(x)
        i += 1
    return (i-1)*n
c = 1
for x in input:
    strx = "Case #{}: {}\n".format(c,frkn(x))
    output.write(strx)
    c += 1







