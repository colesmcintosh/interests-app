from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class Interests(FlaskForm):
    first_name = StringField("First Name:", validators=[DataRequired()])
    last_name = StringField("Last Name:", validators=[DataRequired()])

    color = StringField("What is your favorite color?", validators=[DataRequired()])
    candy = StringField("What is your favorite candy?", validators=[DataRequired()])
    sport_team = StringField("What is your favorite sports team?", validators=[DataRequired()])
    snack = StringField("What is your favorite snack?", validators=[DataRequired()])
    movie = StringField("What is your favorite movie?", validators=[DataRequired()])
    visit = StringField("What is your favorite place to visit?", validators=[DataRequired()])
    food = StringField("What is your favorite food?", validators=[DataRequired()])
    soda = StringField("What is your favorite soda?", validators=[DataRequired()])
    animal = StringField("What is your favorite animal?", validators=[DataRequired()])
    holiday = StringField("What is your favorite Holiday?", validators=[DataRequired()])
    season = StringField("What is your favorite season?", validators=[DataRequired()])
    
    caffeine = SelectField("Caffeine Preference", choices=[("Black Coffee", "Black Coffee"), ("Latte", "Latte"), ("Cappuccino", "Cappuccino"), ("Cold Brew", "Cold Brew"), ("Espresso", "Espresso"), ("Flat White", "Flat White"), ("Tea with Honey", "Tea with Honey"), ("Tea with Lemon", "Tea with Lemon"), ("Iced Sweet Tea", "Iced Sweet Tea"), ("Energy drink", "Energy drink"), ("Other", "Other"), ("None", "None")], validators=[DataRequired()])

    submit = SubmitField("Submit")
    