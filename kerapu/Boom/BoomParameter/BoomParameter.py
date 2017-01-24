"""
Kerapu
"""
import abc


class BoomParameter:
    """
    Abstracte klasse voor boomparameters.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def tel(self, waarde, subtraject):
        """
        Geeft het aantal malen dat de boomparameter voldoet aan een waarde.

        :param [int|str] waarde: De waarde waartegen getest moet worden.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        raise Exception("Not implemented")

# ----------------------------------------------------------------------------------------------------------------------
