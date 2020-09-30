# ETL de vocabulary para Usarlo con RabbitMQ
import mysql.connector
import logging.config
import configparser
import database
import utils
import vocabulary_file_parser
import os

def _get_logger():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    dir_name, filename = os.path.split(os.path.abspath(__file__))
    output_file = dir_name + "/vocabulary_etl.log"
    handler = logging.FileHandler(output_file)
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG) # DEBUG - INFO - WARN - ERROR
    logger.addHandler(handler)
    return logger

logger = _get_logger()

def load_vocabularies(file_path, vocabularies, cnx):
    vocabulary_read = 0
    vocabulary_inserted = 0
    vocabulary_errors = 0
    row = 2
    for line in utils.read_csv_file(file_path, delimiter='\t'):
        vocabulary = vocabulary_file_parser.get_vocabulary(line)
        vocabulary_read += 1
        try:
            if (len(vocabulary['ref']) != 0 and
                len(vocabulary['name']) != 0 and
                len(vocabulary['url']) != 0 and
                len(vocabulary['version']) != 0 and
                len(vocabulary['description']) != 0 and 
                len(vocabulary['status']) != 0):

                # Add new vocabulary to dictionary
                vocabulary_ref = vocabulary['ref'].strip()
                if vocabulary_ref not in vocabularies:
                    id = database.add_vocabulary(vocabulary,
                                                 cnx)
                                                 
                    vocabularies[vocabulary_ref] = id
                    logger.info("Inserting vocabulary ref {0} in database.".format(vocabulary['ref']))
                    vocabulary_inserted += 1
                else:
                    logger.info("Vocabulary ref {0} already exists in database.".format(vocabulary['ref']))
            else:
                message = "Error in row: %d, missing fields to create new vocabulary." % row
                logger.error(message)
                print(message)
                vocabulary_errors += 1
        except Exception as e:
            message = str(e) + " file: {0} - row: {1}".format(file_path, row)
            logger.error(message)
            print(message)
            vocabulary_errors += 1
            return False
        row += 1
    return True

def execute(path_file):
    config = configparser.ConfigParser()
    config.read('config.ini')
    database_configuration = config['database']

    config = {
      'user': database_configuration['db_user'],
      'password': database_configuration['db_password'],
      'host': database_configuration['db_host'],
      'database': database_configuration['db_schema'],
      'raise_on_warnings': True
    }

    logger.info("Connecting to database...")
    cnx = mysql.connector.connect(**config)
    logger.info("The connection to the database was succesfull")

    logger.info('Getting all current vocabularies from database')
    vocabularies = database.get_current_vocabularies(cnx)
    print(vocabularies)

    print("*********** processing file %s *****************" % path_file)
    logger.info('processing file %s' % path_file)
    resultado = load_vocabularies(path_file, vocabularies, cnx)

    print("completed processing of the vocabularies")
    logger.info('Completed processing of file')
    return resultado
