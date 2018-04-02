#dictionary = {
#	'a': 'k', 
#	'b': 'l'
#}
#print dictionary 

#empty_dictionary = dict()
#empty_dictionary['a'] = 'k'
#print empty_dictionary

dictionary = {
	'a':'k', 
	'b':'l', 
	'c':'m',
	'd':'n',
	'e':'o',
	'f':'p',
	'g':'q',
	'h':'r',
	'i':'s',
	'j':'t',
	'k':'u', 
	'l':'v', 
	'm':'x', 
	'n':'y', 
	'o':'z', 
	'p':'a', 
	'q':'b', 
	'r':'c', 
	's':'d', 
	't':'f', 
	'u':'g', 
	'v':'h', 
	'x':'u', 
	'y':'i', 
	'z':'j',
	'_':' ',
	'0':'10-',
	'1':'11-',
	'2':'12-',
	'3':'13-',
	'4':'14-',
	'5':'15-',
	'6':'16-',
	'7':'17-',
	'8':'18-',
	'9':'19-',
} 

tulos=""
ceasar_cypher = "rot13"

for x in ceasar_cypher:
    tulos = tulos + dictionary[x]

print tulos
