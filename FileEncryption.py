infile = open("info_security.txt", "r")

code = { "A": "!", "a": "*", "B": "1", "b": "1", "C": "&", "c": "@", "D": "3", "d": "^", "E": "[", "e": "%", "F": "#", "f": "%",
"G": "d", "g": "/", "H": "3", "h": ":", "I": "*", "i": "$", "J": "^", "j": "<", "K": "<", "k": ")", "L": "b", "l": ",", "M": "-", 
"m": "!", "N": "%", "n": "-", "O": "w", "o": "#", "P": ":", "p": ">", "Q": "/", "q": "-", "R": "9", "r": "7", "S": " i", "s": "3", "T": 
"2", "t": "f", "U": "+", "u": "w", "V": "o", "v": ">", "W": "4", "w": "@", "X": ")", "x": "(", "Y": "k", "y": "e", "Z": ",", "z": "&"

}

for line in infile:
    text = line

encrypted_code = ""

for i in range(0, len(text)):
    if text[i] in code.keys():
        encrypted_code += code[text[i]]
    else:
        encrypted_code += text[i]


print(encrypted_code)

outfile = open("encrypted.txt", "w")
outfile.write(encrypted_code+ "\n")

outfile.close()