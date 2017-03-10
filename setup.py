from setuptools import setup

setup(name='logicaldoc',
      version='0.0.1',
      description='LogicalDoc API library',
      url='http://github.com/storborg/funniest',
      author='Francesco Apruzzese',
      author_email='cescoap@gmail.com',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='logicaldoc api',
      license='AGPL',
      packages=['logicaldoc'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
