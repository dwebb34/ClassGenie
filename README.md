# ClassGenie
ClassGenie is a c++/java class generator written in python. Intended use is for class generation via command line scripts.

Functionally, this is intended to do what most modern IDEs will do when generating a new class. However, I've provided a template grammar and configuration grammar with a json file for making the scripting of class generation possible. Further, you can create an entire project of generated classes. It also provides a class interface to set everything from class name, member variables, adding copy constructors, assignment operator, and everything a solid complete c++ class needs. See the config.json file for an example of an entire project complete with inherited classes and multiple 

#Usage
There are two ways to use Class Genie. You can define everything in the json file and just run classgenie.py or you can use the class interface to programmatically set everything, which uses the same json config file paradigm under the hood.

##Command Line
python classgenie.py --config config.json

##API
TODO
