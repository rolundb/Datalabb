import time
from operator import attrgetter
<<<<<<< HEAD


=======
>>>>>>> origin/master

def readFile():
    """Läser in filen geodataSW2 och skapar objekt med egenskaper motsvarande fem parametrar"""
    with open("geodataSW2.txt", "r", encoding="utf-8") as f:
        array_list = []
        a=1
        for line in f:
            if line.strip() != "" and not line.startswith("#"):

                    if a == 1:
                        name = line
                        a=a+1
                    elif a == 2:
                        description = line
                        a=a+1
                    elif a == 3:
                        latitude = line
                        a=a+1
                    elif a == 4:
                        longitude = line
                        a=a+1
                    elif a == 5:
                        date = line
                        array_list.append(Place(name, description, latitude, longitude, date))
                        a=1

    return array_list

def findPlace(intext, array):
    """Går igenom listan med objekt och hittar objektet med namn motsvarande intext"""
    time_start = time.time() #Tid vid start av "sökfunktionen"
    for x in array:
        if x.getName().lower() == intext.lower(): #Om namnet för specifikt objekt matchar användarens input, kör __str__-funktion för sagda objekt.
            print(x)
    time_end = time.time() #Tid då "sökfunktionen" är klar
    time_passed = time_end-time_start #Åtgången tid
    print(time_passed)

<<<<<<< HEAD

=======
def southernPlace(array_list):
    '''Sorterar listan med objekt i storleksordning vad gäller attributet longitud, från minst till störst och skriver ut den sydligaste'''
    all_places_sorted = sorted(array_list, key=attrgetter('longitude')) 
    print(all_places_sorted[0])
    
            
>>>>>>> origin/master
class Place:
    '''Skapar en klass med attribut för namn, beskrivning, latitud, longitud och datum'''

    def __init__(self, name, description, latitude, longitude, date):
        self.name = name.strip()
        self.description = description.strip()
        self.latitude = latitude.strip()
        self.longitude = longitude.strip()
        self.date = date.strip()


    def getName(self):
        '''Returnerar namnet pÃ¥ platsen'''
        return self.name

    def getLongitude(self):
        '''Returnerar longitud fÃ¶r platsen'''
        return int(self.longitude)


    def __str__(self):
        return "This is " +str(self.name)+ ". Welcome! This is a " +str(self.description)+ " place."

def findSouthernSpot(array_list):
    test = array_list.sort(key = attrgetter('longitude'))
    print(test)


def main():

    all_places = readFile()
    intext = input("Skriv in en geografisk plats: ") #Tar emot indata som sedan blir ett ställe som matchas mot listan med object
    findPlace(intext, all_places)
<<<<<<< HEAD
    findSouthernSpot(all_places)
=======
    southernPlace(all_places)

>>>>>>> origin/master
main()
