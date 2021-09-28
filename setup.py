import os
import re

from setuptools import find_packages, setup

regexp = re.compile(r'.*__version__ = [\'\"](.*?)[\'\"]', re.S)

base_package = 'datapipeline_tests'
base_path = os.path.dirname(__file__)

init_file = os.path.join(base_path, 'src', 'datapipeline_tests', '__init__.py')
with open(init_file, 'r') as f:
    module_content = f.read()

    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError(
            'Cannot find __version__ in {}'.format(init_file))

with open('README.rst', 'r') as f:
    readme = f.read()

with open('CHANGELOG.rst', 'r') as f:
    changes = f.read()

def parse_requirements(filename):
    ''' Load requirements from a pip requirements file '''
    with open(filename, 'r') as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines

requirements = parse_requirements('requirements.txt')


if __name__ == '__main__':
    setup(
        name='datapipeline_tests',
        description='A project to implement data pipeline testing',
        long_description='\n\n'.join([readme, changes]),
        license='Not open source',
        url='https://github.com/somasays/datapipeline_tests',
        version=version,
        author='Soma Sundaram Sekar',
        author_email='soma.sekar@hellofresh.com',
        maintainer='Soma Sundaram Sekar',
        maintainer_email='soma.sekar@hellofresh.com',
        install_requires=requirements,
        keywords=['datapipeline_tests'],
        package_dir={'': 'src',
                     'dags': 'dags'},
        packages=(
            find_packages('src') +
            find_packages(where='./dags')
        ),
        zip_safe=False,
        classifiers=['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8']
    )
