lst = ["Albina", "Rifat", "Max"]

for item in lst:
    print item.rjust(10)

greetings = ["Hi", "Hola", "Privet"]
greeting = "Bonjour"

#if (!greetings.contains(greeting))
if greeting not in greetings:
    greetings.append(greeting)

print ", ".join(greetings)
print " ".join(map(lambda x: x + "!", greetings))