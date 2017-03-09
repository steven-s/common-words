from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
        name='common-words',
        version='0.0.1',
        description='common words translator',
        long_description=readme,
        author='Steven Samson',
        author_email='steven.a.samson@gmail.com',
        url='https://github.com/steven-s/common-words',
        license=license,
        packages=find_packages(exclude=('tests'))
)
