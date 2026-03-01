import requests
import pandas as pd

URL = "https://raw.githubusercontent.com/alura-cursos/challenge2-data-science/refs/heads/main/TelecomX_Data.json"

def extract_data(url=URL) -> pd.DataFrame:
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    df = pd.json_normalize(data)
    
    return df

if __name__ == "__main__":
    df = extract_data()
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(df.head())