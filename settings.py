import os

# we assume that the cloned parent directory name equals the cloned repo name
path = os.path.normpath(os.path.dirname(os.path.realpath(__file__)))
abs_path = os.path.abspath(os.path.join(path, '..'))
REPO_NAME = os.path.basename(abs_path)

APP_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = APP_DIR

# in order to deploy to github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = os.path.join(PROJECT_ROOT, '..')

# since this is a repo page (not a github user page),
# we need to set the base_url to the correct url as per gh pages' standards
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)

# IMPORTANT: if this is True, all app files
# will be deleted when you run the freezer
# NEVER set to True - i tried and erased one hour of work
FREEZER_REMOVE_EXTRA_FILES = False
