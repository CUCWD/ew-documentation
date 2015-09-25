###################
EducateWorkforce Documentation
###################

The ew-documentation repo contains source files for most of the documentation
for the EducateWorkforce platform. This repo is managed by the EducateWorkforce
Documentation team.

API documentation that includes docstrings from code files is stored in the
repository of that module.

Documentation for developers, researchers, course staff, and students is
located in the language-specific subdirectories. 

******************************
View Published Documentation
******************************

EducateWorkforce documentation is published through Read the Docs. Links to all published
documentation are available through `support.educateworkforce.com`_.

.. _support.educateworkforce.com: https://support.educateworkforce.com

******************************
Submit Documentation Issues
******************************

We welcome input from the community on any documentation issues.  You can
submit issues to the Documentation project in the `EducateWorkforce Support JIRA board`_.

.. _EducateWorkforce Support JIRA board: https://cwd-team.ces.clemson.edu/jira/secure/RapidBoard.jspa?rapidView=6&view=null

You can also email support@educateworkforce.com.

**********************************
Contribute to EducateWorkforce Documentation
**********************************

You, the user community, can help update and revise EducateWorkforce documentation.

EducateWorkforce documentation is created using `RST`_ files and `Sphinx`_.

.. _RST: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org

To suggest a revision, fork the project, make changes in your fork, and submit
a pull request back to the original project: this is known as the `GitHub
Flow`_.

.. _GitHub Flow: https://github.com/blog/1557-github-flow-in-the-browser

All pull requests need approval from EducateWorkforce. For more information, contact EducateWorkforce at
support@educateworkforce.com.

Before submitting a pull request, it is recommend you run the test suite on
your contribution to ensure it can be compiled without errors.

To run a test compilation of a contribution, first install the prerequisites:

.. code::
  
  pip install -r shared/travis_requirements.txt

Then run the tests:

.. code::

  ./run_tests.sh

Additionally, you can run tests for a single project:

.. code::
  
  ./run_tests.sh en_us/install_operations/

A convenience script is provided to help you develop new documentation. To use
it you must first install the optional tools, and then run the script.

.. code::

  pip install -r shared/tools.txt
  ./develop.sh en_us/install_operations/

It will output a line of text that looks like this:

::

  Serving on http://127.0.0.1:9090

You can copy this URL into a web browser to see the HTML output for your
project.

The command starts an HTTP server that renders the HTML for the project. This
HTTP server also monitors the project and detects any changes. When you save a
change to a file, the server rebuilds the HTML and refreshes your browser
automatically. In this way you can rapidly see how changes you make will be
rendered as HTML.
