# Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.
n_camisas = int(input('digite el numero de camisas: '))

v_camisas = int(input('digite el valor de la compra sin descuento: $'))
if n_camisas >= 3:
    descuento1 = v_camisas - (v_camisas * 0.3)
    print(f'en valor a pagar con el descuento es: ${descuento1: ,}')
else:
    descuento2 = v_camisas - (v_camisas * 0.1)
    print(f'en valor a pagar con el descuento es: ${descuento2: ,}')

# En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

n_azar = int(input('digite el numero al azar: '))
v_compra = int(input('digite el valor de la compra sin descuento: $'))
if n_azar >= 74:
    descuento1 = v_compra * 0.20
    print(f'en valor del descuento es: ${descuento1: ,} ')
else:
    descuento2 = v_compra * 0.15
    print(f'en valor del descuento es: ${descuento2: ,}')

# Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que conssite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente.

v_monto = int(input('digite el monto por el cual se efectua la finanza: $'))
if v_monto >= 50000:
    v_cuota1 = v_monto * 0.02
    print(f'el valor de la cuota del cliente es: ${v_cuota1: ,} ')
else:
    v_cuota2 = v_monto * 0.03
    print(f'el valor de la cuota del cliente es: ${v_cuota2: ,} ')


# Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.
p_dia1 = int(input('digite los puntos dia 1: '))
p_dia2 = int(input('digite los puntos dia 2: '))
p_dia3 = int(input('digite los puntos dia 3: '))
p_dia4 = int(input('digite los puntos dia 4: '))
p_dia5 = int(input('digite los puntos dia 5: '))

g_dia1 = int(input('digite las ganancias dia 1: '))
g_dia2 = int(input('digite las ganancias dia 2: '))
g_dia3 = int(input('digite las ganancias dia 3: '))
g_dia4 = int(input('digite las ganancias dia 4: '))
g_dia5 = int(input('digite las ganancias dia 5: '))

prom_puntos = (p_dia1 + p_dia2 + p_dia3 + p_dia4 + p_dia5) / 5
s_ganancias = g_dia1 + g_dia2 + g_dia3 + g_dia4 + g_dia5
if prom_puntos > 170:
    v_pagar = s_ganancias * 0.5
    print(f'el valor a pagar por la sancion es: ${v_pagar: ,} ')
else:
    
    print(f'como el promedio de puntos es menor a 170 no tendra ninguna sancion')
    
    
# Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del

v_carro = int(input('digite el valor del carro: $'))
v_terreno = int(input('digite el valor del terreno: $'))
p_devaluacion = int(input('digite el porcentaje de devaluacion anual: '))
p_incremento = int(input('digite el porcentaje de incremento anual: '))
devaluacion = v_carro * ((p_devaluacion * 3) / 100)
incremento = v_terreno * ((p_incremento * 3) / 100)

if devaluacion > incremento / 2:
   
    print(f'la persona debe comprar la casa ')
else:
    
    print(f'la persona debe comprar el carro')


