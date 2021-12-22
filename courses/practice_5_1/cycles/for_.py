"""
for element in range():
    if check0: break
    if check0: continue
    pass
else:
    pass


range - производит серию последовательно  возрастающих целых чисел, которые
        могут использоваться в качестве индексов в цикле for.
zip - возвращает серию кортежей из параллельных элементов, которые могут
      применяться для обхода множества последовательностей в цикле for.
enumerate - генерирует значения и индексы элементов в итерируемом объекте
mар  - обычно принимает функцию и один или более аргументов последовательностей
       и накапливает результаты, вызывая функцию с параллельными элементами,
       которые извлекаются из последовательности (последовательностей)

"""

print(list(range(5, -5, -1)))

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8, 9]

print(list(zip(l1, l2)))

name = list(" урсов Rндрей DdD".strip().lower().replace('r', 'А').replace('ddd', 'Викторович').title())
name.sort()
name = set(name)

dict_name_one = {}
for i in name:
    dict_name_one[i] = ord(i)


print(dict_name_one == {zip(name, map(ord, name))})
print(dict_name_one == dict(zip(name, map(ord, name))))

S = 'spam'

offset = 0
for item in S:
    print(item, 'appears at offset', offset)
    offset += 1


offset = 0
for offset, item in enumerate(S):
    print(item, 'appears at offset', offset)
