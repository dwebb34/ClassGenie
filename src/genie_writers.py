'''

'''
templateTags = {
    'class.name' : '<class.name>',
    'CLASS.NAME' : '<CLASS.NAME>',
    #'class.block' : '<class.name>.*</class.name>',
    'base.class' : '<base_class>',
    'base.class.block' : '<base_class>.*</base_class>',
    'base.class.def.block' : '<base_class.definition_template>.*</base_class.definition_template>',
    'base.class.def' : '<base_class.definition_template>',
    #
    'member.variable.block' : '<member_variable>.*</member_variable>',
    'member.variable' : '<member_variable>',
    'member.variable.type' : '<member_variable.type>'
}

def write_project(project):
    '''
    :param project GenieProject: set of classes and build files being written to file.
    :return boolean: true if everything was created correctly, false otherwise.
    '''
    import os
    from genie_classes import GenProject, GenClass
    import json
    
    projectDir = os.path.join(os.path.abspath(project.project_directory), project.project_name)
    
    if (not os.path.isdir(projectDir)):
        os.makedirs(projectDir)
        
    for gClass in project.gen_class:
        #parsedJson = json.loads(gClass)
        print ("Working on class: " + gClass.class_name)
        write_class(project, gClass)
    
    return True

def write_class(project, gClass):
    '''
    :param gClass GenClass: metadata class being written to file.
    :return boolean: true if everything was created correctly, false otherwise.
    '''
    import os
    from genie_classes import GenClass
    
    defFile = ""
    implFile = ""
    templatePath = project.template_location
    print("HERE --> " + templatePath)
    if (gClass.data_dictionary["definition-template"]):
        defFile = os.path.join(templatePath, gClass.definition_template)
        defFile = os.path.abspath(defFile)
        
    #if (gClass.implementation_template):
    #    implFile = os.path.join(templatePath, gClass.implementation_template)
    
    print("definition file: " + defFile)
    with open(defFile ,"r") as f:
        defTemplate = f.read()
    
    #replace all the tags with the right values
    classDefinition = replace_tags(project, gClass, defTemplate)
    
    #print (classDefinition)
    
    #print the result to file
    extension = project.language
    parentDir = project.project_directory
    defOutFile = os.path.abspath(os.path.join(parentDir, gClass.class_name + extension))
    
    with open(defOutFile, "w") as f:
        f.write(classDefinition)
    
    return True


def replace_tags(project, gClass, template):
    '''
    replaces all tags with grammar file code. Then replace the name tags in the
    grammar code with final values to get complete code.
    
    example:
    template text       ->          grammar text
    <system-includes>               #include <<system-includes>>
    
    grammar text        ->          end result
    #include <<system-includes>>    #include <string>
                                    #include <iostream>
                                    
    This accomodates style preferences and keeps the template files from getting
    too difficult to read.
    
    :param project GenProject: project data
    :param gClass GenClass: class data
    :param template string: definition/implmentation template as a string
    :return string: template string, tags replaced with real values
    '''
    import json
    
    #expand the template file to be more like code syntax. This will still have
    # <tags> in it that need to be replaced
    grammar=""
    with open('../templates/grammar.json', 'r') as grammarFile:
        grammar = json.load(grammarFile)
    
    for key, value in grammar.items():    
        template = template.replace(key, value)
        
    print (template)
    
    #template = template.replace(templateTags['CLASS.NAME'], gClass.name.upper())
    return template

