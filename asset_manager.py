import os

Assets_dir = os.path.join(os.path.dirname(__file__), "Assets")
def get_asset_path(filename):
    """Return the full path to an asset file."""
    return os.path.join(Assets_dir, filename)