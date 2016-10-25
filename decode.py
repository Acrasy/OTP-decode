import sys
import binascii

cypherText = open('cyphertext.txt')

examples = cypherText.readlines()       #import 10 lines of cypher code

cypherText.close()

count       = {}
asciiText   = []
binText     = []
xorED       = []
xorHEX      = []
xorSOL      = []


##___________________________xor messages__________________________##


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


for i in range(len(xorED)):
    xorED[i] = hex(xorED[i])
    
##___________________________Decoding_____________________________##

guess 	= []
xorTRY	= []


guess 	= input("Try which word?")
xorGUESS= str(b,'ascii') 
xorTRY	= binascii.hexlify(guess)

for i in range(len(xorED)):			#fill guesses to whole line
	if len(xorTRY) < len(xorED[i]):
		while(len(xorED) > len(guess)):	
			guess.append(guess)

for i in range(len(xorED)):
	xorSOL = xorTRY ^ xorED 






##___________________________fileausgabe__________________________##


for k in range(len(xorSOL)) :         #hex to ascii
    asciiText.append(''.join(chr(int(xorSOL[k][i:i+2],16)) for i in 
range(0,len(xorSOL),2)))




outTXT = open("output.txt" , "w") 
for i in asciiText:
	outTXT.write(i + "\n")
outTXT.close()


