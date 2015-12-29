"""
Kerapu

:copyright: 2015-2016 Set Based IT Consultancy
:licence: MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
import argparse

from kerapu.Shredder.BoomBestandenShredder import BoomBestandenShredder
from kerapu.Shredder.ReferentieShredder import ReferentieShredder


# ----------------------------------------------------------------------------------------------------------------------
def main():
    """
    The main function of Kerapu's XML shredder.
    """
    parser = argparse.ArgumentParser(description='Converteert XML-bestanden met groupertabellen naar CSV-bestanden')

    parser.add_argument(metavar='<XML-bestand>',
                        nargs=1,
                        dest='filename',
                        help='XML-bestand met groupertabellen, b.v. BoomBestanden.xml, Referenties.xml')
    parser.add_argument(metavar='<folder>',
                        nargs=1,
                        dest='folder',
                        help='folder waar de CSV-bestanden moeten worden opgeslagen')

    args = parser.parse_args()
    filename = args.filename[0]
    folder = args.folder[0]

    # Lees de eerste gedeelte van het XML-bestand en bepaal type.
    kop = open(filename, 'rt').read(1024)

    if '<InlezenBoomBestanden>' in kop:
        shredder = BoomBestandenShredder(folder)
        shredder.shred_xml_file(filename)
        exit(0)

    if '<InlezenReferenties>' in kop:
        shredder = ReferentieShredder(folder)
        shredder.shred_xml_file(filename)
        exit(0)

    raise RuntimeError("Tag <InlezenBoomBestanden> of <InlezenReferenties> niet gevonden in '%s'." % filename)

# ----------------------------------------------------------------------------------------------------------------------
