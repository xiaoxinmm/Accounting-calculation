import requests
#can = input("请输入你要的ASCII的艺术字:")
can = ("Accounting calculation")

urlapi = ("http://artii.herokuapp.com/make?text="+can)

html = requests.get(urlapi)

print(html.text)
print('''
        Author: @xiaoxinmm
        Version: 1.0
''')

def Comde():
  #函数计算单利终值 本金 现值
  print("Simple interest present value calculation","\nF=P*(1+i*n)P=F/(1+i*n)")
  p = float(input("请输入你的P本金数值："))
  i = float(input("请输入银行当前i利息(请自行计算为小数)："))
  n = float(input("请输入存入银行的期数："))
  xxx = float(i*n)
  xxxx = float(xxx+1)
  f1 = float(p*xxxx)
  print("单利终值为",f1)
  p2 = (f1/xxxx)
  print("本金为",p2)
  print("单利现值为",p2)
Comde()
