import pandas as pd
from datetime import datetime


def toOduncXls(data):
    df = pd.DataFrame(data)
    # Try to read the existing Excel file (if it exists)
    try:
        existing_df = pd.read_excel("OduncLogs.xlsx")
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass  # If the file doesn't exist, continue with the new DataFrame

    # Save the DataFrame to an Excel file with the timestamp
    df.to_excel("OduncLogs.xlsx", index=False)


def toIadeXls(data):
    df = pd.DataFrame(data)
    # Try to read the existing Excel file (if it exists)
    try:
        existing_df = pd.read_excel("IadeLogs.xlsx")
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass  # If the file doesn't exist, continue with the new DataFrame

    # Save the DataFrame to an Excel file with the timestamp
    df.to_excel("IadeLogs.xlsx", index=False)


# # Your variables
# tcNo = 47341014396
demirbasNo = "01050652"

# # Create a dictionary with your variables
data = {

    "Demirbas No": [demirbasNo],
    "Tarih": [datetime.now().date().strftime("%d-%m-%Y")],
    "Saat": [datetime.now().time().strftime("%H:%M:%S")],
}

# toOduncXls(data=data)
toIadeXls(data=data)
