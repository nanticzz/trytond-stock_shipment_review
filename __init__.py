# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .configuration import *
from .product import *
from .shipment import *

def register():
    Pool.register(
        ConfigurationLocationReview,
        Configuration,
        Template,
        ShipmentOut,
        ShipmentIn,
        module='stock_shipment_review', type_='model')
