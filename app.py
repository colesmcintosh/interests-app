from flask import Flask, render_template, redirect, url_for, session
from forms import Interests
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secrets
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config["SECRET_KEY"] = secrets.token_urlsafe(32)

@app.route('/', methods=["GET", "POST"])
def home():
    interests = Interests()
    
    first_name = interests.first_name
    last_name = interests.last_name
    
    color = interests.color
    candy = interests.candy
    sport_team = interests.sport_team
    snack = interests.snack
    movie = interests.movie
    visit = interests.visit
    food = interests.food
    soda = interests.soda
    animal = interests.animal
    holiday = interests.holiday
    season = interests.season

    caffeine = interests.caffeine
    submit = interests.submit

    if interests.validate_on_submit():

        sender_email = os.getenv('SENDER_EMAIL')
        receiver_email = os.getenv('RECIEVER_EMAIL')
        g_key = os.getenv('G_KEY')

        message = MIMEMultipart("alternative")
        message["Subject"] = f"{str(first_name.data).title()} {str(last_name.data).title()}'s interests!"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = f"""\
{str(first_name.data).title()} {str(last_name.data).title()} has submitted their interests! Here they are:

        Favorite Color: {str(color.data).title()}
        Favorite Candy: {str(candy.data).title()}
        Favorite Sports Team: {str(sport_team.data).title()}
        Favorite Snack: {str(snack.data).title()}
        Favorite Movie: {str(movie.data).title()}
        Favorite Place to Visit: {str(visit.data).title()}
        Favorite Food: {str(food.data).title()}
        Favorite Soda: {str(soda.data).title()}
        Favorite Animal: {str(animal.data).title()}
        Favorite Holiday: {str(holiday.data).title()}
        Favorite Season: {str(season.data).title()}
        Caffeine Prefercne: {str(caffeine.data).title()}

Thanks for using Cole's interest platform!

- Sent with Python :)
        """
        # html = """\
        # <html>
        # <body>
        #     <p>Hi,<br>
        #     How are you?<br>
        #     <a href="http://www.realpython.com">Real Python</a> 
        #     has many great tutorials.
        #     </p>
        # </body>
        # </html>
        # """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        # part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        # message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, g_key)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        
        session['first_name'] = first_name.data


        return redirect(url_for('thank'))
    



    return render_template('index.html',
    interests=interests,
    first_name=first_name,
    last_name=last_name,
    color=color,
    candy=candy,
    sport_team=sport_team,
    snack=snack,
    movie=movie,
    visit=visit,
    food=food,
    soda=soda,
    animal=animal,
    holiday=holiday,
    season=season,
    caffeine=caffeine,
    submit=submit)
    

@app.route("/thank")
def thank():
    first_name = session.get("first_name",None)
    return render_template("thanks.html", first_name=first_name)

if __name__ == '__main__':
    app.run()