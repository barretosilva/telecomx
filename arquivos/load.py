import os
from extract import extract_data
from transform import transform_data

def load_data():
    df = extract_data()
    df = transform_data(df)

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/churn_tratado.csv", index=False)

    print("processado")
    

if __name__ == "__main__":
    load_data()