from setuptools import setup, find_packages

setup(
    name='pythonodbc',
    version='1.0.0',
    # packages=["impodbc"],
    py_modules=['pythonodbc'],
    # packages=find_packages(),
    #url='python repo url'
    install_requires=[
        'pyodbc == 4.0.32'
    ],
    entry_points={
    })


# pip install wheel
#python setup.py bdist_wheel