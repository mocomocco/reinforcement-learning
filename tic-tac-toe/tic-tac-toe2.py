import random

'''
1. 初期設定
1.1 step-size パラ メ ータ α, exploration 確率 ε を 決める .
1.2 全可能 state の表 S を 準備し ， そ れぞれに 勝利確率の初期値を 設定:
X が整列なら 0, O が整列なら 1, それ以外なら 0.5 2.メインループ: 以下を適当な episode数だけ繰り返す
2.1 現 state を 記録する 盤の初期化: 9個の升をすべて空白にし， この状態を sに記録する.
2.2 サブループ:
2.2.1相手が(ランダムに)選んだ着手の場所を盤に Xと記録→state s 2.2.2 sが相手勝利の場面ならV(s)←V(s)+α(0−V(s))とし， 2.1に戻る 2.2.3この盤面 s で可能な手の記録用バッファを初期化 2.2.4 sにおける空升を順にサーチし， その位置kと,そこを Xに変えた
state の現在の確率値 p のペア (k,p) をバッファに追加. 2.2.5[0,1]の一様乱数から xをサンプルし,actionを決める;
2.2.5.1x<εならバッファからランダムに選んだものを aとし
2.2.5.2 さ も なく ば確率値最大のも のを (複数有れば乱択で) 選び a と する 2.2.6 a に対応する盤の升を X に変えこの状態を state s’ に記録
2.2.7 「 2.2.5.2 の場合」 は新し い state s’ の確率値 V (s′) を 読み込み，
以前の状態 s の確率値 V(s) を V(s) ← V(s)+α(V(s′)−V(s)) と更新 2.2.8 s′ が勝利場面か, 盤が埋ま れば引分と し て 2.1 へ,
   さもなくばs←s′ で2.2.1へ.
'''
class Game:
	def __init__(self,pieces):
		self.pieces=pieces
		self.next=1

	def Pos(self,x):
		return Pos(self.pieces,x)

	def Next(self):
		return self.next

def piecechange(g,x):
	if g.Pos[x]=0:
		g.Pos[x]=g.Next
		g.Next=g.Next%2+1
		return g.pieces
	return None


def Pos(pieces,x):
	if 0<=x and x<=8:
		return pieces[x]
	return None


def test(epsilon,alpha,percentage_table):
	print("epsilon: {0}".format(epsilon)+"\n"+"alpha {0}".format(alpha))
	print("(1,2,2,1,1,2,2,0,1): {0}".format(percentage_table[(1,2,2,1,1,2,2,0,1)]))


def OrginPercentage(first,second,third,pieces,percentage):
	if abs(pieces.count(1)-pieces.count(2))>1:
		return 3
	if pieces[first]==pieces[second] and pieces[first]==pieces[third]:
		if pieces[first]!=0:
			if percentage==0.5:
				return pieces[first]-1
			else:
				return 3
		else:
			return percentage
	else:
		return percentage

def possibility(pieces):
	percentage=0.5
	percentage=OrginPercentage(0,1,2,pieces,percentage)
	percentage=OrginPercentage(3,4,5,pieces,percentage)
	percentage=OrginPercentage(6,7,8,pieces,percentage)
	percentage=OrginPercentage(0,3,6,pieces,percentage)
	percentage=OrginPercentage(1,4,7,pieces,percentage)
	percentage=OrginPercentage(2,5,8,pieces,percentage)
	percentage=OrginPercentage(0,4,8,pieces,percentage)
	percentage=OrginPercentage(2,4,6,pieces,percentage)
	return percentage

def OrginPercentageTable():
	pieces=[0,0,0,0,0,0,0,0,0]
	percentage_table={(0,0,0,0,0,0,0,0,0):0.5}
	counter=0

epsilon=random.random()
alpha=random.uniform(0.0,0.5)


pieces=list()
pieces=[0,0,0,0,0,0,0,0,0]
percentage_table={(0,0,0,0,0,0,0,0,0):0.5}
percentage=0.5

counter=0
percentage_table=OrginPercentageTable()
for ii in range(0,3):
	pieces[0]=0
	pieces[0]=pieces[0]+ii
	for itw in range(0,3):
		pieces[1]=0
		pieces[1]=pieces[1]+itw
		for ith in range(0,3):
			pieces[2]=0
			pieces[2]=pieces[2]+ith
			for twi in range(0,3):
				pieces[3]=0
				pieces[3]=pieces[3]+twi
				for twtw in range(0,3):
					pieces[4]=0
					pieces[4]=pieces[4]+twtw
					for twth in range(0,3):
						pieces[5]=0
						pieces[5]=pieces[5]+twth
						for thi in range(0,3):
							pieces[6]=0
							pieces[6]=pieces[6]+thi
							for thtw in range(0,3):
								pieces[7]=0
								pieces[7]=pieces[7]+thtw
								for thth in range(0,3):
									pieces[8]=0
									pieces[8]=pieces[8]+thth
									percentage=possibility(pieces)
									if 	percentage!=3:
										counter+=1
										#print(pieces,counter)
										t_pieces=tuple(pieces)
										percentage_table[t_pieces]=percentage

s=game([0,0,0,0,0,0,0,0,0])
for iin range(1,3)
	print("You are player2")
	print("player",s.Next,"'s'turn:")

	changed_piece=int(input())
	pieces=piecechange(s,changed_piece)
	if possibility(pieces)==0:
		t_pieces=tuple(pieces)
		percentage_table[t_pieces]=(1-alpha)*percentage_table(t_pieces)
	else:



test(epsilon,alpha,percentage_table)
