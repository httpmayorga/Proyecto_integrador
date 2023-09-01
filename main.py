import readchar
nombre=input()
print("Bienvenido "+ nombre + " al laberinto de la anaconda")


while True:
    key = readchar.readkey()
    print(f'Tecla presionada: {key}')
    if key == '\x1b[A':  # Esto representa la tecla "UP"
        break

print('Programa terminado.')
