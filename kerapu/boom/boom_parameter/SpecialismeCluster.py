"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class SpecialismeCluster(BoomParameter):
    """
    Klasse voor boomparameter specialismecluster.

    Boomparameternummers: 210, 202.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, cluster_nummer: int):
        """
        Object constructor.

        :param int cluster_nummer: Het clusternummer (1..2).
        """
        self._cluster_nummer = cluster_nummer

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, cluster_code: str, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen (d.w.z. 0 of 1) dat het uitvoerend specialisme van een subtraject voldoet aan een
        specialismecluster.

        :param str cluster_code: De clustercode waartegen getest moet worden.
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_specialisme_cluster_telling(cluster_code, self._cluster_nummer)

# ----------------------------------------------------------------------------------------------------------------------
