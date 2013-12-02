from distutils.core import setup
import py2exe
setup(
    windows = [
    {
        "script": "selectFile.py",
        "icon_resources": [(1, "ico/Rename.ico")]
    }
    ],
)