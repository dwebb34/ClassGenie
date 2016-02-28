################################################################################
# ClassGeneie is a utilty to generate C++ classes from a template file
# 
#
#
# Devin Webb
#   devin.a.webb@gmail.com
################################################################################

def import_args():
    import argparse
    
    description = 'Command line interface for ClassGenie '

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--config_file', dest='config', action='store', required='True',
                        help='Config file that sets necessary class definition'
                        'parameters. If a configuration item is present in both')
    parser.add_argument('--version', action='version',
                        version='ClassGenie 0.1',
                        help='Show the version number and exit.')


    '''options = parser.parse_args()
    
    if isinstance(options, tuple):
        args = options[0]
    else:
        args = options
    del options'''
    
    #return the args as a dictionary
    args = vars(parser.parse_args())
    
    return args

def start():
    
    from genie_classes import GenieProject
    from genie_writers import write_genie_project as write_
    import os
    
    args = import_args()
    
    pathToConfig = args['config']
    
    if (not os.path.isfile(pathToConfig)):
        '''might be a relative path'''
        pathToConfig = os.path.abspath(pathToConfig)
        if (not os.path.isfile(pathToConfig)):
            print("didn't find path...")
            print("do something...")

    genie = GenieProject()
    genie.prepare(args['config'])
    write_(genie)
    
    return

def main():
    try:
        start()
    except KeyboardInterrupt:
        print_('\nCancelling...')

if __name__ == "__main__":
    main()
