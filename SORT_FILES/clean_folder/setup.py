from setuptools import setup

setup(
    name = 'clean_folder',
    version = '1.0',
    description = 'Script which sort files in the folder by file extension',
    author = 'Kinga KG',
    packages = ['clean_folder'],
    entry_points = {'console_scripts': ['clean_folder = clean_folder.clean:main']}
    )