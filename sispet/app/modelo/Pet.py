from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Date 
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders


class Pet(Model, AuditMixin):
    __tablename__   = 'sispet_pet'
    
    id              = Column(Integer   ,               primary_key=True)
    nome            = Column(String(120), nullable = False, unique = False)
    tipo_animal     = Column(String(120), nullable = False, unique = True)
    raca            = Column(String(120), nullable = False, unique = False)
    sexo                             = Column(Enum('Masculino',
                                                   'Feminino',
                                        name = 'sexo'), nullable = False)
    data_nascimento               = Column(Date        , nullable = False , unique = False)
    
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
        