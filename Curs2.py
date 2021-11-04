variabila = 'Ana are mere'

lista = [i for i in variabila]
print(lista)

for item, value in enumerate(variabila):
    print(f"{item} => {value}")

dictionar = {"key1": "value1", "key2": "value2"}
for item in dictionar.items():
    #print(item)
    #print(key, value)
    item0, item1 = item
    print(item0, item1)

#variabila = (1)
variabila = (1,)
print(type(variabila))

variabila = "Ana \"are\" mere"
print(variabila)