# Definieren einer Liste von Zahlen
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialisieren einer Variablen, um die Summe der ungeraden Zahlen zu speichern
summe_ungerade = 0

# Schleife durch jede Zahl in der Liste
for zahl in zahlen:
    # Überprüfen, ob die Zahl ungerade ist
    if zahl % 2 != 0:
        # Die ungerade Zahl zur Summe hinzufügen
        summe_ungerade += zahl

# Das Ergebnis ausgeben
print("Die Summe der ungeraden Zahlen ist:", summe_ungerade)
