from datetime import datetime

from models.KlientBiznesowy import KlientBiznesowy
from models.KlientDetaliczny import KlientDetaliczny
from models.Magazyn import Magazyn
from models.Produkt import Produkt
from models.Zamowienie import Zamowienie

kl_detaliczny = KlientDetaliczny(1,
                                 'Imie Nazwisko',
                                 'Adres1',
                                 '333555666',
                                 True)
magazyn = Magazyn('Magazyn1',
                  1500,
                  41,
                  'Katowice',
                  kl_detaliczny)
produkt1 = Produkt('Produkt1',
                   29.99,
                   'Ubranie',
                   magazyn,
                   True)
produkt2 = Produkt('Produkt Inny',
                   199.99,
                   'Sprzęt',
                   magazyn,
                   False)
kl_biznesowy = KlientBiznesowy(1,
                               'Hurtownia 1',
                               'Adres hurtowni',
                               '114758652',
                               '635-256987')

zamowienie = Zamowienie(1,
                        [produkt1, produkt2],
                        kl_biznesowy,
                        datetime(2021, 11, 28),
                        'Pracownik 1')

print(zamowienie)
