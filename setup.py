"""
Creating PIPY package instruction:

python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist
python3 -m pip install --user --upgrade twine
twine check dist/*
twine upload dist/*
"""

from setuptools import setup, find_packages
from numpy.distutils.core import setup, Extension
from os import path
import io

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

if __name__ == "__main__":
    setup(name = 'coastsat',
          author            = "kvos",
          author_email      = "https://github.com/kvos/CoastSat",
          url               = "https://github.com/kvos/CoastSat",
          version           = "0.0.2",
          description       = "Coastal Processes, Environments & Systems.",
          long_description  = long_description,
          long_description_content_type='text/markdown',
          packages          = ['coastsat'],
          install_requires  = [
                        'numpy>=1.16.3',
                        'earthengine-api==0.1.236',
                        'geopandas==0.4.1',
                        'pytz==2020.1',
                        'spyder==3.3.4',
                        'pandas>=0.25',
                        'seaborn>=0.9',
                        'matplotlib==3.0.3',
                        'scipy>=1.2.1',
                        'shapely>=1.6.4',
                        'scikit-image>=0.15.0',
                        'scikit-learn>=0.20.3',
                        'astropy=3.2.1',
                        ],
          python_requires   = '>=3.7',
          # package_data      = {'coastsat': ['Notebooks/notebooks/*ipynb',
          #                                 'Notebooks/notebooks/*py'] },
          include_package_data = True,
          classifiers       = ['Programming Language :: Python :: 3.7']
          )
