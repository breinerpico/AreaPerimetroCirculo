import math

#input
r = input("ingrese el radio")
r = int(r)

# processing 
a = math.pi * r**2
P = 2 * math.pi * r

# output 
print("El area es: " + str(a))
print("El perimetro es: " + str(P))
