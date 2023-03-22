import pandas as pd
import numpy as np
import os
import glob

g = pd.Series(np.random.randn(5),index=["a","b","c","d","e"])
# print(s)
# print(s.index)

d = {"b":1,"a":0,"c":2}
s = pd.Series(d)

d = {"b":1.0,"a":0.0,"c":2.0}
s=pd.Series(d,index=["b","c","d","a"])

f=pd.Series(5,index=["a","b","c","d","e"])

without = s.dropna()
#print(without)

# current=os.getcwd()
# file=glob.glob(current+"/*.csv")
#mmse=pd.read_csv(file[0],sep=";")
mmse2 =  pd.read_csv(r"C:\Users\SALASDRAI\Desktop\clase\Info2\MMSE.csv",sep=";")
#print(mmse2)

mmse2.size
mmse2.shape
mmse2.columns
mmse2["Sexo"]
mmse2["Escolaridad"].describe()
mmse2_copy=mmse2.copy()
#mmse2_copy.reset_index()
#mmse2_copy=mmse2_copy.drop(["index"],axis=1)
#mmse2_copy=mmse2_copy.assign(falseIndex=np.random.rand(23))
mmse2_copy=mmse2_copy.set_index("Codigo")
#print(mmse2_copy)
#print(mmse2_copy.index)

print(mmse2_copy.loc["CTR_001"])
print(mmse2_copy.iloc[1])

mmse_edad = mmse2[(mmse2['Edad en la visita'] >= 40)]
mmse_edad = mmse_edad[(mmse_edad['Edad en la visita'] <= 50)]
mmse_escolaridad = mmse_edad[(mmse_edad['Escolaridad'] >= 11)]