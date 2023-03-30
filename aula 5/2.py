## if a note is bellow 7, ask for a new note until is 7 or above
nota = float(input("Digite uma nota: "))
while nota < 7:
    nota = float(input("Digite uma nota: "))
    print("Nota válida")


