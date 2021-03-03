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


# En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que
# compre. Si las computadoras son menos de cinco se les dará un 10%
# de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco pero menos de diez se le
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
# precio de cada computadora es de $11.000.


p_computadora = 11000
cantidad = int(input("Ingrese la cantidad de computadoras a comprar: "))

v_total = p_computadora*cantidad

if(cantidad < 5):
    v_pagar1 = v_total * 0.9
    print(f'El precio a pagar es: ${v_pagar1: ,}')
     
elif(cantidad >= 5 and cantidad < 10):
    v_pagar2 = v_total * 0.8
    print(f'El precio a pagar es: ${v_pagar2: ,}')
     
else:
    v_pagar3 = v_total * 0.6
    print(f'El precio a pagar es: ${v_pagar3: ,}')

# Un proveedor de estéreos ofrece un descuento del 10% sobre el
# precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
# independientemente de esto, ofrece un 5% de descuento si la marca
# es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
# cualquiera por la compra de su aparato. IVA es del 16%.

marca = input('Ingrese marca del articulo: ')
compra = int(input('Valor estereos: $'))

if(compra > 2000 and compra and marca == 'NOSY' or marca == 'nosy'):
    
    v_estereo = compra * 0.85 
    e_iva = v_estereo + (v_estereo * 0.16)
    print(f'El ciente paga: ${e_iva: ,}')

elif(compra > 2000):
     v_estereo2 = compra * 0.90 
     e_iva2 = v_estereo2 + (v_estereo2 * 0.16)
     print(f'El ciente paga: ${e_iva2: ,}') 

else:
    e_iva3 = compra + (compra * 0.16)
    print(f'El ciente paga: ${e_iva3: ,}') 

# Una empresa quiere hacer una compra de varias piezas de la misma
# clase a una fábrica de refacciones. La empresa, dependiendo del
# monto total de la compra, decidirá que hacer para pagar al fabricante.
# Si el monto total de la compra excede de $500.000 la empresa tendrá
# la capacidad de invertir de su propio dinero un 55% del monto de la
# compra, pedir prestado al banco un 30% y el resto lo pagará
# solicitando un crédito al fabricante. Si el monto total de la compra no
# excede de $500.00 la empresa tendrá capacidad de invertir de su
# propio dinero un 70% y el restante 30% lo pagará solicitando crédito
# al fabricante. El fabricante cobra por concepto de interes un 20%
# sobre la cantidad que se le pague a crédito. Obtener la cantidad a
# inverir, valor del préstamo, valor del crédito y los intereses.

n_piezas = int(input ('digite el numero de piezas que desea comprar: '))
v_pieza = int(input('diga el valor de unitario de las piezas: $'))
v_pagar = n_piezas * v_pieza
if(v_pagar > 500000):
    p_empresa = v_pagar * 0.55
    p_banco = v_pagar * 0.30
    c_fabricante = v_pagar * 0.15
    c_intereses = c_fabricante * 0.20
    print(f'el cliente pagara de su propio dinero : ${p_empresa: ,}')
    print(f'el cliente con prestamo del banco : ${p_banco: ,}')
    print(f'el cliente pagara con credito : ${c_fabricante: ,}')
    print(f'el cliente pagara por intereses del credito : ${c_intereses: ,}')

else:
    p_empresa1 = v_pagar * 0.70
    c_fabricante1 = v_pagar * 0.30
    c_intereses1 = c_fabricante1 * 0.20
    print(f'el cliente pagara de su propio dinero : ${p_empresa1: ,}')
    print(f'el cliente pagara con credito : ${c_fabricante1: ,}')
    print(f'el cliente pagara por intereses del credito : ${c_intereses1: ,}')

# Leer 2 números; si son iguales que lo multiplique, si el primero es
# mayor que el segundo que los reste y sino que los sume.

numero_1 = int(input('diga el primer numero: '))
numero_2 = int(input('diga el segundo numero: '))
if (numero_1 == numero_2):
    mult = numero_1 * numero_2
    print(f' como son iguales se multiplica y el resultado es: {mult}')

elif(numero_1 > numero_2):
    resta = numero_1 - numero_2
    print(f' numero 1 mayor que numero 2 se restan y el resultado es: {resta}')

else:
    suma = numero_1 + numero_2
    print(f' numero 1 menor que numero 2 se suman y el resultado es: {suma}')

# Leer tres números diferentes e imprimir el número mayor de los
# tres.

numero_1 = int(input('diga el primer numero: '))
numero_2 = int(input('diga el segundo numero: '))
numero_3 = int(input('diga el tercer numero: '))
if(numero_1 > numero_2 and numero_1 > numero_3):
    print(f' el mayor de los numeros es: {numero_1}')

elif(numero_2 > numero_1 and numero_2 > numero_3):
    print(f' el mayor de los numeros es: {numero_2}')

else:
    print(f' el mayor de los numeros es: {numero_3}')
