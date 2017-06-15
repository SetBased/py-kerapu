"""
Kerapu
"""
import csv


class Shredder:
    """
    Klasse voor het schreden van XML-bestanden en opslaan in CSV-formaat.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io, target_dir):
        """
        Object constructor.

        :param str target_dir: De folder waar de CSV-bestanden moeten worden opgeslagen.
        """
        self._io = io
        """
        The output decorator.

        :type: kerapu.style.KerapuStyle.KerapuStyle
        """

        self.__target_dir = target_dir
        """
        De folder waar de CSV-bestanden moeten worden opgeslagen.

        :type: str
        """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def extract_field(element, tag):
        """
        Extracts de waarde van een XML element.

        :param lxml.etree.Element element: Het parent XML element.
        :param str tag: De tag van het gevraagde XML-element.

        :rtype: str
        """
        elements = element.xpath(tag, namespaces={'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/'})
        if elements:
            return elements[0].text

        return ''

    # ------------------------------------------------------------------------------------------------------------------
    def extract_table(self, table, filename, fields, xpaths):
        """
        Extracts een groupertabel uit XML een slaat de tabel op in een CSV-bestand.

        :param Element table: De naam van de groupertabel.
        :param str filename: De filenaam van het CSV-bestaand.
        :param list fields: Een lijst met velden (d.w.z. kolomen in het CSV-bestand).
        :param list xpaths: Een lijst met xpath voor het extracten van de bovenstaande velden.
        """
        # Sanity test.
        if len(fields) != len(xpaths):
            raise ValueError("fields and xpaths must have equal length")

        # Open the file and create CSV writer.
        file = open(self.__target_dir + '/' + filename, 'wt', encoding='utf-8')
        writer = csv.writer(file)

        # Write header row.
        writer.writerow(fields)

        # Write all rows in the XML 'table'.
        row_count = 0
        for element in table:
            row = []
            for xpath in xpaths:
                row.append(Shredder.extract_field(element, xpath))
            writer.writerow(row)
            row_count += 1

        # Close the file.
        file.close()

        self._io.text('Wrote {:6d} rows to <fso>{}</fso>'.format(row_count, filename))

# ----------------------------------------------------------------------------------------------------------------------
