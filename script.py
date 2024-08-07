zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

summe = 0

for zahl in zahlen:
    if zahl % 2 == 0:
        summe += zahl

print("Die Summe der geraden Zahlen ist:", summe)
