CORS_URLS_REGEX = r'^/api/.*$' # CORS HEADERS ENBALED
# CORS_ORIGIN_WHITELIST = (
#     'localhost:8000',
#     'localhost:4200',
#     '192.168.2.107:8000'
# )
CORS_ORIGIN_ALLOW_ALL = True

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + (
    'X-CSRFToken',
)