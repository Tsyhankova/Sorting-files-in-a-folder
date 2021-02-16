from setuptools import setup, find_packages


setup(
    name='clean_folder',
    version='1.0',
    description='Sorting_file_in_a_folder',
    author='Tatsiana Tsyhankova',
    packages=find_packages(),
    entry_points = {
        'console_scripts' : ['clean-folder = clean_folder.clean:main'],
        },
    )
        
