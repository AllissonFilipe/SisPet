from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from .modelo.Cliente import Cliente
from .modelo.Especie import Especie
from .modelo.Raca import Raca
from .modelo.Vacina import Vacina
from .modelo.Pet import Pet

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
        
