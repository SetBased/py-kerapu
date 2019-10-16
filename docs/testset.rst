Testset
=======

De grouperbestanden bevatten sinds 2019 een testset. Deze testset is terug te vinden in bestand ``var/lib/testset.csv`` en zijn een onderdeel van de unittesten van Kerapu.

Het commando voor het converteren van de XML-bestanden met test data is:

.. code:: sh

   ./bin/kerapu kerapu:test-shredder ~/Downloads/20190101\ Testset\ Grouper\ RZ19b\ v20180920.zip  test/var/lib/testset.csv
