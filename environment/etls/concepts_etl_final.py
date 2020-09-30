# ETL de concepts para Usarlo con RabbitMQ
import mysql.connector
import logging.config
import configparser
import database
import utils
import concepts_file_parser
import os

def _get_logger():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    dir_name, filename = os.path.split(os.path.abspath(__file__))
    output_file = dir_name + "/concepts_etl.log"
    handler = logging.FileHandler(output_file)
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG) # DEBUG - INFO - WARN - ERROR
    logger.addHandler(handler)
    return logger

logger = _get_logger()

def load_concepts(file_path, concept1, cnx):
    concepts_read = 0
    concepts_inserted = 0
    concepts_errors = 0
    row = 2
    for line in utils.read_csv_file(file_path, delimiter='\t'):
        concept = concepts_file_parser.get_concepts(line)
        concepts_read += 1
        try:
            if (len(concept['pxordx']) != 0 and
                len(concept['codetype']) != 0 and
                len(concept['vocabulary_id']) != 0 and 
                len(concept['domain_id']) != 0 and 
                len(concept['code']) != 0):

                # Add new concept to dictionary
                ref1 = concept['concept_id']
                if ref1 != None:
                    concepts_ref = concept['code'] + ref1
                else:
                    concepts_ref = concept['code']
                if (concepts_ref not in concept1):
                    id = database.add_concepts(concept,
                                                 cnx)
                                                 
                    concept[concepts_ref] = id
                    logger.info("Inserting concept code {0} in database.".format(concepts_ref))
                    concepts_inserted += 1
                else:
                    logger.info("concept code {0} already exists in database.".format(concepts_ref))
            else:
                message = "Error in row: %d, missing fields to create new concept." % row
                logger.error(message)
                print(message)
                concepts_errors += 1
        except Exception as e:
            message = str(e) + " file: {0} - row: {1}".format(file_path, row)
            logger.error(message)
            print(message)
            concepts_errors += 1
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
    concepts = database.get_current_concepts(cnx)
    print(concepts)

    print("*********** processing file %s *****************" % path_file)
    logger.info('processing file %s' % path_file)
    resultado = load_concepts(path_file, concepts, cnx)

    print("completed processing of the vocabularies")
    logger.info('Completed processing of file')
    return resultado
