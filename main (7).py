import math
import matplotlib.pyplot as plt


# --- Завдання 1: Числа Фібоначчі ---
def fib(n):
    """
    Обчислює N-й елемент послідовності Фібоначчі.
    """
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# Обчислення чисел Фібоначчі для заданих номерів
fib_numbers = [fib(n) for n in [5, 10, 15, 20, 25]]
print("Числа Фібоначчі:", fib_numbers)


# --- Завдання 2: Рекурентне рівняння ---
def compute_y(n, t0, t, k, xi, u):
    """
    Обчислює значення y[k] для заданих параметрів рекурентного рівняння.
    """
    y = [0, 0]  # Початкові умови: y[0] = 0, y[1] = 0
    for k in range(2, n + 1):
        coeff1 = 2 * (1 - (xi * t0) / t)
        coeff2 = 2 * (xi * t0) / t - 1 - (t0 ** 2) / (t ** 2)
        coeff3 = k * (t0 ** 2) / (t ** 2)
        y_k = coeff1 * y[k - 1] + coeff2 * y[k - 2] + coeff3 * u
        y.append(y_k)
    return y


# Параметри
T = 1
K = 1.5
xi = 2
U = 1
N = 50
T0 = T / N

# Обчислення y[k]
y_values = compute_y(N, T0, T, K, xi, U)
time_points = [k * T0 for k in range(N + 1)]

# Візуалізація
plt.figure(figsize=(8, 6))
plt.plot(time_points, y_values, label="y[k] (\u03c9, рад/с)", color="blue")
plt.title("Графік функції y[k]")
plt.xlabel("Час (с)")
plt.ylabel("y[k] (\u03c9, рад/с)")
plt.grid(True)
plt.legend()
plt.show()

# Збереження у файл
filename = "output_data.txt"
separator = ";" if 12 % 2 == 0 else "#"
with open(filename, "w") as file:
    for t, y in zip(time_points, y_values):
        file.write(f"{t}{separator}{y}\n")
print(f"Дані збережено у файл: {filename}")
