# easycodegen
esaycodegen is a c++/java class generator written in python. Intended for class generation via command line scripts.

Functionally, this is intended to do what most modern IDEs will do when generating a new class. However, I've provided a template grammar and configuration grammar using json files for making the scripting of class generation possible. Further, you can create an entire project of generated classes complete with support for inheritence. It also provides a class wrapper interface to set everything from class name, member variables, adding copy constructors, assignment operator, and everything a solid complete c++ class needs. Any value in the json file can be set with the class API. See the config.json file for an example of an entire project complete with inherited classes.

##Usage
There are two ways to use esaycodegen. You can define everything in the json file and just run classgenie.py or you can use the class interface to programmatically set everything in your own script using the gen_classes module, which uses the same json config file paradigm under the hood.

###Command Line
python classgenie.py --config config.json

###API
TODO
