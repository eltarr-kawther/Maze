#teste labyrinthe

from random import shuffle, randrange

def make_maze(w = 5, h =5):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["#."] * w + ['#'] for _ in range(h)] + [[]]
    hor = [["##"] * w + ['#'] for _ in range(h + 1)]

    def debugPrint():
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
 


    def walk(x, y):
        debugPrint()

        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "#."
            if yy == y: ver[y][max(x, xx)] = " ."

            walk(xx, yy)



    walk(randrange(w), randrange(h))

    s = ""
    cpt = 0
    for (a, b) in zip(hor, ver):
        if cpt == 0:
            b[0]='..'
            s += ''.join(a + ['\n'] + b + ['\n'])
        elif cpt == w-1:
            b[-1]='.'
            s += ''.join(a + ['\n'] + b + ['\n']) 
        else:
            s += ''.join(a + ['\n'] + b + ['\n'])
        cpt += 1
    print(s)
    return s

if __name__ == '__main__':
    tailleLab =int(input("\033[35mVeuillez entrez la taille du labyrinthe: \033[0m"))
    nameFile = input("\033[35mVeuillez renseigner le nom du fichier contenant le labyrinthe parfait: \033[0m")
    fichier= open(nameFile, 'w')		
    fichier.write(make_maze(tailleLab,tailleLab))
    fichier.close()
   
    

	
