from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date, Float, Table, Text, Boolean 
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders
from ..modelo.Cliente import Cliente
from ..modelo.Especie import Especie
from ..modelo.Raca import Raca
from ..modelo.Vacina import Vacina

assoc_pet_vacina = Table('assoc_pet_vacina', Model.metadata,
                             Column('id', Integer, primary_key=True),
                             Column('pet_id', Integer, ForeignKey('sispet_pet.id')),
                             Column('vacina_id', Integer, ForeignKey('sispet_vacina.id'))
)


class Pet(Model, AuditMixin):
    __tablename__   = 'sispet_pet'
    
    id              = Column(Integer   ,               primary_key=True)
    cliente_id      = Column(Integer, ForeignKey('sispet_cliente.id'),nullable = True, default= None)
    cliente         = relationship("Cliente")
    nome            = Column(String(120), nullable = False, unique = False)
    sexo            = Column(Enum('Masculino','Feminino',
                                        name = 'sexo'), nullable = False)
    data_nascimento = Column(Date, nullable = True, unique = False)
    especie_id      = Column(Integer, ForeignKey('sispet_especie.id'),nullable = True, default= None)
    especie         = relationship("Especie")
    raca_id         = Column(Integer, ForeignKey('sispet_raca.id'),nullable = True, default= None)
    raca            = relationship("Raca")
    identificacao   = Column(String(120), nullable = False, unique = False)
    vacinas         = relationship("Vacina", secondary=assoc_pet_vacina)
    informacoes     = Column(Text        , nullable = False , unique = False)
    ativo           = Column(Boolean, server_default = 'True')
    
    def __repr__(self):
        var = self.nome
        if var:
            return var
        else:
            return ''

    @renders('data_nascimento')
    def data_nascimento_fmt(self):
        if self.data_nascimento:
            return self.data_nascimento.strftime('%d/%m/%Y')
        else:
            return ' '

    @renders('ativo')
    def ativo_fmt(self):
        if self.ativo:
            return 'sim'
        else:
            return 'não'
        