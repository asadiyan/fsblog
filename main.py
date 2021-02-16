import os
import pathlib

WORK_PATH = "/tmp/posts"


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
    pathlib.Path(post_path).mkdir(parents=True, exist_ok=True)

    # Return id
    return post_id


def get_post_ids() -> list:
    """
    """
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


def new_post(title: str, content: str) -> int:
    post_id = generate_post_id()
    post_dir = get_post_path(post_id)


new_post("My new post", "I will tell it later.")