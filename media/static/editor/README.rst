BBC micro:bit MicroPython Editor for pythonineducation.org
==========================================================

This project is an editor that targets the MicroPython
(http://micropython.org) version of the Python programming language
(http://python.org/). Code written with this editor is expected to run on the
BBC's micro:bit device (https://en.wikipedia.org/wiki/Micro_Bit).

Developer Setup
---------------

This editor is written to be embedded in the http://pythonineducation.org/
website. It means this project is served within an iFrame in the hosting
website. For this to work for development purposes, you'll need both the
pythonineducation.org site and this project serving locally.

https://github.com/python/pythonineducation.org

Code
++++

* ace - a directory containing the Ace editor (http://ace.c9.io).
* design - a directory containing design resources created by Steve Hawkes.
* editor.html - the page to be embedded within the iFrame in TouchDevelop.
* firmware.hex - copy of the "vanilla" MicroPython firmware used by the editor.
* help.html - a single page user facing help page.
* tests.html - the browser based test runner.
* static - contains css, js and img sub-directories.
* tests - contains the Python specific test suite.

Usage
-----

The Python editor is based upon the "Ace" JavaScript editor (http://ace.c9.io)
and includes syntax highlighting, code folding and (semi) intelligent
auto-indentation.

Following the TouchDevelop conventions, naming scripts is done automatically -
it'll be something like, "distinct script" or "awesome script 2". This also
applies to the description - it's automatically set to "A MicroPython script".
You can change these at any time by clicking on them.

All new scripts default to something simple and sensible.

The layout and functionality apes Microsoft's own editors. Importantly this
includes saving scripts to Microsoft's cloud and sharing them with others via
TouchDevelop's publish functionality.

The four buttons at the top left, act as follows:

* My Scripts - returns you to the main menu listing all your scripts.
* Download - creates a .hex file locally in the user's browser and prompts the user to download it. The resulting file should be copied over to the micro:bit device just like when using all the other editors. The filename will be the name of the script with spaces replaced by "_" and ending in .py. So "extraordinary script" is saved as extraordinary_script.py.
* Snippets - allow user's to write code from pre-defined Python fragments (functions, loops, if...else etc). They are triggered by typing a keyword followed by TAB. For example, type "wh" followed by TAB to insert a while... loop. Clicking on the code snippets button opens up a modal dialog window containing instructions and a table of the available snippets along with their trigger and a short and simple description.
* Help - opens a single page in a new tab that contains user-facing help.

Directly next to the four large buttons are four smaller icons. In the first
column are zoom in and zoom out buttons that make it easy for teachers to
display code via a projector. In the second column the top icon indicates the
script's status (changed, saved locally, saved to the cloud) and the other,
shaped like a bug, will display a log of the events that occured during the
current session of using the editor.

In other TouchDevelop editors there are "compile" and "run" buttons. These
target the TouchDevelop platform to create an AST and either use a third party
service contacted via the network to create a downloadable .hex
file (for the former) or run the code on an embedded simulator (for the
latter).

Since we're targeting MicroPython instead, we simply allow the user to
download their locally generated .hex file. They simply drag the resulting
file onto the device. If you connect to the device (and the script ISN'T in an
infinite loop) you'll be presented with the Python REPL. If there was an error
you should also see an error message.

If you plug in your micro:bit and want to get the REPL you'll need to install
pyserial and run the following command with the appropriate permissions (such
as root, as shockingly demonstrated below)::

    $ sudo python -m serial.tools.miniterm -b 115200 /dev/ttyACM0

Remember to replace tty/ACM0 with the appropriate device for your computer.

The .hex file is generated in the following way:

* A "vanilla" version of the MicroPython hex is hidden within the DOM.
* We take the Python code in the editor and turn it into a hex representation.
* We insert the Python derived hex into the correct place within the MicroPython hex.
* The resulting combination is downloaded onto the user's local filesystem for flashing onto the device.

The hidden MicroPython hex is just over 600k. While this sounds large, it's
relatively small when you consider:

* The Guardian's front page is around 1.5mb
* compression is built into the server
* the web has caching built in (we should trust it)
* we actually want kids to view source and find the .hex file in as raw a form as possible.

Finally, we have removed the device simulator from the right hand side and
put something "Pythonic" in its place.

Documentation
-------------

For documentation for this project - you're reading it. ;-)

For in-editor documentation aimed at the user, this is to be done but will
encompass both code snippets and generic help in the help.html file.
