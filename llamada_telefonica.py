# programa para calcular el costo de la llamada telefonica
# input

minutos = int(input("ingrese los minutos de la llamada: "))

# procesing

if minutos < 3:
    costo = 300

if minutos >= 3:
    costo = 300 + (minutos - 3) * 50








# output

print("el costo de la llamada es: ", costo)



