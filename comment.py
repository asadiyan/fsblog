import os
import pathlib

from settings import WORK_PATH
from post import create_directory, create_file, get_post_path


def generate_comment_id(post_id: int) -> int:
    """This function creats a new directoy inside posts with post id and
    returns it.

    :rtype: int
    """

    max_comment_id = 0

    for i in get_comment_ids(post_id):
        if i > max_comment_id:
            max_comment_id = i

    comment_id = max_comment_id + 1
    comment_path = get_comment_path(post_id, comment_id)

    # Create folder
    create_directory(comment_path)

    # Return id
    return comment_id


def get_comment_ids(post_id: int) -> list:
    """
    """
    post_path = get_post_path(post_id)
    comments_path = f'{post_path}/comments'
    list_of_files_and_folders = os.listdir(comments_path)

    list_of_folders = []
    for p in list_of_files_and_folders:
        path = f'{comments_path}/{p}'
        if os.path.isdir(path):
            list_of_folders.append(p)

    list_of_post_ids = []
    for p in list_of_folders:
        if int(p) > 0:
            list_of_post_ids.append(int(p))

    return list_of_post_ids


def get_comment_path(post_id: int, comment_id: int) -> str:
    post_path = get_post_path(post_id)
    return f'{post_path}/comments/{comment_id}'


def reply(post_id: int, name: str, content: str, ip: str, ref: int=None):
    comment_id = generate_comment_id(post_id)
    comment_path = get_comment_path(post_id, comment_id)
    
    ip_file_path = f'{comment_path}/ip.txt'
    create_file(ip_file_path, ip)
    
    name_file_path = f'{comment_path}/name.txt'
    create_file(name_file_path, name)
    
    content_file_path = f'{comment_path}/content.txt'
    create_file(content_file_path, content)

    if ref is not None:
        ref_file_path = f'{comment_path}/ref.txt'
        create_file(ref_file_path, str(ref))

    return comment_id


