'''
:module genie_classes:
Contains all the classes that encapsulate the C++/Java/Python objects. Each class
correlates to the project_grammar xml schema and provides funcionality for parsing
the appropriate tags.

:author: Devin Webb
:email: devin.a.webb@gmail.com
'''
indent = "   "
nl = "\n"

class Language:
    '''
    Languages is enum class representing the genie supported languages
    '''
    cpp = "c++"
    java = "java"
    python = "python"
    
class BuildType:
    '''
    BuildType is enum class representing the genie supported build types
    '''
    cmake = "cmake"
    ant = "ant"
  
class Types:
    '''
    Types is enum class representing the genie supported primative types
    '''
    none = None    

class Operator:
    def parse(self, xml):
        import xml.etree.ElementTree as ET
        
        #ET.dump(xml)
        
        #get all the class attributes
        self.type = xml.get('type', "")
        return
    
    assignment = "assignment"
    equals = "equals"
    not_equals = "not_equals"
    output_stream = "output_stream"
    input_stream = "input_stream"
    
    def __init__(self):
        self.type = ""
        return
    
    def __str__(self):
        retVal = "Operator (" + self.type + ")" + nl
        
        return retVal
    
################################################################################
class MemberVariable:
    
    def parse(self, xml):
        import xml.etree.ElementTree as ET
        
        #ET.dump(xml)
        
        #get all the class attributes
        self.name = xml.get('name', "")
        self.type = xml.get('type', "")
        
        return
    
    def __init__(self):
        self.name = ""
        self.type = Types.none
        return
    
    def __str__(self):
        retVal = "MemberVariable (" + self.type + " " + self.name + ")" + nl
        
        return retVal
    
################################################################################
class Function:
    def parse(self, xml):
        import xml.etree.ElementTree as ET
        
        #ET.dump(xml)
        
        #get all the class attributes
        self.scope = xml.get('scope', "")
        return
    
    def __init__(self):
        self.name = ""
        self.return_val = Types.none
        self.param_list = []
        self.code = []
        return
    
    def __str__(self):
        retVal = "Function (" + self.scope + ")" + nl
        
        return retVal

class BaseClass:
    
    def parse(self, xml):
        import xml.etree.ElementTree as ET
        
        #ET.dump(xml)
        
        #get all the class attributes
        self.implementation_template = xml.get('implementation_template', "")
        self.definition_template = xml.get('definition_template', "")
        self.namespace = xml.get('namespace', "")
        self.name = xml.get('name', "")
        
        return
    
    def __init__(self):
        self.implementation_template = ""
        self.definition_template = ""
        self.namespace = ""
        self.name = ""
        
        return
    
    def __str__(self):
        retVal = "BaseClass" + nl
        
        retVal += indent + self.implementation_template + nl
        retVal += indent + self.definition_template + nl
        retVal += indent + self.namespace + nl
        retVal += indent + self.name + nl
        
        return retVal
    
################################################################################
# GenieClass encapsulates all the meta data neeed to generate C++/Java classes. 
################################################################################
class GenieClass:
    def prepare(self, config):
        
        return
    
    def parse(self, xml):
        '''parse
        parse the <class> tag from a project_gramar schema
        
        :param xml xml.etree.ElementTree: object representing the xml tag <class>
        :return: None
        '''
        import xml.etree.ElementTree as ET
        
        #ET.dump(xml)
        
        #get all the class attributes
        self.output_directory = xml.get('output_directory', "")
        self.license = xml.get('license', "")
        self.name = xml.get('name', "")
        self.language = xml.get('language', "")
        self.namespace = xml.get('namespace', "")
        self.definition_template = xml.get('definition_template', "")
        self.implementation_template = xml.get('implementation_template', "")
        
        # all the operators
        for op in xml.findall('operator'):
            newOp = Operator()
            newOp.parse(op)
            self.operators.append(newOp)
            
        # all the member variables
        for member in xml.findall('member_variable'):
            newMember = MemberVariable()
            newMember.parse(member)
            self.member_variables.append(newMember)
            
        # all the private functions
        for func in xml.findall('function'):
            newFunc = Function()
            newFunc.parse(func)
            self.functions.append(newFunc)
            
        # all the base classes
        for base in xml.findall('base_class'):
            newBase = BaseClass()
            newBase.parse(base)
            self.base_classes.append(newBase)
            
        return
    
    def __init__(self):
        self.output_directory = ""
        self.license = ""
        self.name = ""
        self.language = Language.cpp
        self.namespace = ""
        self.definition_template = ""
        self.implementation_template = ""
        
        self.operators = []
        self.member_variables = []
        self.functions = []
        self.base_classes = []
        
        #self.args = 
        self.config = ""

        return
    
    def __str__(self):
        retVal = ""
        
        retVal += "GenieClass"
        retVal += indent + self.output_directory + nl
        retVal += indent + self.license + nl
        retVal += indent + self.name + nl
        retVal += indent + self.language + nl
        retVal += indent + self.namespace + nl
        retVal += indent + self.definition_template + nl
        retVal += indent + self.implementation_template + nl
        
        for op in self.operators:
            retVal += str(op)
        
        for member in self.member_variables:
            retVal += str(member)
            
        for func in self.functions:
            retVal += str(func)

        for base in self.base_classes:
            retVal += str(base)
        
        return retVal

################################################################################
class GenieBuildFile:
    
    def __init__(self):
        self.build_type = BuildType.cmake
        return

################################################################################
class GenieProject:
    
    def prepare(self, config):
        import xml.etree.ElementTree as ET
        import os.path
        
        if (not os.path.isfile(config)):
            print(config + " is not a file")
            return
        
        self.config = config
        
        import xml.etree.ElementTree as ET
        xml = ET.parse(self.config)
        self.parse(xml)
        
        return
    
    def parse(self, xml=None):
        import xml.etree.ElementTree as ET
        
        if (not xml):
            xml = ET.parse(self.config)

        root = xml.getroot()
        
        self.name = root.get('name', "GenieProject")
        self.parent_directory = root.get('parent_directory', "")

        for gClass in root.findall('class'):
            newClass = GenieClass()
            newClass.parse(gClass)
            self.classes.append(newClass)

        return
    
    def __init__(self):
        self.name = None
        self.parent_directory = None
        self.classes = []
        self.build_files = []
        #self.tests = []
        
        self.config = None
        
        return

    def __str__(self):
        retVal = "GenieProject"
        return retVal