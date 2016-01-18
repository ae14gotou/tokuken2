import AntTree_Script_StockPrice_Repeat as at_s_sp_r
ST = []
NO = []
K = []
H = []

for i in range(20):
    a,b,c,d = at_s_sp_r.main()
    print 'st: ',a
    print 'no: ',b
    print 'k : ',c
    print 'h : ',d
    ST.append(a)
    NO.append(b)
    K.append(c)
    H.append(d)

print 'stoch'
print 'max:',max(ST)
print 'min:',min(ST)
print 'ave:',sum(ST)/len(ST)

print 'no thresholds'
print 'max:',max(NO)
print 'min:',min(NO)
print 'ave:',sum(NO)/len(NO)

print 'k-means'
print 'max:',max(K)
print 'min:',min(K)
print 'ave:',sum(K)/len(K)

print 'hierarchy'
print 'max:',max(H)
print 'min:',min(H)
print 'ave:',sum(H)/len(H)
