from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
        name='pgbtool',
        version='1.0',
        author='Amine Rostane',
        author_email='amine.rostane@outlook.com',
        description='CLI backup tool for PostgreSQL databases',
        long_description=long_description,
        url='https://github.com/amineross/pgbtool.git',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=['boto3'],
        entry_points={
                'console_scripts': [
                    'pgbtool=pgbtool.cli:main'
                    ]
                },
        python_requires='>=3.6',
    )
