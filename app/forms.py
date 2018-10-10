from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField

class PubContractSearch(FlaskForm):
	region = StringField('Region')
	min = IntegerField('Min')
	max = IntegerField('Max')
	submit = SubmitField('Search')
