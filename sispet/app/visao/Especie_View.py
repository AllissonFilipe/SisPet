from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from ..modelo.Especie import Especie


class Especie_View(ModelView):

    datamodel     = SQLAInterface(Especie)

    base_order    = ('nome','asc')

    # search_columns = ['changed_by','created_by','created_on','changed_on','nome','decreto']

    list_title    = 'Espécies'
    add_title     = 'Adição de Espécie'
    edit_title    = 'Edição de Espécie'
    show_title    = 'Exibição de Espécie'
    list_columns  = ['nome','ativo_fmt']
    add_columns   = ['nome']

    edit_columns  = add_columns + ['ativo']
    show_columns  = list_columns
    label_columns = {
                     #-------------------------------------Native---------------------------------------------------#
                      'nome'                                 : 'Nome',
                      'ativo'                                : 'Ativo',
                     #-------------------------------------Custom---------------------------------------------------#
                      'ativo_fmt'                            : 'Ativo',
                     #--------------------------------------INFO----------------------------------------------------#
                      'created_on'                           : 'Data do Cadastro',
                      'created_by'                           : 'Cadastrado por',
                      'changed_on'                           : 'Data da Ultima Alteração',
                      'changed_by'                           : 'Alterado por',
    }
    show_fieldsets = [('Dados Básicos da Categoria',
                       {'fields':show_columns,'expanded':True}),
                      ('Informações de Auditoria',
                       {'fields': ['created_on','created_by','changed_on','changed_by'], 'expanded': False})]