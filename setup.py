import os
from distutils.core import setup
 
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
 
README = read('README.markdown')
 
setup(
    name = "django-qimg",
    version = "0.5.1",
    url = 'http://github.com/issackelly/django-qimg',
    license = 'MIT',
    description = "Dynamically Create Images of any size for quick wireframes",
    long_description=README,
 
    author = 'Issac Kelly',
    author_email = 'issac@issackelly.com',
    packages = [
        'qimg',
        'qimg.templatetags',
    ],
    package_data = {
        'qimg': [
                'fonts/CartoGothic-Std/*',
            ],
    },
    requires = [
        'PIL',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers and Webdesigners',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)