import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()
    
setuptools.setup(
    name='pysign-jeertmans',
    version='0.1',
    author='Jérome Eertmans',
    author_email='jeertmans@icloud.com',
    description='checking function signature',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jeertmans/pysign',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    license='MIT',
    python_requires='>=3'
)
