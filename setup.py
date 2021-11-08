from setuptools import setup, find_packages

# with open('README.md') as readme_file:
#    readme = readme_file.read()

requirements = []

extra_requirements = {}

if extra_requirements:
    extra_requirements["all"] = list(set.union(*(set(i) for i in extra_requirements.values())))

setup_requirements = []  # ['pytest-runner', ]

test_requirements = []  # ['pytest>=3', ]


setup(
    author="ALBA Controls",
    author_email='controls@cells.es',
    maintainer='ctbeamlines',
    maintainer_email='ctbeamlines@cells.es',
    python_requires='>=3.5',
    classifiers=[
        # How mature is this project? Common values are
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Python library to easily configure the python logging.",
    entry_points={},
    install_requires=requirements,
    extras_require=extra_requirements,
    license="GNU General Public License v3",
    # long_description=readme + '\n\n' + history,
    long_description="""Python library to easily configure the python logging
    from a configuration file.""",
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='logging',
    name='logger',
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='',
    version='0.2.3',
    zip_safe=False,
)
