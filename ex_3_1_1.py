s = input()
a = input()
b = input()

counter = 0

while a in s:
    s = s.replace(a, b)
    counter += 1
    if counter == 1000:
        break

print(counter) if counter < 1000 else print("Impossible")
