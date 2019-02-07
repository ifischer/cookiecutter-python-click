from setuptools import setup, find_packages

setup(
    name='example_project',
    description='example_description',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'example_cliscript=example_module.commands:cli'
        ]
    },
    python_requires='>=3.7'
)
