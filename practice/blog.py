"""
Design exercise: User class and Post class for a microblog application.
"""

from datetime import datetime
import uuid


class User:
    def __init__(self, first_name, last_name, username, password):
        # class variable = variable passed in
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.posts = []  # empty list
        self.friends = []  # no friends to start with

    def __str__(self):
        return str([self.first_name, self.last_name, self.username, self.password])

    def __repr__(self):
        return str([self.first_name, self.last_name, self.username, self.password])

    def write_post(self, text, is_public):
        # create a new Post and pass text + visibility in
        new_post = Post(text, is_public)
        # add it to self.posts
        self.posts.append(new_post)

    def print_posts(self):
        # print all the posts
        for post in self.posts:
            print(str(post))

    def get_post(self, post_id):
        # look through my list of posts for a post with matching post_id
        # if post_id can't be found just print an error message
        for post in self.posts:
            if post.id == post_id:
                return post
        print("Post not found")
        return None

    # my_list = ["a","c","d"]
    # del my_list[1] ---> deletes "c" using the index 1
    # my_list.remove("c") ---> find "c" AND remove it

    def delete_post(self, post_id):
        # creating a dummy post so we can look for this in self.posts
        post_to_delete = Post()
        post_to_delete.id = post_id

        self.posts.remove(post_to_delete)
        # for post in self.posts:
        # if post.id == post_id:
        #   self.posts.remove(post_id)

    def add_friend(self, new_friend):
        self.friends.append(new_friend)


# Posts -> written by a user
# 1 user can have many posts
class Post:
    def __init__(self, text="", is_public=True):
        self.id = uuid.uuid4()  # this will give each post a unique ID
        self.text = text
        self.is_public = is_public
        self.creation_date = datetime.now()
        self.edit_date = datetime.now()

    def __str__(self):
        return str([self.text, self.is_public, self.creation_date, self.edit_date])

    def __eq__(self, other_post):
        # return true if the post_ids are the same, otherwise return false
        return self.id == other_post.id

    def edit(self, new_text):
        # change self.text to next_text in this post
        # update self.edit_date in this post
        self.text = new_text
        self.edit_date = datetime.now()


my_user = User("Alice", "Smith", "asmith", "asklfdjkl;fj")
my_user.write_post(text="it was not too cold today", is_public=True)
my_user.write_post(text="now it's too hot", is_public=True)
my_user.write_post(text="I left my jacket at home", is_public=True)
my_user.write_post(text="it was not too cold today", is_public=True)
print(my_user)
my_user.print_posts()
post_to_edit = my_user.get_post(my_user.posts[1].id)
post_to_edit.edit("some new text here")
print(post_to_edit)

bob = User("Bob", "Adams", "badams", "asklfdjkl;fj")
# Alice adds Bob as a friend
my_user.add_friend(bob)
print(f"Alice's friends: {str(my_user.friends)}")

my_user.delete_post(my_user.posts[-1].id)
my_user.print_posts()
