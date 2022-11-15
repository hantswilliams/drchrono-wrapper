from setuptools import setup, find_packages

setup(
    name='drchrono-wrapper',
    version='0.0.1',
    license='MIT',
    author="Hants Williams",
    author_email='hantsawilliams@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/hantswilliams/drchrono-wrapper',
    keywords='drchrono api wrapper',
    install_requires=[
          'requests',
          'faker',
          'python-dotenv'
      ],

)
