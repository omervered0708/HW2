import sys
import data
import district
import statistiscs


def main(argv):
    print("Question 1:")
    dataset1 = data.Data(argv[1])
    dist1 = district.District(dataset1)
    dist1.filter_district({"L", "S"})
    features = ["hospitalized_with_symptoms", "intensive_care", "total_hospitalized", "home_insulation"]
    stat_funcs = [statistiscs.mean, statistiscs.median]
    dist1.print_details(features, stat_funcs)
    dataset2 = data.Data(argv[1])
    district_names = dataset2.get_all_districts()
    print("\nQuestion 2:")
    print(f"Number of districts: {len(district_names)}")
    dist2 = district.District(dataset2)
    not_green = dist2.not_green_num()
    print(f"Number of not green districts: {not_green}")
    print(f"Will a lockdown be forced on whole of Italy?: {'Yes' if not_green > 10 else 'No' }")


if __name__ == '__main__':
    main(sys.argv)
