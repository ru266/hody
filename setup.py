from setuptools import setup, find_packages

setup(
    name='hody',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    author='Hody Milo',
    author_email='hodymilo@aol.com',
    description='Twitter account information fetcher',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ru266/hody',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)