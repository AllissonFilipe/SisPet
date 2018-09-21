from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from ..modelo.Cliente import Cliente


class Cliente_View(ModelView):

    datamodel     = SQLAInterface(Cliente)

    base_order    = ('nome','asc')

    # search_columns = ['changed_by','created_by','created_on','changed_on','nome','decreto']

    list_title    = 'Clientes'
    add_title     = 'Adição de Cliente'
    edit_title    = 'Edição de Cliente'
    show_title    = 'Exibição de Cliente'
    list_columns  = ['nome','cpf','telefone','endereco','email','ativo_fmt']
    add_columns   = ['nome','cpf','telefone','endereco','email']

    edit_columns  = add_columns + ['ativo']
    show_columns  = list_columns
    label_columns = {
                     #-------------------------------------Native---------------------------------------------------#
                      'nome'                                 : 'Nome',
                      'cpf'                                  : 'CPF',
                      'telefone'                             : 'Telefone',
                      'endereco'                             : 'Endereço',
                      'email'                                : 'Email',
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