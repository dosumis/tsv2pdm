from distutils.core import setup
setup(
  name = 'dosumis.tsv2pdm',
  packages = ['dosumis.tsv2pdm'], # this must be the same as the name above
  version = '0.1',
  description = 'A lightweight system for loading, '
                'manipulating and saving tsv files via simple' \
                'Python data model intermediates.  ' \
                'Has some spreadsheet-like features.',
  author = 'David Osumi-Sutherland',
  author_email = 'dosumis@gmail.com',
  url = 'https://github.com/dosumis/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['tsv', 'spreadsheet', 'csv'], # arbitrary keywords
  classifiers = [],
)