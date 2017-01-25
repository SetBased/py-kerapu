"""
Kerapu
"""
from kerapu.boom.boom_parameter.BehandelKlasse import BehandelKlasse
from kerapu.boom.boom_parameter.DiagnoseCluster import DiagnoseCluster
from kerapu.boom.boom_parameter.DiagnoseCode import DiagnoseCode
from kerapu.boom.boom_parameter.Geslacht import Geslacht
from kerapu.boom.boom_parameter.Leeftijd import Leeftijd
from kerapu.boom.boom_parameter.SpecialismeCluster import SpecialismeCluster
from kerapu.boom.boom_parameter.SpecialismeCode import SpecialismeCode
from kerapu.boom.boom_parameter.ZorgActiviteitCluster import ZorgActiviteitCluster
from kerapu.boom.boom_parameter.ZorgActiviteitCode import ZorgActiviteitCode
from kerapu.boom.boom_parameter.ZorgInstellingCode import ZorgInstellingCode
from kerapu.boom.boom_parameter.ZorgTypeCode import ZorgTypeCode
from kerapu.boom.boom_parameter.ZorgVraagCluster import ZorgVraagCluster
from kerapu.boom.boom_parameter.ZorgVraagCode import ZorgVraagCode

# ----------------------------------------------------------------------------------------------------------------------
_boom_parameters = {}
"""
Poel met alle boomparameters
"""


# ----------------------------------------------------------------------------------------------------------------------
def create_boom_parameter(boom_parameter_nummer):
    """
    Een fabriek met hergebruik voor het maken van boomparameters. Het aanroepen van deze functie met hetzelfde
    boomparameternummer zal tekens het zelfde object opleveren.

    :param int boom_parameter_nummer: Het nummer van de boomparameter.

    :rtype: kerapu.Boom.BoomParameter.BoomParameter.BoomParameter
    """
    if boom_parameter_nummer in _boom_parameters:
        return _boom_parameters[boom_parameter_nummer]

    _boom_parameters[boom_parameter_nummer] = _create_boom_parameter(boom_parameter_nummer)

    return _boom_parameters[boom_parameter_nummer]


# ----------------------------------------------------------------------------------------------------------------------
def _create_boom_parameter(boom_parameter_nummer):
    """
    Een fabriek voor het maken van boomparameters.

    :param int boom_parameter_nummer: Het nummer van de boomparameter.

    :rtype: BoomParameter
    """
    if boom_parameter_nummer == 100:
        return Leeftijd()

    if boom_parameter_nummer == 101:
        return Geslacht()

    if boom_parameter_nummer == 110:
        return ZorgInstellingCode()

    if boom_parameter_nummer == 111:
        # Zorginstellingscluster 1
        # Deze boomparameter wordt thans niet gebruikt door de grouper.
        raise NotImplementedError('Boomparameter %d is niet geïmplementeerd.' % boom_parameter_nummer)

    if boom_parameter_nummer == 112:
        # Zorginstellingscluster 2
        # Deze boomparameter wordt thans niet gebruikt door de grouper.
        raise NotImplementedError('Boomparameter %d is niet geïmplementeerd.' % boom_parameter_nummer)

    if boom_parameter_nummer == 200:
        return SpecialismeCode()

    if boom_parameter_nummer == 201:
        return SpecialismeCluster(1)

    if boom_parameter_nummer == 202:
        return SpecialismeCluster(2)

    if boom_parameter_nummer == 210:
        return ZorgTypeCode()

    if boom_parameter_nummer == 211:
        # Zorgtypecluster 1
        # Deze boomparameter wordt thans niet gebruikt door de grouper.
        raise NotImplementedError('Boomparameter %d is niet geïmplementeerd.' % boom_parameter_nummer)

    if boom_parameter_nummer == 212:
        # Zorgtypecluster 2
        # Deze boomparameter wordt thans niet gebruikt door de grouper.
        raise NotImplementedError('Boomparameter %d is niet geïmplementeerd.' % boom_parameter_nummer)

    if boom_parameter_nummer == 220:
        return ZorgVraagCode()

    if boom_parameter_nummer == 221:
        return ZorgVraagCluster(1)

    if boom_parameter_nummer == 222:
        return ZorgVraagCluster(2)

    if boom_parameter_nummer == 230:
        return DiagnoseCode()

    if boom_parameter_nummer == 231:
        # ICD-diagnosecode
        # Deze boomparameter wordt thans niet gebruikt door de grouper.
        raise NotImplementedError('Boomparameter %d is niet geïmplementeerd.' % boom_parameter_nummer)

    if 232 <= boom_parameter_nummer <= 237:
        return DiagnoseCluster(boom_parameter_nummer - 231)

    if boom_parameter_nummer == 241:
        # Begindatum subtraject
        # Deze boomparameter wordt thans niet gebruikt door de grouper.
        raise NotImplementedError('Boomparameter %d is niet geïmplementeerd.' % boom_parameter_nummer)

    if boom_parameter_nummer == 300:
        return ZorgActiviteitCode(0)

    if 301 <= boom_parameter_nummer <= 310:
        return ZorgActiviteitCluster(boom_parameter_nummer - 300, 0)

    if boom_parameter_nummer == 351:
        return BehandelKlasse(0)

    if boom_parameter_nummer == 400:
        return ZorgActiviteitCode(1)

    if 401 <= boom_parameter_nummer <= 410:
        return ZorgActiviteitCluster(boom_parameter_nummer - 400, 1)

    if boom_parameter_nummer == 451:
        # Behandelklasse – som van (aantal * weegfactor 1)
        # Deze boomparameter wordt thans niet gebruikt door de grouper.
        # return BehandelKlasse(1)
        raise NotImplementedError('Boomparameter %d is niet geïmplementeerd.' % boom_parameter_nummer)

    if boom_parameter_nummer == 500:
        return ZorgActiviteitCode(2)

    if 501 <= boom_parameter_nummer <= 510:
        return ZorgActiviteitCluster(boom_parameter_nummer - 500, 2)

    if boom_parameter_nummer == 551:
        # Behandelklasse – som van (aantal * weegfactor 2)
        # Deze boomparameter wordt thans niet gebruikt door de grouper.
        # return BehandelKlasse(1)
        raise NotImplementedError('Boomparameter %d is niet geïmplementeerd.' % boom_parameter_nummer)

    raise RuntimeError("Onbekende boomparameter '%s'." % boom_parameter_nummer)

# ----------------------------------------------------------------------------------------------------------------------
