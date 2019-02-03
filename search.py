from wtforms.validators import DataRequired
from wtforms import Form, IntegerField, StringField

class Search(Form):
    
    v=[DataRequired()]
    
    # Établissement
    building = StringField('Nom d\'établissement', validators=v)

    # Département
    depInt = IntegerField('Département', validators=v)

    # Ville
    ville = StringField('Ville', validators=v)

    #Filière
    filiere = StringField('Fiière', validators=v)

    # Académie
    area_high = StringField('Académie', validators=v)

    # Année
    year_min = IntegerField('Année', validators=v)
    year_max = IntegerField('Année', validators=v)


