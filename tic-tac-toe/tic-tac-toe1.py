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
	def __init__(self,pieces=null,next=null):
		if pieces:
			self._board["Pieces"]=[[0,0,0],[0,0,0],[0,0,0]]
			self._board["Next"]=1
			self._board["table"]=0.5
		else:
			self._board["Pieces"] = pieces
			self._board["Next"]=next

	def Pos(self,x,y):
		return Pos(self._board["Pieces"],x,y)

	def Next(self):
		return self._board["Next"]

	def Persentage(self):
		



def Pos(pieces,x,y):
	if 1<=x and x<=3 and 1<=y and y<=3:
		return pieces[y-1][x-1]
	return None


def test(epsilon,alpha):
	print("epsilon: {0}alpha {1}".format(epsilon,alpha))


epsilon=random.random()
alpha=random.uniform(0.0,0.5)
test(epsilon,alpha)
next=1
g=Game()
next=next%2+1

pieces=g._board["Pieces"]

persentage_table={'[[{0},{1},{2}],[{3},{4},{5}],[{6},{7},{8}]]'.format(pieces[0],pieces[1],pieces[2],pieces[3],pieces[4],pieces[5],pieces[6],pieces[7],pieces[8]):'{0}'.format(parcentage)}
