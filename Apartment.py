# containing class definition for Apartment object

class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition 

    def getApartmentDetails(self):
        '''returns a str with all of the Apartment attributes'''
        return("(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(self.rent, self.metersFromUCSB, self.condition))

    def __gt__(self, other):
        cond = ['excellent', 'average', 'bad']
        if self.rent > other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB > other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
               if cond.index(self.condition) > cond.index(other.condition):
                    return True
               else:
                    return False
            else:
                return False
        else:
            return False
            
    def __lt__(self, other):
        cond = ['excellent', 'average', 'bad']
        if self.rent < other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB < other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                if cond.index(self.condition) < cond.index(other.condition):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
                
    def __eq__(self, other):
        if self.rent == other.rent and self.metersFromUCSB == other.metersFromUCSB and self.condition == other.condition:
            return True
        else:
            return False

##a0 = Apartment(1204, 200, "bad")
##a1 = Apartment(1000, 200, "excellent")
##a2 = Apartment(1000, 200, "bad")

##a3 = Apartment(1200, 500, "average")
####a4 = Apartment(1200, 500, "average")
##a3 = Apartment(3230, 700, "excellent")
##a4 = Apartment(3230, 700, "bad")
##print(a4 > a3)
##print(a3 > a4)
####print(a0.getApartmentDetails())
### check rent, if the same rent, check meters, if same, check condition 
