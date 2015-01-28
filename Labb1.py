def readFile():
    with open("geodataSW2.txt", "r", encoding="utf-8") as f:
        Haj = []
        for line in f:
            if line.strip() != "" and not line.startswith("#"):
                for a in range(6):
                    if a == 1:
                        name = line
                    elif a == 2:
                        description = line
                    elif a == 3:
                        latitude = line
                    elif a == 4:
                        longitude = line
                    elif a == 5:
                        date = line

                Haj.append(Place(name, description, latitude, longitude, date))
                
            else:
                None
    return Haj

            
class Place:

    def __init__(self, name, description, latitude, longitude, date):
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.date = date


    def getName(self):
        '''Returnerar namnet på platsen'''
        return self.name

    def getLongitude(self):
        return int(self.longitude)
        
        
    def __str__(self):
        return "This is " +str(self.name)+ ". Welcome! This is a " +str(self.description)+ " place."

def main():

    all_places = readFile()
    print(all_places[1])
    print("poop")


main()
