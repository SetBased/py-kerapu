Voorbeeld
=========

Hieronder een voorbeeld om de zorgproductcode van een subtraject af te leiden.

.. code:: python

   from kerapu.Kerapu import Kerapu
   from kerapu.lbz.Subtraject import Subtraject

   # Maak een Grouper object en laad boombestanden en referentietabellen.
   grouper = Kerapu()
   grouper.init_static('var/lib')

   # Maak een subtraject object.
   subtraject = Subtraject('1',             # Subtrajectnummer
                           '0303',          # Zorgverlenerspecificatiecode
                           '0280',          # Diagnosecode
                           '11',            # Zorgtypecode
                           '000',           # Zorgvraagcode
                           '2012-01-01',    # Begindatum subtraject
                           '2000-01-01',    # Geboortedatum
                           'M',             # Geslachtscode
                           '01234567')      # AGB-code zorginstelling

   # Voeg uitgevoerde zorgactiviteiten aan het subtraject toe.
   subtraject.add_zorg_activiteit('038940', 1)
   subtraject.add_zorg_activiteit('038941', 1)
   subtraject.add_zorg_activiteit('190012', 1)
   subtraject.add_zorg_activiteit('190015', 1)

   # Bepaal zorgproductgroep en zorgproduct.
   zorg_product_code = grouper.bepaal_zorg_product(subtraject)

   print('Zorgproductgroepcode: {}'.format(subtraject.zorg_product_groep_code))
   print('Zorgproductcode: {}'.format(subtraject.zorg_product_code))
