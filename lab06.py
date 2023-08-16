# file containing mergesort and functions 

from Apartment import *

def mergesort(apartmentList):
    '''performs a mergesort on the apartmentList passed as input.
    sorts the Apartment objects based on the specifications in the introduction'''
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0 # index for the left half 
        j = 0 # index for the right half
        k = 0 # index for apartmentList

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i += 1
            else:
                apartmentList[k] = righthalf[j]
                j = j + 1
            k = k + 1
            
        # puts remaining into apartmentList
        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1
            
        # puts remaining into apartmentList
        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1 

def ensureSortedAscending(apartmentList):
    '''returns boolean value, true if apartmentList is sorted correctly in order,
    false otherwise'''
    for i in range(len(apartmentList) - 1):
        if apartmentList[i] < apartmentList[i + 1]:
            return True
        else:
            return False

def getBestApartment(apartmentList):
    '''returns str detailing the best apartment's rent, meters, condition
    make use of getApartmentDetails(self) and mergesort.'''
    mergesort(apartmentList)
    best = apartmentList[0]
    info = best.getApartmentDetails()
    return info
    

def getWorstApartment(apartmentList):
    '''returns str detailing the worst apartment's rent, meters, condition
    make use of getApartmentDetails(self) and mergesort.'''
    mergesort(apartmentList)
    worst = apartmentList[len(apartmentList)-1]
    info = worst.getApartmentDetails()
    return info

def getAffordableApartments(apartmentList, budget):
    '''returns labeled, newline separated str detailing rent, meters, condition of all
    the apartments whose rent is less than or equal to the budget from the
    apartment list in sorted order'''
    mergesort(apartmentList)
    info = ""
    for i in apartmentList:
        if i.getRent() < budget or i.getRent() == budget:
            info += i.getApartmentDetails() + "\n"
    return info[:-1]
