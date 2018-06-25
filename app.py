import os

import configparser
import connexion
import glog as log

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')

log.info("Starting the app")

app_directory = os.path.dirname(os.path.realpath(__file__))
swagger_directory = os.path.join(app_directory, 'swagger')
APP = connexion.App(__name__, port=int(CONFIG.get('Development', 'PORT')), specification_dir=swagger_directory)
APP.add_api('app.yaml')

if __name__ == '__main__':
    APP.run(server='gevent', host="0.0.0.0")