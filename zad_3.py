from decimal import *

from models.Flat import Flat
from models.House import House

getcontext().prec = 2

if __name__ == "__main__":
    flat = Flat(area='Area1',
                rooms=4,
                price=1999.99,
                address='Address1',
                floor=1)
    house = House(area='Area2',
                  rooms=3,
                  price=6999.99,
                  address='Address2',
                  plot=98)
    print(flat)
    print(house)
