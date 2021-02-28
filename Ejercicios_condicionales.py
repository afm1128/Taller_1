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
    print(f'en valor de la cuota del cliente es: ${v_cuota1: ,} ')
else:
    v_cuota2 = v_monto * 0.03
    print(f'en valor de la cuota del cliente es: ${v_cuota2: ,} ')



# 
