import pandas as pd
import numpy as np

data = []
a = 0
for i in range(4):
	for j in range(50):
		tmp = [0,0,0,0,0,0,0,0,0,0]
		tmp.insert(i+a, random.randint(1,100))
		tmp.insert(i+a+1, random.randint(1,100))
		tmp.insert(i+a+2, random.randint(1,100))
		tmp.pop()
		tmp.pop()
		tmp.pop()
		data.append(tmp)
	a=i+2

pdata = pd.DataFrame(data)
pdata.to_csv('10d_randomData.csv')
