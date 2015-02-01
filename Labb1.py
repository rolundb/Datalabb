import time

from operator import attrgetter

def readFile():
    """Läser in filen geodataCH och skapar objekt med egenskaper motsvarande fem parametrar"""
    with open("geodataSW2.txt", "r", encoding="utf-8") as f:
        array_list = []
        a=1
        for line in f:
            if line.strip() != "" and not line.startswith("#"):

                    if a == 1:
                        name = line
                        a+=1
                    elif a == 2:
                        description = line
                        a+=1
                    elif a == 3:
                        latitude = line
                        a+=1
                    elif a == 4:
                        longitude = line
                        a+=1
                    elif a == 5:
                        date = line
                        array_list.append(Place(name, description, latitude, longitude, date))
                        a=1
               
    return array_list #returnerar en array med platser lagrade som objekt från klassen Place

def findPlace(intext, array):
    """Tar emot input från användaren och en lista med objekt, hittar objektet med namn motsvarande intext, och tar tid på sökningen."""
    time_start = time.time() #Tid vid start av "sökfunktionen"
    for x in array:
        if x.getName().lower() == intext.lower(): #Om namnet för specifikt objekt matchar användarens input, kör __str__-funktion för sagda objekt.
            print(x)


       #else:
            #print(intext +"could not be found, try again")
            
            
            
    time_end = time.time() #Tid då "sökfunktionen" är klar
    time_passed = time_end-time_start #Åtgången tid
    print("Time for search:" + str(time_passed))


def userData():
    """Tar emot indata som sedan blir ett ställe som matchas mot listan med object"""
    return input("Welcome to Locator! \n You can search for a location and get information about it.\n Type in a geografic location: ") 

def southernPlace(array_list):
    '''Sorterar en lista med objekt i storleksordning vad gäller attributet longitud, från minst till störst och skriver ut den sydligaste'''
    all_places_sorted = sorted(array_list, key=attrgetter('longitude')) 
    print("However, the most southern place is " + str(all_places_sorted[0]))
    

class Place:
    '''Skapar en klass med attribut för namn, beskrivning, latitud, longitud och datum'''

    def __init__(self, name, description, latitude, longitude, date):
        self.name = name.strip()
        self.description = description.strip()
        self.latitude = latitude.strip()
        self.longitude = longitude.strip()
        self.date = date.strip()


    def getName(self):
        '''Returnerar namnet på platsen'''
        return self.name

    def getLongitude(self):
        '''Returnerar longitud för platsen'''
        return int(self.longitude)
        
        
    def __str__(self):
        """Returnerar en string av argumentet name och description"""
        return  str(self.name)+ ", often refferd to as " +str(self.description)

def main():
    """mainfunktionen för programmet"""
    all_places = readFile()
    intext = userData()
    findPlace(intext, all_places)

    southernPlace(all_places)

main()
