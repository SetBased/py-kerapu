Installatie
===========

Kerapu kan eenvoudig geïnstalleerd worden met pip:

.. code:: sh

    pip3 install kerapu

Voorbereiding
-------------

Alvorens gebruik te kunnen maken van Kerapu moeten de boombestanden en referentietabellen worden geconverteerd en opgeslagen. Ten tijde van schrijven van dit document was de meest recente versie van Grouper Tabellen ``v20180920``, vervang in de onderstaande tekst deze versie voor de meest recente versie.

* Download het bestand ``Grouper Tabellen v20180920`` van https://puc.overheid.nl/nza/doc/PUC_259930_22/.
* Extract de XML-bestanden uit het ZIP-bestand:

.. code:: sh

   unzip -x "20190101 Groupertabellen v20180920.zip"

* Converteer de XML-bestanden naar CSV (in het voorbeeld hieronder worden de CSV-bestanden weggeschreven in de folder ``var/lib``):

.. code:: sh

   kerapu kerapu:shredder "20190101 BoomBestanden v20180920.xml" var/lib/
   kerapu kerapu:shredder "20190101 Referenties v20180920.xml" var/lib/