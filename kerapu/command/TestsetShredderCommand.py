import csv
import datetime
import os
import random
import shutil
import string
import zipfile
from typing import Iterable, List, Dict

from cleo import Command
from lxml import etree

from kerapu.style.KerapuStyle import KerapuStyle


class TestShredderCommand(Command):
    """
    Converteert XML-bestand met de testset naar een CSV-bestand

    kerapu:test-shredder
        {testset-zip : ZIP-bestand met de testset}
        {testset-csv : Path waar het CSV-bestand met de tests moeten worden opgeslagen}
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __extract_zip_file(self, zip_filename: str, tmp_dir: str):
        """
        Extracts het ZIP-bestand met de testset in een folder.

        :param str zip_filename: Het path naar het ZIP-bestand met de testset.
        :param str tmp_dir: Path naar de folder.
        """
        self.output.writeln('Uitpakken van <fso>{}</fso> in <fso>{}</fso>'.format(zip_filename, tmp_dir))

        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(tmp_dir)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def ordinal(path: str) -> int:
        """
        Geeft het volgnummer van een test.

        :param str path: Het path naar het XML-bestand met de test case.
        """
        parts = os.path.basename(path).split('_')

        return int(parts[6])

    # ------------------------------------------------------------------------------------------------------------------
    def __lees_test_cases_lijst(self, folder: str) -> List:
        """
        Geeft een lijst met alle bestanden in een folder.

        :param str folder: Het path naar de folder.
        """
        entries = os.listdir(folder)
        filenames = list()
        for entry in entries:
            path = os.path.join(folder, entry)
            if os.path.isfile(path):
                filenames.append(path)

        self.output.writeln('Aantal gevonden test cases: {}'.format(len(filenames)))

        return sorted(filenames, key=TestShredderCommand.ordinal)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __maak_xpath(parts: Iterable) -> str:
        """
        Maakt een string met een xpath.

        :param tuple parts: The onderdelen van het xpath.

        :rtype: str
        """
        xpath = ''
        for part in parts:
            if xpath:
                xpath += '/'
            xpath += 'xmlns:' + part

        return xpath

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __convert_date(date: str) -> str:
        """
        Converteert een datum in YYYYMMDD formaat naar YYYY-MM-DD format.

        :param str date: De datum in YYYYMMDD format.

        :rtype: str
        """
        return date[:4] + '-' + date[4:6] + '-' + date[6:8]

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __leeftijd_geboorte_datum(date: str, leeftijd: int) -> str:
        """
        Geeft de geboortedatum gegeven een datum en een leeftijd (en de persoon is niet jarig).

        :param str date: De gegeven datum in YYYY-MM-DD format.
        :param int leeftijd: De leeftijd in jaren.

        :rtype: int
        """
        date = datetime.date(int(date[:4]) - leeftijd, int(date[5:7]), int(date[8:10]))
        date -= datetime.timedelta(days=1)

        return date.isoformat()

    # ------------------------------------------------------------------------------------------------------------------
    def __shred_xml_bestand(self, filename: str) -> Dict:
        """
        Leest de relevante data in een XML-bestand met een test case.

        :param str filename: De filenaam van het XML bestand.

        :rtype: dict
        """
        doc = etree.parse(filename)

        xpath = '/soapenv:Envelope/soapenv:Body/xmlns:FICR_IN900101NL04'
        namespaces = {'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
                      'xmlns':   'urn:hl7-org:v3'}

        # Lees declaratiecode.
        parts = ('ControlActProcess', 'subject', 'Declaratiedataset', 'component', 'subtraject', 'id')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        declaratie_code = elements[0].get('extension')

        # Lees specialismecode.
        parts = ('ControlActProcess', 'subject', 'Declaratiedataset', 'component', 'subtraject', 'derivedFrom',
                 'zorgtraject', 'responsibleParty', 'assignedPerson', 'code')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        specialisme_code = elements[0].get('code')

        # Lees diagnosecode.
        parts = (
            'ControlActProcess', 'subject', 'Declaratiedataset', 'component', 'subtraject', 'pertinentInformation1',
            'typerendeDiagnose', 'value')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        diagnose_code = elements[0].get('code')

        # Lees zorgtypecode.
        parts = ('ControlActProcess', 'subject', 'Declaratiedataset', 'component', 'subtraject', 'code')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        zorg_type_code = elements[0].get('code') if elements else None

        # Lees zorgvraagcode.
        parts = ('ControlActProcess', 'subject', 'Declaratiedataset', 'component', 'subtraject', 'derivedFrom',
                 'zorgtraject', 'reason', 'zorgvraag', 'value')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        zorg_vraag_code = elements[0].get('code') if elements else None

        # Lees begindatum.
        parts = ('ControlActProcess', 'subject', 'Declaratiedataset', 'component', 'subtraject', 'effectiveTime', 'low')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        begin_datum = self.__convert_date(elements[0].get('value')) if elements else None

        # Lees de geboortedatum van de patient.
        parts = ('ControlActProcess', 'subject', 'Declaratiedataset', 'subject', 'patient', 'subjectOf', 'leeftijd',
                 'value')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        leeftijd = int(elements[0].get('value')) if elements else None
        geboorte_datum = self.__leeftijd_geboorte_datum(begin_datum, leeftijd)

        # Lees het geslacht van de patient.
        parts = ('ControlActProcess', 'subject', 'Declaratiedataset', 'subject', 'patient', 'patientPerson',
                 'administrativeGenderCode')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        geslacht_code = elements[0].get('code') if elements else None

        # Lees de AGB-code van de zorginstelling.
        parts = ('ControlActProcess', 'subject', 'Declaratiedataset', 'author', 'assignedOrganization', 'id')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        zorg_instelling_code = elements[0].get('extension') if elements else None

        # Lees alle zorgactiviteiten.
        zorg_activiteiten = list()
        parts = ('ControlActProcess', 'subject', 'Declaratiedataset', 'component', 'subtraject', 'debit',
                 'zorgactiviteit')
        elements = doc.xpath(xpath + '/' + self.__maak_xpath(parts), namespaces=namespaces)
        for element in elements:
            path = 'xmlns:code'
            sub_elements = element.xpath(path, namespaces=namespaces)
            zorg_activiteit_code = sub_elements[0].get('code') if sub_elements else None

            path = 'xmlns:repeatNumber'
            sub_elements = element.xpath(path, namespaces=namespaces)
            aantal = int(sub_elements[0].get('value')) if sub_elements else None

            zorg_activiteiten.append((zorg_activiteit_code, aantal))

        return {'subtraject_nummer':    os.path.basename(filename),
                'declaratie_code':      declaratie_code,
                'specialisme_code':     specialisme_code,
                'diagnose_code':        diagnose_code,
                'zorg_type_code':       zorg_type_code,
                'zorg_vraag_code':      zorg_vraag_code,
                'begin_datum':          begin_datum,
                'geboorte_datum':       geboorte_datum,
                'geslacht_code':        geslacht_code,
                'zorg_instelling_code': zorg_instelling_code,
                'zorg_activiteiten':    zorg_activiteiten}

    # ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __write_subtraject(writer, subtraject: Dict) -> None:
        """
        Schrijft het subtraject met alle zorgactiviteiten naar een CSV-bestand.

        :param writer: De handle naar de CSV writer.
        :param dict subtraject: De details van het subtract.
        """
        writer.writerow((subtraject['subtraject_nummer'],
                         subtraject['specialisme_code'],
                         subtraject['diagnose_code'],
                         subtraject['zorg_type_code'],
                         subtraject['zorg_vraag_code'],
                         subtraject['begin_datum'],
                         subtraject['geboorte_datum'],
                         subtraject['geslacht_code'],
                         subtraject['zorg_instelling_code'],
                         subtraject['declaratie_code']))

        for zorgactiviteit in subtraject['zorg_activiteiten']:
            writer.writerow((zorgactiviteit[0], zorgactiviteit[1]))

    # ----------------------------------------------------------------------------------------------------------------------
    def __extract_files(self, writer, filenames: List) -> None:
        """
        Extract de data van een lijst met XML-bestanden met test cases en schrijft deze data naar een CSV-bestand.

        :param writer:  De handle naar de CSV writer.
        :param list filenames: De lijst met bestandsnamen van XML-bestanden met test cases.
        """
        for filename in filenames:
            subtraject = self.__shred_xml_bestand(filename)
            self.__write_subtraject(writer, subtraject)

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self) -> int:
        """
        Executes the command.
        """
        self.output = KerapuStyle(self.input, self.output)

        zip_filename = self.argument('testset-zip')
        csv_filename = self.argument('testset-csv')
        tmp_dir = '.kerapu-' + ''.join(random.choices(string.ascii_lowercase, k=12))

        os.mkdir(tmp_dir)

        self.__extract_zip_file(zip_filename, tmp_dir)
        files = self.__lees_test_cases_lijst(tmp_dir)

        with open(csv_filename, 'w', encoding='utf-8') as handle:
            csv_writer = csv.writer(handle, dialect=csv.unix_dialect)
            self.__extract_files(csv_writer, files)

        shutil.rmtree(tmp_dir)

        return 0

# ----------------------------------------------------------------------------------------------------------------------
