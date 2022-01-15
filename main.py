from models.Developer import Developer
from models.Dom import Dom
from models.Mieszkanie import Mieszkanie
from models.Zamowienie import Zamowienie

developer = Developer("Budowniczy", "Katowice", 5000000, 555666777)
mieszkanie = Mieszkanie(219999.99, 3, 65, "gazowe")
dom = Dom(560000.74, 10, 93, 2)
list_lokum = [mieszkanie, dom]
zamowienie = Zamowienie()

zamowienie.id_zamowienia = 1
zamowienie.developer = developer
zamowienie.list_of_lokums = list_lokum
zamowienie.sposob_platnosci = "Przelew bankowy"

print(zamowienie)
