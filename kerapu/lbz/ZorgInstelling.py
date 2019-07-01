"""
Kerapu
"""
from kerapu import clean_code, LEN_ZORG_INSTELLING_CODE


class ZorgInstelling:
    """
    Klasse voor zorginstellingen.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, zorg_instelling_code: str):
        """
        Object constructor.

        :param str zorg_instelling_code: De code van deze zorginstelling.
        """
        self.__zorg_instelling_code = clean_code(zorg_instelling_code, LEN_ZORG_INSTELLING_CODE)
        """
        De code van deze zorginstelling.

        :type: str
        """

    # ------------------------------------------------------------------------------------------------------------------
    def get_zorg_instelling_aantal(self, zorg_instelling_code: str) -> int:
        """
        Geeft het aantal malen (met inachtneming van weegfactor) dat deze zorginstelling voldoet aan een
        zorginstellingcode.

        :param str zorg_instelling_code: De AGB-code van de zorginstelling.

        :rtype: int
        """
        return 1 if self.__zorg_instelling_code == clean_code(zorg_instelling_code, LEN_ZORG_INSTELLING_CODE) else 0

    # ----------------------------------------------------------------------------------------------------------------------
