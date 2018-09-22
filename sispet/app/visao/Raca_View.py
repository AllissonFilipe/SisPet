from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from ..modelo.Raca import Raca
from ..validacoes import ValidaObrigatorio


class Raca_View(ModelView):

    datamodel     = SQLAInterface(Raca)

    base_order    = ('nome','asc')

    # search_columns = ['changed_by','created_by','created_on','changed_on','nome','decreto']

    list_title    = 'Raças'
    add_title     = 'Adição de Raça'
    edit_title    = 'Edição de Raça'
    show_title    = 'Exibição de Raça'
    list_columns  = ['nome','especie','ativo_fmt']
    add_columns   = ['nome','especie']

    edit_columns  = add_columns + ['ativo']
    show_columns  = list_columns
    label_columns = {
                     #-------------------------------------Native---------------------------------------------------#
                      'nome'                                 : 'Nome',
                      'ativo'                                : 'Ativo',
                      'especie'                              : 'Espécie',
                     #-------------------------------------Custom---------------------------------------------------#
                      'ativo_fmt'                            : 'Ativo',
                     #--------------------------------------INFO----------------------------------------------------#
                      'created_on'                           : 'Data do Cadastro',
                      'created_by'                           : 'Cadastrado por',
                      'changed_on'                           : 'Data da Ultima Alteração',
                      'changed_by'                           : 'Alterado por',
    }

    validators_columns = { 'especie'            : [  ValidaObrigatorio()  ] }

    show_fieldsets = [('Dados Básicos da Categoria',
                       {'fields':show_columns,'expanded':True}),
                      ('Informações de Auditoria',
                       {'fields': ['created_on','created_by','changed_on','changed_by'], 'expanded': False})]