import sys
import data
import district
import statistiscs


def main(argv):
    dataset = data.Data(argv[1])
    dist = district.District(dataset)
    dist.filter_district({"L", "S"})
    features = ["hospitalized_with_symptoms", "Intensive_care", "total_hospitalized", "home_insulation"]
    stat_funcs = [statistiscs.mean, statistiscs.median]
    dist.print_details(features, stat_funcs)


if __name__ == '__main__':
    main(sys.argv)
