import datetime

import allure
from allure_commons.model2 import Link, Label
from allure_commons.types import LinkType, LabelType

from helpers.file_reader import load_yml


def add_tags_allure(item):
    # add tags to allure report
    if hasattr(Context.test_result, 'labels'):
        for marker in item.iter_markers():
            if marker.name == 'case_id':
                Context.case_ids = marker.args
                Context.test_result.labels.extend(
                    Label(name=LabelType.TAG, value=case_id) for case_id in Context.case_ids
                )
            else:
                Context.test_result.labels.append(
                    Label(name=LabelType.TAG, value=marker.name))


def add_links_allure():
    # add links to allure report
    for case_id in Context.case_ids:
        link_to_tr = f"https://gdcgroup.testrail.io/index.php?/cases/view/{case_id}"
        Context.test_result.links.append(
            Link(type=LinkType.TEST_CASE, url=link_to_tr, name=link_to_tr
                 ))


class Context(type):
    """Used to store variables that are globally available"""

    def content(cls):
        return {key: value for key, value in cls.__dict__.items()
                if not key.startswith('_') and key != 'content'}

    def __getattr__(cls, item):
        return cls.__dict__[item]

    def __setattr__(cls, key, value):
        cls.__dict__[key] = value


def load_yaml_file():
    yaml_config = load_yml()
    Context.config = yaml_config


def get_config_key(config_key):
    """
    Get value from config
    :param config_key: File name without the .json
    :return: Returns string
    """
    dict_key = Context.config[config_key]
    for i in dict_key:
        for k, v in i.items():
            if v is True:
                return k.lower()


def get_time_stamp():
    current_time = datetime.datetime.now()
    return current_time
