import STOCH as st
import NO_THRESHOLDS as nt
import K_means as kmeans
import cluster_Ant as cl_ant
import Evaluate as eva
import time

N = 20 #繰り返し回数
#データ読み込み
#fname = "corners_value.csv"
#k = 4 #k-means用のクラスタ数
#d = [50,100,150,200] #正解クラスの区切り
fname = "10d_randomData_value.csv"
k = 4 #k-means用のクラスタ数
d = [50,100,150,200] #正解クラスの区切り
#fname = "iris_value.csv"
#k = 3 #k-means用のクラスタ数
#d = [50,100,150] #正解クラスの区切り
#fname = "glass_value.csv"
#k = 6 #k-means用のクラスタ数
#d = [70,146,163,176,186,214] #正解クラスの区切り
#fname = "wine_value.csv"
#k = 3 #k-means用のクラスタ数
#d = [59,130,178] #正解クラスの区切り
#fname = "wbc_value.csv"
#k = 2 #k-means用のクラスタ数
#d = [458,699] #正解クラスの区切り

print "DataFile is %s" %fname

#--- STOCH ---
P = 0.0
E = 0.0
C = 0.0
for i in range(N):
    #time.sleep(1)
    Ant,X,count = st.main(fname)
    code = cl_ant.ant_label(Ant)
    p, e, c = eva.Evaluate_All(code, X.tolist(), d, fname)
    P = P + p
    E = E + e
    C = C + c
    
#kmeans.show_plot(code, X)
print "STOCH Algorithm : %s" %N
print "P: ", P/float(N)
print "E: ", E/float(N)
print "C: ", C/float(N)
print "count:", count

#--- NO-THRESHOLDS ---
P = 0.0
E = 0.0
C = 0.0
for i in range(N):
    #time.sleep(1)
    Ant,X,count = nt.main(fname)
    code = cl_ant.ant_label(Ant)
    p, e, c = eva.Evaluate_All(code, X.tolist(), d, fname)
    P = P + p
    E = E + e
    C = C + c

#kmeans.show_plot(code, X)
print "NO-THRESHOLDS Algorithm : %s" %N
print "P: ", P/float(N)
print "E: ", E/float(N)
print "C: ", C/float(N)
print "count:", count

#--- K-means ---
P = 0.0
E = 0.0
C = 0.0
for i in range(N):
    #time.sleep(1)
    code,X = kmeans.main(fname,k)
    p, e, c = eva.Evaluate_All(code, X.tolist(), d, fname)
    P = P + p
    E = E + e
    C = C + c

print "K-means Algorithm : %s" %N
print "P: ", P/float(N)
print "E: ", E/float(N)
print "C: ", C/float(N)
