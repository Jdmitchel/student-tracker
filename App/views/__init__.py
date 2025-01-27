# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .course import course_views
from .review import review_views
from .student import student_views

views = [user_views, index_views, auth_views, course_views, student_views] 
# blueprints must be added to this list