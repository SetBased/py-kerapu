"""
Kerapu
"""
from kerapu.boom.attribuut.Attribuut12 import Attribuut12
from kerapu.boom.attribuut.Attribuut21 import Attribuut21


def maak_attribuut(attribuut_id,
                   boom_parameter_nummer,
                   filter_toets_wijze,
                   filter_waarde_type,
                   onder_filter_waarde,
                   boven_filter_waarde):
    """
    Fabriek voor het maken van attributen.

    :param int attribuut_id: Het ID van het attribuut.
    :param int boom_parameter_nummer: Het ID van de boomparameter van het attribuut.
    :param int filter_toets_wijze: De filtertoetswijze
    :param int filter_waarde_type: Het type van de waarde van het attribuut.
    :param str onder_filter_waarde: De ondergrens.
    :param str boven_filter_waarde: De bovengrens.

    :rtype: Attribuut
    """
    if filter_toets_wijze == 1 and filter_waarde_type == 2:
        return Attribuut12(attribuut_id, boom_parameter_nummer, onder_filter_waarde)

    if filter_toets_wijze == 2 and filter_waarde_type == 1:
        return Attribuut21(attribuut_id, boom_parameter_nummer, int(onder_filter_waarde), int(boven_filter_waarde))

    if not 1 <= filter_toets_wijze <= 2:
        raise RuntimeError("Onbekende filtertoetswijze %d." % filter_toets_wijze)

    if not 1 <= filter_waarde_type <= 3:
        raise RuntimeError("Onbekende type %d van de waarde van het attribuut." % filter_waarde_type)

    raise NotImplementedError("Attribuut met filtertoetswijze %d en waarde type %d is niet geïmplementeerd" % (
        filter_toets_wijze, filter_waarde_type))

# ----------------------------------------------------------------------------------------------------------------------
