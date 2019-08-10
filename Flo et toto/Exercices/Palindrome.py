texte = input("Entrer en votre texte :")
texte = texte.lower()

palindrome = True

for pos in range(0,len(texte)):
    debut = texte[pos]
    fin = texte[len(texte) - 1 - pos]
    if (debut != fin):
        palindrome = False

print(palindrome)
