from prettytable import PrettyTable
from math import fabs

def f(x, y):
	return x**2 + y**2

def pikar_1(x):
	return 1/3*(x**3)

def pikar_2(x):
	return 1/3*(x**3) + \
		   1/54*(x**7)

def pikar_3(x):
	return 1/3*(x**3) + \
		   1/54*(x**7) + \
		   1/810*(x**11) + \
		   1/40824*(x**15)

def pikar_4(x):
	return (
			1/3*(x**3) +
			1/63*(x**7) +
			1/891*(x**11) +
			1/135*(x**15)*(1/324+1/135) +
			1/171*(x**19)*(1/6804+1/2430) +
			1/207*(x**23)*(1/122472+1/72900) +
			1/49601160*(x**27) +
			1/5740507584*(x**31)
			)



def pikar(x0, x1, h):
	result1 = list()
	result2 = list()
	result3 = list()
	result4 = list()

	while fabs(x0 - x1) > EPS:
		result1.append(round(pikar_1(x0), ROUNDED_NUM))
		result2.append(round(pikar_2(x0), ROUNDED_NUM))
		result3.append(round(pikar_3(x0), ROUNDED_NUM))
		result4.append(round(pikar_4(x0), ROUNDED_NUM))

		x0 += h

	return [result1, result2, result3, result4]

def floatrange(a, b, h):
	result = list()
	while fabs(a - b) > 1e-5:
		a += h
		a = round(a, 4)
		result.append(round(a, ROUNDED_NUM))
	return result

def euler_simple(x0, x1, h):
	result = list()

	# x0 -> a
	# x1 -> b
	# h  -> step

	yk = 0
	while fabs(x0 - x1) > EPS:
		x0 += h
		yk += f(x0, yk) * h


		result.append(round(yk, ROUNDED_NUM))

	return result

def euler_imprv(x0, x1, h):
	result = list()

	# x0 -> a
	# x1 -> b
	# h  -> step

	yk = 0
	while fabs(x0 - x1) > EPS:

		tmp = yk + f(x0 + h , yk) * h
		yk += (f(x0, yk) + f(x0 + h, tmp)) * h * 0.5
		x0 += h

		result.append(round(yk, ROUNDED_NUM))

	return result

def rounge_kutt2(x0, x1, h, alpha):
	y = 0
	result = list()

	while fabs(x0 - x1) > EPS:
		y = (
				y +
				h * ((1 - alpha) * f(x0, y) +
					 alpha * f(x0 + h / (2 * alpha), y + (h / (2 * alpha)) * f(x0, y)))
			)

		x0 += h
		result.append(round(y, ROUNDED_NUM))

	return result

def rounge_kutt4(x0, x1, h):
    solutions = []
    y = 0

    while fabs(x1 - x0) > EPS:
        k1 = f(x0, y)
        k2 = f(x0 + h / 2, y + h / 2 * k1)
        k3 = f(x0 + h / 2, y + h / 2 * k2)
        k4 = f(x0 + h, y + h * k3)

        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 += h
        solutions.append(round(y, ROUNDED_NUM))

    return solutions


if __name__ == '__main__':
	EPS = 1e-6
	ROUNDED_NUM = 11

	a = 1
	b = 2
	h = 0.01
	alpha = 1

	# a = float(input("Введите левую границу: "))
	# b = float(input("Введите правую границу: "))
	# h = float(input("Введите шаг: "))
	# alpha = float(input("Введите коэфф. alpha: "))

	pikar_res = pikar(a, b, h)
	euler_simple = euler_simple(a, b, h)
	euler_imprve = euler_imprv(a, b, h)
	rk_res2 = rounge_kutt2(a, b, h, alpha)
	rk_res4 = rounge_kutt4(a, b, h)


	table = PrettyTable()
	table.add_column(fieldname = "x", column = floatrange(a, b, h))

	table.add_column(fieldname = "Пикар^1", column = pikar_res[0])
	table.add_column(fieldname = "Пикар^2", column = pikar_res[1])
	table.add_column(fieldname = "Пикар^3", column = pikar_res[2])
	table.add_column(fieldname = "Пикар^4", column = pikar_res[3])

	table.add_column(fieldname="Эйлера ", column = euler_simple)
	table.add_column(fieldname="Эйлер улучш.", column = euler_imprve)

	table.add_column(fieldname="Рунге-Кутты 2", column = rk_res2)
	table.add_column(fieldname="Рунге-Кутты 4", column=rk_res4)
	print(table)

	# pik3 = pikar_3(a)
	# pik4 = pikar_4(a)



	# print(a)
	# print(pik3)
	# print(pik4)
	#
	# while fabs(pik3 - pik4) < EPS:
	# 	a += h
	# 	pik3 = pikar_3(a)
	# 	pik4 = pikar_4(a)
	# 	print(a)
