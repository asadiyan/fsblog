from post import new_post, get_post_path, get_post_content, get_post_title, get_post_ids
from comment import reply, get_comment_path, get_comment_ids
from comment import get_comment_content, get_comment_ip, get_comment_name
from utils import get_date_time

post_id = new_post("My new post", "I will tell it later.")
comment_id = reply(post_id, "Abi", "You are the best.", "localhost")
reply(post_id, "Hamidreza", "Yes I am :)", "localhost", comment_id)


def get_post_data(post_id: int) -> dict:
    post_path = get_post_path(post_id)
    post_date = get_date_time(post_path)
    post_content = get_post_content(post_id)
    post_title = get_post_title(post_id)

    list_of_comment_ids = get_comment_ids(post_id)
    comments = []
    for comment_id in list_of_comment_ids:
        comment_data = get_comment_data(post_id, comment_id)
        comments.append(comment_data)

    post_data = {
        'id': post_id,
        'date': post_date,
        'content': post_content,
        'title': post_title,
        'comments': comments
    }
    return post_data


def get_comment_data(post_id: int, comment_id: int) -> dict:
    comment_path = get_comment_path(post_id, comment_id)
    comment_date = get_date_time(comment_path)
    comment_content = get_comment_content(comment_path)
    comment_ip = get_comment_ip(comment_path)
    comment_name = get_comment_name(comment_path)

    comment_data = {
        'id': comment_id,
        'date': comment_date,
        'content': comment_content,
        'ip': comment_ip,
        'name': comment_name
    }
    return comment_data


def get_post_titles() -> list:
    results = []
    for i in get_post_ids():
        post_path = get_post_path(post_id)
        post_date = get_date_time(post_path)
        post_title = get_post_title(post_id)
        results.append({
            'id': i,
            'date': post_date,
            'title': post_title
        })
    return results


post_data = get_post_data(post_id)
comment_data = get_comment_data(post_id, comment_id)
print(post_data)
