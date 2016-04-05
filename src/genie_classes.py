'''
:module genie_classes:
Contains all the classes that encapsulate the C++ objects. Each class
correlates to the project_grammar xml schema and provides funcionality for parsing
the appropriate tags.

:author: Devin Webb
:email: devin.a.webb@gmail.com
'''
indent = "   "
nl = "\n"

def contains_whitespace(val):
    import re
    #contains whitespace?
    retVal = True if re.search('\s', val) else False
    return retVal

class Parameter:
    '''
    Parameter represents a C/C++ style function parameter. Note that attempts
    are made to validate the types, but it is up to the user to add valid data
    types, values, and names for the types.
    
    It is a data dict with keys
    :param name string: parameter name. Default "param1"
    :param type string: parameter type as string. Default int.
    :param default-value string: string representation of the default value.
        Defaulted to 0, will be converted to type in generated class.
    '''
    
    def name(self, name):
        '''
        Sets the name key in the data dictionary. Does minimal validation.
        '''
        if contains_whitespace(name):
            raise ValueError('name cannot contain whitespace.')
        
        self.data_dictionary["name"] = name
        return
    
    def type(self, type="int"):
        self.data_dictionary["type"] = type
        return
    
    def default_value(self, val="0"):
        self.data_dictionary["default-value"] = val
        return
    
    def __init__(self):
        self.data_dictionary = {
                                "name":"param1",
                                "type":"int",
                                "default-value":"0"
                            }
        return
    
    def __str__(self):
        import json
        
        retVal = json.dumps(self.data_dictionary, indent=4, sort_keys=True)
        
        return retVal
    
################################################################################
class MemberVariable:
    '''
    MemberVariable reperesents a C/C++ member variable, complete with scope,
    type, default value, and a flag for generating setters/getters
    '''

    def name(self, name):
        '''
        Sets the name of the MemberVariable. dictionary["name"] = name
        Does some minimal checking for validity
        
        :param name string: name of variable
        :raise ValueError: if name contains whitespace
        '''
        
        if contains_whitespace(name):
            raise ValueError('name cannot contain whitespace.')
        
        self.data_dictionary["name"] = name
        return
    
    def scope(self, scope="private"):
        self.data_dictionary["scope"] = scope
        return
    
    def type(self, type="int"):
        self.data_dictionary["type"] = type
        return
    
    def access_function(self, createFunction = True):
        '''
        Tell Function whether to generate standard setter/getter for this member
        variable.
        
        :param createFunction bool=True: True = generate accessors. False = don't
        '''
        val = "true" if createFunction else "false"
            
        self.data_dictionary["access-function"] = val
        return
    
    def default_value(self, defaultVal = "0"):
        self.data_dictionary["default-value"] = defaultVal
        return
    
    def __init__(self):
        self.data_dictionary = {
                            "name":"exampleInt",
                            "scope":"private",
                            "type":"integer",
                            "access-function":"false",
                            "default-value":"0"
                        }
        return
    
    def __str__(self):
        import json
        retVal = json.dumps(self.data_dictionary, indent=4, sort_keys=True)
        return retVal

class Function:
    '''
    Function represents a C/C++ function, complete with scope, return type,
    a flag to generate default doxygen style documentation, and parameters.
    '''
    
    def name(self, name):
        '''
        Sets the name of the Function. dictionary["name"] = name
        Does some minimal checking for validity
        
        :param name string: name of variable
        :raise ValueError: if name contains whitespace
        '''
        
        if contains_whitespace(name):
            raise ValueError('name cannot contain whitespace.')
        
        self.data_dictionary["name"] = name
        return
    
    def documentation(self, val=True):
        strVal = "true" if val else "false"
        self.data_dictionary["documentation"] = strVal
        return
    
    def scope (self, scope="private"):
        self.data_dictionary["scope"] = scope
        return
    
    def return_type(self, type):
        self.data_dictionary["return-type"] = type
        return
    
    def add_parameter(self, param):
        '''
        Adds a Parameter to the Function data dictionary. Does check that param
        is a Parameter. Any existing Parameter with the same name is replaced
        
        :param param Parameter: function Parameter
        :raise TypeError:if param is not a Parameter type
        '''
        if not isinstance(param, Parameter):
            raise TypeError('param must of type Parameter')
        
        self.data_dictionary["parameters"][param["name"]] = param
            
        return
    
    def __init__(self):
        self.data_dictionary = {
                        "name":"examplePrivateFunction",
                        "documentation":"false",
                        "scope":"private",
                        "return-type":"integer",
                        "parameters":{}
                    }
        return
    
    def __str__(self):
        import json
        retVal = json.dumps(self.data_dictionary, indent=4, sort_keys=True)
        return retVal
    
class GenClass:
    '''
    GenClass represents a C/C++ class.
    '''
    
    def name(self,name):
        '''
        Sets the name of the GenClass. dictionary["name"] = name
        Does some minimal checking for validity
        
        :param name string: name of class
        :raise ValueError: if name contains whitespace
        '''
        
        if contains_whitespace(name):
            raise ValueError('name cannot contain whitespace.')
        
        self.data_dictionary["name"] = name
        return
    
    def definition_template(self, defTemplate):
        self.data_dictioanry["definition-template"] = defTemplate
        return
    
    def implementation_template(self, implTemplate):
        self.data_dictioanry["implementation-template"] = implTemplate
        return
    
    def class_license(self, license):
        self.data_dictioanry["class-license"] = license
        return
    
    def namespace(self, namespace):
        self.data_dictioanry["namespace"] = namespace
        return
    
    def subdirectory(self, subDir):
        self.data_dictioanry["subdirectory"] = subDir
        return
    
    def add_base_class(self, baseClass):        
        #if baseClass is already in the data_dictionary, don't put another one
        if param not in self.data_dictionary["base-classes"]:
            self.data_dictionary["base-classes"].append(baseClass)
        return
    
    def add_system_include(self, include):        
        #if baseClass is already in the data_dictionary, don't put another one
        if include not in self.data_dictionary["system-includes"]:
            self.data_dictionary["base-classes"].append(include)
        return

    def add_dependency(self, depends):        
        #if param is already in the data_dictionary, don't put another one
        if depends not in self.data_dictionary["dependencies"]:
            self.data_dictionary["dependencies"].append(depends)
            
        return
    
    def default_constructor(self, provideDefault = True):
        val = "true" if provideDefault else "false"
        self.data_dictionary["default-constructor"] = val
        return
    
    def default_destructor(self, provideDefault = True):
        val = "true" if provideDefault else "false"
        self.data_dictionary["default-destructor"] = val
        return
    
    def add_destructor_variable(self, destructorVar):        
        #if param is already in the data_dictionary, don't put another one
        if destructorVar not in self.data_dictionary["destructor-variables"]:
            self.data_dictionary["destructor-variables"].append(destructorVar)
            
        return
    
    def copy_constructor(self, provideDefault = True):
        val = "true" if provideDefault else "false"
        self.data_dictionary["copy-constructor"] = val
        return
    
    def assignment_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["assignment-operator"] = val
        return
    
    def equals_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["equals-operator"] = val
        return
    
    def not_equals_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["not-equals-operator"] = val
        return
    
    def output_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["output-operator"] = val
        return
    
    def input_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["input-operator"] = val
        return
    
    def add_member_variable(self, memVar):
        if not isinstance(memVar, MemberVariable):
            raise TypeError('memVar must of type MemberVariable')
        
        self.data_dictionary["member-variables"][memVar["name"]] = memVar
        return
    
    def add_function(self, func):
        if not isinstance(func, Function):
            raise TypeError('func must of type Function')
        
        self.data_dictionary["functions"][func["name"]] = func
        return
    
    
    def __init__(self):
        self.data_dictionary = {
            "name":"ExampleClass",
            "definition-template":"",
            "implementation-template":"",
            "class-license":"",
            "namespace":"",
            "subdirectory":"",
            "base-classes":[],#list of strings
            "system-includes":[],#list of strings
            "dependencies":[],#list of strings
            "default-constructor":"true",
            "default-destructor":"true",
            "copy-constructor":"true",
            "destructor-variables":[],#list of strings
            "assignment-operator":"true",
            "equals-operator":"true",
            "not-equals-operator":"true",
            "output-operator":"false",
            "input-operator":"false",
            "member-variables":{},
            "functions":{}
        }

        return
    
    def __str__(self):
        import json
        
        retVal = json.dumps(self.data_dictionary, indent=4, sort_keys=True)
        
        return retVal

class GenProject:
    '''
    GenProject represents a collection of related C/C++ classes, aka project.
    
    Some project-wide settings can be overwritten in classes and are used as 
    defaults for classes that don't specify them. These include
    
    project                             class override
    ----------------------------------------------------------------------------
    default-license                     class-license
    default-definition-template         definition-template
    default-implementation-template     implementation-template
    default-namespace                   namespace
    '''
    
    def import_config(self):
        if not self.config:
            raise ValueError('config cannot be empty. GenProject')
        
        if  not self.config.find('json'):
            raise ValueError('config must be a json file')

        import json
        with open(self.config, 'r') as inFile:
            self.data_dictionary = json.load(inFile)

        return
    
    def project_name(self, name):
        '''
        Sets the name of the GenProject. dictionary["name"] = name
        Does some minimal checking for validity
        
        :param name string: name of variable
        :raise ValueError: if name contains whitespace
        '''
        
        if contains_whitespace(name):
            raise ValueError('name cannot contain whitespace.')
        
        self.data_dictionary["project-name"] = name
        return
    
    def default_license(self, val):
        self.data_dictionary["default-license"] = val
        return
    
    def project_directory(self, val):
        self.data_dictionary["project-directory"] = val
        return
    
    def template_location(self, val):
        self.data_dictionary["template-location"] = val
        return
    
    def default_definition_template(self, val):
        self.data_dictionary["default-definition-template"] = val
        return
    
    def default_implementation_template(self, val):
        self.data_dictionary["default-implementation-template"] = val
        return
    
    def default_namespace(self, val):
        self.data_dictionary["default-namespace"] = val
        return
    
    def language(self, val):
        self.data_dictionary["language"] = val
        return
    
    def add_class(self, newClass):
        '''
        Adds a new GenClass to the project. Any existing GenClass with the same
        name will be overwritten.
        
        :param newClass GenClass: class to add to this GenProject
        :raises TypeError: if newClass is not of type GenClass
        '''
        if not isinstance(newClass, GenClass):
            raise TypeError('newClass must of type GenClass')
        
        self.data_dictionary["classes"][newClass["name"]] = newClass
            
        return
    
    def __init__(self):
        self.data_dictionary = {
            "project-name":"TestGenPyProject",
            "default-license":"license.txt",
            "project-directory":"",
            "template-location":"../templates",
            "default-definition-template":"definition.template",
            "default-implementation-template":"impl.template",
            "default-namespace":"test",
            "language":"c++",
            "classes":{}
        }

        self.config = None
        
        return

    def __str__(self):
        import json
        retVal = json.dumps(self.data_dictionary, indent=4, sort_keys=True)
        return retVal