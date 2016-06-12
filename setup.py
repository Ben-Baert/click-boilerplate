from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='<reponame>',
      version='0.0.1',
      description='<short_description>',
      long_description=readme(),
      url='http://github.com/<username>/<reponame>',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'License :: OSI Approved :: MIT License'],
      author='<full author name>',
      author_email='<email address>',
      license='MIT',
      packages=['<reponame>', '<reponame>.commands'],
      install_requires=['click'],
      include_package_data=True,
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      entry_points='''
              [console_scripts]
              <reponame>=<reponame>.cli:cli
              ''',
      zip_safe=False)
