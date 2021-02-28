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
print(f'el monto de la bonificacion por hijos es de: ${bonificacion}: ,')
print(f'salario total del empleado es: ${s_total}: ,')

# Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.


