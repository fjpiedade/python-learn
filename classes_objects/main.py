# import user - user
from user import User
import post

app_user_one = User("raiz@tech.phi", "Raiz Tech", "pws", "Software Developer")
app_user_one.get_user_info()
app_user_one.change_job_title("Software Engineer")
app_user_one.get_user_info()

new_post = post.Post("Love for perfect place", app_user_one.name)
new_post.get_post_info()
