import pandas as pd

def extract_data():

    df = pd.read_csv(
    r"C:\Users\AKSHAT\Desktop\jupyter projects\Electricity consumption project\smart electricity project pipeline\DATA\household_power_consumption.csv",
    sep=",",
    na_values=["?"]
    )
    
    print("Data extracted successfully")

    return df