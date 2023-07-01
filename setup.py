from setuptools import setup, find_packages

classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Bug Tracking',
    ]

setup(
    name='pycomplexity',
    version='0.0.1',
    description='Measure complexity of your algorithm',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Hagai',
    author_email='n.simakoff@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=["asymptotic notation", "measure", "algorithm", "complexity", "time complexity", "bigo", "big-o", "bigomega", "big-omega", "bigtheta", "big-theta"],
    packages=find_packages(),
    requires=[''],
)