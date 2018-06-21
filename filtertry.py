# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 21:17:12 2018

@author: prabhat
"""

import os
import numpy as np
import pandas as pd

file=open('write.txt',"w")
lines=open('movie_lines.txt',"r").readlines()

file.writelines(" {\n\t\"conversations\": \n [ \n\n\n")
k=0        
for i in lines:
    j=1
    
   # print(i)
    stri=i.split('+++$+++')
    #print(stri)
    l=0
    
    for j in stri:
       l=l+1
       if(l%5==0):
           k=k+1
           print(k)
           if k%2==1 :
               file.write("[\n \"")
               print(j)
               file.write(j.strip('\n'))
               file.writelines("\" \n")
           if k%2==0 :
               print(j)
               file.write("\"")
               file.write(j.strip('\n'))
               file.write("\"\n],\n")
                      
print("end")           
file.write(" \n\n  ] \n }")
    
