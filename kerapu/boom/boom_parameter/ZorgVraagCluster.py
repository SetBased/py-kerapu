"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class ZorgVraagCluster(BoomParameter):
    """
    Klasse voor boomparameter zorgvraagcluster.

    Boomparameternummers: 221, 222.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, cluster_nummer):
        """
        Object constructor.

        :param int cluster_nummer: Het clusternummer (1..2):
        """
        self._cluster_nummer = cluster_nummer

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, cluster_code, subtraject):
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat de zorgvraag van een subtraject voorkomt in een zorgvraagcluster.

        :param str cluster_code: De cluster_code waartegen getest moet worden.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_zorg_vraag_cluster_telling(cluster_code, self._cluster_nummer)

# ----------------------------------------------------------------------------------------------------------------------
