pythonineducation.org
=====================

.. image:: https://travis-ci.org/python/pythonineducation.org.svg?branch=master
       :target: https://travis-ci.org/python/pythonineducation.org
-> For the better understanding go to http://pythonineducation.org/ website.
This is the website for the http://pythonineducation.org/ website. It is hosted
via GitHub Pages.

If you have a suggestion to make, please feel free to create an issue_.

We welcome pull requests for improvements! (Please see CONTRIBUTING.rst_ for
more details).

Development
~~~~~~~~~~~

This site uses wok_. To install wok and other dependencies, run
``pip install -r requirements.txt``. wok currently only works with Python 2.7.

wok builds the site by assembling several components:

* Pages are found in ``content/``. Pages may be HTML, Markdown_ or reStrcturedText_, and contain some YAML metadata.
* Statuc files are found in ``media/``.
* The various jinja2_ templates for pages can be found in ``templates/``.

To build the site, run ``make build``. This pulls together all the components
into a set of HTML files in ``output/``.

Windows users: you need to run the (extensionless) ``wok`` script in
``c:\pythonxx\scripts``. e.g. ``py -2 c:\python27\scripts\wok``.

Alternatively, if you run ``make serve``, wok will build the site, serve the
built site on port 8000, and watch for changes.

Windows users: you ned to run the (extensionless) ``work`` script with the
``--serve`` parameter in ``c:\pythonxx\scripts``. e.g.
``py -2 c:\python27\scripts\wok --serve``.

You can test that the site contains no broken links and that various common
mis-spellings are caught correctly (hint, it's a "BBC micro:bit" for example)
by running ``make test``.

Travis will test branches, and branches won't get merged without review and
passing tests, so dive in!


Internationalisation
~~~~~~~~~~~~~~~~~~~~

Python is used all over the world. Education takes place all over the world!

This site should be available to people for whom English is not a native
language.

As a result and *from the very start of our development process* we have made
it easy for contributions to be made in different languages. Here's how it
works:

* Each language specific version of the site lives under a path containing the
  `ISO 639-1 <https://en.wikipedia.org/wiki/ISO_639-1>`_ language code. For
  example, the English version is found under the ``/en`` path whereas the
  German version is under the ``/de`` path.
* In the ``template/`` directory of this repository as the page templates for
  different languages. All inherit from the ``base.html`` template. They are
  named ``page_XX.html`` where XX is the appropriate ISO 639-1 code for the
  language for which the template is used. For example, English content uses
  the ``page_en.html`` template whereas the German template is
  ``page_de.html``. These pages should contain the localised header and footer.
* In the ``content/`` directory of this repository are directories named after
  the ISO 639-1 language code. They contain the content for this website in
  the langauge referenced by the language code in the name of the directory.
  For example, the English content is found in the ``content/en/`` directory
  whereas the German content is in ``content/de/``. You must make sure that
  the ``type`` field in the YAML header for the content is set to the correct
  page template for the language.
* If in doubt, just look at what happens in the English version of the site and
  adapt to the desired language.

Deployment
~~~~~~~~~~

The site is hosted as a Project Page on GitHub Pages, and so it is the
``gh-pages`` branch of the repository that gets served. wok generates the site
in the ``output/`` directory, and Travis is configured to push any changes to
the ``output/`` directory to this branch. See ``deploy.sh`` for details.

This should be done automatically by Travis after it has built the ``master``
branch, but in case this does not happen, somebody with commit access to the
repository can run ``make deploy``.

When setting up Travis to run this initially you must provide an OAuth token
for authentication in the ``GH_TOKEN`` env var. To do this create a
`Personal Access Token on GitHub <https://github.com/settings/tokens>`_ then
create the ``GH_TOKEN`` key pair on the Travis
`settings page <https://travis-ci.org/python/pythonineducation.org/settings>`_
for the project.

Note: this is tied to a single user on GitHub, however any other GitHub user
with valid permissions can replace the key on Travis.

.. _wok: http://wok.mythmon.com/
.. _Markdown: https://pythonhosted.org/Markdown/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _jinja2: http://jinja.pocoo.org/
.. _issue: https://github.com/python/pythonineducation.org/issues
.. _CONTRIBUTING.rst: ./CONTRIBUTING.rst
