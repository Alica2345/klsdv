def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

class MyIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iter(range(self.n + 1))

    def count_down(self):
        return (i for i in range(self.n, -1, -1))

    def multiplier(self, m):
        return lambda x: x * m

iterator = MyIterator(5)

print("Итератор:", list(iterator))
print("генератор обратного отсчета:", list(iterator.count_down()))

multiplier_by_3 = iterator.multiplier(3)
print("множення на 3:", multiplier_by_3(10), multiplier_by_3(5))

@print_result
def square(x):
    return x * x

square(5)

