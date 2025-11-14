######################################
# @Author: Nick Horn
# @Date: 14-11-2025 
# @Description: Vokabeltrainer
######################################
while True:
    # Menü anzeigen
    wahl = input("\n1=Neue Vokabeln  2=Lernen  3=Ende\nWahl: ")
    if wahl == "3":
        break
    if wahl not in ("1", "2"):
        print("Ungültige Eingabe!")
        continue

    name = input("Name der Vokabelliste: ")

    # Neue Vokabeln speichern
    if wahl == "1":
        n = int(input("Wie viele Vokabeln? "))
        with open(f"{name}.txt", "w") as f:
            for _ in range(n):
                wort = input("Wort: ")
                uebersetzung = input("Übersetzung: ")
                f.write(f"{wort}:{uebersetzung}\n")
        print("Gespeichert!")

    # Vokabeln lernen
    else:
        try:
            with open(f"{name}.txt") as f:
                paare = [line.strip().split(":", 1) for line in f if line.strip()]
        except FileNotFoundError:
            print("Datei existiert nicht.")
            continue
        korrekt = 0
        for wort, uebersetzung in paare:
            antwort = input(f"Was heisst '{wort}'? ")
            if antwort == uebersetzung: 
                korrekt += 1
                print("Richtig!")
            else:
                print("Falsch! Richtig:", uebersetzung)
        print(f"Ergebnis: {korrekt}/{len(paare)} richtig")
