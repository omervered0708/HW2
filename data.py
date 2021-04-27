import pandas


class Data:
    def __init__(self, path):
        """
        the function loads the data from the csv file
         :param path: the path to the csv file
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        """

        :return: return the a list of the districts names
        """
        helper = set(self.data["denominazione_region"])
        return list(helper)

    def set_districts_data(self, districts):
        """
        the functions changes data so that only the records with districts in district remain
        :param districts: a list of district names
        """
        help_dict = {}
        init_dict(help_dict, self.data)
        for i, district in enumerate(self.data["denominazione_region"]):
            if district in districts:
                copy_to_dict(self.data, i, help_dict)
        self.data = help_dict


def init_dict(dict, data):
    """
    the function initializes dict with the keys from data and empty lists as values
    :param dict: a dictionary to initialize
    :param data: a dictionary with the keys used to initialize dict
    :return: none
    """
    for key in data.keys():
        dict[key] = []


def copy_to_dict(data, i, dict):
    """
    the function copies the ith value in each list in data to dict
    :param data: a dictionary to copy from
    :param i: index in the lists to copy
    :param dict: a dictionary to copy to
    :return: none
    """
    for key, dict_value in data.items():
        dict[key].append(dict_value[i])
