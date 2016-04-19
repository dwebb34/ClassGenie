'''
:module genie_classes:
Contains all the classes that encapsulate the C++ objects. Each class
correlates to the project_grammar json config file and provides funcionality for 
parsing the appropriate tags.

This is basically a set of wrapper classes for the data dictionary defining our
classes. You could create your own dictionary, populate it correctly, and hand
it to the writers, but these classes should make it a lot cleaner.

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


class MemberFunction:
    
    @property
    def custom_code(self):
        return self.data_dictionary("custom-code")
    
    @custom_code.setter
    def custom_code(self, code):
        '''
        Custom code for this member function. Given code will overwrite existing code.
        Each string in the list is one line of code. Do not give the function
        definition. The code is everything between opening and closing brackets
        
        {
           custom code
        }
        
        This does not check for the validity of the code given.
        
        :param code list: list of strings to use as custom code in this member function
        '''
        if not isinstance(code, basestring):
            self.data_dictionary["custom-code"] = code
        else:
            raise TypeError("Code must be a list of strings. Each string is 1 line of code.")
                
        return
    
    @property
    def generate(self):
        return self.data_dictionary["generate"]
    
    @generate.setter
    def generate(self, gen=False):
        
        strVal = "true" if gen else "false"
        
        self.data_dictionary["generate"] = strVal
        return
    
    def __init__(self):
        self.data_dictionary = {
                        "generate":"false",
                        "custom-code":[]
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
    def name(self):
        return self.data_dictionary["name"]
    
    @class_name.setter
    def name(self, newName):
        '''
        Sets the name of the GenClass. dictionary["name"] = name
        Does some minimal checking for validity
        
        :param name string: name of class
        :raise ValueError: if name contains whitespace
        '''
        
        if contains_whitespace(newName):
            raise ValueError('name cannot contain whitespace.')
        
        self.data_dictionary["name"] = newName
        return
    
    @property
    def definition_template(self):
        return self.data_dictionary["definition-template"]
        
    @definition_template.setter
    def definition_template(self, defTemplate):
        self.data_dictionary["definition-template"] = defTemplate
        return
    
    @property
    def implementation_template(self):
        return self.data_dictionary["implementation-template"]
    
    @implementation_template.setter
    def implementation_template(self, implTemplate):
        self.data_dictionary["implementation-template"] = implTemplate
        
    @property
    def grammar_file(self):
        return self.data_dictionary["grammar-file"]

    @grammar_file.setter
    def grammar_file(self, gramFile):
        self.data_dictionary["grammar-file"] = gramFile
        return
        
    @property
    def class_license(self):
        return self.data_dictioanry["class-license"]
    
    @class_license.setter
    def class_license(self, license):
        self.data_dictioanry["class-license"] = license
        return
    
    @property
    def namespace(self):
        return self.data_dictionary["namespace"]
    
    @namespace.setter
    def namespace(self, newNamespace):
        self.data_dictioanry["namespace"] = newNamespace
        return
    
    @property
    def subdirectory(self):
        return self.data_dictionary["subdirectory"]
    
    @subdirectory.setter
    def subdirectory(self, subDir):
        self.data_dictionary["subdirectory"] = subDir
        return
    
    @property
    def base_classes(self):
        return self.data_dictionary["base-classes"]
    
    @base_classes.setter
    def base_classes(self, baseClass):        
        #if baseClass is already in the data_dictionary, don't put another one
        if param not in self.data_dictionary["base-classes"]:
            self.data_dictionary["base-classes"].append(baseClass)
        return
    
    @property
    def system_includes(self):
        return self.data_dictionary["system-includes"]
    
    @system_includes.setter
    def system_includes(self, include):        
        #if baseClass is already in the data_dictionary, don't put another one
        if include not in self.data_dictionary["system-includes"]:
            self.data_dictionary["system-includes"].append(include)
        return

    @property
    def dependencies(self):
        return self.data_dictionary["dependencies"]
    
    @class_dependencies.setter
    def dependencies(self, depends):        
        #if param is already in the data_dictionary, don't put another one
        if depends not in self.data_dictionary["dependencies"]:
            self.data_dictionary["dependencies"].append(depends)
        return
    
    @property
    def default_constructor(self):
        '''
        :return MemberFunction:
        '''
        retVal = MemberFunction()
        retVal.data_dictionary = self.data_dictionary["default-constructor"]
        return retVal
    
    def default_constructor_as_dict(self):
        return self.data_dictionary["default-constructor"]
    
    @default_constructor.setter
    def default_constructor(self, memFunc):
        if isinstance(memFunc, MemberFunction):
            self.data_dictionary["default-constructor"] = memFunc.data_dictionary
        elif isinstance(memFunc, dict):
            #avoids putting unacceptable values into the data dictionary
            if "generate" in memFunc:
                self.data_dictionary["default-constructor"]["generate"] = memFunc["generate"]
            
            if "custom-code" in memFunc:
                self.data_dictionary["default-constructor"]["custom-code"] = memFunc["custom-code"]
        else:
            raise TypeError("memFunc must be type MemberFunction or a data dictionary")
        return
    
    @property
    def default_destructor(self):
        '''
        :return MemberFunction:
        '''
        retVal = MemberFunction()
        retVal.data_dictionary = self.data_dictionary["default-destructor"]
        return retVal
    
    def default_destructor_as_dict(self):
        return self.data_dictionary["default-destructor"]
    
    @default_destructor.setter
    def default_destructor(self, memFunc):
        if isinstance(memFunc, MemberFunction):
            self.data_dictionary["default-destructor"] = memFunc.data_dictionary
        elif isinstance(memFunc, dict):
            #avoids putting unacceptable values into the data dictionary
            if "generate" in memFunc:
                self.data_dictionary["default-destructor"]["generate"] = memFunc["generate"]
            
            if "custom-code" in memFunc:
                self.data_dictionary["default-destructor"]["custom-code"] = memFunc["custom-code"]
        else:
            raise TypeError("memFunc must be type MemberFunction or a data dictionary")
        return
    
    @property
    def copy_constructor(self):
        '''
        :return MemberFunction:
        '''
        retVal = MemberFunction()
        retVal.data_dictionary = self.data_dictionary["copy-constructor"]
        return retVal
    
    def copy_constructor_as_dict(self):
        return self.data_dictionary["copy-constructor"]
    
    @copy_constructor.setter
    def copy_constructor(self, memFunc):
        if isinstance(memFunc, MemberFunction):
            self.data_dictionary["copy-constructor"] = memFunc.data_dictionary
        elif isinstance(memFunc, dict):
            #avoids putting unacceptable values into the data dictionary
            if "generate" in memFunc:
                self.data_dictionary["copy-constructor"]["generate"] = memFunc["generate"]
            
            if "custom-code" in memFunc:
                self.data_dictionary["copy-constructor"]["custom-code"] = memFunc["custom-code"]
        else:
            raise TypeError("memFunc must be type MemberFunction or a data dictionary")
        return
    
    @property
    def assignment_operator(self):
        '''
        :return MemberFunction:
        '''
        retVal = MemberFunction()
        retVal.data_dictionary = self.data_dictionary["assignment-operator"]
        return retVal
    
    def assignment_operator_as_dict(self):
        return self.data_dictionary["assignment-operator"]
    
    @assignment_operator.setter
    def assignment_operator(self, memFunc):
        if isinstance(memFunc, MemberFunction):
            self.data_dictionary["assignment-operator"] = memFunc.data_dictionary
        elif isinstance(memFunc, dict):
            #avoids putting unacceptable values into the data dictionary
            if "generate" in memFunc:
                self.data_dictionary["assignment-operator"]["generate"] = memFunc["generate"]
            
            if "custom-code" in memFunc:
                self.data_dictionary["assignment-operator"]["custom-code"] = memFunc["custom-code"]
        else:
            raise TypeError("memFunc must be type MemberFunction or a data dictionary")
        return
    
    @property
    def equals_operator(self):
        '''
        :return MemberFunction:
        '''
        retVal = MemberFunction()
        retVal.data_dictionary = self.data_dictionary["equals-operator"]
        return retVal
    
    def equals_operator_as_dict(self):
        return self.data_dictionary["equals-operator"]
    
    @equals_operator.setter
    def equals_operator(self, memFunc):
        if isinstance(memFunc, MemberFunction):
            self.data_dictionary["equals-operator"] = memFunc.data_dictionary
        elif isinstance(memFunc, dict):
            #avoids putting unacceptable values into the data dictionary
            if "generate" in memFunc:
                self.data_dictionary["equals-operator"]["generate"] = memFunc["generate"]
            
            if "custom-code" in memFunc:
                self.data_dictionary["equals-operator"]["custom-code"] = memFunc["custom-code"]
        else:
            raise TypeError("memFunc must be type MemberFunction or a data dictionary")
        return
    
    @property
    def not_equals_operator(self):
        '''
        :return MemberFunction:
        '''
        retVal = MemberFunction()
        retVal.data_dictionary = self.data_dictionary["not-equals-operator"]
        return retVal
    
    def not_equals_operator_as_dict(self):
        return self.data_dictionary["not-equals-operator"]
    
    @not_equals_operator.setter
    def not_equals_operator(self, memFunc):
        if isinstance(memFunc, MemberFunction):
            self.data_dictionary["not-equals-operator"] = memFunc.data_dictionary
        elif isinstance(memFunc, dict):
            #avoids putting unacceptable values into the data dictionary
            if "generate" in memFunc:
                self.data_dictionary["not-equals-operator"]["generate"] = memFunc["generate"]
            
            if "custom-code" in memFunc:
                self.data_dictionary["not-equals-operator"]["custom-code"] = memFunc["custom-code"]
        else:
            raise TypeError("memFunc must be type MemberFunction or a data dictionary")
        return
    
    @property
    def output_operator(self):
        '''
        :return MemberFunction:
        '''
        retVal = MemberFunction()
        retVal.data_dictionary = self.data_dictionary["output-operator"]
        return retVal
    
    def output_operator_as_dict(self):
        return self.data_dictionary["output-operator"]
    
    @output_operator.setter
    def output_operator(self, memFunc):
        if isinstance(memFunc, MemberFunction):
            self.data_dictionary["output-operator"] = memFunc.data_dictionary
        elif isinstance(memFunc, dict):
            #avoids putting unacceptable values into the data dictionary
            if "generate" in memFunc:
                self.data_dictionary["output-operator"]["generate"] = memFunc["generate"]
            
            if "custom-code" in memFunc:
                self.data_dictionary["output-operator"]["custom-code"] = memFunc["custom-code"]
        else:
            raise TypeError("memFunc must be type MemberFunction or a data dictionary")
        return
    
    @property
    def input_operator(self):
        retVal = MemberFunction()
        retVal.data_dictionary = self.data_dictionary["input-operator"]
        return retVal
    
    def input_operator_as_dict(self):
        return self.data_dictionary["input-operator"]
    
    @input_operator.setter
    def input_operator(self, memFunc):
        if isinstance(memFunc, MemberFunction):
            self.data_dictionary["input-operator"] = memFunc.data_dictionary
        elif isinstance(memFunc, dict):
            #avoids putting unacceptable values into the data dictionary
            if "generate" in memFunc:
                self.data_dictionary["input-operator"]["generate"] = memFunc["generate"]
            
            if "custom-code" in memFunc:
                self.data_dictionary["input-operator"]["custom-code"] = memFunc["custom-code"]
        else:
            raise TypeError("memFunc must be type MemberFunction or a data dictionary")
        return
    
    @property
    def member_variables(self):
        '''
        :return MemberVariable list:
        '''
        retVal = []
        
        for key, value in self.data_dictionary["member-variables"]:
            newMember = MemberVariable()
            newMember.data_dictionary = value
            retVal.append(newMember)
        
        return retVal
    
    def member_variables_as_dict(self):
        '''
        :return MemberVariable dict:
        '''
        return self.data_dictionary["member-variables"]
    
    @member_variable.setter
    def member_variables(self, memVar):
        if isinstance(memVar, MemberVariable):
            self.data_dictionary["member-variables"][memVar["name"]] = memVar
        elif isinstance(memVar, dict):
            self.data_dictionar["member-variables"].update(memVar)
        else:
            raise TypeError('memVar must of type MemberVariable or a data dictionary')
        return
    
    @property
    def functions(self):
        '''
        :return Function list:
        '''
        
        retVal = []
        for key, val in self.data_dictionary["functions"].items():
            newFunc = Function()
            newFunc.data_dictionary = val
            retVal.append(newFunc)
        
        return retVal
    
    def functions_as_dict(self):
        '''
        :return Function dict:
        '''
        return self.data_dictionary["functions"]
    
    @functions.setter
    def functions(self, func):
        if isinstance(func, Function):
            self.data_dictionary["functions"][func["name"]] = func
        elif isinstance(func, dict):
            self.data_dictionary["functions"].update(func)
        else:
            raise TypeError('func must of type Function or a data dictionary')
        return
    
    
    def __init__(self):
        self.data_dictionary = {
            "name":"ExampleClass",
            "definition-template":"",
            "implementation-template":"",
            "grammar-file":"",
            "class-license":"",
            "namespace":"",
            "subdirectory":"",
            "base-classes":[],#list of strings
            "system-includes":[],#list of strings
            "dependencies":[],#list of strings
            "default-constructor":{},
            "default-destructor":{},
            "copy-constructor":{},
            "assignment-operator":{},
            "equals-operator":{},
            "not-equals-operator":{},
            "output-operator":{},
            "input-operator":{},
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
    def default_grammar_file(self):
        return self.data_dictionary["default-grammar-file"]
    
    @defaulr_grammar_file.setter
    def default_grammar_file(self, gramFile):
        self.data_dictionary["default-grammar-file"]
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
        '''
        :return list GenClass: list of GenClass objects
        '''
        retVal = []
        for key, classDict in self.data_dictionary["classes"].items():
            newClass = GenClass()
            newClass.data_dictionary = classDict
            retVal.append(newClass)
        
        return retVal
    
    def find_gen_class(self, name):
        retVal = GenClass()
        
        if name in self.data_dictionary["classes"]:
            retVal.data_dictionary = self.data_dictionary["classes"][name]
        
        return retVal
    
    def find_gen_class_as_dict(self, name):
        retVal = {}
        
        if name in self.data_dictionary["classes"]:
            retVal = self.data_dictionary["classes"][name]
        
        return retVal
    
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

        #check that default values propogate to the class when an override isn't provided.
        #class values should take precedence
        if not newClass.class_license:
            newClass.class_license = self.default_license
            
        if not newClass.definition_template:
            newClass.definition_template = self.default_definition_template
            
        if not newClass.implementation_template:
            newClass.implementation_template = self.default_implementation_template
            
        if not newClass.class_namespace:
            newClass.class_namespace = self.default_namespace
            
        if not newClass.grammar_file:
            newClass.grammar_file = self.default_grammar_file
             
        self.data_dictionary["classes"][newClass.class_name] = newClass.data_dictionary
            
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
            "default-grammar-file":"grammar.json",
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