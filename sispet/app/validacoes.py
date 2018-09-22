from wtforms.validators import ValidationError,DataRequired, StopValidation

#Valida se o campo foi preenchido
class ValidaObrigatorio(object):
    """
       Valida se o campo não está Nulo ou Vazio
    """

    def __call__(self,form,field):
        if field.data is None or field.data == ' ':
            raise StopValidation("O campo "+str(field.label)+" é Obrigatório !")