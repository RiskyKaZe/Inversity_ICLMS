import pandas


def main():

    database = "C:\\Users\\rishi\\Downloads\\UK_Seabed_Information.csv"
    dataframe = pandas.read_csv(database)
    
    print(dataframe)


if __name__ == "__main__":
    main()