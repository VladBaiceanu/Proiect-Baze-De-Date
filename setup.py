from setuptools import setup

APP = ['MainPageGUI.py']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app = APP,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app']
)