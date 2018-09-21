from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date, Boolean 
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders
from ..modelo.Especie import Especie


class Raca(Model, AuditMixin):
    __tablename__   = 'sispet_raca'
    
    id              = Column(Integer   ,               primary_key=True)
    nome            = Column(String(120), nullable = False, unique = False)
    especie_id      = Column(Integer, ForeignKey('sispet_especie.id'),nullable = True, default= None)
    especie         = relationship("Especie")
    ativo           = Column(Boolean, server_default='True')
    
    def __repr__(self):
        var = self.nome
        if var:
            return var
        else:
            return ''

    @renders('ativo')
    def ativo_fmt(self):
        if self.ativo:
            return 'sim'
        else:
            return 'não'