
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
	M[1][0] = '.'
	M[-2][-1] = '.'
	
	"""
	nameFile = input("\033[35mVeuillez renseigner le nom du fichier contenant le labyrinthe parfait: \033[0m")
	fichier= open(nameFile, 'a')		
	for j in M:
		fichier.write(j+'\n')
	fichier.close()
	print(len(M[3]),len(M[0]))
	"""
	for j in M:
		print(j)
	return M
#lab(5)
#tailleLab =int(input("\033[35mVeuillez entrez la taille du labyrinthe: \033[0m"))




def verif_4_Murs(maze,x,y):

	if x > len(maze)-2 or y > len(maze)-2:
		print('x or y depasse les limites du labyrinthe')
		return False
	directions = {'droite':maze[x][y+1],'gauche':maze[x][y-1],'haut':maze[x-1][y],'enBas':maze[x+1][y]}
	
	
	if directions['droite'] == directions['gauche'] == directions['haut'] == directions['enBas']=='#':
		return True
	else:
		return False

# ~ print(verif_4_Murs(lab(5),0,0))
# ~ print(verif_4_Murs(lab(5),1,2))

def resolu(maze,x=1,y=0):
	Nb_pas=list(range(0,len(maze),2))
	
	if maze[x][y+1] == '.':
		y += 1
	if verif_4_Murs(maze,x+2,y)==True:
		maze[x+1][y] = '.'
		x +=2
		
	if verif_4_Murs(maze,x,y+2)==True:
		maze[x][y+1] = '.'
		y += 2
	if verif_4_Murs(maze,x,y+2)==True:
		maze[x][y+1] = '.'
		y += 2
	if verif_4_Murs(maze,x,y+2)==True:
		maze[x][y+1] = '.'
		y += 2
	print(y)
	if verif_4_Murs(maze,x,y+2)==True:
		maze[x][y+1] = '.'
		y +=4
	if verif_4_Murs(maze,x-2,y)==True:
		maze[x-1][y] = '.'
		
	
		
		
	print('******************')
	tab = ''
	lon = len(maze)
	aa=list(range(len(maze)+1))
	for i,l in enumerate(maze):
		for m in l:
			tab += m
			
		if i in aa:
				tab += '\n'
	print(tab)
			

	
resolu(lab(5))
		
	
