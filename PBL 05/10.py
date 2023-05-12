number = [2, 4, 7, 2, 3, 1, 0, 2, 6]
count = {}

for n in number:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

most_common_number = None
max_count = 0

for n, c in count.items():
    if c > max_count:
        most_common_number = n
        max_count = c

print(f"O número que aparece com mais frequência é: {most_common_number}")
