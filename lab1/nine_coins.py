import random
class Ninecoins(object):
    def __init__(self,value):   #讀取初始值
      self.value=value  
    def __str__(self):
      b=format(self.value,'09b')  #轉換成binary的形式
      return('binary: '+str(b) + ' and decimal: '+str(self.value))  
      
    def __repr__(self): 
        b=format(self.value,'09b')   #轉換成binary的形式
        str1=''
        for i in range(0,len(str(b))):  #遇到1放入T 遇到0放入H
          if str(b)[i]=='1':
           str1+='T' 
          elif str(b)[i]=='0':
           str1+='H'
        return('Nine_Coins: '+str1)
    def toss(self):
      self.value=random.randint(0, 511) #以亂數重新產生value的值