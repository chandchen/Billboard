from setuptools import setup, find_packages

setup(
    name="superman",
    version="1.0",
    url="https://github.com/changduchen/Superman.git",
    license="BSD",
    description="Build a complete blog application, ready for production use.",
    author="changduchen",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools',
                      'pytz',
                      'Pillow',
                      ],
)
