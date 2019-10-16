from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class DiagnoseCode(BoomParameter):
    """
    Klasse voor boomparameter diagnosecode.

    Boomparameternummer: 230.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, diagnose_attribuut_code: str, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat een subtraject voldoet aan een een
        (specialismecode, diagnosecode) combinatie.

        :param str diagnose_attribuut_code: De attribuutcode voor (specialismecode, diagnosecode) combinatie.
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.telling_diagnose_attribuut(diagnose_attribuut_code)

# ----------------------------------------------------------------------------------------------------------------------
