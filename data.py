import pandas


class Data:

    def __init__(self, path):
        """

        :param path:
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        """
        :return: list of the names of all different districts in data
        """
        return self.data["denominazione_region"]

    def set_districts_data(self, districts):
        """
        update data to contain all and only the districts from the parameters districts
        :param districts: list of districts
        :return: none
        """
