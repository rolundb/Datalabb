def readFile():
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
    for x in array:
        if x.getName() == intext:
            print(x)

            
class Place:

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
        return "This is " +str(self.name)+ ". Welcome! This is a " +str(self.description)+ " place."

def main():

    all_places = readFile()
    print(all_places)
    intext = input("Skriv ett land: ")
    findPlace(intext, all_places)
    


main()
