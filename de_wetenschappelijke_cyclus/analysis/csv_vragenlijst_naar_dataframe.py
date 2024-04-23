"""
Python programma om de data uit een .csv bestand te halen
Datum: 23-04-2024
Versie: 0
"""
import sys


def lees_csv():
    data_lijst = [] # de lijst met mensen die de vragenlijst ingevuld hebben en de waarden die daarbij horen. 
    with open(sys.argv[1]) as data:
        next(data)
        next(data) # skip de eerste twee regels, hier zit niets belangrijks. 
        for i in data:
            i = i.strip()
            i = i.split(";")
            data_lijst.append(i)
    return data_lijst

def verwerk_data(data_lijst):
    for i in data_lijst:
        print(f"Persoon nummer: {i[0]} ingevuld op: {i[1]}, antwoord op test_vraag_1: {i[5]} etc.")


if __name__ == "__main__":
    data_lijst = lees_csv()
    verwerk_data(data_lijst)