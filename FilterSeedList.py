import logging
import os
import sys
from datetime import datetime

# logging configuration
logger = logging.getLogger('FilterSeedListLogger')
logger.setLevel(logging.DEBUG)
logFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)
now = datetime.now()
dateTime = now.strftime("%Y-%m-%d_%H_%M_%S")
LOG_FILE_NAME = "FilterSeedList_" + dateTime + ".log"
fileHandler = logging.FileHandler(LOG_FILE_NAME)
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

INPUT_SEED_FILE = ""
FILTER_OUT_FILE = ""
LOG_LEVEL = ""
filterOutList = []


def main(argv):
    logger.info("********************************************")
    logger.info("**********   FilterSeedList   *************")
    logger.info("********************************************\n\n")

    now = datetime.now()
    dateTime = now.strftime("%Y-%m-%d %H:%M:%S")
    logger.info("Starting datetime: " + dateTime)

    load_external_configuration()
    url_list = load_seed_file(INPUT_SEED_FILE)
    global filterOutList
    filterOutList = load_filter_out_file(FILTER_OUT_FILE)
    produce_filtered_list(url_list)

    now = datetime.now()
    dateTime = now.strftime("%Y-%m-%d %H:%M:%S")
    logger.info("Ending datetime: " + dateTime)


def load_external_configuration():
    global INPUT_SEED_FILE
    global FILTER_OUT_FILE
    global LOG_LEVEL

    config_file = "config.cfg"
    if not os.path.isfile(config_file):
        logger.error("No \"config.cfg\" configuration file found in the program directory !")
        logger.error("USAGE: FilterSeedList config.cfg")
        raise FileNotFoundError("No \"config.cfg\" configuration file found in the program directory !")

    external_settings = dict()
    with open(config_file, "rt") as f:
        for line in f.readlines():
            if not line.startswith("#"):
                tokens = line.split("=")
                if len(tokens) == 2:
                    external_settings[tokens[0]] = tokens[1]

    INPUT_SEED_FILE = str(external_settings.get("INPUT_SEED_FILE", "")).rstrip()
    if not os.path.isfile(INPUT_SEED_FILE):
        logger.error("Invalid INPUT_SEED_FILE parameter !")
        raise FileNotFoundError("Invalid INPUT_SEED_FILE parameter !")

    FILTER_OUT_FILE = str(external_settings.get("FILTER_OUT_FILE", "")).rstrip()
    if not os.path.isfile(FILTER_OUT_FILE):
        logger.error("Invalid FILTER_OUT_FILE parameter !")
        raise FileNotFoundError("Invalid FILTER_OUT_FILE parameter !")

    LOG_LEVEL = str(external_settings.get("LOG_LEVEL", "INFO")).rstrip()
    consoleHandler.setLevel(LOG_LEVEL)
    fileHandler.setLevel(LOG_LEVEL)


def produce_filtered_list(url_list):
    url_list_len = len(url_list)
    now = datetime.now()
    dateTime = now.strftime("%Y-%m-%d_%H_%M_%S")
    filtered_file_name = "filteredSeed_" + dateTime + ".txt"
    deleted_file_name = "deletedSeed_" + dateTime + ".txt"

    with open(deleted_file_name, 'a+', encoding='utf-8') as p:
        with open(filtered_file_name, 'a+', encoding='utf-8') as f:
            f.writelines("firm_id" + "\t" + "link_pos" + "\t" + "url" + "\n")
            p.writelines("firm_id" + "\t" + "link_pos" + "\t" + "url" + "\n")
            for i, row in enumerate(url_list[1:]):
                logger.info(str(i + 1) + " / " + str(url_list_len) + " ) I am processing link " + row[1] + " of firm having id " + row[0])
                if is_acceptable(str(row[2])):
                    f.writelines(str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\n")
                    f.flush()
                else:
                    p.writelines(str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\n")
                    f.flush()


def is_acceptable(url):
    result = True
    for domain in filterOutList:
        if domain in url:
            result = False
            break
    return result


def load_seed_file(seed_file):
    url_list = []

    with open(seed_file, "rt") as f:
        for line in f.readlines():
            tokens = line.split("\t")
            if len(tokens) == 3:
                my_tuple = (tokens[0], tokens[1].rstrip(), tokens[2].rstrip())
                url_list.append(my_tuple)

            else:
                logger.warning("the row having id=" + tokens[0] + " is malformed and will not be considered !")

    return url_list


def load_filter_out_file(filter_out_file):
    filter_list = []

    with open(filter_out_file, "rt") as f:
        for line in f.readlines():
            if len(line.strip()) > 0:
                filter_list.append(line.strip())

    return filter_list


if __name__ == "__main__":
    main(sys.argv[1:])
