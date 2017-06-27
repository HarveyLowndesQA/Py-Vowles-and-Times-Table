'''
Created on 30 May 2017

@author: Administrator
'''

def TimesTable(x, y):
        g=lambda x,y:range(x,y-1,-1)if(x>y)else range(x,y+1) 
        for z in g(x,y): print ("".join("%dx%d=%d \n"%(z,w,(z*w)) for w in range(1,11)))
            #for w in range(1,11):print("%dx%d=%d"%(z,w,(z*w)))     
            
TimesTable(20,10)