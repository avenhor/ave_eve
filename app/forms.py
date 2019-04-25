from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class PubContractSearch(FlaskForm):
	region = StringField('Region')
	min = IntegerField('Min')
	max = IntegerField('Max')
	multiple = BooleanField('Exclude Multiple Items?')
	submit = SubmitField('Search')

class ConcordeSearch(FlaskForm):
	start = StringField('Starting System', validators=[DataRequired()])
	submit = SubmitField('Search', validators=[DataRequired()])
