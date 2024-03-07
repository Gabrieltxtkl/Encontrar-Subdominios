import random

words = []
counter = 0
answ = "s"
word = 0

while answ == "s":
    answ = str.lower(input("Você quer gerar uma WordList?(S/N): "))
    if answ != "s":
        print("Você não quer fazer uma wordlist e o script parou")
        break
    print("Para parar de entrar palavras digite -0")
    while word != "-0":
        counter += 1
        word = input("Digite uma palavra: ")
        if word == "-0":
            print("Você escolheu parar de entrar palavras")
            break
        else:
            words.append(word)
    senhas = int(input("Quantas palavras personalizadas você quer?: "))
    dig = int(input("Quantos caracteres você quer?: "))
    wordlist = []
    list1 = words[:]  
    list2 = words[:]  
    list1.sort(reverse=True)
    random.shuffle(list2)  
    for w in range(senhas):
        word = random.choice(list1)
        while len(word) < dig:
            word += random.choice(list2)
        wordlist.append(word)
    with open("words.txt", "w") as file:
        file.write("\n".join(wordlist)) 
