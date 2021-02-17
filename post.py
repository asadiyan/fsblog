import os
import pathlib

from settings import WORK_PATH


def get_post_path(post_id: int) -> str:
    return f'{WORK_PATH}/{post_id}'


def generate_post_id() -> int:
    """This function creats a new directoy inside posts with post id and
    returns it.

    :rtype: int
    """

    max_post_id = 0
    for i in get_post_ids():
        if i > max_post_id:
            max_post_id = i

    post_id = max_post_id + 1
    post_path = get_post_path(post_id)

    # Create folder
    create_directory(post_path)

    # Return id
    return post_id


def create_directory(path: str):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)


def create_file(file_path: str, data: str):
    with open(file_path, 'w') as fi:
        fi.write(data)


def get_post_ids() -> list:
    """
    """
    create_directory(WORK_PATH)
    list_of_files_and_folders = os.listdir(WORK_PATH)

    list_of_folders = []
    for p in list_of_files_and_folders:
        path = f'{WORK_PATH}/{p}'
        if os.path.isdir(path):
            list_of_folders.append(p)

    list_of_post_ids = []
    for p in list_of_folders:
        if int(p) > 0:
            list_of_post_ids.append(int(p))

    return list_of_post_ids



def create_post_title_file(post_id: int, title: str):
    post_path = get_post_path(post_id)
    file_path = f'{post_path}/title.txt'
    create_file(file_path, title)


def create_post_content_file(post_id: int, content: str):
    post_path = get_post_path(post_id)
    file_path = f'{post_path}/content.txt'
    create_file(file_path, content)


def create_comments_directory(post_id: int):
    post_path = get_post_path(post_id)
    comment_path = f'{post_path}/comments'
    create_directory(comment_path)

def new_post(title: str, content: str) -> int:
    post_id = generate_post_id()
    create_post_title_file(post_id, title)
    create_post_content_file(post_id, content)
    create_comments_directory(post_id)
    return post_id


