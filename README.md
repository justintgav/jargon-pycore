# jargon
Modular Natural Language Project

TODO format this stuff, pasted from paper
../conf/*
The conf directory contains components specific to the current installation of jargon. The file ../conf/conf.py contains subroutines to load configuration information, build data structures, initialize/inventory modules, etc.
../conf/module/*
The ../module/ directory contains all modules. A module is a self-contained unit of functionality to be invoked by jargon. Each module must conform to the following specification:
Have a directory:
../conf/module/the_module_name
Under this directory, the following files must exist:
	../conf/module/the_module_name/the_module_name.dict
The first line of this file must be the_module_name. Each line following will contain keywords/keyphrases that should be associated with this module. These *.dict files are used to build the data structure to associate keywords/keyphrases with the specific module.
	../conf/module/the_module_name/the_module_name.keys
The first line of this file must be the_module_name. Each line following will contain ‘keys’. These are used as keys for the associative array that will be passed as a parameter to the logic of the module. This is the way for the module to specify what it is expecting to receive when invoked.
	../conf/module/the_module_name/the_module_name.py
Must contain the function “module_main(args)”. “args” will be an associative array containing information linked/relevant to the keys specified in the *.keys file. Optionally may return a string to be presented to the user (either as text printed to the terminal or through text-to-speech). This is where the logic of the module is defined.



installed packages:
    pocket-sphinx
    wolframalpha
    ledcontroller

Voice Driver Installation
Requires pocketsphinx
    https://github.com/cmusphinx/pocketsphinx-python
sudo apt-get install -y python python-dev python-pip build-essential swig git
sudo pip install pocketsphinx
