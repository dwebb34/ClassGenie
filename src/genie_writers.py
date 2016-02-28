'''

'''
templateTags = {
    'class.name' : '<class.name>',
    'CLASS.NAME' : '<CLASS.NAME>',
    'class.block' : '<class.name>.*</class.name>',
    #'' : '',
    #'' : '',
    #'' : '',
}

def write_genie_project(project):
    '''
    :param project GenieProject: set of classes and build files being written to file.
    :return boolean: true if everything was created correctly, false otherwise.
    '''
    import os
    from genie_classes import GenieProject
    
    projectDir = os.path.join(os.path.abspath(project.parent_directory), project.name)
    
    if (not os.path.isdir(projectDir)):
        os.mkdir(projectDir)
        
    for gClass in project.classes:
        write_genie_class(projectDir, gClass)
    
    return

def write_genie_class(parentDir, gClass):
    '''
    :param project GenieClass: metadata class being written to file.
    :return boolean: true if everything was created correctly, false otherwise.
    '''
    import os
    from genie_classes import GenieClass
    from genie_classes import Language as lang
    
    defFile = ""
    implFile = ""
    extension = gClass.language
    templatePath = os.getcwd()

    if (gClass.definition_template):
        defFile = os.path.join(templatePath, gClass.definition_template)
        
    if (gClass.implementation_template):
        implFile = os.path.join(templatePath, gClass.implementation_template)
    
    with open(defFile ,"r") as f:
        defTemplate = f.read()
    
    #replace all the tags with the right values
    defTemplate = replace_class_tags(gClass, defTemplate)
    
    print defTemplate
    
    #print the result to file
    extension = ""
    if gClass.language == lang.cpp:
        extension = ".h"
        
    defOutFile = os.path.join(parentDir, gClass.name + extension)
    
    with open(defOutFile, "w") as f:
        f.write(defTemplate)
    
    return

def read_template(fileName):
    import os
    
    #if (not os.path.isfile(fileName)):
    #    print "Oops"
    #    return ""
    
    retVal = ""
    
    f = open(fileName, "r")

    retVal = f.read()
    
    return retVal

def replace_class_tags(gClass, template):
    '''
    replaces all three known <class> tags
    <class.name>
    <CLASS.NAME>
    <class.name> </class.name>
    
    :param gClass GenieClass: class data
    :param template string: template as a string
    :return string: template with tags replaced with real values
    '''
    
    template = template.replace(templateTags['class.name'], gClass.name)
    
    template = template.replace(templateTags['CLASS.NAME'], gClass.name.upper())
    return template