def desenhar_oval(largura, altura):
    for y in range(-altura, altura + 1):
        for x in range(-largura, largura + 1):
            # Equação de uma elipse: (x/a)^2 + (y/b)^2 <= 1
            if (x / largura) ** 2 + (y / altura) ** 2 <= 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Quebra de linha ao final de cada linha

# Dimensões do oval
largura = int(input("Digite a largura da oval: "))
altura = int(input("Digite a altura da oval: "))

print("Desenhando o oval:")
desenhar_oval(largura, altura)
input()