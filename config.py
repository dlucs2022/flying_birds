import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
CACHE_DIR = os.path.join(CURRENT_DIR, "upload", "cache")

if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)
