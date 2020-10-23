from igramscraper.instagram import Instagram

from settings import user_id



instagram = Instagram()

#ПЕРЕПИСАТЬ ВСЕ В КЛАСС




def get_comments_point(score=None, media=None, point=2):

    if score is None:
        score = dict()
    if media is None:
        return score

    comments = instagram.get_media_comments_by_code(media.short_code, 10000)

    for comment in comments['comments']:
        if score.get(f'{comment.owner.username}') is None:
            score.update({f'{comment.owner.username}': point})
        else:
            current_points = score.get(f'{comment.owner.username}')
            score.update({f'{comment.owner.username}': current_points + point})






def get_likes_point(score=None, media=None, point=1):

    if score is None:
        score = dict()
    if media is None:
        return score

    likes = instagram.get_media_likes_by_code(media.short_code, 10000)

    for like in likes['accounts']:
        if score.get(f'{like.username}') is None:
            score.update({f'{like.username}': point})
        else:
            current_points = score.get(f'{like.username}')
            score.update({f'{like.username}': current_points+point})




def get_score():
    score = dict()

    medias = instagram.get_medias_by_user_id(user_id, count=3)

    for media in medias:
        get_likes_point(score, media)
        get_comments_point(score, media)

    return score


def get_the_most_active_users():
    score = get_score()
    dict_of_max_values = dict()

    max_value = score.get(max(score, key=score.get))

    for key, value in score.items():
        if value == max_value:
            dict_of_max_values.update({f'{key}': value})

    return dict_of_max_values
