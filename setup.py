import io

from setuptools import find_packages
from setuptools import setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='ganapati',
    version='0.0.1',
    url='',
    license='BSD',
    maintainer='Thanathip Limna',
    maintainer_email='thanathip.l@coe.psu.ac.th',
    description='Basic web for CI/CD workflow.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask'],
    extras_require={'test': ['nosetests', 'coverage']},
)
