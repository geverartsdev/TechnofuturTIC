dict = {}
def morse(dict):
    dict["A"] = ".-"
    dict["B"] = "-..."
    dict["C"] = "-.-."
    dict["D"] = "-.."
    dict["E"] = "."
    dict["F"] = "..-."
    dict["G"] = "--."
    dict["H"] = "...."
    dict["I"] = ".."
    dict["J"] = ".---"
    dict["K"] = "-.-"
    dict["L"] = ".-.."
    dict["M"] = "--"
    dict["N"] = "-."
    dict["O"] = "---"
    dict["P"] = ".--."
    dict["Q"] = "--.-"
    dict["R"] = ".-."
    dict["S"] = "..."
    dict["T"] = "-"
    dict["U"] = "..-"
    dict["V"] = "...-"
    dict["W"] = ".--"
    dict["X"] = "-..-"
    dict["Y"] = "-.--"
    dict["Z"] = "--.."

    dict["0"] = "-----"
    dict["1"] = ".----"
    dict["2"] = "..---"
    dict["3"] = "...--"
    dict["4"] = "....-"
    dict["5"] = "....."
    dict["6"] = "-...."
    dict["7"] = "--..."
    dict["8"] = "---.."
    dict["9"] = "----."
    
    dict[" "] = " "
    dict["."] = ".-.-.-"
    dict[","] = "--..--"
    dict["?"] = "..--.."
    dict["'"] = ".----."
    dict["!"] = "-.-.--"
    dict["/"] = "-..-."
    dict["("] = "-.--."
    dict[")"] = "-.--.-"
    dict["&"] = ".-..."
    dict[":"] = "---..."
    dict[";"] = "-.-.-."
    dict["+"] = ".-.-."
    dict["="] = "-...-"
    dict["-"] = "-....-"
    dict["_"] = "..--.-"
    dict['"'] = '.-..-.'
    dict["$"] = "...-..-"
    dict["@"] = ".--.-."

def alphabet(dict):
    dict[".-"] = "A"
    dict["-..."] = "B"
    dict["-.-."] = "C"
    dict["-.."] = "D"
    dict["."] = "E"
    dict["..-."] = "F"
    dict["--."] = "G"
    dict["...."] = "H"
    dict[".."] = "I"
    dict[".---"] = "J"
    dict["-.-"] = "K"
    dict[".-.."] = "L"
    dict["--"] = "M"
    dict["-."] = "N"
    dict["---"] = "O"
    dict[".--."] = "P"
    dict["--.-"] = "Q"
    dict[".-."] = "R"
    dict["..."] = "S"
    dict["-"] = "T"
    dict["..-"] = "U"
    dict["...-"] = "V"
    dict[".--"] = "W"
    dict["-..-"] = "X"
    dict["-.--"] = "Y"
    dict["--.."] = "Z"

    dict["-----"] = "0"
    dict[".----"] = "1"
    dict["..---"] = "2"
    dict["...--"] = "3"
    dict["....-"] = "4"
    dict["....."] = "5"
    dict["-...."] = "6"
    dict["--..."] = "7"
    dict["---.."] = "8"
    dict["----."] = "9"

    dict[" "] = " "
    dict[".-.-.-"] = "."
    dict["--..--"] = ","
    dict["..--.."] = "?"
    dict[".----."] = "'"
    dict["-.-.--"] = "!"
    dict["-..-."] = "/"
    dict["-.--."] = "("
    dict["-.--.-"] = ")"
    dict[".-..."] = "&"
    dict["---..."] = ":"
    dict["-.-.-."] = ";"
    dict[".-.-."] = "+"
    dict["-...-"] = "="
    dict["-....-"] = "-"
    dict["..--.-"] = "_"
    dict['.-..-.'] = '"'
    dict["...-..-"] = "$"
    dict[".--.-."] = "@"

    


    
Texte = input("Entrez votre texte :")
Texte = Texte.upper()
Traduction = ""
morse(dict)
for lettre in Texte:
    trad = dict[lettre]
    Traduction = Traduction + trad + "/"
print(Traduction)

Code = input("Entrez le code morse :")
Code = Code.split("/")
Xtraduction = ""
alphabet(dict)
for symboles in Code:
    xtrad = dict[lettre]
    Xtraduction = Xtraduction + xtrad + "/"
print(Xtraduction)
