from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from ..modelo.Pet import Pet
from ..modelo.Especie import Especie
from flask_appbuilder.models.sqla.filters import FilterEqual


class Pet_View(ModelView):

    datamodel     = SQLAInterface(Pet)

    base_order    = ('nome','asc')

    # search_columns = ['changed_by','created_by','created_on','changed_on','nome','decreto']

    list_title    = 'Pet'
    add_title     = 'Adição de Pet'
    edit_title    = 'Edição de Pet'
    show_title    = 'Exibição de Pet'
    list_columns  = ['cliente','nome','sexo','data_nascimento_fmt','especie','raca',
                     'identificacao','vacinas','informacoes','ativo_fmt']
    add_columns   = ['cliente','nome','sexo','data_nascimento','especie','raca',
                     'identificacao','vacinas','informacoes']

    edit_columns  = add_columns + ['ativo']
    show_columns  = list_columns
    label_columns = {
                     #-------------------------------------Native---------------------------------------------------#
                      'cliente'                              : 'Dono',
                      'nome'                                 : 'Nome',
                      'sexo'                                 : 'Sexo',
                      'data_nascimento'                      : 'Data de Nascimento',
                      'especie'                              : 'Espécie',
                      'raca'                                 : 'Raça',
                      'identificacao'                        : 'Identificação',
                      'vacinas'                              : 'Vacinas',
                      'informacoes'                          : 'Informações',
                      'ativo'                                : 'Ativo',
                     #-------------------------------------Custom---------------------------------------------------#
                      'data_nascimento_fmt'                  : 'Data de Nascimento',
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