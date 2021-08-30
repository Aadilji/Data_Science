import logging 

## Normal Levels of Errors. (Low Level)
logging.debug("this is a debug")
logging.info('This is Info')

# Some Critical Levels of Erros.:----> It gets Printed. (High Level)
logging.warning('This is a Warning')
logging.error('This is a Error')
logging.critical('This is Critical') 

# Basic Logging:-
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename = 'logfile1.log')     
logging.debug("this is a debug")
logging.info('This is Info')
logging.warning('This is a Warning')
logging.error('This is a Error')
logging.critical('This is Critical')

# Basic 2 
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename='logfile2.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö') 