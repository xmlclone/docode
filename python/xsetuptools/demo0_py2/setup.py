from setuptools import setup, find_packages

version = '1.1.0'

setup(
    name='mgairflistener',
    version=version,
    packages=find_packages(),
    install_requires=[
        "requests>=2.18.0",
        "robotframework>=3.0.0"
    ],
    description='mg test group ai automation analysis robotframework listener.',
    python_requires='>=2.7',
    author='xmlclone',
    author_email='xmlclone@gmail.com',
    setup_requires=['setuptools', 'wheel'],
)
# python setup.py sdist bdist_wheel