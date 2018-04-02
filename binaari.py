
dictionary = {
	'0000001':'a', 
	'0000010':'b', 
	'0000011':'c',
	'0000100':'d',
	'0000101':'e',
	'0000111':'f',
	'0001000':'g',
	'0001001':'h',
	'0001011':'i',
	'0001111':'j',
	'0010000':'k', 
	'0010001':'l', 
	'0010011':'m', 
	'0010111':'n', 
	'0011111':'o', 
	'0100000':'p', 
	'0100001':'q', 
	'0100011':'r', 
	'0100111':'s', 
	'0101111':'t', 
	'0111111':'u', 
	'1000000':'v', 
	'1000001':'x', 
	'1000011':'y', 
	'1000111':'z',
	'_':' ',
} 
tulos=list()
binary = "0001011_0100111_0010001_0000001"
binaarik=binary.split('_')


vastasuunta="lauri"
for x in vastasuunta:
	for k,v in dictionary.iteritems():	
		if(v==x): 
			tulos.append(k)
tulos = "_".join(tulos)
			
print tulos

takaisin = ""
binaarik=tulos.split('_')
for x in binaarik:
    takaisin = takaisin + dictionary[x]

print takaisin
