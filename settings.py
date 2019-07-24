from utils.config_to_json import load_json_file_to_dict

config = load_json_file_to_dict()

WORKER_NAME = config['WORKER_NAME']
MQ_CMD = config['MQ_CMD']
MQ_URL = config['MQ_URL']
IMAGE_PATH = config['IMAGE_PATH']
