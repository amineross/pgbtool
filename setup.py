from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
        name='pgbtool',
        version='0.1',
        author='Amine Rostane',
        author_email='amine.rostane@outlook.com',
        description='CLI backup tool for PostgreSQL databases',
        long_description=long_description,
        url='',
        packages=find_packages('src'),
        python_requires='>=3.6',
    )
