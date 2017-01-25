"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class ZorgInstellingCode(BoomParameter):
    """
    Klasse voor boomparameter zorginstelling.

    Boomparameternummers: 110.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, waarde, subtraject):
        """
        Niet geïmplementeerd.

        :param int|str waarde: De waarde waartegen getest moet worden.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        # Deze boomparameter komt slechts 4 keer voor in tabel attribuut.
        raise NotImplementedError('Boomparameter 110 is niet geïmplementeerd.')

# ----------------------------------------------------------------------------------------------------------------------
