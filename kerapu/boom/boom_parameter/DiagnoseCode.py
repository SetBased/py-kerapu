"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class DiagnoseCode(BoomParameter):
    """
    Klasse voor boomparameter diagnosecode.

    Boomparameternummer: 230.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, diagnose_attribuut_code, subtraject):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat een subtraject voldoet aan een een
        (specialismecode, diagnosecode) combinatie.

        :param str diagnose_attribuut_code: De attribuutcode voor (specialismecode, diagnosecode) combinatie.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_diagnose_attribuut_telling(diagnose_attribuut_code)

# ----------------------------------------------------------------------------------------------------------------------
