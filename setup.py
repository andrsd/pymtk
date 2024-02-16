from setuptools import setup, find_packages
import os.path as op

with open(op.join(op.dirname(op.realpath(__file__)), 'pymtk',
                  '_version.py')) as version_file:
    exec(version_file.read())

install_requires = [
    'matplotlib'
]
tests_require = [
    'pytest>=7.1.0'
]
setup_requires = [
]

setup(
    name='pymtk',
    version=__version__,
    description='Simple support classes for creating meshes for finite element analysis',
    url='https://github.com/andrsd/pymtk',
    author='David Andrs',
    author_email='andrsd@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=setup_requires
)
