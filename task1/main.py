import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (станції метро)
stations = ["Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська", "Шулявська", "Політехнічний інститут", 
            "Вокзальна", "Університет", "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк", "Лівобережна",
            "Дарниця", "Чернігівська", "Лісова",
            "Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка", "Контрактова площа", 
            "Поштова площа", "Майдан Незалежності", "Площа Льва Толстого", "Олімпійська", "Палац Україна", 
            "Либідська", "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр", "Іподром", "Теремки",
            "Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац Спорту", "Кловська", "Печерська", 
            "Дружби народів", "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", "Червоний Хутір"]

G.add_nodes_from(stations)

# Додавання ребер (маршрути між станціями)
edges = [("Академмістечко", "Житомирська"), ("Житомирська", "Святошин"), ("Святошин", "Нивки"), ("Нивки", "Берестейська"),
         ("Берестейська", "Шулявська"), ("Шулявська", "Політехнічний інститут"), ("Політехнічний інститут", "Вокзальна"),
         ("Вокзальна", "Університет"), ("Університет", "Театральна"), ("Театральна", "Хрещатик"), ("Хрещатик", "Арсенальна"),
         ("Арсенальна", "Дніпро"), ("Дніпро", "Гідропарк"), ("Гідропарк", "Лівобережна"), ("Лівобережна", "Дарниця"),
         ("Дарниця", "Чернігівська"), ("Чернігівська", "Лісова"),
         ("Героїв Дніпра", "Мінська"), ("Мінська", "Оболонь"), ("Оболонь", "Почайна"), ("Почайна", "Тараса Шевченка"),
         ("Тараса Шевченка", "Контрактова площа"), ("Контрактова площа", "Поштова площа"), ("Поштова площа", "Майдан Незалежності"),
         ("Майдан Незалежності", "Хрещатик"), ("Площа Льва Толстого", "Олімпійська"), ("Олімпійська", "Палац Україна"),
         ("Палац Україна", "Либідська"), ("Либідська", "Деміївська"), ("Деміївська", "Голосіївська"), ("Голосіївська", "Васильківська"),
         ("Васильківська", "Виставковий центр"), ("Виставковий центр", "Іподром"), ("Іподром", "Теремки"),
         ("Сирець", "Дорогожичі"), ("Дорогожичі", "Лук'янівська"), ("Лук'янівська", "Золоті ворота"), 
         ("Золоті ворота", "Театральна"), ("Палац Спорту", "Кловська"), ("Кловська", "Печерська"), 
         ("Печерська", "Дружби народів"), ("Дружби народів", "Видубичі"), ("Видубичі", "Славутич"), 
         ("Славутич", "Осокорки"), ("Осокорки", "Позняки"), ("Позняки", "Харківська"), ("Харківська", "Вирлиця"),
         ("Вирлиця", "Бориспільська"), ("Бориспільська", "Червоний Хутір")]

G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(14, 10))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', font_size=10)
plt.title("Київський метрополітен")
plt.show()

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, deg in degree.items():
    print(f"Вершина {node}: ступінь {deg}")



