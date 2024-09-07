import requests
import pandas as pd
import xlwings as xw
import time
import os
from datetime import datetime

def fetch_nse_data():
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    
    try:
        session = requests.Session()
        response = session.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()["records"]["data"]
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_data(data):
    rows = []
    for item in data:
        call_vol = item.get('CE', {}).get('totalTradedVolume', 0)
        if call_vol:
            call_vol *= 25  # Multiply CALL VOL by 25
        row = {
            'STRIKE': item['strikePrice'],
            'CALL LTP': item.get('CE', {}).get('lastPrice', ''),
            'CALL LTPCHG': item.get('CE', {}).get('change', ''),
            'CALL VOL': call_vol,
            'CALL OI': item.get('CE', {}).get('openInterest', ''),
            'CALL OICHG': item.get('CE', {}).get('changeinOpenInterest', ''),
            'PUT LTP': item.get('PE', {}).get('lastPrice', ''),
            'PUT LTPCHG': item.get('PE', {}).get('change', ''),
            'PUT VOL': item.get('PE', {}).get('totalTradedVolume', ''),
            'PUT OI': item.get('PE', {}).get('openInterest', ''),
            'PUT OICHG': item.get('PE', {}).get('changeinOpenInterest', ''),
        }
        rows.append(row)
    
    df = pd.DataFrame(rows)
    df = df.sort_values('STRIKE')
    return df

def save_to_excel(df, file_path='optionchaintracker1.xlsx', sheet_name='nifty'):
    if os.path.exists(file_path):
        wb = xw.Book(file_path)
    else:
        wb = xw.Book()
        wb.save(file_path)

    if sheet_name in [sheet.name for sheet in wb.sheets]:
        st = wb.sheets[sheet_name]
    else:
        st = wb.sheets.add(sheet_name)

    # Clear existing content
    st.clear_contents()

    # Write the DataFrame to the sheet
    st.range("A1").value = df

    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.range(f"A{len(df)+3}").value = f"Last updated: {timestamp}"

    wb.save(file_path)
    wb.close()

def main():
    while True:
        data = fetch_nse_data()
        if data:
            df = parse_data(data)
            save_to_excel(df)
            print(f"Data saved at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("Failed to fetch data. Retrying in 60 seconds...")
        
        time.sleep(60)  # Wait for 60 seconds before the next fetch

if __name__ == "__main__":
    main()