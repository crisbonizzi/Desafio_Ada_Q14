# Solicitar ao usuário que digite a velocidade inicial, posição inicial e instante de tempo
v0 = float(input("Digite a velocidade inicial (m/s): "))
y0 = float(input("Digite a posição inicial (m): "))
t = float(input("Digite o instante de tempo (s): "))

# Aceleração da gravidade
g = -10  # m/s^2

# Calcular a posição final
y_t = y0 + v0 * t + (g * (t ** 2)) / 2

# Imprimir a posição final
print("A posição do projétil no instante de tempo t é:", y_t, "m")