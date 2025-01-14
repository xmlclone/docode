from setuptools import setup, find_packages

setup(
    # [project]
    name='xmltest',
    version='1.0.0',
    install_requires=[
        "requests>=2.31.0",
        "selenium",
        "robotframework~=5.1", # 可以是 5.1 或之后的版本，但不能是 5.0 及之前，也不能是 6.0 及之后的版本
        "schedule>1.0,<2.0", # 区间范围
    ],

    # [tool.setuptools.packages.find]
    packages=find_packages(
        # All keyword arguments below are optional:
        where='.',  # '.' by default
        include=['xmltest'],  # ['*'] by default
        exclude=[],  # empty by default
    ),

    # [tool.setuptools]
    include_package_data=True,

    # [project.scripts]
    entry_points={
        'console_scripts': [
            'xmltest = xmltest.__main__:main',
        ]
    }
)