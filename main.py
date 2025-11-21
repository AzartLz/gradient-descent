def loss_funtion(x):
    return (x-3)**2

def gradient(x):
    return 2*(x-3)

def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    for i in range(num_iterations):
        grad = gradient(x)
        x = x - learning_rate*grad
        if i % 20 == 0:
            current_loss = loss_funtion(x)
            print(f"Итерация {i}: x = {x:.6f}, f(x) = {current_loss:.6f}, градиент = {grad:.6f}")
    return x


if __name__ == "__main__":
    # Параметры алгоритма
    starting_point = 0    # Начальная точка
    learning_rate = 0.1   # Шаг обучения
    num_iterations = 100  # Количество итераций
    
    print("Запуск градиентного спуска...")
    print(f"Начальная точка: {starting_point}")
    print(f"Скорость обучения: {learning_rate}")
    print(f"Количество итераций: {num_iterations}")
    
    # Запускаем градиентный спуск
    minimum = gradient_descent(starting_point, learning_rate, num_iterations)
    
    print("Результаты:")
    print(f"Найденное значение x: {minimum:.6f}")
    print(f"Значение функции в найденной точке: {loss_funtion(minimum):.6f}")
    print(f"Истинный минимум: 3.0")
    print(f"Ошибка: {abs(minimum - 3.0):.6f}")