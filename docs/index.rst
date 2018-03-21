.. PyIonic documentation master file, created by
   sphinx-quickstart on Wed Mar 21 08:12:26 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyIonic's documentation!
===================================

PyIonic is a Python library to interact with Ion Channel's API.

Example
---------------

Install PyIonic:
```
pip install pyionic
```

Set the IONCHANNEL_TOKEN:
```
export IONCHANNEL_TOKEN=####IONCHANNEL_TOKEN####
```

Write code:
```python
from pyionic import core

vuln = core.Vulnerability()
vulnerabilities = vuln.get_vulnerabilities('python', '3.4')
print('%s total vulnerabilities found.' % vulnerabilities['meta']['total_count'])
```

Run code:
```
python test.py
7 total vulnerabilities found.
```

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
