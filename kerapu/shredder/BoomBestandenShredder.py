"""
Kerapu
"""
from lxml import etree

from kerapu.shredder.Shredder import Shredder


class BoomBestandenShredder(Shredder):
    """
    Klasse voor het schreden en opslaan in CSV-formaat van boombestanden opgeslagen in XML-formaat.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def shred_xml_file(self, filename):
        """
        Slaat de boombestanden op in CSV-formaat.

        :param str filename: De filenaam van het XML bestand.
        """
        self._io.title('Shredder')

        doc = etree.parse(filename)

        xpath = '/soapenv:Envelope/soapenv:Body/InlezenBoomBestanden/BoomBestanden/'
        namespaces = {'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/'}

        # Extract beslis regels.
        table = doc.xpath(xpath + 'BeslisRegels/BeslisRegel', namespaces=namespaces)
        fields = ['BeslisRegelId',
                  'AttribuutGroepId',
                  'BeslisRegelTrue',
                  'BeslisRegelFalse',
                  'LabelTrue',
                  'LabelFalse',
                  'IndicatieAanspraakbeperking',
                  'VersieDatum']
        self.extract_table(table, 'BeslisRegels.csv', fields, fields)

        # Extract attribuut groep.
        table = doc.xpath(xpath + 'AttribuutGroepen/AttribuutGroep', namespaces=namespaces)
        fields = ['AttribuutGroepId',
                  'AttribuutGroepOmschrijving',
                  'AantalVoorwaardenVoorTrue',
                  'VersieDatum']
        self.extract_table(table, 'AttribuutGroepen.csv', fields, fields)

        # Extract attribuut groep koppeling.
        table = doc.xpath(xpath + 'AttribuutGroepKoppelingen/AttribuutGroepKoppeling', namespaces=namespaces)
        fields = ['AttribuutGroepKoppelingId',
                  'AttribuutGroepId',
                  'AttribuutId',
                  'AttribuutToetsWijze',
                  'OnderToetsWaarde',
                  'BovenToetsWaarde',
                  'VersieDatum']
        self.extract_table(table, 'AttribuutGroepKoppelingen.csv', fields, fields)

        # Extract attributen
        table = doc.xpath(xpath + 'Attributen/Attribuut', namespaces=namespaces)
        fields = ['AttribuutId',
                  'AttribuutOmschrijving',
                  'BoomParameterNummer',
                  'FilterToetsWijze',
                  'FilterWaardeType',
                  'OnderFilterWaarde',
                  'BovenFilterWaarde',
                  'VersieDatum']
        self.extract_table(table, 'Attributen.csv', fields, fields)

        # Extract boomparameters.
        table = doc.xpath(xpath + 'BoomParameters/BoomParameter', namespaces=namespaces)
        fields = ['BoomParameterNummer',
                  'Omschrijving',
                  'TabelNaam',
                  'VeldNaam']
        self.extract_table(table, 'BoomParameters.csv', fields, fields)

# ----------------------------------------------------------------------------------------------------------------------
