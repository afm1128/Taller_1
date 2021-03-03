# Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.

i_socio1 = int(input('diga la cantidad de dinero invertido por el socio 1: $'))

i_socio2 = int(input('diga la cantidad de dinero invertido por el socio 2: $'))

i_socio3 = int(input('diga la cantidad de dinero invertido por el socio 3: $'))

t_inversion = i_socio1 + i_socio2 + i_socio3

p_socio1 = (i_socio1 / t_inversion) * 100

p_socio2 = (i_socio2 / t_inversion) * 100

p_socio3 = (i_socio3 / t_inversion) * 100

print(f'el porcentaje del socio 1 es: {p_socio1}%')

print(f'el porcentaje del socio 2 es: {p_socio2}%')

print(f'el porcentaje del socio 3 es: {p_socio3}%')


# Una empresa paga a sus empleados además del sueldo base una
# bonificación especial de $80.000 por cada hijo. Realice un programa
# en python que determine el monto de la bonificación y el monto total a
# pagar al trabajador.


s_base = int(input('digite el salario base del empleado: $'))
n_hijos = int(input('diga el numero de hijos del empleado: '))
bonificacion = n_hijos * 80000
s_total = s_base + bonificacion
print(f'el monto de la bonificacion por hijos es de: ${bonificacion: ,}')
print(f'salario total del empleado es: ${s_total}: ,')

# Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.


m_ahorrado = int(input('diga el monto inicial ahorrado: $'))
s_final = m_ahorrado + (m_ahorrado * 0.015)
print(f'el saldo final es: ${s_final: ,}')


# Una inmobiliria vende terrenos a $80.000 el metro cuadrado. El
# cliente debe dar una cuota inicial del 35%y el resto lo paga en 12
# cuotas. Determine el valor a pagar por cuota inicial y el monto de
# cada cuota.

m_comprados = float(input('diga en numero de metros cuadrados comprados: '))

v_terreno = m_comprados * 80000

v_ctainicial = v_terreno * 0.35

v_ctamensual = (v_terreno - v_ctainicial) / 12

print(f'el valor de la cuota inicial es: {v_ctainicial: ,}')
print(f'el valor de la cuotas mensuales es: {v_ctamensual: ,}')


# Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# programa en Java que determine el monto de cada descuento y el
# monto total a pagar al trabajador.

sueldo = int(input("Ingrese el sueldo base del trabajador: $"))

descuento_ley = sueldo *0.01
descuento_seguro_social = sueldo * 0.04
descuento_seguro_forzoso = sueldo * 0.005
descuento_caja = sueldo * 0.05

print(f"Descuento de politica publica: ${descuento_ley: ,}")
print(f"Descuento de seguro social: ${descuento_seguro_social: ,}")
print(f"Descuento de seguro forzoso: ${descuento_seguro_forzoso: ,}")
print(f"Descuento por caja de ahorro: ${descuento_caja: ,}")
sueldo_total = sueldo - (descuento_ley + descuento_seguro_social + descuento_seguro_forzoso + descuento_caja)

print(f"El monto toal a pagar es: ${sueldo_total: ,}")

# El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.
print("Datos para un aviso clasificado")

palabras = int(input("Ingresar el numero de palabras: "))
tamaño = int(input("Ingresa el tamaño(cm): "))
colores = int(input("Ingresa el numero de colores: "))

v_palabras = palabras * 20000
v_tamaño = tamaño * 15000
v_colores = colores * 25000

t_pagar = v_palabras + v_tamaño + v_colores

print(f"El monto a pagar por un aviso clasificado es: ${t_pagar: ,}")

# Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un programa en Java que determine el monto
# del bono a pagar a un trabajador que tiene varios años en la empresa.

años = int(input("Ingrese la cantidad de años laborales: "))
bprimer_año = 100000
b_años = (años - 1) * 120000

t_bono = bprimer_año + b_años
print(f"El bono a pagar al trabajador es: ${t_bono: ,}")

# Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.

horas = int(input("Ingrese la cantidad de horas: "))

descuento = (horas*20000) * 0.05
t_horas = (horas * 20000) - descuento
print(f"Descuento por concepto de caja de ahorro: ${descuento}")

print(f"El monto total a pagar es: ${t_horas: ,}")

# Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.
