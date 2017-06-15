"""
Kerapu
"""
from cleo import Command

from kerapu.shredder.BoomBestandenShredder import BoomBestandenShredder
from kerapu.shredder.ReferentieShredder import ReferentieShredder
from kerapu.style.KerapuStyle import KerapuStyle


class ShredderCommand(Command):
    """
    Converteert XML-bestanden met groupertabellen naar CSV-bestanden

    kerapu:shredder
        {XML-bestand : XML-bestand met groupertabellen, b.v. BoomBestanden.xml, Referenties.xml}
        {folder : Folder waar de CSV-bestanden moeten worden opgeslagen}
    """

    # ------------------------------------------------------------------------------------------------------------------
    def handle(self):
        """
        Executes the command.
        """
        self.output = KerapuStyle(self.input, self.output)

        filename = self.argument('XML-bestand')
        folder = self.argument('folder')

        # Lees de eerste gedeelte van het XML-bestand en bepaal type.
        with open(filename, 'rt', encoding="ascii", errors="surrogateescape") as handle:
            kop = handle.read(1024)

            if '<InlezenBoomBestanden>' in kop:
                shredder = BoomBestandenShredder(self.output, folder)
                shredder.shred_xml_file(filename)

            elif '<InlezenReferenties>' in kop:
                shredder = ReferentieShredder(self.output, folder)
                shredder.shred_xml_file(filename)

            else:
                raise RuntimeError("Tag <InlezenBoomBestanden> of <InlezenReferenties> niet gevonden in '{}'".
                                   format(filename))

        return 0

# ----------------------------------------------------------------------------------------------------------------------
