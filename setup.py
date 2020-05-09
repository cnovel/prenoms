import prenoms
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name=prenoms.__title__,
    version=prenoms.__version__,
    author=prenoms.__author__,
    author_email='pypi-prenoms@kosmon.fr',
    url="https://github.com/cnovel/prenoms",
    description="Générateur de noms aléatoire",
    long_description_content_type='text/markdown',
    long_description=readme,
    license=prenoms.__license__,
    packages=find_packages(),
    package_data={'prenoms': ['dist.*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'names = prenoms.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='test_prenoms',
)
