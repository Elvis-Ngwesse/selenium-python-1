import os
import json
import yaml

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))


def get_feature_file_path(file_name: str):
    feature_file = os.path.join(ROOT_DIR, f"tests/features/genesis/{file_name}.feature")
    return feature_file


def load_json(data_file: str):
    """
    Get file path from data folder
    :param data_file: File name without the .json
    :return: Returns file path
    """
    data_folder = {}
    try:
        with open(os.path.join(ROOT_DIR, f"json_data/{data_file}.json"), encoding="utf-8") as json_data:
            data_folder[f'{data_file}'] = json.load(json_data)
    except IOError as error:
        return error
    return data_folder[f"{data_file}"]


def load_yml(file_name="conf"):
    """Use this function to load the root yml file"""
    with open(os.path.join(ROOT_DIR, "%s.yml" % file_name), encoding="utf-8") as config:
        settings = yaml.load(config, Loader=yaml.FullLoader)
    return settings
