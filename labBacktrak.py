
def lab(tailleLab):
	M =[]
	for i in list(range(tailleLab*2)):
		if i < 1:
			M.append(list('.'+ 2*tailleLab * "#"))
		elif i < (2*tailleLab -1) and i%2 != 0:
			M.append(list('#.'*tailleLab+"#"))
		elif i < (2*tailleLab -1) and i%2 == 0:
			M.append(list('#'+ 2*tailleLab * "#"))
		else:
			M.append(list((2*tailleLab)*"#"+'.'))
	M.insert(-1,list('#.'*tailleLab + '#'))
	M[1][0] = '.'									#Entree
	M[-2][-1] = '.'									#sortie

	return M
#lab(5)




def verif_4_Murs(maze,x,y):

	if x > len(maze)-2 or y > len(maze)-2 or x<0 or y<0:
		#print('x or y depasse les limites du labyrinthe')
		return False
	directions = {'droite':maze[x][y+1],'gauche':maze[x][y-1],'haut':maze[x-1][y],'enBas':maze[x+1][y]}
	
	
	if directions['droite'] == directions['gauche'] == directions['haut'] == directions['enBas']=='#':
		return True
	else:
		return False

# ~ print(verif_4_Murs(lab(5),0,0))
# ~ print(verif_4_Murs(lab(5),1,2))

def resolu(maze,x=1,y=0):
	Nb_pas=list(range(0,len(maze)-2,2))
	if maze[x][y+1] == '.':
		y += 1
	if maze[x+1][y] == '.':
		x += 1
	if verif_4_Murs(maze,x+2,y):
		maze[x+1][y] = '.'
		x +=2
		resolu(maze,x,y)

	if verif_4_Murs(maze,x-2,y):
		maze[x-1][y] = '.'
		x += -2
		resolu(maze,x,y)
				
	if verif_4_Murs(maze,x,y+2):
		maze[x][y+1] = '.'
		y += 2
		resolu(maze,x,y)	
				
	if verif_4_Murs(maze,x,y-2):
		maze[x][y-1] = '.'
		y -= 2
		resolu(maze,x,y)
	

	tab = ''
	lon = len(maze)
	aa=list(range(len(maze)+1))
	for i,l in enumerate(maze):
		for k,m in enumerate(l):
			if i == len(maze)-2 and k ==len(maze)-3 :
				m ='.'
				tab += m
			else:
				tab += m
			
		if i in aa:
			tab += '\n'
	return tab
			
if __name__ == '__main__':
	
	tailleLab =int(input("\033[35mVeuillez entrez la taille du labyrinthe: \033[0m"))
		
		
	nameFile = input("\033[35mVeuillez renseigner le nom du fichier contenant le labyrinthe parfait: \033[0m")
	fichier= open(nameFile, 'w')		
	fichier.write(resolu(lab(tailleLab)))
	fichier.close()
	
