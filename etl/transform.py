import pandas as pd

def transform_data(df):

    cols = [
        "Global_active_power",
        "Global_reactive_power",
        "Voltage",
        "Global_intensity",
        "Sub_metering_1",
        "Sub_metering_2",
        "Sub_metering_3"
    ]

    df[cols] = df[cols].apply(pd.to_numeric)

    df = df.dropna()

    df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"])

    df = df.drop(["Date","Time"], axis=1)

    df["hour"] = df["datetime"].dt.hour
    df["day"] = df["datetime"].dt.day
    df["month"] = df["datetime"].dt.month
    df["year"] = df["datetime"].dt.year

    df["other_appliances"] = (
        df["Global_active_power"] * 1000 / 60
        - df["Sub_metering_1"]
        - df["Sub_metering_2"]
        - df["Sub_metering_3"]
    )

    print("Data transformed successfully")

    return df