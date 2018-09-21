from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from .visao.Cliente_View import Cliente_View
from .visao.Especie_View import Especie_View
from .visao.Raca_View import Raca_View
from .visao.Vacina_View import Vacina_View
from .visao.Pet_View import Pet_View
"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""

appbuilder.add_view(Especie_View             , "Espécie"               , icon="fa-book", category="Cadastros Básicos"          , category_icon='fa-envelope')
appbuilder.add_view(Raca_View                , "Raça"                  , icon="fa-book", category="Cadastros Básicos"          , category_icon='fa-envelope')
appbuilder.add_view(Vacina_View              , "Vacina"                , icon="fa-book", category="Cadastros Básicos"          , category_icon='fa-envelope')
appbuilder.add_view(Cliente_View             , "Cliente"               , icon="fa-user ", category="Cadastro de Clientes"          , category_icon='fa-envelope')
appbuilder.add_view(Pet_View                 , "Pet"                   , icon="fa-paw", category="Cadastro de Animais"          , category_icon='fa-envelope')





@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()


