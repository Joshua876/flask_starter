from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField, StringField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

class propertyForm(FlaskForm):
    prop_title = StringField('Property Title', validators=[InputRequired()])
    prop_bedrooms = StringField('Bedrooms', validators=[InputRequired()])
    prop_bathrooms = StringField('Bathrooms', validators=[InputRequired()])
    prop_location = StringField('Property Location', validators=[InputRequired()])
    prop_price = StringField('Property Price', validators=[InputRequired()])
    prop_type = SelectField(u'Property Type', choices=[('House','House'),('Apartment','Apartment')])
    prop_descrip = StringField('Property Description', validators=[InputRequired()])
    prop_img = FileField('Property Image', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg', 'Images only!'])])
    SubmitField('Add a Property')
