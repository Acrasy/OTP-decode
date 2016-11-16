# -*- coding: utf-8 -*-
cypherText = open('cyphertext.txt')
  
examples = cypherText.readlines()       #import 10 lines of cypher code
  
cypherText.close()
  
count       = {}
asciiText   = []
binText     = []
xorED       = []
xorHEX      = []
  
for j in range(len(examples)) :         #get rid of '\n'
      if j< 9 :
          examples[j]=examples[j][0:-2]
  
  #for k in range(len(examples)) :         #convert to binary
  #    h_size = len(examples[k]) * 4
  #    binText.append(bin(int(examples[k],16))[2:].zfill(h_size))
  
for i in range(len(examples)) :         #xor every message
      for j in range(len(examples)) :
          xorED.append(int(examples[i],16) ^ int(examples[j],16))
  
xorED.sort()                            #get rid of duplicates
xorED = xorED[10::2]
  
  
  #for k in range(len(examples)) :         #hex to ascii
  #    asciiText.append(''.join(chr(int(examples[k][i:i+2],16)) for i in range(0,len(examples),2)))
  
xorHEX = xorED[:]
  
for i in range(len(xorHEX)):
     xorHEX[i] = hex(xorHEX[i])
     
outTXT = open("output1.txt" , "w") 
for i in xorHEX:
	outTXT.write(i + "\n")
outTXT.close()