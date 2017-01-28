"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class DiagnoseCluster(BoomParameter):
    """
    Klasse voor boomparameter diagnosecluster.

    Boomparameternummers: 232, 233, 234, 235, 236, 237.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, cluster_nummer):
        """
        Object constructor.

        :param int cluster_nummer: Het clusternummer (1..6).
        """
        self._cluster_nummer = cluster_nummer

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, cluster_code, subtraject):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat een subtraject voldoet aan een diagnoseclustercode.

        :param str cluster_code: De cluster_code waartegen getest moet worden.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_diagnose_cluster_telling(cluster_code, self._cluster_nummer)

# ----------------------------------------------------------------------------------------------------------------------
