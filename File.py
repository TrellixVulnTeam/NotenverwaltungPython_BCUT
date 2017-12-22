import csv
import os

dateipfad = "NotenDaten.csv"

def getFaecher():
    with open(dateipfad, newline='') as datei:
        reader = csv.reader(datei, delimiter=";")
        faecher = []
        for zeile in reader:
            counter = 0
            for spalte in zeile:
                # Ein Eintrag enthält: Note, Fach, Datum, Gewichtung
                if counter == 1:
                    if not spalte in faecher:
                        faecher.append(spalte)
                counter += 1
        return faecher

def getNotenByFach(fachname):
    with open(dateipfad, newline='') as datei:
        reader = csv.reader(datei, delimiter=";")
        noten = []
        for zeile in reader:
            counter = 0
            for spalte in zeile:
                # Ein Eintrag enthält: Note, Fach, Datum, Gewichtung
                if counter == 1:
                    if str(spalte) == fachname:
                        noten.append(zeile[0])
                counter += 1
        return noten

def getGewichtungenByFach(fachname):
    with open(dateipfad, newline='') as datei:
        reader = csv.reader(datei, delimiter=";")
        gewichtungen = []
        for zeile in reader:
            counter = 0
            for spalte in zeile:
                # Ein Eintrag enthält: Note, Fach, Datum, Gewichtung
                if counter == 1:
                    if str(spalte) == fachname:
                        gewichtungen.append(zeile[3])
                counter += 1
        return gewichtungen

def printFaecher():
    print("Fach auswaehlen")
    print("-------------------------------")
    counter = 1
    faecher = []
    for fach in getFaecher():
        faecher.append(fach)
        print("(" + str(counter) + ") " + fach)
        counter += 1
    print("(-1) Zurück")
    print("(-2) Eigenes Fach")

    wahl = int(input("Wählen Sie ein Fach aus: "))
    if wahl > 0:
        return faecher[wahl-1]
    elif wahl == -2:
        return "keinFachGewaehlt"
    elif wahl == -1:
        return "geheZurueck"

def printNoten():
    with open(dateipfad, newline='') as datei:
        reader = csv.reader(datei, delimiter=";")
        counter = 1
        for zeile in reader:
            # Ein Eintrag enthält: Note, Fach, Datum, Gewichtung
            print(str(counter) + ") " + zeile[1] + ": "+ zeile[0] + " - " + zeile[2] + " [Gewichtung]: " + zeile[3])
            counter += 1
        print("(-1) Zurück")
    return input("Wählen Sie eine Note zum Löschen aus: ")

def deleteNote(index):
    if not index == -1:
        # zeilenZumBehalten = ""
        index = int(index)
        os.rename(dateipfad, dateipfad+"_old")
        input = open(dateipfad + "_old", "r")
        output = open(dateipfad, "a")
        reader = csv.reader(input)
        counter = 1
        for row in reader:
            eintrag = ""
            for col in row:
                if not col == row[len(row)-1]:
                    eintrag += str(col) + ";"
                else:
                    eintrag += str(col)
            if not counter == index:
               output.write(eintrag+"\n")
            counter += 1
        input.close()
        output.close()
        os.remove(dateipfad+"_old")
        print("Note erfolgreich gelöscht!")
    else:
        print("keine Note gelöscht...")


def addNote(note, fach, datum, gewichtung):
    with open(dateipfad, "a", newline='') as datei:
        eintrag = "\n" + str(note) + ";" + fach + ";" + str(datum) + ";" + str(gewichtung)
        datei.write(eintrag)
        datei.close()
    print("Note " + str(note) + " zum Fach " + fach + " hinzugefügt.")