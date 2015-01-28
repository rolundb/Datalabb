def readFile():
    with open("geodataSW2.txt", "r", encoding="utf-8") as f:
        i = 0;
        for line in f:
            if line.strip() != "" and not line.startswith("#"):
                for a in range(5):
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
            else:
                None

            Place[i] = Place(name, description, latitude, longitude, date)
            i = i+1


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


objekt1 = Place("Paris", "cold", "0123123", "0102349", "20140291")

print(objekt1)

readFile()

print("haj")
