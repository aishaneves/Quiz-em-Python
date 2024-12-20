print("bem vindo ao quiz da tecnologia da Aisha ")
answer_user= input("Deseja começar? (S/N) ")

if answer_user != "S" :
    quit()

score = 0 

print("Começando...")
print("Quem desenvolveu o Git?\n A- Guido van Rossum \n B- Chris Wanstrath \n C- Linus Torvalds \n D- N.D.A")
answer_1 = input("Resposta:")

if answer_1 == "C":
    print("A resposta está correta ")
    score = score + 1

else:
    print("A resposta está incorreta")

print("Qual das linguagens a seguir é fortimente tipada?\n A- Python \n B- Java \n C- JavaScript  \n D- PHP")
answer_2 = input("Resposta:")

if answer_2 == "B":
    print("A resposta está correta ")
    score = score + 1

else:
    print("A resposta está incorreta")


print("Quem é considerado o pai da computação ?\n A- Bill Gates \n B- Steve Jobs \n C- Charles Babbage \n D- Alan Turing")
answer_3 = input("Resposta:")

if answer_3 == "D":
    print("A resposta está correta ")
    score = score + 1

else:
    print("A resposta está incorreta")

print("Qual a principal diferença entre um HDD e um SSD ?\n A- Tamanho físico \n B- Velocidade de leitura e escrita, sendo o SSD mais rápido \n C- Capacidade de armazenamento \n D- Consumo de energia, sendo o HDD mais eficiente")
answer_4 = input("Resposta:")

if answer_4 == "B":
    print("A resposta está correta ")
    score = score + 1

else:
    print("A resposta está incorreta")


print("O que é um banco de dados?\n A- Um programa de edição de texto \n B-Um tipo de rede de computadores \n C- Um dispositivo de armazenamento externo \n SD- Uma coleção organizada de dados")
answer_5 = input("Resposta:")

if answer_5 == "D":
    print("A resposta está correta ")
    score = score + 1

else:
    print("A resposta está incorreta")


print(f"O Quiz acabou! Sua pontuação foi: {score}/5")


