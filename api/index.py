import os
import sys

# Add the project root to the Python path so imports work
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_course_correct.settings')

app = get_wsgi_application()