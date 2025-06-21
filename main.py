print("Часть 1: List")
films = ["1+1", "Зеленая книга", "Гладиатор," "Тайна Коко", "Районы", "Патруль"]
print(films)
films.remove("Зеленая книга")
print(films)
print("\n ")
print("Часть 2: Tuple")
# Кортеж с днями недели
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# Первый и последний день
print(days[0])     # Первый
print(days[-1])    # Последний
# Индекс Wednesday
print(days.index("Wednesday"))
print("\n ")
print("Часть 3: Dict")
book = {
        "Title": "Маленький принц",
        "Author":"Антуан де Сент-Экзюпери",
        "Year": "1943",
        "Genre": "сказка-притча"
}
print(book)
Title = book.get("Title", "guest")
print(Title)
Author = book.get("Author", "guest")
print(Author)
Year = book.get("Year", "guest")
print(Year)
Genre = book.get("Genre", "guest")
print(Genre)
print("\n ")
print("Часть 4: Set")
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)
print(my_set)
my_set.discard(3)
print(my_set)
my_set.add(7)
print(my_set)
my_set.add(8)
print(my_set)