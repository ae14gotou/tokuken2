#-*- coding: utf-8 -*-
import Ant
import pandas as pd
import numpy as np
import scipy
import scipy.spatial.distance as dis
import time

Lmax = 9999 #1匹のアリの接続限界数 このアルゴリズムでは限界を決めないため十分大きく設定


def Sim(Oi, Oj): #オブジェクト間の類似度(0～1)
    ai = np.array(Oi.data)
    aj = np.array(Oj.data)
    ans = 0.0
    #偏角のcos cos類似度 
    #ans = dis.cosine(ai, aj)

    #正規化ユークリッド距離　
    #ans1 = ai / np.linalg.norm(ai)
    #ans2 = aj / np.linalg.norm(aj)
    #ans = np.linalg.norm(ans1-ans2)
    ans = np.linalg.norm(ai-aj) / np.sqrt(len(Oi.data))
    
    if ans > 1.0 :
        #print ans, Oi.data, Oj.data
        ans = 1.0

    return 1.0 - ans

#アリの接続解除
def ant_remove(index, ant):
    #子を持たない場合
    if len(ant[index].children) == 0:
        p = ant[index].parent[0]
        ant[p].rm_children(index)
        ant[index].disconect()
        #ant[index].first = True #！！要検討！！　サポートに戻ったとき初回に戻すかどうか
    #子を持つ場合，再帰呼び出し
    else :
        for i in ant[index].children :
            ant_remove(i)

def build_organize(a_pos, ai, ant):
    if len(a_pos.children) < 2: #0～1匹のアリがa_posとつながっているとき
        #aiとa_posをつなげる
        ai.set_parent(a_pos.Id)
        a_pos.set_children(Lmax, ai.Id)

    #2匹のアリがa_posとつながっている(初回)とき
    elif len(a_pos.children) == 2 and a_pos.first == True:
        #aiとより似ていないアリをa_posから取り去る
        tmp = Sim(ai, ant[a_pos.children[0]]) #a_posの1番目の子とaiとの類似度
        dsim = a_pos.children[0] #似てない方をとりあえず1番目の子に設定
        if Sim(ai, ant[a_pos.children[1]]) < tmp : #a_posの2番目の子とaiとの類似度がtmpより小さいとき
            dsim = a_pos.children[1] #似てない方を2番目の子に設定
        #似てない方をa_posから取る
        ant_remove(dsim, ant)
        a_pos.fin_first()
        #aiとa_posをつなげる
        ai.set_parent(a_pos.Id)
        a_pos.set_children(Lmax, ai.Id)
        

    #2匹以上のアリがa_posとつながっている(2回目)とき
    elif len(a_pos.children) >= 2 and a_pos.first == False :
        #a_posの子ノードの類似度最小値設定
        #----Tdsim : a_posの子同士での最小類似度----
        tmp = 1.0
        for j in a_pos.children :
            for k in a_pos.children :
                if Sim(ant[j], ant[k]) < tmp :
                    tmp = Sim(ant[j], ant[k])
                    a_pos.set_Tdsim(tmp)
        #print a_pos.Tdsim
        #----a_plus : a_posの子の中で一番aiに類似するデータ----
        tmp = 0.0
        for i in a_pos.children :
            if Sim(ai, ant[i]) > tmp :
                tmp = Sim(ai, ant[i])
                ai.set_plus(i)
        #---------------------------------------------------

        if Sim(ai, ant[ai.a_plus]) < a_pos.Tdsim : #aiがa_plusと十分似ていない
            #aiとa_posをつなげる
            ai.set_parent(a_pos.Id)
            a_pos.set_children(Lmax, ai.Id)

        else :
            #a_plusに移動
            ai.set_pos(ai.a_plus)
           
    return 0
            
#if __name__ == '__main__':
def main(fname1, fname2):
    data = []
    ant = []

    #データの読み込み
    O_data = pd.read_csv(fname1)
    code_data = pd.read_csv(fname2)
    
    V_data = O_data.values
    V_code_data = code_data.values
    #np.random.shuffle(V_data) #ランダムに並び替え
    
    T_data = V_data.tolist()
    T_code_data = V_code_data.tolist()
    #データを0~1に標準化
    vmin = float(V_data.min())
    vmax = float(V_data.max())
    V_data = (V_data - vmin) / (vmax - vmin)

    data = V_data.tolist() #標準化されたデータのリスト
    X = []
    
    #ant.append(Ant.Ant([],0,0)) #root 根　サポート役
    for i in range(len(T_code_data)):  #アリ（データ）の初期化
        ant.append(Ant.d_Ant(data[i], i, 0, int(T_code_data[i][0])))
        X.append(T_data[i]) #cluster_Ant用
    #木の構築
    count1 = 0 #繰り返しの上限
    count2 = 0 #接続済みアリのカウント
    while count1 <  1000 and count2 < len(data)-1:
        count2 = 0
        for ai in ant[1:] : #0番目はサポート
            if ai.conect == False:
                a_pos = ant[ai.a_pos]
                build_organize(a_pos, ai, ant)
            else : count2 = count2 + 1
        count1 = count1 + 1

    #----サポート(root)の子の中で一番類似するデータ----
    tmp = 0
    for i in ant[0].children :
        if Sim(ant[0],ant[i]) > tmp :
            tmp = Sim(ant[0], ant[i])
            ant[0].set_plus(i)
    #---------------------------------------------------
    ant[0].set_parent(0)
    X = np.array(X)

   
    print "Id  code  parent  children  a_plus  conect  Tsim  Tdsin  Pos"
    for ai in ant :
        print ai.Id, ai.code, ai.parent, ai.children, ai.a_plus, ai.conect, ai.Tsim, ai.Tdsim, ai.a_pos
    print "count1:",count1 ,"count2:",count2
    return ant, X, count1-1
