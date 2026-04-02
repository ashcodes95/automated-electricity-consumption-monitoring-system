from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def run_pipeline():

    print("Starting pipeline...")

    df = extract_data()

    df = transform_data(df)

    print("Sending data to load step...")

    load_data(df)

    print("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()