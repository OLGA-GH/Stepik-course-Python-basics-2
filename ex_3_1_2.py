s = input()
t = input()

s_len = len(s)
t_len = len(t)

counter = 0

if s_len >= t_len:
    for i in range(0, s_len):
        if s[i:].startswith(t):
            counter += 1

print(counter)
