import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    prefixos = ["customer.", "phone.", "internet.", "account."]
    df.columns = df.columns.str.replace("|".join(prefixos), "", regex=True)

    df.columns = (
    df.columns
        .str.strip()
        .str.replace(".", "_", regex=False)
        .str.lower()
    )

    df = df.rename(columns={"customerid": "customer_id", "d": "customer_id"})

    if "churn" in df.columns:
        df["churn"] = df["churn"].replace("", pd.NA)
        df = df[df["churn"].isin(["Yes", "No"])]

    if "charges_total" in df.columns:
        df["charges_total"] = pd.to_numeric(df["charges_total"], errors="coerce")
        df = df.dropna(subset=["charges_total"])

    mapa_binario = {"Yes": 1, "No": 0}

    colunas_yes_no = [
        "churn", "partner", "dependents", "phoneservice",
        "paperlessbilling", "onlinebackup", "deviceprotection",
        "techsupport", "streamingtv", "streamingmovies", 'multiplelines'
    ]

    for col in colunas_yes_no:
        if col in df.columns:
            df[col] = df[col].map(mapa_binario).astype("Int64")

    return df