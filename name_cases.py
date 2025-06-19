
name = input("Введите ваше имя: ")
name = name.strip()
name = name.title()
print(f"Здравствуйте, {name}, не хотите ли вы изучить Python сегодня?")
print(name.upper())
print(name.lower())
print(name.title())
print('Альберт Эйнштейн однажды сказал: "Тот, кто никогда не совершал ошибок, никогда не пробовал ничего нового".')
famous_person = "Альберт Эйнштейн"
print(famous_person, 'однажды сказал: "Тот, кто никогда не совершал ошибок, никогда не пробовал ничего нового".')
famous_person2 = "Альберт Эйнштейн\tАльберт Эйнштейн\nАльберт Эйнштейн\tАльберт Эйнштейн\nАльберт Эйнштейн    "
print(famous_person2)
famous_person2 = famous_person2.title()
print(famous_person2)
famous_person2 = famous_person2.strip()
print(famous_person2)
filename = "python_notes.txt"
filename =  filename.removesuffix(".txt")
print(filename)
print(0.2+0.2)