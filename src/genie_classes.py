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
    
    @property
    def parameter_name(self):
        return self.data_dictionary["name"]
    
    @parameter_name.setter
    def parameter_name(self, name):
        '''
        Sets the name key in the data dictionary. Does minimal validation.
        '''
        if contains_whitespace(name):
            raise ValueError('name cannot contain whitespace.')
        
        self.data_dictionary["name"] = name
        return
    
    @property
    def type(self):
        return self.data_dictionary["type"]
    
    @type.setter
    def type(self, type="int"):
        self.data_dictionary["type"] = type
        return
    
    @property
    def default_value(self):
        return self.data_dictionary["default-value"]
    
    @default_value.setter
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

class MemberVariable:
    '''
    MemberVariable reperesents a C/C++ member variable, complete with scope,
    type, default value, and a flag for generating setters/getters
    '''
    
    @property
    def member_name(self):
        return self.data_dictionary["name"]
    
    @member_name.setter
    def member_name(self, name):
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
    
    @property
    def scope(self):
        return self.data_dictionary["scope"]
    
    @scope.setter
    def scope(self, scope="private"):
        self.data_dictionary["scope"] = scope
        return
    
    @property
    def type(self):
        return self.data_dictionary["type"]
    
    @type.setter
    def type(self, type="int"):
        self.data_dictionary["type"] = type
        return
    
    @property
    def access_function(self):
        return self.data_dictionary["access-function"]
    
    @access_function.setter
    def access_function(self, createFunction = True):
        '''
        Tell Function whether to generate standard setter/getter for this member
        variable.
        
        :param createFunction bool=True: True = generate accessors. False = don't
        '''
        val = "true" if createFunction else "false"
            
        self.data_dictionary["access-function"] = val
        return
    
    @property
    def default_value(self):
        return self.data_dictionary["default-value"]
    
    @default_value.setter
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
    @property
    def function_name(self):
        return self.data_dictionary["name"]
    
    @function_name.setter
    def function_name(self, name):
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
    
    @property
    def documentation(self):
        return self.data_dictionary["documentation"]
    
    @documentation.setter
    def documentation(self, val=True):
        strVal = "true" if val else "false"
        self.data_dictionary["documentation"] = strVal
        return
    
    @property
    def scope(self):
        return self.data_dictionary["scope"]
    
    @scope.setter
    def scope (self, scope="private"):
        self.data_dictionary["scope"] = scope
        return
    
    @property
    def return_type(self):
        return self.data_dictionary["return-type"]
    
    @return_type.setter
    def return_type(self, type):
        self.data_dictionary["return-type"] = type
        return
    
    @property
    def parameter(self):
        return self.data_dictionary["parameters"]
    
    @parameter.setter
    def parameter(self, param):
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
    
    @property
    def class_name(self):
        return self.data_dictionary["name"]
    
    @class_name.setter
    def class_name(self,name):
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
    
    @property
    def definition_template(self):
        return self.data_dictionary["definition-template"]
        
    @definition_template.setter
    def definition_template(self, defTemplate):
        self.data_dictioanry["definition-template"] = defTemplate
        return
    
    @property
    def implementation_template(self):
        return self.data_dictionary["implementation-template"]
    
    @implementation_template.setter
    def implementation_template(self, implTemplate):
        self.data_dictionary["implementation-template"] = implTemplate
        
    @property
    def class_license(self):
        return self.data_dictioanry["class-license"]
    
    @class_license.setter
    def class_license(self, license):
        self.data_dictioanry["class-license"] = license
        return
    
    @property
    def class_namespace(self):
        return self.data_dictionary["namespace"]
    
    @class_namespace.setter
    def class_namespace(self, namespace):
        self.data_dictioanry["namespace"] = namespace
        return
    
    @property
    def subdirectory(self):
        return self.data_dictionary["subdirectory"]
    
    @subdirectory.setter
    def subdirectory(self, subDir):
        self.data_dictionary["subdirectory"] = subDir
        return
    
    @property
    def base_class(self):
        return self.data_dictionary["base-classes"]
    
    @base_class.setter
    def base_class(self, baseClass):        
        #if baseClass is already in the data_dictionary, don't put another one
        if param not in self.data_dictionary["base-classes"]:
            self.data_dictionary["base-classes"].append(baseClass)
        return
    
    @property
    def system_include(self):
        return self.data_dictionary["system-includes"]
    
    @system_include.setter
    def system_include(self, include):        
        #if baseClass is already in the data_dictionary, don't put another one
        if include not in self.data_dictionary["system-includes"]:
            self.data_dictionary["base-classes"].append(include)
        return

    @property
    def class_dependency(self):
        return self.data_dictionary["dependencies"]
    
    @class_dependency.setter
    def class_dependency(self, depends):        
        #if param is already in the data_dictionary, don't put another one
        if depends not in self.data_dictionary["dependencies"]:
            self.data_dictionary["dependencies"].append(depends)
        return
    
    @property
    def default_constructor(self):
        return self.data_dictionary["default-constructor"]
    
    @default_constructor.setter
    def default_constructor(self, provideDefault = True):
        val = "true" if provideDefault else "false"
        self.data_dictionary["default-constructor"] = val
        return
    
    @property
    def default_destructor(self):
        return self.data_dictionary["default-destructor"]
    
    @default_destructor.setter
    def default_destructor(self, provideDefault = True):
        val = "true" if provideDefault else "false"
        self.data_dictionary["default-destructor"] = val
        return
    
    @property
    def destructor_variable(self):
        return self.data_dictionary["destructor-variables"]
    
    @destructor_variable.setter
    def destructor_variable(self, destructorVar):        
        #if param is already in the data_dictionary, don't put another one
        if destructorVar not in self.data_dictionary["destructor-variables"]:
            self.data_dictionary["destructor-variables"].append(destructorVar)
        return
    
    @property
    def copy_constructor(self):
        return self.data_dictionary["copy-constructor"]
    
    @copy_constructor.setter
    def copy_constructor(self, provideDefault = True):
        val = "true" if provideDefault else "false"
        self.data_dictionary["copy-constructor"] = val
        return
    
    @property
    def assignment_operator(self):
        return self.data_dictionary["assignment-operator"]
    
    @assignment_operator.setter
    def assignment_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["assignment-operator"] = val
        return
    
    @property
    def equals_operator(self):
        return self.data_dictionary["equals-operator"]
    
    @equals_operator.setter
    def equals_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["equals-operator"] = val
        return
    
    @property
    def not_equals_operator(self):
        return self.data_dictionary["not-equals-operator"]
    
    @not_equals_operator.setter
    def not_equals_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["not-equals-operator"] = val
        return
    
    @property
    def output_operator(self):
        return self.data_dictionary["output-operator"]
    
    @output_operator.setter
    def output_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["output-operator"] = val
        return
    
    @property
    def input_operator(self):
        return self.data_dictionary["input-operator"]
    
    @input_operator.setter
    def input_operator(self, provideOp = True):
        val = "true" if provideOp else "false"
        self.data_dictionary["input-operator"] = val
        return
    
    @property
    def member_variable(self):
        return self.data_dictionary["member-variables"]
    
    @member_variable.setter
    def member_variable(self, memVar):
        if not isinstance(memVar, MemberVariable):
            raise TypeError('memVar must of type MemberVariable')
        
        self.data_dictionary["member-variables"][memVar["name"]] = memVar
        return
    
    @property
    def function(self):
        return self.data_dictionary["functions"]
    
    @function.setter
    def function(self, func):
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
    
    @property
    def project_name(self):
        return self.data_dictionary["project-name"]
    
    @project_name.setter
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
    
    @property
    def default_license(self):
        return self.data_dictionary["default-license"]
    
    @default_license.setter
    def default_license(self, val):
        self.data_dictionary["default-license"] = val
        return
    
    @property
    def project_directory(self):
        return self.data_dictionary["project-directory"]

    @project_directory.setter
    def project_directory(self, val):
        self.data_dictionary["project-directory"] = val
        return
    
    @property
    def template_location(self):
        return self.data_dictionary["template-location"]
    
    @template_location.setter
    def template_location(self, val):
        self.data_dictionary["template-location"] = val
        return
    
    @property
    def default_definition_template(self):
        return self.data_dictionary["default-definition-template"]
    
    @default_definition_template.setter
    def default_definition_template(self, val):
        self.data_dictionary["default-definition-template"] = val
        return
    
    @property
    def default_implementation_template(self):
        return self.data_dictionary["default-implementation-template"]
        
    @default_implementation_template.setter
    def default_implementation_template(self, val):
        self.data_dictionary["default-implementation-template"] = val
        return
    
    @property
    def default_namespace(self):
        return self.data_dictionary["default-namespace"]
    
    @default_namespace.setter
    def default_namespace(self, val):
        self.data_dictionary["default-namespace"] = val
        return
    
    @property
    def language(self):
        return self.data_dictionary["language"]
    
    @language.setter
    def language(self, val):
        self.data_dictionary["language"] = val
        return
    
    @property
    def gen_class(self):
        return self.data_dictionary["classes"]
    
    @gen_class.setter
    def gen_class(self, newClass):
        '''
        Adds a new GenClass to the project. Any existing GenClass with the same
        name will be overwritten.
        
        :param newClass GenClass: class to add to this GenProject
        :raises TypeError: if newClass is not of type GenClass
        '''
        if not isinstance(newClass, GenClass):
            raise TypeError('newClass must of type GenClass')

        print("HERE")
        self.data_dictionary["classes"][newClass.name] = newClass.data_dictionary
            
        return
    
    def __init__(self, configPath = None):
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

        self.config = configPath
        
        if self.config:
            self.import_config()
        
        return

    def __str__(self):
        import json
        retVal = json.dumps(self.data_dictionary, indent=4, sort_keys=True)
        return retVal