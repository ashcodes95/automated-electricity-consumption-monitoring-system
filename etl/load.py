from sqlalchemy import create_engine

def load_data(df):

    engine = create_engine(
        "postgresql://postgres@localhost:5432/energy_project"
    )

    df.to_sql(
        "electricity_usage",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded to PostgreSQL successfully")