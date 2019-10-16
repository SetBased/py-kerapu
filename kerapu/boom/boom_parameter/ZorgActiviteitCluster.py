from kerapu.boom.boom_parameter.BoomParameter import BoomParameter
from kerapu.lbz.Subtraject import Subtraject


class ZorgActiviteitCluster(BoomParameter):
    """
    Klasse voor boomparameter zorgactiviteitcluster.

    Boomparameternummers: 301..310, 401..410, 401..510.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, cluster_nummer: int, weeg_factor_nummer: int):
        """
        Object constructor.

        :param int cluster_nummer: Het clusternummer (1..10):
        :param int weeg_factor_nummer: Weegfactornummer:

                                       * 0: geen weegfactor
                                       * 1: weegfactor 1
                                       * 2: weegfactor 2
        """
        self._cluster_nummer: int = cluster_nummer
        """
        Het clusternummer (1..10).
        """

        self._weeg_factor_nummer: int = weeg_factor_nummer
        """
        Weegfactornummer.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, cluster_code: str, subtraject: Subtraject) -> int:
        """
        Geeft het aantal zorgactiviteiten (met inachtneming van weegfactor) in een subtraject voorkomt in een
        zorgactiviteitcluster.

        :param str cluster_code: De zorgactiviteitclustercode.
        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.telling_zorg_activiteit_cluster(cluster_code, self._cluster_nummer, self._weeg_factor_nummer)

# ----------------------------------------------------------------------------------------------------------------------
