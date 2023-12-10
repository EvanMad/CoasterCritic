from . import db
from . import models
from sqlalchemy import func

def get_average_score(rollercoaster_id):
        average_score = (
            db.session.query(func.avg(models.Review.rating))
            .join(models.Review.rollercoaster) 
            .filter(models.Review.rollercoaster_id == rollercoaster_id)
            .first()
        )[0]
        average_score = round(average_score,2)
        return average_score