nome = input("Digite o nome do produto")
preco = int(input("Digite o preço"))

if(preco < 0):
    print(f"Esse não é um preço valido")
elif(preco <= 50):
    print(f"o {nome} tem um valor considerado baixo. O Valor dele é {preco} reais")
elif(preco <= 100):
    print(f"O {nome} tem um valor considerado médio. O Valor dele é {preco} reais")
else:
    print(f"O {nome} tem um valor considerado Alto. O Valor dele é {preco} reaissss")


