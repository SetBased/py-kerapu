"""
Kerapu
"""


class BeslisRegel:
    """
    Klasse voor beslisregels.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self,
                 beslist_regel_id,
                 attribuut_groep,
                 label_true,
                 label_false,
                 indicatie_aanspraakbeperking):
        """
        Object constructor.

        :param int beslist_regel_id: Het ID van deze beslisregel.
        :param kerapu.Boom.AttribuutGroep.AttribuutGroep attribuut_groep: De attribuutgroep van deze beslisregel.
        :param str label_true: Label voor True.
        :param str label_false: Label voor False.
        :param bool indicatie_aanspraakbeperking: Vlag voor aanspraakbeperking.
        """
        self._beslist_regel_id = beslist_regel_id

        self._attribuut_groep = attribuut_groep
        """
        :type: kerapu.Boom.AttribuutGroep.AttribuutGroep
        """

        self._beslist_regel_true = None
        """
        :type: BeslisRegel
        """

        self._beslist_regel_false = None
        """
        :type: BeslisRegel
        """

        self._label_true = label_true
        self._label_false = label_false
        self._indicatie_aanspraakbeperking = indicatie_aanspraakbeperking

    # ------------------------------------------------------------------------------------------------------------------
    def verrijk(self, beslist_regel_true, beslist_regel_false):
        """
        Verrijkt deze beslisregel met beslisregels voor True and False.

        :param kerapu.Boom.BeslisRegel.BeslisRegel beslist_regel_true: De beslisregel voor True.
        :param kerapu.Boom.BeslisRegel.BeslisRegel beslist_regel_false: De beslisregel voor False.
        """
        self._beslist_regel_true = beslist_regel_true
        self._beslist_regel_false = beslist_regel_false

    # ------------------------------------------------------------------------------------------------------------------
    def klim(self, subtraject):
        """
        Klimt door de beslisboom een geeft het uiteindelijk gevonden label terug.

        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: str
        """
        test = self._attribuut_groep.test(subtraject)

        if not test:
            if self._beslist_regel_false:
                return self._beslist_regel_false.klim(subtraject)

            return self._label_false

        if self._beslist_regel_true:
            return self._beslist_regel_true.klim(subtraject)

        return self._label_true

# ----------------------------------------------------------------------------------------------------------------------
