def readFile():
    with open("geodataSW2.txt", "r", encoding="utf-8") as f:
        Haj = []
        
        for line in f:
            a = 1
            while a != 0:
                if line.strip() != "" and not line.startswith("#"):
                    
                    if a == 1:
                        name = line
                        a=a+1

                    elif a== 2:
                         description = line
                         a=a+1

                    elif a== 3:
                        latitude = line
                        a=a+1

                    elif a == 4:
                        longitude = line
                        a=a+1

                    elif a == 5:
                        date = line
                        a=0                   
      

            Haj.append(Place(name, description, latitude, longitude, date))
                
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


print("kiss")
