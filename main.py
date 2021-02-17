from post import new_post
from comment import reply

post_id = new_post("My new post", "I will tell it later.")
comment_id = reply(post_id, "Abi", "You are the best.", "localhost")
reply(post_id, "Hamidreza", "Yes I am :)", "localhost", comment_id)

