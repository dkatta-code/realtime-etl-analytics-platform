import pandas as pd
import numpy as np

def normalize_dataframe(records):

    dataframe = pd.DataFrame(records)

    dataframe["amount_category"] = pd.cut(
        dataframe["amount"],
        bins=[0, 100, 500, 1000, 5000],
        labels=[
            "LOW",
            "MEDIUM",
            "HIGH",
            "PREMIUM"
        ]
    )

    dataframe["quantity_bucket"] = pd.cut(
        dataframe["quantity"],
        bins=[0, 2, 5, 10],
        labels=[
            "SMALL",
            "MEDIUM",
            "BULK"
        ]
    )

    dataframe["processing_fee"] = np.where(
        dataframe["amount"] > 1000,
        dataframe["amount"] * 0.03,
        dataframe["amount"] * 0.015
    )

    dataframe["net_amount"] = (
        dataframe["amount"] -
        dataframe["processing_fee"]
    )

    dataframe["event_date"] = pd.to_datetime(
        dataframe["created_at"]
    ).dt.date

    dataframe["event_hour"] = pd.to_datetime(
        dataframe["created_at"]
    ).dt.hour

    dataframe["is_high_value_customer"] = np.where(
        dataframe["amount"] > 1500,
        1,
        0
    )

    dataframe["risk_flag"] = np.where(
        (
            (dataframe["payment_status"] == "FAILED") &
            (dataframe["amount"] > 2000)
        ),
        "HIGH_RISK",
        "NORMAL"
    )

    return dataframe
