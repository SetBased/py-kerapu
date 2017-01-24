Kerapu
======

Een implementatie van de Grouper in Python.

|Scrutinizer Code Quality| |Build Status|

.. |Scrutinizer Code Quality| image:: https://scrutinizer-ci.com/g/SetBased/Kerapu/badges/quality-score.png?b=master&s=65d8d14cd2f09dfd62dd631b1c953098ac210426
   :target: https://scrutinizer-ci.com/g/SetBased/Kerapu/?branch=master
.. |Build Status| image:: https://scrutinizer-ci.com/g/SetBased/Kerapu/badges/build.png?b=master&s=074278b1cacd9223d21ad5cd623f283cc31febdf
   :target: https://scrutinizer-ci.com/g/SetBased/Kerapu/build-status/master


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

   unzip -x 20170101\ Grouper\ Tabellen\ v20161117.zip
   
* Converteer de XML-bestanden naar CSV (in het voorbeeld hieronder worden de CSV -bestanden weggeschreven in de folder ``var/lib``):

.. code:: sh

   kerapu shredder "20170101 BoomBestanden v20161117.xml" var/lib/
   kerapu shredder "20170101 Referenties v20161117.xml" var/lib/
   
 

