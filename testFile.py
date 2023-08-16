
from Apartment import *
from lab06 import *

# Apartment.py tests

def test_getApartmentDetails():
    a0 = Apartment(1204, 200, "bad")
    a2 = Apartment(500, 300, "average")
    a3 = Apartment(3230, 700, "excellent")
    a4 = Apartment(5523, 100, "bad")
    assert a0.getRent() == 1204
    assert a2.getRent() == 500
    assert a3.getMetersFromUCSB() == 700
    assert a4.getMetersFromUCSB() == 100
    assert a3.getCondition() == "excellent"
    assert a0.getCondition() == "bad"
    assert a0.getApartmentDetails() == "(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad"
    assert a2.getApartmentDetails() == "(Apartment) Rent: $500, Distance From UCSB: 300m, Condition: average"
    assert a3.getApartmentDetails() == "(Apartment) Rent: $3230, Distance From UCSB: 700m, Condition: excellent"
    assert a4.getApartmentDetails() == "(Apartment) Rent: $5523, Distance From UCSB: 100m, Condition: bad"

def test___gt__():
    a0 = Apartment(1204, 200, "bad")
    a2 = Apartment(500, 300, "average")
    a3 = Apartment(3230, 700, "excellent")
    a4 = Apartment(3230, 700, "bad")
    assert a0.__gt__(a2) == True
    assert a2.__gt__(a0) == False
    assert a4.__gt__(a3) == True
    assert a3.__gt__(a4) == False

def test___lt__():
    a0 = Apartment(1204, 200, "bad")
    a2 = Apartment(500, 300, "average")
    a3 = Apartment(3230, 700, "excellent")
    a4 = Apartment(3230, 700, "bad")
    assert a2.__lt__(a0) == True
    assert a3.__lt__(a4) == True
    assert a4.__lt__(a3) == False
    assert a0.__lt__(a2) == False

def test__eq__():
    a0 = Apartment(1204, 200, "bad")
    a2 = Apartment(500, 300, "average")
    a3 = Apartment(500, 300, "average")
    assert a0.__eq__(a2) == False
    assert a2.__eq__(a3) == True


# lab06.py Tests
a0 = Apartment(1115, 330, "bad")
a1 = Apartment(2000, 215, "average")
a2 = Apartment(3000, 215, "excellent")
a3 = Apartment(950, 190, "average")
a4 = Apartment(900, 200, "bad")
a5 = Apartment(500, 200, "average")
apartmentList1 = [a0, a1, a2, a3, a4, a5]

def test_lab06a():
    mergesort(apartmentList1)
    assert ensureSortedAscending(apartmentList1) == True
    assert getBestApartment(apartmentList1) == ("(Apartment) Rent: $500, Distance From UCSB: 200m, Condition: average")
    assert getWorstApartment(apartmentList1) == ("(Apartment) Rent: $3000, Distance From UCSB: 215m, Condition: excellent")
    assert getAffordableApartments(apartmentList1, 950) == ("(Apartment) Rent: $500, Distance From UCSB: 200m, Condition: average\n(Apartment) Rent: $900, Distance From UCSB: 200m, Condition: bad\n(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: average") 

a6 = Apartment(2100, 200, "average")
a7 = Apartment(2100, 200, "excellent")
a8 = Apartment(980, 113, "bad")
a9 = Apartment(1500, 225, "excellent")
a10 = Apartment(300, 50, "bad")
a11 = Apartment(80, 25, "average")
apartmentList2 = [a6, a7, a8, a9, a10, a11]

def test_lab06b():
    assert ensureSortedAscending(apartmentList2) == False
    mergesort(apartmentList2)
    assert ensureSortedAscending(apartmentList2) == True
    assert getBestApartment(apartmentList2) == ("(Apartment) Rent: $80, Distance From UCSB: 25m, Condition: average")
    assert getWorstApartment(apartmentList2) == ("(Apartment) Rent: $2100, Distance From UCSB: 200m, Condition: average")
    assert getAffordableApartments(apartmentList2, 50) == ""
    assert getAffordableApartments(apartmentList2, 100) == ("(Apartment) Rent: $80, Distance From UCSB: 25m, Condition: average")
    assert getAffordableApartments(apartmentList2, 500) == "(Apartment) Rent: $80, Distance From UCSB: 25m, Condition: average\n(Apartment) Rent: $300, Distance From UCSB: 50m, Condition: bad"



    
