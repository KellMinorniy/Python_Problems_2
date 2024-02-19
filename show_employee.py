def show_employee(name, salary=100000):
    return f"{name}: {salary}р."


print(show_employee("Иванов Иван Иванович",  30000))
print(show_employee("Артемов Артем Артемович"))