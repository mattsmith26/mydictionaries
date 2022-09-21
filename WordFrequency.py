
infile = open("sometext.txt", "r")
words = {}


txt_file = infile.read()
txt_file = txt_file.rstrip("\n" + "," + ".")
list = txt_file.split(" ")



for line in list:
    if line in list and line not in words:
        i = list.count(line)
        words[line] = {"count": i}


print(words)



