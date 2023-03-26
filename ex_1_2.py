unique_objects = []

for obj in objects:  # доступная переменная objects
    if obj not in unique_objects:
        unique_objects.append(obj)

print(len(unique_objects))
