from distutils.core import setup
setup(
  name = 'bios',         # How you named your package folder (MyLib)
  packages = ['bios'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='GNU Affero General Public License v3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'bios is a library which helps you to read and write data to determined type of files.',   # Give a short description about your library
  author = 'Bilgehan NAL',                   # Type in your name
  author_email = 'bilgehannal@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/bilgehannal/bios',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/bilgehannal/bios/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['io', 'read', 'write', 'file'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Affero General Public License v3.0',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)