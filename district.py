import data
import statistics


class District:

    def __init__(self, dataset):
        """
        constructor for District objects
        :param dataset: Data object
        """
        self.dataset = dataset

    def filter_district(self, letters):
        """
        update 'self.dataset' to contain only data for districts with names beginning with letters from 'letters'.
        :param letters: set of letters
        :return: none
        """
        districts_set = [ district for district in self.dataset.data["denominazione_region"] if district[0] in letters ]
        self.dataset.set_districts_data(districts_set)

    def print_details(self, features, statistic_functions):
        """
        print statistical indices on the 'data' field of 'self.dataset' only by the features in 'features' with the
        functions in 'statistic_functions'.
        :param features: list of features
        :param statistic_functions: list of statistic functions from statistics.py
        :return:
        """
        for feature in features:
            print(f"{feature}: ", end='')
            print(*[func(self.dataset.data[feature]) for func in statistic_functions], sep=', ', end='\n')

    def determine_day_type(self):
        """
        add a key to field 'data' of 'self.dataset' named 'day_type' whose value is a list of indicators representing
        whether a day is a "good_day"(=1) or a "bad_day"(=0) for each record
        :return: none
        """
        # add 'day_type' key to 'self.dataset.data'
        self.dataset.data["day_type"] = []
        # create zip object of pairs of "resigned_healed" and "new_positives"
        relevant_pairs = zip(self.dataset.data["resigned_healed"], self.dataset.data["new_positives"])
        # fill 'self.dataset.data["day_type"]'
        for res_heal, new_pos in relevant_pairs:
            self.dataset.data["day_type"].append(int(res_heal > new_pos))

    def get_district_class(self):
        """
        :return: dictionary whose keys are the names of all districts in 'self.dataset.data' and values are the stings
        "green" or "not green"
        """
        self.determine_day_type()
        # initialize 'return_dict'
        return_dict = {}
        for dist in self.dataset.data["denominazione_region"]:
            return_dict[dist] = 0
        # create zip object of pairs of "district" and "day_type"
        relevant_pairs = zip(self.dataset.data["denominazione_region"], self.dataset.data["day_type"])
        # fill 'return_dict'
        for district, day_type in relevant_pairs:
            return_dict[district] += day_type

        for dist_key in return_dict.keys():
            if return_dict[dist_key] > 340:
                return_dict[dist_key] = "green"
            else:
                return_dict[dist_key] = "not green"

        return return_dict

    def not_green_num(self):
        """
        :return: the number of district which are not green
        """
        # find green and not green district
        is_green_dict = self.get_district_class()
        # count the number of 'not green' districts
        count = 0
        for value in is_green_dict.values():
            if value == "not green":
                count += 1

        return count

