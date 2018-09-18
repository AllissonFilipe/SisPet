from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from ..modelo.Pet import Pet


class PetView(ModelView):

    datamodel     = SQLAInterface(Pet)

    base_order    = ('nome','asc')

    # search_columns = ['changed_by','created_by','created_on','changed_on','nome','decreto']

    list_title    = 'Pet'
    add_title     = 'Adição de Pet'
    edit_title    = 'Edição de Pet'
    show_title    = 'Exibição de Pet'
    list_columns  = ['nome','tipo_animal','raca','sexo','data_nascimento_fmt']
    add_columns   = ['nome','tipo_animal','raca','sexo','data_nascimento']

    edit_columns  = add_columns
    show_columns  = list_columns
    label_columns = {
                     #-------------------------------------Native---------------------------------------------------#
                      'nome'                                 : 'Nome',
                      'tipo_animal'                          : 'Tipo do animal',
                      'raca'                                 : 'Raça',
                      'sexo'                                 : 'Sexo',
                      'data_nascimento'                      : 'Data de Nascimento',
                     #-------------------------------------Custom---------------------------------------------------#
                      'data_nascimento_fmt'                  : 'Data de Nascimento',
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