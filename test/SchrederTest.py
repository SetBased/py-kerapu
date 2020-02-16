from unittest import TestCase

from cleo import Application
from cleo import CommandTester

from kerapu.command.ShredderCommand import ShredderCommand


class ShredderTest(TestCase):
    """
    Test cases voor XML shredder.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_referentie(self):
        """
        Test extractie referentietabellen.
        """
        application = Application()
        application.add(ShredderCommand())

        command = application.find('kerapu:shredder')
        command_tester = CommandTester(command)
        status = command_tester.execute([('command', command.get_name()),
                                         ('XML-bestand', 'test/var/lib/20200101 Referenties v20190919.xml'),
                                         ('folder', 'test/var/lib')])

        output = command_tester.get_display().rstrip()

        self.assertEqual(0, status)

        for tabel in ['AfsluitRedenen',
                      'BehandelKlassen',
                      'Diagnosen',
                      'Geslachten',
                      'LimitatieMachtigingen',
                      'Specialismen',
                      'VertaalZorgActiviteiten',
                      'ZorgProductGroepen',
                      'ZorgTypen',
                      'ZorgVragen']:
            self.assertRegex(output, r'Wrote \s*\d+ rows to {}.csv'.format(tabel), tabel)

    # ------------------------------------------------------------------------------------------------------------------
    def test_boom(self):
        """
        Test extractie boombestanden.
        """
        application = Application()
        application.add(ShredderCommand())

        command = application.find('kerapu:shredder')
        command_tester = CommandTester(command)
        status = command_tester.execute([('command', command.get_name()),
                                         ('XML-bestand', 'test/var/lib/20200101 BoomBestanden v20190919.xml'),
                                         ('folder', 'test/var/lib')])

        output = command_tester.get_display().rstrip()

        self.assertEqual(0, status)

        for tabel in ['BeslisRegels',
                      'AttribuutGroepen',
                      'AttribuutGroepKoppelingen',
                      'Attributen',
                      'BoomParameters']:
            self.assertRegex(output, r'Wrote \s*\d+ rows to {}.csv'.format(tabel), tabel)

# ------------------------------------------------------------------------------------------------------------------
