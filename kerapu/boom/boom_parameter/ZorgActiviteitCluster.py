"""
Kerapu
"""
from kerapu.boom.boom_parameter.BoomParameter import BoomParameter


class ZorgActiviteitCluster(BoomParameter):
    """
    Klasse voor boomparameter zorgactiviteitcluster.

    Boomparameternummers: 301..310, 401..410, 401..510.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, cluster_nummer, weeg_factor_nummer):
        """
        Object constructor.

        :param int cluster_nummer: Het clusternummer (1..10):
        :param int weeg_factor_nummer: Weegfactornummer:

                                       * 0: geen weegfactor
                                       * 1: weegfactor 1
                                       * 2: weegfactor 2
        """
        self._cluster_nummer = cluster_nummer
        self._weeg_factor_nummer = weeg_factor_nummer

    # ------------------------------------------------------------------------------------------------------------------
    def tel(self, cluster_code, subtraject):
        """
        Geeft het aantal zorgactiviteiten (met inachtneming van weegfactor) in een subtraject voorkomt in een
        zorgactiviteitcluster.

        :param str cluster_code: De zorgactiviteitclustercode.
        :param kerapu.Lbz.Subtraject.Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        return subtraject.get_zorg_activiteit_cluster_telling(cluster_code,
                                                              self._cluster_nummer,
                                                              self._weeg_factor_nummer)

# ----------------------------------------------------------------------------------------------------------------------
