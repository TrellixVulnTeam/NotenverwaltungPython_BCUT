import File
import sys
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def getDurchschnitt(noten, gewichtungen):
    summe = 0.0
    gewichtungsSumme = 0.0
    counter = 0
    for note in noten:
        summe += float(note) * float(gewichtungen[counter])
        gewichtungsSumme += float(gewichtungen[counter])
        counter += 1
    return summe/gewichtungsSumme

def getDurchschnittGerundet(noten, gewichtungen):
    summe = 0.0
    gewichtungsSumme = 0.0
    counter = 0

    for note in noten:
        summe += float(note) * float(gewichtungen[counter])
        gewichtungsSumme += float(gewichtungen[counter])
        counter += 1
    return round(2*summe / gewichtungsSumme,0)/2

def getPromotionsstatus():
    minusPunkte = 0
    plusPunkte = 0
    durchschnitte = []
    for fach in File.getFaecher():
        durchschnitte.append(getDurchschnittGerundet(File.getNotenByFach(fach), File.getGewichtungenByFach(fach)))
    for durchschnitt in durchschnitte:
        if durchschnitt < 4:
            minusPunkte += ((4 - durchschnitt) *2)
        else:
            plusPunkte += - ((4 - durchschnitt))
    print("Pluspunkte: " + str(plusPunkte))
    print("Minuspunkte: " + str(minusPunkte))
    return minusPunkte < plusPunkte

def printPromotionsstatus():
    promstatus = ""
    if getPromotionsstatus():
        promstatus = "Bestanden"
    else:
        promstatus = "Promotion gefaehrdet (PG)"
    print("Promotionsstatus: " + promstatus + "\n")

def printDurchschnitte():
    for fach in File.getFaecher():
        print(fach)
        print("-------------")
        print("Durchschnitt: " + str(getDurchschnitt(File.getNotenByFach(fach), File.getGewichtungenByFach(fach))))
        print("Gerundet: " + str(getDurchschnittGerundet(File.getNotenByFach(fach), File.getGewichtungenByFach(fach))))
        print("\n")

def printNoten(noten, gewichtungen):
    counter = 0
    for note in noten:
        print(note + " [Gewichtung: " + gewichtungen[counter] + "]")
        counter += 1

def programmSchleife():
    while True:
        printMenu()
        eingabe = input("\nWas möchten Sie tun? ")
        starteFunktion(eingabe)

def printMenu():
    print("Notenverwaltung")
    print("-------------------------------")
    print("(F) Fach wählen")
    print("(P) Promotionsstatus berechnen")
    print("(H) Note hinzufuegen")
    print("(L) Note loeschen")
    print("(Q) Programm beenden")

def starteFunktion(eingabe):
    if (eingabe == "F") or (eingabe == "f"):
        printFachMenu()
    elif (eingabe == "P") or (eingabe == "p"):
        printPromotionsstatus()
    elif (eingabe == "H") or (eingabe == "h"):
        noteHinzufuegen(File.printFaecher())
    elif (eingabe == "L") or (eingabe == "l"):
        noteLoeschen()
    elif (eingabe == "Q") or (eingabe == "q"):
        print("Programm wird beendet...")
        sys.exit()
    else:
        print("Eingabe war nicht gültig!\n")

def printFachMenu():
    while(True):
        #clear()
        gewaehltesFach = -2
        print("Alle Faecher")
        print("-------------------------------")
        counter = 1
        for fach in File.getFaecher():
            print("(" + str(counter) + ") " + fach)
            counter += 1
        print("(-1) Zurück")

        gewaehltesFach = int(input("Waehlen Sie ein Fach: "))
        if(gewaehltesFach == -1):
            break
        starteFachFunktion(gewaehltesFach)

def printFachFunktionsMenu():
    #clear()
    print("(D) Durchschnitt ausgeben")
    print("(N) Noten anzeigen")
    print("(H) Note hinzufügen")
    print("(Z) Zurueck")
    return input("\nWas möchten Sie tun? ")


def starteFachFunktion(fachIndex):
    if not fachIndex == -1:
        while(True):
            if fachIndex > 0:
                gewaehltesFach = File.getFaecher()[fachIndex - 1]
                #clear()
                print(gewaehltesFach)
                print("-----------------")
                funktion = printFachFunktionsMenu()
                if (funktion == "D") or (funktion == "d"):
                    print("Durchschnitt im Fach '" + gewaehltesFach + "': "+ str(getDurchschnitt(File.getNotenByFach(gewaehltesFach), File.getGewichtungenByFach(gewaehltesFach))))
                    print("gerundeter Durchschnitt: "+ str(getDurchschnittGerundet(File.getNotenByFach(gewaehltesFach), File.getGewichtungenByFach(gewaehltesFach))))
                elif (funktion == "N") or (funktion == "n"):
                    print(gewaehltesFach + "\n-------------------------------")
                    printNoten(File.getNotenByFach(gewaehltesFach), File.getGewichtungenByFach(gewaehltesFach))
                elif (funktion == "H") or (funktion == "h"):
                    noteHinzufuegen(gewaehltesFach)
                elif (funktion == "Z") or (funktion == "z"):
                    break
            elif fachIndex == -1:
                printFachMenu()
            elif fachIndex == -2:
                print("Eingabe war nicht korrekt!")
                printFachFunktionsMenu()

def noteHinzufuegen(fach):
    if not fach == "geheZurueck":
        print("Note hinzufuegen")
        print("------------------")
        note = input("Note: ")
        if fach == "keinFachGewaehlt":
            fach = input("Fach: ")
        datum = input("Datum: ")
        gewichtung = input("Gewichtung: ")
        File.addNote(note, fach, datum, gewichtung)

def noteLoeschen():
    print("Note loeschen")
    print("------------------")
    File.deleteNote(File.printNoten())

printDurchschnitte()
printPromotionsstatus()
programmSchleife()
