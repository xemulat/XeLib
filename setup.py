from distutils.core import setup
setup(
  name = 'XeLib',         # How you named your package folder (MyLib)
  packages = ['XeLib'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='mit',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Xems QOL Library',   # Give a short description about your library
  author = 'Xemulated',                   # Type in your name
  author_email = 'xemulated@tuta.io',      # Type in your E-Mail
  url = 'https://github.com/xemulat',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/xemulat/XeLib/archive/refs/tags/0.2.tar.gz',    # I explain this later on
  keywords = ['QOL', 'xemulated', 'downloader'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'colorama'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
