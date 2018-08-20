import re

def verifica_se_string_eh_ponto_flutuante(string):
    resultado = re.search(r'^[0-9+-]+\.[0-9]*$', string)
    if resultado:
        print("True")
    else:
        resultado = re.search(r'^[0-9+-]*\.[0-9]+$', string)
        if resultado:
            print("True")
        else:
            print("False")


quantidade_testes = int(input("Entre com a quantidade de testes que deseja fazer: "))
contador = 1;
lista_strings = []
for i in range(0, quantidade_testes):
    string_teste = input("Entre com a string para teste: ")
    lista_strings.append(string_teste)

for j in range(0, quantidade_testes):
    verifica_se_string_eh_ponto_flutuante(lista_strings[j])