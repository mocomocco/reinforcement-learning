import random
import copy

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

	def Pos(self,x):
		return Pos(self.pieces,x)

	def Next(self):
		return self.next

epsilon=random.random()
alpha=random.uniform(0.0,0.5)

def piecechange(s,x,next_player):
	new_s=copy.deepcopy(s)
	if new_s[x]==0:
		new_s[x]=next_player
		return new_s
	print("you cannnot choose ",x)
	print_board(new_s)
	print("player",next_player,"'s turn\n choose piece:'")
	x=int(input())
	return piecechange(s,x,next_player)


def Pos(pieces,x):
	if 0<=x and x<=8:
		return pieces[x]
	return None

def Thereis3(first,second,third,pieces,possibility):
	if abs(pieces.count(1)-pieces.count(2))>1:
		return 3
	if pieces[first]==pieces[second] and pieces[first]==pieces[third]:
		if pieces[first]!=0:
			if possibility==0.5:
				return pieces[first]-1
			else:
				return 3
		else:
			return possibility
	else:
		return possibility

def OrginPossibility(pieces):
	possibility=0.5
	possibility=Thereis3(0,1,2,pieces,possibility)
	possibility=Thereis3(3,4,5,pieces,possibility)
	possibility=Thereis3(6,7,8,pieces,possibility)
	possibility=Thereis3(0,3,6,pieces,possibility)
	possibility=Thereis3(1,4,7,pieces,possibility)
	possibility=Thereis3(2,5,8,pieces,possibility)
	possibility=Thereis3(0,4,8,pieces,possibility)
	possibility=Thereis3(2,4,6,pieces,possibility)
	return possibility

def OrginPTable():
	pieces=[0,0,0,0,0,0,0,0,0]
	P_table={(0,0,0,0,0,0,0,0,0):0.5}
	counter=0
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
										possibility=OrginPossibility(pieces)
										if 	possibility!=3:
											counter+=1
											#print(pieces,counter)
											t_pieces=tuple(pieces)
											P_table[t_pieces]=possibility
	return P_table

def test(epsilon,alpha,P_table):
	print("epsilon: {0}".format(epsilon)+"\n"+"alpha {0}".format(alpha))
	print("(1,2,2,1,1,2,2,0,1): {0}".format(P_table[(1,2,2,1,1,2,2,0,1)]))

def GameIsOver(s):
	P_table[tuple(s)]=(1-alpha)*P_table[tuple(s)]
	return P_table

def FindValidMoves(valid_moves,s):
	for i in range(0,9):
		if s[i]==0:
			new_s=piecechange(s,i,2)
			t_new_s=tuple(new_s)
			p=P_table[t_new_s]
			valid_moves[i]=p
	return valid_moves

def Suggest(s):
	valid_moves={}
	print(valid_moves)
	valid_moves=FindValidMoves(valid_moves,s)
	print(valid_moves)
	x=random.uniform(0,1)
	if(x<epsilon):
		a=random.randint(0,len(valid_moves)-1)
	else:
		max_p=max(valid_moves.values())
		max_piece=[key for key in valid_moves if valid_moves[key]==max_p]
		a=max_piece[0]
	print("You are player2  choose ",a)
	print("player2's'turn:")
	changed_piece=int(input())
	new_s=piecechange(s,changed_piece,2)
	print_board(new_s)
	if(x>=epsilon):
		t_s=tuple(s)
		t_new_s=tuple(new_s)
		P_table[t_s]=(1-alpha)*P_table[t_s]+alpha*P_table[t_new_s]
	return new_s

def print_board(pieces):
	print(pieces[0]," ",pieces[1]," ",pieces[2])
	print(pieces[3]," ",pieces[4]," ",pieces[5])
	print(pieces[6]," ",pieces[7]," ",pieces[8])

def OpponentTurn():


def round(s):
	s=OpponentTurn()


P_table=OrginPTable()




s=[0,0,0,0,0,0,0,0,0]
print_board(s)
for i in range(1,10):
	print("You are player2")
	print("player1's'turn:")
	changed_piece=int(input())
	new_s=piecechange(s,changed_piece,1)
	print_board(new_s)
	if P_table[tuple(new_s)]==0:
		print("You lose...")
		print(P_table[tuple(s)])
	if P_table[tuple(new_s)]==0:
		P_table=GameIsOver(s)
	else:
		new_s=Suggest(new_s)
	s=new_s
	if P_table[tuple(s)]==1:
		print("You win!")
		print(P_table[tuple(s)])

test(epsilon,alpha,P_table)
