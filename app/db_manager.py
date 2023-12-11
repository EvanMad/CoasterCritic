from . import db
from . import models
from sqlalchemy import func
from datetime import datetime, timedelta

def get_average_score(rollercoaster_id):
        average_score = (
            db.session.query(func.avg(models.Review.rating))
            .join(models.Review.rollercoaster) 
            .filter(models.Review.rollercoaster_id == rollercoaster_id)
            .first()
        )[0]
        average_score = round(average_score,2)
        return average_score

def get_trending_rollercoasters(timestamp_trending_treshold):
    # Trending rollercoasters in the last 36 hours
    trending_rollercoasters = (
        models.Rollercoaster.query
        .join(models.Review, models.Rollercoaster.id == models.Review.rollercoaster_id)
        .join(models.Likes, (models.Review.id == models.Likes.review_id) & (models.Review.user_id == models.Likes.user_id))
        .filter(models.Likes.created_at >= timestamp_trending_treshold)
        .group_by(models.Rollercoaster.id)
        .order_by(func.count(models.Likes.user_id).desc())
        .limit(5)
        .all()
    )
    # If there's no review likes in last 36 hours, then use total review likes as backup
    if len(trending_rollercoasters) == 0:
        trending_rollercoasters = (models.Rollercoaster.query
        .join(models.Review, models.Rollercoaster.id == models.Review.rollercoaster_id)
        .group_by(models.Rollercoaster.id)
        .limit(5)
        .all()
    )

    trending_rollercoasters_data = []
    for rollercoaster in trending_rollercoasters:
        average_score = get_average_score(rollercoaster.id)
        trending_rollercoasters_data.append({'rollercoaster': rollercoaster, 'average_score': average_score})
    return trending_rollercoasters_data

def get_trending_review(timestamp_trending_treshold):
    # Trending review with most likes in the last 36 hours
    trending_review = (
        models.Review.query
        .join(models.Likes, (models.Review.id == models.Likes.review_id) & (models.Review.user_id == models.Likes.user_id))
        .filter(models.Likes.created_at >= timestamp_trending_treshold)
        .order_by(models.Likes.created_at.desc())
        .first()
    )
    # If there's no review likes in last 36 hours, then use total review likes as backup
    if(trending_review == None):
        # Review with most likes
        trending_review = (models.Review.query
            .order_by(models.Review.likes.desc())
            .first()
    )
    return trending_review

def get_highest_rollercoaster():
    highest_rated_rollercoasters = (models.Rollercoaster.query
        .outerjoin(models.Review)
        .group_by(models.Rollercoaster.id)
        .order_by(func.avg(models.Review.rating).desc())
        .limit(5)
        .all()
    )

    average_scores = {rollercoaster.id: get_average_score(rollercoaster.id) for rollercoaster in highest_rated_rollercoasters}
    highest_rated_rollercoasters.sort(key=lambda rollercoaster: average_scores.get(rollercoaster.id, 0), reverse=True)

    highest_rated_rollercoasters = {'rollercoasters': highest_rated_rollercoasters, 'average_scores': average_scores}


    return highest_rated_rollercoasters, average_scores

def get_most_liked_users():
    # User with most review likes
    most_liked_users_data = (models.User.query 
        .join(models.Review, models.User.id == models.Review.user_id) 
        .group_by(models.User.id) 
        .with_entities(models.User, func.sum(models.Review.likes).label('total_likes'))
        .order_by(func.sum(models.Review.likes).desc())
        .limit(5)
        .all()
    )

    # Extract relevant information
    most_liked_users = [{'user': user_data[0], 'total_likes': user_data.total_likes} for user_data in most_liked_users_data]
    return most_liked_users