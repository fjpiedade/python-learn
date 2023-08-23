#import user - user.
from user import User

app_user_one = User("raiz@tech.phi", "Raiz Tech", "pws", "Software Developer")
app_user_one.get_user_info()
app_user_one.change_job_title("Software Engineer")
app_user_one.get_user_info()
