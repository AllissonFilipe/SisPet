from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date, Boolean, BigInteger 
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders


class Cliente(Model, AuditMixin):
    __tablename__   = 'sispet_cliente'
    
    id              = Column(Integer   ,               primary_key=True)
    nome            = Column(String(120), nullable = False, unique = False)
    cpf             = Column(String(50), nullable = False, unique = True)
    telefone        = Column(BigInteger, nullable = False, unique = True)
    endereco        = Column(Text, nullable = False, unique = False)
    email           = Column(String(120), nullable = True, unique = True)
    ativo           = Column(Boolean, server_default = 'True')

    
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