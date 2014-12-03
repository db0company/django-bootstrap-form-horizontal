import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bootstrap-form-horizontal',
    version='0.0.1',
    packages='bootstrap_form_horizontal',
    include_package_data=True,
    license='BSD License',
    description='Templates for bootstrap3 style horizontal forms',
    long_description=README,
    url="https://github.com/yourcelf/django-bootstrap-form-horizontal",
    author="Charlie DeTar",
    author_email="cfd@media.mit.edu",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "license :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)
