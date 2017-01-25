Kerapu
======

Een implementatie van de Grouper in Python.

|Scrutinizer Code Quality| |Build Status|

.. |Scrutinizer Code Quality| image:: https://scrutinizer-ci.com/g/SetBased/py-kerapu/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/SetBased/py-kerapu/?branch=master
.. |Build Status| image:: https://scrutinizer-ci.com/g/SetBased/py-kerapu/badges/build.png?b=master
   :target: https://scrutinizer-ci.com/g/SetBased/py-kerapu/build-status/master


Installatie
===========

Kerapu kan eenvoudig geinstalleeerd worden met pip:

.. code:: sh

  pip3 install kerapu

Voorbereiding
=============

Alvorens gebruik te kunnen maken van Kerapu moeten de boombestanden en referentietabellen worden geconverteerd  en opgeslagen. Ten tijde van schrijven van dit document was de meest recente versie van Grouper Tabellen ``v20161117``, vervang in de onderstaande tekst deze versie voor de meest recente versie.

* Download het bestand ``Grouper Tabellen v20161117`` van http://werkenmetdbcs.nza.nl/zz-releases/algemeen-4/nu-geldende-documenten/menu-id-1954.
* Extract de XML-bestanden uit het ZIP-bestand:

.. code:: sh

   unzip -x "20170101 Grouper Tabellen v20161117.zip"
   
* Converteer de XML-bestanden naar CSV (in het voorbeeld hieronder worden de CSV-bestanden weggeschreven in de folder ``var/lib``):

.. code:: sh

   kerapu shredder "20170101 BoomBestanden v20161117.xml" var/lib/
   kerapu shredder "20170101 Referenties v20161117.xml" var/lib/
   
Voorbeeld
=========

Hieronder een voorbeeld 

.. code:: python

   from kerapu.Kerapu import Kerapu
   from kerapu.Lbz.Subtraject import Subtraject

   # Maak Grouper object en laad boom- en referentietabellen.
   grouper = Kerapu()
   grouper.init_static('var/lib')

   # Maak een subtraject object.
   subtraject = Subtraject('1',
                           '0303',
                           '0280',
                           '11',
                           '000',
                           '2012-01-01',
                           '2000-01-01',
                           'M')

   # Voeg uitgevoerde zorgactiviteiten toe aan het subtraject.
   subtraject.add_zorg_activiteit('038940', 1)
   subtraject.add_zorg_activiteit('038941', 1)
   subtraject.add_zorg_activiteit('190012', 1)
   subtraject.add_zorg_activiteit('190015', 1)

   # Bepaal zorgproductgroep en zorgproduct.
   zorg_product_groep_code = grouper.bepaal_zorg_product_groep(subtraject)
   if zorg_product_groep_code != '0':
       zorg_product_code = grouper.bepaal_zorg_product(subtraject, zorg_product_groep_code)
       print('Zorgproductcode: {}'.format(zorg_product_code))


