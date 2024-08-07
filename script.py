# Definieren einer Liste von Zahlen
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialisieren einer Variablen, um die Summe der geraden Zahlen zu speichern
summe_gerade = 0

# Schleife durch jede Zahl in der Liste
for zahl in zahlen:
    # Überprüfen, ob die Zahl gerade ist
    if zahl % 2 == 0:
        # Die gerade Zahl zur Summe hinzufügen
        summe_gerade += zahl

# Das Ergebnis ausgeben
print("Die Summe der geraden Zahlen ist:", summe_gerade)
