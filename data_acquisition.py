import pandas


def main():

    database = "C:\\Users\\rishi\\Downloads\\UK_Seabed_Information.csv"
    dataframe = pandas.read_csv(database)
    
    average_depth_weight = -1
    stability_weight = 2
    proximity_weight = -1
    wildlife_presence_weight = -2
    average_wind_speed_weight = 3
    average_wave_height_weight = -1
    average_population_density_of_fish_weight = -1
    average_population_density_of_birds_weight = -1
    wind_consistency_weight = 3
    number_of_wildlife_migration_paths_weight = -2

    for index, row in dataframe.iterrows():
        score = (float(row["Average_Depth"]) * average_depth_weight) + (float(row["Stability"]) * stability_weight) + (float(row["Proximity"]) * proximity_weight) + (float(row["Wildlife_Presence"]) * wildlife_presence_weight) + (float(row["Average_Wind_Speed"]) * average_wind_speed_weight) + (float(row["Average_Wave_Height"]) * average_wave_height_weight) + (float(row["Average_Population_Density_of_Fish"]) * average_population_density_of_fish_weight) + (float(row["Average_Population_Density_of_Birds"]) * average_population_density_of_birds_weight) + (float(row["Wind_Consistency"]) * wind_consistency_weight) + (float(row["Number_of_Wildlife_Migration_Paths"]) * number_of_wildlife_migration_paths_weight)
        dataframe.loc[index, "Score"] = score

    dataframe.to_csv("C:\\Users\\rishi\\Downloads\\UK_Seabed_Information.csv", index=False)

if __name__ == "__main__":
    main()