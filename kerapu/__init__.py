""" Kerapu
"""
# ----------------------------------------------------------------------------------------------------------------------
LEN_DIAGNOSE_CODE = 4
LEN_SPECIALISME_CODE = 4
LEN_ZORG_ACTIVITEIT_CODE = 6
LEN_ZORG_PRODUCT_CODE = 9
LEN_ZORG_PRODUCT_GROEP_CODE = 6
LEN_ZORG_TYPE_CODE = 2
LEN_ZORG_VRAAG_CODE = 3


# ----------------------------------------------------------------------------------------------------------------------
def clean_bool(x):
    if x == '0':
        return False

    if x == '1':
        return True

    raise RuntimeError("Not a boolean value '%s'." % x)


# ----------------------------------------------------------------------------------------------------------------------
def clean_code(code, lengte):
    """
    Schoont een code van voor- en naloop whitespace en voorziet de code van het juiste aantal voorloop nullen.

    :param str code: De code.
    :param int lengte: De gewenste lengte van de code.

    :rtype: str
    """
    return code.zfill(lengte)


# ----------------------------------------------------------------------------------------------------------------------
def clean_date(x):
    if x == '':
        return '9999-12-31'

    return x


# ----------------------------------------------------------------------------------------------------------------------
def clean_int(x, leeg=None):
    if x == '' or not x:
        return leeg

    return int(x)


# ----------------------------------------------------------------------------------------------------------------------
def clean_str(x):
    if x == '':
        return None

    return x

# ----------------------------------------------------------------------------------------------------------------------
