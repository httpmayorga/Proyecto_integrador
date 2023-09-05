import readchar
print("Inserte su nombre por favor")
nombre=input()
print("Bienvenido "+ nombre + " al laberinto de la anaconda")


while True:
   key = readchar.readkey()
   print(f"Tecla presionada: {key}")
   if key == readchar.key.UP:
         print("Se presionó la tecla de flecha hacia arriba. Saliendo del bucle.")
         break
    