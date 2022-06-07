import pygame
import sys
import math
import random
#(1,1)(1,2)行列
# pygame 初始化
pygame.init()
# 设置棋盘大小，DFS规定必须是奇数,每一个奇数的格子必须是节点
chess_number=89
IF_RANDOM_START_END=0#是否随机终点和起点
TICK=100
BG=(144,136,145)#背景色
LINECOLOR=(112,73,46)#网格色
STARTCOLOR=(253,176,36)#起点格子的颜色
ENDCOLOR=(224,90,9)#终点(224,90,9)橙色     （252，61，63 ）大红
WALLCOLOR=(33,41,48)#墙壁的颜色

#迷宫在画布上显示的位置
START_POS=(50,50)
START_POSX=50
START_POSY=50
CELL_LENGTH=int(600/chess_number)#每个格子的像素大小
LINE_WIDTH=3#线的宽度
BIAS=5#中心偏差,取奇数,起点和终点离对角线的距离
# 设置背景框大小等pygame初始化操作
size = width, height = 2*START_POSX+chess_number*CELL_LENGTH,2*START_POSY+chess_number*CELL_LENGTH
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ace Cheney made")


if IF_RANDOM_START_END==1:
	# 设置起始位置
	start_posx=random.randint(0,chess_number-1)
	start_posy=random.randint(0,chess_number-1)
	# 设置终点始位置
	end_posx=random.randint(0,chess_number-1)
	end_posy=random.randint(0,chess_number-1)
else:
	# 设置起始位置
	start_posx=0+BIAS
	start_posy=0+BIAS
	# 设置终点始位置
	end_posx=chess_number-1-BIAS
	end_posy=chess_number-1-BIAS

startpos=[start_posx,start_posy]
endpos=[end_posx,end_posy]
#设置墙格子列表
wallcell=[]


def draw(screen,wallcell):
	global pos
	global endflag,endpath
	for i in range(chess_number+1):
		pygame.draw.line(screen, LINECOLOR, (START_POSX,START_POSY+i*CELL_LENGTH), (START_POSX+chess_number*CELL_LENGTH,START_POSY+i*CELL_LENGTH), LINE_WIDTH)#横线
		pygame.draw.line(screen, LINECOLOR, (START_POSX+i*CELL_LENGTH,START_POSY),(START_POSX+i*CELL_LENGTH,START_POSY+chess_number*CELL_LENGTH), LINE_WIDTH)#竖线#
	#画墙
	drawwall(wallcell)
	drawcell(screen,start_posx, start_posy, STARTCOLOR)#起点
	drawcell(screen,end_posx, end_posy, ENDCOLOR) #终点

def drawcell(screen,i,j,cellkind):
	pygame.draw.rect(screen,cellkind,[START_POSX+CELL_LENGTH*j+(LINE_WIDTH-1),START_POSY+CELL_LENGTH*i+(LINE_WIDTH-1),CELL_LENGTH-LINE_WIDTH,CELL_LENGTH-LINE_WIDTH],0)

def DFScreatwall(chess_number):
	'''
	生成迷宫，有路为0，墙为1
	param:chess_number
	return:一个储存全局地图信息的二维数组，0为无墙，1为有墙
	'''
	neighborcell=[]
	maincell=[]
	#初始状态下，迷宫内所有点都是墙壁，只有满足条件，节点才会由墙壁变成通路，而且节点和相邻选中非节点之间的阻碍打破
	wallcell=[[1]*chess_number for i in range(chess_number)]
	wallcell[start_posx][start_posy]=0
	neighborcell.append(startpos)
	con=1
	#对一个节点进行选择拓展，规则：选择的拓展节点一定是孤立的
	while con:
		#在邻居中选择最后的一个，因为最后一个储存的是最深的
		[x,y]=neighborcell[-1]
		nextcell=[]
		#一个潜在的邻居，如果他的上下左右的墙都是未打通的，那么他是符合要求的
		if x-2>=1 and wallcell[x-2][y] ==1 and wallcell[x-1][y] == 1 and wallcell[x-3][y]==1 and wallcell[x-2][y+1]==1 and wallcell[x-2][y-1]==1:
			nextcell.append([x-2,y])
		if x+2<=chess_number-2 and wallcell[x+2][y] ==1 and wallcell[x+1][y] == 1 and wallcell[x+3][y]==1 and wallcell[x+2][y+1]==1 and wallcell[x+2][y-1]==1:
			nextcell.append([x+2,y])
		if y-2>=1 and wallcell[x][y-2]==1 and wallcell[x][y-3] ==1 and wallcell[x][y-1] == 1 and wallcell[x-1][y-2]==1 and wallcell[x+1][y-2]==1:
			nextcell.append([x,y-2])
		if y+2<=chess_number-2 and wallcell[x][y+2] ==1 and wallcell[x][y+1] == 1 and wallcell[x][y+3]==1 and wallcell[x-1][y+2]==1 and wallcell[x+1][y+2]==1:
			nextcell.append([x,y+2])
		try:
			#随机选一个符合要求的邻居作为真正的邻居
			num=random.randint(0,len(nextcell)-1)
			neighborcell.append([nextcell[num][0],nextcell[num][1]])
			#邻居和墙均需要被打通
			wallcell[nextcell[num][0]][nextcell[num][1]]=0
			if nextcell[num]==[x-2,y]:
				wallcell[x-1][y]=0
			elif nextcell[num]==[x+2,y]:
				wallcell[x+1][y]=0
			elif nextcell[num]==[x,y-2]:
				wallcell[x][y-1]=0
			elif nextcell[num]==[x,y+2]:
				wallcell[x][y+1]=0
		except:
			#数组越界
			#该路径没有合适的邻居,那就把这个流程再来一次,在此之前必须先去除最后一个不满足要求的
			neighborcell.pop()
		#当所有的关键点全联通,结束遍历
		odd1=0
		con=0
		for y in wallcell:
			if odd1%2==1:
				odd2=0
				for x in y:
					if odd2%2==1:
						if x==1:
							con=1
							break
					odd2+=1
			if con==1:
				break
			odd1+=1
	return wallcell

def drawwall(wallcell):
	for i in range(chess_number):
		for j in range(chess_number):
			if wallcell[i][j]==1:
				drawcell(screen, i, j, WALLCOLOR)
def main(screen):
	RUN = True
	FOUND = False
	wallcell = DFScreatwall(chess_number)
	draw(screen,wallcell)
	while RUN:
		clock.tick(TICK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				RUN = False

	pygame.quit()

if __name__ == "__main__":
	main(screen)