# ClassGenie
ClassGenie is a c++/java class generator written in python. Intended use is for class generation via command line scripts.

Functionally, this is intended to do what most modern IDEs will do when generating a new class. However, I've provided a template grammar and configuration grammar with an xml for making the scripting of class generation possible.

#Example
classgenie --config config.xml --privateMember int-newMember
