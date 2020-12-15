# Списал. Не очень понял, если честно.
class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join([str(x) for x in y]) for y in self.data])

    def __add__(self, z):
        answer = ''
        for el_1, el_2 in zip(self.data, z.data):
            summ = [ q + w for q, w in zip(el_1, el_2)]
            answer += ' '.join([str(i) for i in summ]) + '\n'
        return answer


matr_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matr_2 = Matrix([[2, 3], [4, 5], [6, 7]])

# print(matr_1)
# print(matr_2)

print(matr_1 + matr_2)