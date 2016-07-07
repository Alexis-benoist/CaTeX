from setuptools import setup
try:
    with open('readme.rst') as f:
        long_description = f.read()
except IOError:
    with open('readme.md') as f:
        long_description = f.read()


def read_version():
    with open('catex/version.py') as f:
        code = f.readlines()[0]
    exec(code)
    assert('version' in locals())
    return locals()['version']

setup(
    name='CaTeX',

    version=read_version(),

    description='CaTeX Concatenates LateX documents.',
    long_description=long_description,

    # The project's main homepage.d
    url='https://github.com/Alexis-benoist/catex',

    # Author details
    author='Alexis Benoist',
    author_email='alexis@benoist.it',

    # Choose your license
    license='Apache License 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='latex',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=[
        'catex',
    ],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'click==6.6'
    ],
    entry_points={
        'console_scripts': [
            'catex=catex.cli:cli',
        ],
    },
)
