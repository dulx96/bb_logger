from distutils.core import setup
setup(
    name='bb_logger',
    packages=['bb_logger'],
    version='0.1',
    # Chose a license from here:
    # https://help.github.com/articles/licensing-a-repository
    license='MIT',
    description='setup logger bb',
    author='le du',
    author_email='dulx96@gmail',
    # Provide either the link to your github or to your website
    url='https://github.com/dulx96/bb_logger.git',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
        # I explain this later on
    keywords=['BB', 'LOGGER', 'LOGGING'],
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3'
    ],
)
