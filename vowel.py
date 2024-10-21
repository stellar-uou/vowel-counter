print("Seja bem-vindo(a) ao programa das vogais! Digite uma palavra ou frase e o programa irá retornar quantas vogais ela tem.")

palavra = input("Digite uma palavra ou frase: ")

def contar_vogais(texto):
  vogais = "aeiouAEIOU"
  contador = 0

  for letra in texto:
    if letra in vogais:
      contador += 1

  return contador

total_vogais = contar_vogais(palavra)

print(f"O total de vogais na frase/palavra é de {total_vogais}")
