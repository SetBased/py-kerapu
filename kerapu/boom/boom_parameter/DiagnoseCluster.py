"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class DiagnoseCluster(BoomParameter):
    """
    Klasse voor boomparameter diagnosecluster.

    Boomparameternummers: 232, 233, 234, 235, 236, 237.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, cluster_nummer: int):
        """
        Object constructor.

        :param int cluster_nummer: Het clusternummer (1..6).
        """
        self._cluster_nummer: int = cluster_nummer
        """
        Het clusternummer (1..6).
        """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, cluster_code: str, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat een subtraject voldoet aan een diagnoseclustercode.

        :param str cluster_code: De cluster_code waartegen getest moet worden.
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.telling_diagnose_cluster(cluster_code, self._cluster_nummer)

# ----------------------------------------------------------------------------------------------------------------------
