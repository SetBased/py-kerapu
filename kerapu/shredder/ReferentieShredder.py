"""
Kerapu
"""
from lxml import etree

from kerapu.shredder.Shredder import Shredder


class ReferentieShredder(Shredder):
    """
    Klasse voor het schreden en opslaan in CSV-formaat van referentietabellen opgeslagen in XML-formaat.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def shred_xml_file(self, filename):
        """
        Slaat de referentietabellen op in CSV-formaat.

        :param str filename: De filenaam van het XML bestand.
        """
        self._io.title('Shredder')

        doc = etree.parse(filename)

        xpath = '/soapenv:Envelope/soapenv:Body/InlezenReferenties/Referenties/'
        namespaces = {'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/'}

        # Extract AfsluitReden.
        table = doc.xpath(xpath + 'AfsluitRedenen/AfsluitReden', namespaces=namespaces)
        fields = ['AfsluitRedenCode',
                  'AfsluitRedenOmschrijving',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'AfsluitRedenen.csv', fields, fields)

        # Extract BehandelKlasse.
        table = doc.xpath(xpath + 'BehandelKlassen/BehandelKlasse', namespaces=namespaces)
        fields = ['ZorgProductGroepCode',
                  'ZorgActiviteitCode',
                  'BehandelKlasseCode',
                  'BehandelKlasseOmschrijving',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'BehandelKlassen.csv', fields, fields)

        # Extract Diagnose.
        table = doc.xpath(xpath + 'Diagnosen/Diagnose', namespaces=namespaces)
        fields = ['SpecialismeCode',
                  'DiagnoseCode',
                  'DiagnoseOmschrijving',
                  'DiagnoseAttribuutCode',
                  'ICD10DiagnoseCode',
                  'DiagnoseCluster1',
                  'DiagnoseCluster2',
                  'DiagnoseCluster3',
                  'DiagnoseCluster4',
                  'DiagnoseCluster5',
                  'DiagnoseCluster6',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        xpaths = ['SpecialismeCode',
                  'DiagnoseCode',
                  'DiagnoseOmschrijving',
                  'DiagnoseAttribuutCode',
                  'ICD10DiagnoseCode',
                  "DiagnoseCluster/DiagnoseClusterItem[@Key='1']",
                  "DiagnoseCluster/DiagnoseClusterItem[@Key='2']",
                  "DiagnoseCluster/DiagnoseClusterItem[@Key='3']",
                  "DiagnoseCluster/DiagnoseClusterItem[@Key='4']",
                  "DiagnoseCluster/DiagnoseClusterItem[@Key='5']",
                  "DiagnoseCluster/DiagnoseClusterItem[@Key='6']",
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'Diagnosen.csv', fields, xpaths)

        # Extract Geslacht.
        table = doc.xpath(xpath + 'Geslachten/Geslacht', namespaces=namespaces)
        fields = ['GeslachtCodeNEN',
                  'GeslachtCodeHL7',
                  'GeslachtOmschrijving',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'Geslachten.csv', fields, fields)

        # Extract LimitatieMachtiging.
        table = doc.xpath(xpath + 'LimitatieMachtigingen/LimitatieMachtiging', namespaces=namespaces)
        fields = ['SpecialismeCode',
                  'DiagnoseCode',
                  'DiagnoseOmschrijving',
                  'ZorgActiviteitCode',
                  'ZorgActiviteitOmschrijving',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'LimitatieMachtigingen.csv', fields, fields)

        # Extract Specialisme.
        table = doc.xpath(xpath + 'Specialismen/Specialisme', namespaces=namespaces)
        fields = ['SpecialismeCode',
                  'SpecialismeOmschrijving',
                  'SpecialismeIndicatie',
                  'SpecialismeOID',
                  'SpecialismeCluster1',
                  'SpecialismeCluster2',
                  'IndicatieAanspraakbeperking',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        xpaths = ['SpecialismeCode',
                  'SpecialismeOmschrijving',
                  'SpecialismeIndicatie',
                  'SpecialismeOID',
                  'SpecialismeCluster/SpecialismeClusterItem[(@Key=1)]',
                  'SpecialismeCluster/SpecialismeClusterItem[(@Key=2)]',
                  'IndicatieAanspraakbeperking',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'Specialismen.csv', fields, xpaths)

        # Extract VertaalZorgActiviteit.
        table = doc.xpath(xpath + 'VertaalZorgActiviteiten/VertaalZorgActiviteit', namespaces=namespaces)
        fields = ['ZorgActiviteitCode',
                  'ZorgActiviteitOmschrijving',
                  'ZorgActiviteitCodeOud',
                  'ZorgActiviteitOmschrijvingOud',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'VertaalZorgActiviteiten.csv', fields, fields)

        # Extract ZorgActiviteit.
        table = doc.xpath(xpath + 'ZorgActiviteiten/ZorgActiviteit', namespaces=namespaces)
        fields = ['ZorgActiviteitCode',
                  'ZorgActiviteitOmschrijving',
                  'ZorgActiviteitCluster01',
                  'ZorgActiviteitCluster02',
                  'ZorgActiviteitCluster03',
                  'ZorgActiviteitCluster04',
                  'ZorgActiviteitCluster05',
                  'ZorgActiviteitCluster06',
                  'ZorgActiviteitCluster07',
                  'ZorgActiviteitCluster08',
                  'ZorgActiviteitCluster09',
                  'ZorgActiviteitCluster10',
                  'ZorgActiviteitWeegFactor1',
                  'ZorgActiviteitWeegFactor2',
                  'WBMVCode',
                  'InnovatieCode',
                  'AanspraakCode',
                  'TariefType',
                  'Zorgprofielklassecode',
                  'OpNota',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        xpaths = ['ZorgActiviteitCode',
                  'ZorgActiviteitOmschrijving',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=1]',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=2]',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=3]',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=4]',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=5]',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=6]',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=7]',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=8]',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=9]',
                  'ZorgActiviteitCluster/ZorgActiviteitClusterItem[@Key=10]',
                  'ZorgActiviteitWeegFactor/ZorgActiviteitWeegFactorItem[@Key=1]',
                  'ZorgActiviteitWeegFactor/ZorgActiviteitWeegFactorItem[@Key=2]',
                  'WBMVCode',
                  'InnovatieCode',
                  'AanspraakCode',
                  'TariefType',
                  'Zorgprofielklassecode',
                  'OpNota',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'ZorgActiviteiten.csv', fields, xpaths)

        # Extract ZorgProductGroep.
        table = doc.xpath(xpath + 'ZorgProductGroepen/ZorgProductGroep', namespaces=namespaces)
        fields = ['ZorgProductGroepCode',
                  'ZorgProductGroepOmschrijving',
                  'BeslisRegelStart',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'ZorgProductGroepen.csv', fields, fields)

        # Extract ZorgType.
        table = doc.xpath(xpath + 'ZorgTypen/ZorgType', namespaces=namespaces)
        fields = ['SpecialismeCode',
                  'ZorgTypeCode',
                  'ZorgTypeOmschrijving',
                  'ZorgTypeAttribuutCode',
                  'ZorgTypeCluster1',
                  'ZorgTypeCluster2',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        xpaths = ['SpecialismeCode',
                  'ZorgTypeCode',
                  'ZorgTypeOmschrijving',
                  'ZorgTypeAttribuutCode',
                  'ZorgTypeCluster/ZorgTypeClusterItem[(@Key=1)]',
                  'ZorgTypeCluster/ZorgTypeClusterItem[(@Key=2)]',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'ZorgTypen.csv', fields, xpaths)

        # Extract ZorgVraag.
        table = doc.xpath(xpath + 'ZorgVragen/ZorgVraag', namespaces=namespaces)
        fields = ['SpecialismeCode',
                  'ZorgVraagCode',
                  'ZorgVraagOmschrijving',
                  'ZorgVraagAttribuutCode',
                  'ZorgVraagCluster1',
                  'ZorgVraagCluster2',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        xpaths = ['SpecialismeCode',
                  'ZorgVraagCode',
                  'ZorgVraagOmschrijving',
                  'ZorgVraagAttribuutCode',
                  'ZorgVraagCluster/ZorgVraagClusterItem[(@Key=1)]',
                  'ZorgVraagCluster/ZorgVraagClusterItem[(@Key=2)]',
                  'BeginDatum',
                  'EindDatum',
                  'VersieDatum']
        self.extract_table(table, 'ZorgVragen.csv', fields, xpaths)

# ----------------------------------------------------------------------------------------------------------------------
