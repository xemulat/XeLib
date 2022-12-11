from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'XeLib',
  packages = ['XeLib'],
  version = '0.9',
  license='mit',
  description = "Xemulated's QOL Library",
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Xemulated',
  author_email = 'xemulated@tuta.io',
  url = 'https://github.com/xemulat',
  download_url = 'https://github.com/xemulat/XeLib/archive/refs/tags/0.9.tar.gz',
  keywords = ['QOL', 'xemulated', 'downloader'],
  install_requires=['colorama', 'ping3', 'tqdm'],
  classifiers=[
    'Development Status :: 4 - Beta',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.10',
  ],
)