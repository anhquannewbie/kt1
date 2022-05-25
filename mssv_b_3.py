char_to_dots = {
 	 'A': '.-', 	'B': '-...', 	'C': '-.-.',	'D': '-..',	'E': '.', 		'F': '..-.', 'G': '--.',	'H': '....', 	'I': '..',		'J': '.---', 	'K': '-.-', 	'L': '.-..', 'M': '--', 	'N': '-.', 	'O': '---',	'P': '.--.', 	'Q': '--.-', 	'R': '.-.', 'S': '...', 	'T': '-', 		'U': '..-', 	'V': '...-', 	'W': '.--', 	'X': '-..-', 'Y': '-.--', 	'Z': '--..', 	' ': '/', 		'0': '-----',	'1': '.----', 	'2': '..---', '3': '...--', 	'4': '....-', 	'5': '.....',	'6': '-....', 	'7': '--...', 	'8': '---..', '9': '----.',	'&': '.-...', 	"'": '.----.', 	'@': '.--.-.', 	')': '-.--.-',	 '(': '-.--.', ':': '---...', 	',': '--..--', 	'=': '-...-', 	'!': '-.-.--', 	'.': '.-.-.-',	'-': '-....-', '+': '.-.-.', 	'"': '.-..-.', 	'?': '..--..',	 '/': '-..-.'
}


dots_to_char = {
 	 '.-': 'A', 	 '-...': 'B', 	'-.-.': 'C',	'-..': 'D',	'.': 'E', 		'..-.': 'F',
 	 '--.':'G',	'....':'H', 	'..':'I',		'.---':'J', 	'-.-':'K', 	'.-..':'L',
 	 '--':'M', 	'-.': 'N', 	'---': 'O',	'.--.': 'P', 	'--.-': 'Q', 	'.-.': 'R',
 	 '...':'S', 	'-':'T', 		'..-':'U', 	'...-':'V', 	'.--':'W', 	'-..-':'X',
 	 '-.--': 'Y', 	'--..': 'Z', 	'/': ' ', 		'-----': '0',	'.----': '1', 	'..---': '2',
'...--':'3', 	'....-':'4', 	'.....':'5',	'-....':'6', 	'--...':'7', 	'---..':'8',
'----.':'9',	'.-...': '&', 	'.----.': "'", 	'.--.-.': '@', 	'-.--.-': ')',	'-.--.': '(',
 	'---...': ':', 	'--..--': ',', 	'-...-': '=', 	'-.-.--': '!', 	'.-.-.-': '.',	'-....-': '-',
'.-.-.': '+', 	'.-..-.': '"', 	'..--..': '?',	'-..-.': '/'
}

def encode_morse(myStr2Encode="SOS SOS"):
    myEncode = ""
    myStr2Encode = myStr2Encode.upper()
    for c in myStr2Encode:
        if char_to_dots.get(c) != None:
            myEncode += char_to_dots.get(c)+" "
        else:
            myEncode += "# "
    return myEncode

def decode_morse(myStr2Decode=".... . .-.. .--. / -- .   -.-.--"):
    myDecode = ""
    listDecode = myStr2Decode.split()
    for l in listDecode:
        if dots_to_char.get(l) != None:
            myDecode += dots_to_char.get(l)
        else:
            myDecode += "#"
    return myDecode

#print(encode_morse("dang anh quan"))