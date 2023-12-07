from app import db, app
from config import SQLALCHEMY_DATABASE_URI
import os
import csv
from app.models import *
from werkzeug.security import generate_password_hash
import random

os.remove("app.db")

with app.app_context():
    db.create_all()

    with open("rollercoaster_data.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
            rc = Rollercoaster(
                name = row['name'],
                year = row['year'],
                height = row['height'],
                length = row['length'],
                manufacturer = row['manufacturer'],
                model = row['model'],
                inversions = row['inversions'],
                speed = row['speed']
            )
            db.session.add(rc)
    db.session.commit()

    usernames = ["evanwpm",
                 "Daulton Varsho",
                 "ninjamoomoo",
                 "epictomboygamer",
                 "George Springer",
                 "Shohei Ohtani",
                 "Juan Soto",
                 "Jram203"
                 ]

    for username in usernames:
        root = User(name=username, password=generate_password_hash("root", method='pbkdf2:sha256'))
        db.session.add(root)
        db.session.commit()

    for i in range(142):
        rollercoaster_id = random.randint(1,13)
        review_text = f"This is a review for rollercoaster {rollercoaster_id}. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Hello World <3"
        rating = round(random.uniform(5.0, 10.0),2)  # Random rating between 5.0 and 10.0
        user = random.randint(1,8)
        review = Review(user_id=user, rollercoaster_id=rollercoaster_id, rating=rating, review_text=review_text)
        db.session.add(review)
    db.session.commit()


#     reivew_test_text = """A timeless masterpiece, the epitome of thrill engineering, Alton Towers' Nemesis transcends the mere bounds of amusement park rides to stand as an unparalleled triumph of coaster craftsmanship. Nestled within the verdant embrace of the Staffordshire landscape, this marvel of engineering challenges gravity with an audacious defiance that leaves mere mortals breathless.

# From the very moment one sets eyes on the sinuous coils of Nemesis, a visceral anticipation grips the soul. As the roller coaster unfurls its labyrinthine twists and turns, it unveils a choreography of exhilaration, a ballet of adrenaline that dances upon the precipice of human experience. The interplay of G-forces and inversions unfolds with a precision that could only be conceived in the dreams of visionaries.

# The architectural prowess of Nemesis is not merely confined to its imposing structure; it extends to the symphony of elemental forces harnessed by B&M's engineering prowess. The guttural roars of steel against steel harmonize with the collective gasps of riders, creating a cacophony of excitement that reverberates through the very fabric of this theme park masterpiece.

# Nemesis, a monument to the audacity of human ingenuity, epitomizes the convergence of art and engineering. Its relentless assault on the senses is not for the faint-hearted but is a rhapsody for those seeking an odyssey into the heart of visceral exhilaration. Alton Towers' Nemesis stands not merely as a roller coaster but as an everlasting testament to the pursuit of boundary-pushing, spine-tingling, and utterly transcendent amusement park experiences.

# """

#     review = Review(user_id=1, rollercoaster_id=1, rating=7.6, review_text=reivew_test_text)
#     db.session.add(review)
#     db.session.commit()

#     review_2_test_text = """In the hallowed realms of amusement, where mere mortal rollercoasters dare to tread, Alton Towers unveils its pièce de résistance — Galactica. This cosmic symphony of engineering ingenuity and celestial allure transcends the ordinary, beckoning thrill-seekers to embark on a journey beyond the terrestrial confines of conventional amusement.

# From the very moment one sets foot in the shadow of Galactica, a palpable aura of transcendence encapsulates the discerning visitor. The minimalist aesthetic of the entrance foretells an experience not bound by the mundane, but rather an odyssey that flirts with the cosmic unknown.

# As the restraints embrace the willing acolyte, a sense of anticipation akin to an otherworldly prelude envelops the psyche. Galactica's departure is not merely a transition from station to summit; it is a departure from the known into the uncharted territories of gravity-defying elegance.

# """
#     review2 = Review(user_id=1, rollercoaster_id=2, rating=6.5, review_text=review_2_test_text)
#     db.session.add(review2)
#     db.session.commit()
