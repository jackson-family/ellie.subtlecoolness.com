import json
import pathlib

package_json = json.loads(pathlib.Path("package.json").read_text())
BOOTSTRAP_VERSION = package_json.get("dependencies").get("bootstrap")

# WARNING Feeds generated without SITEURL set properly may not be valid
SITEURL = "https://ellie.subtlecoolness.com"

# WARNING No timezone information specified in the settings. Assuming your timezone is UTC for feed generation.
TIMEZONE = "America/Chicago"

# Default path is working directory, so change to "content" directory
PATH = "content"

# Article urls
ARTICLE_SAVE_AS = "{category}/{slug}.html"
ARTICLE_URL = "{category}/{slug}"
ARTICLE_ORDER_BY = "basename"

# Set the theme
THEME = "themes/default"

# Read default date for content from file system
DEFAULT_DATE = "fs"

# I don't want to remember to delete the output directory before every build
DELETE_OUTPUT_DIRECTORY = True

# Some files need to land in special locations
EXTRA_PATH_METADATA = {"images/gitignore.txt": {"path": ".gitignore"}}

# I don't want the default archive, author, category, and tag pages
ARCHIVES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAGS_SAVE_AS = ""

# Disable default Atom feed
CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_ATOM = None

SITENAME = "Ellie&#x02bc;s Corner"
