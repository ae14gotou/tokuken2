#-*- coding: utf-8 -*-
import Ant
import pandas as pd
import numpy as np
import scipy.spatial.distance as dis
import time

#パラメータ
alpha1 = 0.99
alpha2 = 0.1
Lmax = 20 #1匹のアリの接続限界数


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
    #ansが0に近い=>オブジェクト間の距離が近い=>似ている
    return 1.0 - ans

def build_organize(a_pos, ai, ant):
    if a_pos == ant[0] : #a_posがサポートのとき
        if len(a_pos.children) == 0:    #サポートにアリが全くつながってない
            ai.set_parent(0)    #根をaiの親にセット
            a_pos.set_children(Lmax, ai.Id) #a_posにつなげる
            a_pos.set_plus(ai.Id)
            a_pos.set_parent(0)
            
        else :  #サポートにアリが１匹以上つながっている
            #----a_plus : a_posの子の中で一番aiに類似するデータ----
            tmp = 0.0
            for i in a_pos.children :
                if Sim(ai,ant[i]) > tmp :
                    tmp = Sim(ai, ant[i])
                    ai.set_plus(i)
            #---------------------------------------------------

            if Sim(ai, ant[ai.a_plus]) >= ai.Tsim : #類似度が高ければ移動
                    #aiをa_plusに移動
                    ai.set_pos(ai.a_plus)

            else :
                if Sim(ai, ant[ai.a_plus]) < ai.Tdsim : 
                    if len(a_pos.children) >= Lmax : #Lmaxに達しているとき
                        ai.dec_Tsim(alpha1)
                        #aiをa_plusに移動
                        ai.set_pos(ai.a_plus)
                    else : #Lmaxに達していないとき
                        #aiとa0をつなげる
                        ai.set_parent(a_pos.Id)
                        a_pos.set_children(Lmax, ai.Id)

                else :
                    #現在の位置を保つ a_pos = a0まま
                    ai.set_pos(0)
                    ai.dec_Tsim(alpha1)
                    ai.inc_Tdsim(alpha2)
                                            
    else :  #a_posがその他のアリのとき
        tmp = [a_pos.parent[0]]
        for i in range(len(a_pos.children)):
            tmp.append(a_pos.children[i])
        a_k = ant[np.random.choice(tmp)] #a_posの近傍からランダムに選択　確率的なところ

        #----a_plus : a_posの子の中で一番aiに類似するデータ----
        tmp = 0.0
        for i in a_pos.children :
            if Sim(ai,ant[i]) > tmp :
                tmp = Sim(ai, ant[i])
                ai.set_plus(i)
        #---------------------------------------------------
        if Sim(ai, a_pos) >= ai.Tsim : #類似度が高ければ
            if Sim(ai, ant[ai.a_plus]) < ai.Tdsim :
                if len(a_pos.children) >= Lmax : #Lmaxに達しているとき
                    ai.set_pos(a_k.Id)

                else :
                    ai.set_parent(a_pos.Id)
                    a_pos.set_children(Lmax, ai.Id) #a_posにつなげる
                    
            else :
                ai.dec_Tsim(alpha1)
                ai.inc_Tdsim(alpha2)
                #a_kに移動
                ai.set_pos(a_k.Id)
                
        else:
            ai.dec_Tsim(alpha1)
            ai.inc_Tdsim(alpha2)
            #a_kに移動
            ai.set_pos(a_k.Id)
            
    return 0

#if __name__ == '__main__':
def main():
    #fname = '10d_randomData_value.csv'
    data = []
    ant = []
    #データの読み込み
    O_data = pd.read_csv('return_index_values.csv')
    code_data = pd.read_csv('return_index_codes.csv')

    V_data = O_data.values
    V_code_data = code_data.values
    #np.random.shuffle(V_data) #データをランダムに並び替える
    
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
        ant.append(Ant.Ant(data[i], i, 0, int(T_code_data[i][0])))#変更点
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

    #----サポートの子の中で一番類似するデータ----
    #tmp = alpha1
    tmp = 0.0
    for i in ant[0].children :
        if Sim(ant[0],ant[i]) > tmp :
            tmp = Sim(ant[0], ant[i])
            ant[0].set_plus(i)
    #---------------------------------------------------
    X = np.array(X)

    return ant, X, count1-1
    #print "Id  code  parent  children  a_plus  conect  Tsim  Tdsin  Pos"
    #for ai in ant :
    #    print ai.Id, ai.code, ai.parent, ai.children, ai.a_plus, ai.conect, ai.Tsim, ai.Tdsim, ai.a_pos
    #print "count1:",count1 ,"count2:",count2
    
