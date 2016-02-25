# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

def write_genie_project(project):
    '''
    :param project GenieProject: metadata class being written to file.
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
    
    defFile = ""
    implFile = ""
    extension = gClass.language
    
    if (gClass.definition_template):
        defFile = os.path.join(parentDir, gClass.definition_template)
        
    if (gClass.implementation_template):
        implFile = os.path.join(parentDir, gClass.implementation_template)
        
    print (defFile)
    print (implFile)
    
    #defTemplate = read_template(defFile)
    #implTemplate = read_template(implFile)
    
    #print (defTemplate)
    #print (implTemplate)
    
    f = open(defFile ,"r")
    print ("ok")
    retVal = f.read()
    print retVal
    
    return

def read_template(fileName):
    import os
    
    #if (not os.path.isfile(fileName)):
    #    print "Oops"
    #    return ""
    
    retVal = ""
    
    f = open(fileName, "r")
    print ("ok")
    retVal = f.read()
    print retVal
    
    return retVal