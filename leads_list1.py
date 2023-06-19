
import streamlit as st
import pandas as pd
import random

# Define the tables
tables = {
  'Arrel Example Leads': {
        'Wallet Address': ['0x016dbc709b8c1667d7205e2c4129167d660dc010', '0x26013b787aac632a92053f669e2de85103ad2536', '0xbc17b5a63fa8fdf28220546bc24b0beb10e2c80f', '0x92f3919d142000396205c613ecd2e428d91cf9220', '0x3615e04d0f21e2c7d2051e561ce8d4a5d0594ee7', '0x2465bd53a0e4f726d289bf059e07979715c44dc0b', '0xde58c7b2335c895c27471a6f237c78b066924370', '0xdc23d1367d84aad239913b8c8579c29e3707e309', '0x7706abe0d94e88760375dc3d0e997d5680324e38', '0xf9dbd46ec67dad89094fe788c29147e00fc25fe7', '0xa0553e045fda77d890741ffd5b58ae7cefdab379', '0xa0553e045fda77890e741ffd5b58ae7cefdab380', '0x016dbc709b8c1667d7205e2c4129167d660dc010', '0x26013b787aac632a92053f669e2de85103ad2536', '0x06a30395353d7d3742e49bf69fd25fdf69a131c8', '0xbc17b5a63fa8fdf28220546bc24b0beb10e2c80f', '0x3615e04d0f21e2c7d2051e561ce8d4a5d0594ee7', '0xbc17b5a63fa8fdf28220546bc24b0beb10e2c80f', '0x016dbc709b8c1667d7205e2c4129167d660dc010', '0xdc23d1367d84aad239913b8c8579c29e3707e309'],
        'GLP Held (USD Value)': ['$5,452.93', '$6,537.06', '$11,117.74', '$11,237.44', '$16,276.17', '$24,459.51', '$3,943.03', '$3,887.21', '$3,509.44', '$945,271.05', '$4,154.09', '$2,986.18', '$2,919.87', '$2,712.84', '$4,434.13', '$4,687.85', '$5,964.27', '$40,734.84', '$16,726.15', '$9,923.58'],
        'Wallet (USD Value)': ['$81,793.95', '$98,055.90', '$166,766.10', '$168,561.56', '$244,142.55', '$366,892.65', '$59,145.45', '$58,308.15', '$52,641.60', '$14,179,065.75', '$62,311.35', '$44,792.70', '$43,798.05', '$40,692.60', '$66,511.89', '$70,317.75', '$89,464.05', '$611,022.60', '$250,892.25', '$148,853.70'],
        'Binance User': ['Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No'],
        'Last On-Chain Activity': ['2023-04-28 13:18:23', '2023-01-11 3:26:58', '2023-04-26 0:51:15', '2023-03-27 4:23:19', '2023-04-27 15:16:41', '2023-04-25 0:31:29', '2023-02-17 12:18:13', '2023-04-26 19:31:05', '2023-03-28 11:05:54', '2023-03-23 8:01:57', '2023-04-01 7:38:00', '2023-02-03 10:15:09', '2023-04-25 21:11:38', '2023-04-27 12:45:18', '2023-04-23 18:01:25', '2023-04-19 21:12:36', '2023-04-20 20:51:37', '2023-04-28 1:12:27', '2023-04-25 9:48:11', '2023-04-28 1:12:27'],
        'Total EVM Transactions': ['817', '2,724', '1,795', '3,543', '88', '769', '913', '479', '778', '1,022', '117', '515', '620', '2,338', '121', '57', '596', '95', '282', '267'],
        'Twitter': ['N/A', 'N/A', '***********', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'Redacted', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'Redacted', 'N/A', 'N/A', 'N/A'],
        'Discord': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'Redacted', 'N/A', 'N/A', 'N/A'],
        'Email': ['N/A', 'N/A', 'Redacted', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
        'Discord': ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'Redacted', 'N/A', 'N/A', 'N/A'],
             
  },
 'Gambling Example Leads': {
        'Wallet/User': ['0x29ab82Ec552573b1B7d4933B2AaA3C568be9C6D1', '0xBE7CE5358977B00868C52045fb6c2790514efE68', '0xc9a648CF30D16079e48404F6Fd1Fd7Be83650C4d', '0xB5A16b3962BAcEB2CB292047333b58AaD1E060EE']*5,
        'Wallet Value (USD)': [1000, 500, 2000, 1500]*5,
        'Email': ['John33@gmail.com', 'Allenkjb@gmail.com', 'Opal@gmail.com', 'CryptoJacob@hotmail.com']*5,
        'Twitter': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
        'Telegram': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
        'Discord': ['John33#1234', 'Allenkjb#1234', 'Opal#1234', 'CryptoJacob#1234']*5,
        'linkedin': ['John33', 'Allenkjb', 'Opal', 'CryptoJacob']*5,
        'Deposit Value': [500, 1000, 1500, 200]*5,
        'TLV': [15000, 1500, 350000, 17000]*5,
        'Last Transaction Date': ['2022-05-01', '2023-03-15', '2023-04-20', '2023-05-25']*5,

    },
    'Liquidity Provider Example Leads': {
        'Wallet/User': ['0x29ab82Ec552573b1B7d4933B2AaA3C568be9C6D1', '0xBE7CE5358977B00868C52045fb6c2790514efE68', '0xc9a648CF30D16079e48404F6Fd1Fd7Be83650C4d', '0xB5A16b3962BAcEB2CB292047333b58AaD1E060EE']*5,
        'Wallet Value (USD)': [1000, 500, 2000, 1500]*5,
        'Liquidity Provider Y/N': ['N', 'Y', 'N', 'Y']*5,
        'Deposit Value': [500, 1000, 1500, 200]*5,
        'TLV': [1500, 1500, 3500, 1700]*5,
        'Last Transaction Date': ['2022-05-01', '2023-03-15', '2023-04-20', '2023-05-25']*5,
        'Email': ['John33@gmail.com', 'Allenkjb@gmail.com', 'Opal@gmail.com', 'CryptoJacob@hotmail.com']*5,
        'Twitter': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
        'Telegram': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
        'Discord': ['John33#1234', 'Allenkjb#1234', 'Opal#1234', 'CryptoJacob#1234']*5,
        'linkedin': ['John33', 'Allenkjb', 'Opal', 'CryptoJacob']*5,
   },
    'NFT Lending Example Leads': {
        'Wallet/User': ['0x' + ''.join(random.choices('0123456789ABCDEF', k=40)) for _ in range(20)],
        'Wallet Value (USD)': random.choices(range(1000, 5000), k=20),
        'Gambling User Y/N': random.choices(['N', 'Y'], k=20),
        'Deposit Value': random.choices(range(100, 2000), k=20),
        'TLV': random.choices(range(1000, 5000), k=20),
        'Last Transaction Date': pd.date_range(start='2023-06-01', periods=20),
        'Email': ['emma12@gmail.com', 'N/A', 'cryptoconnect@gmail.com', 'N/A']*5,
        'Twitter': ['@emma12', '@davidsmith23', 'N/A', '@johnnybrown']*5,
        'Telegram': ['N/A', '@davidsmith23', '@cryptoconnect', '@johnnybrown']*5,
        'Discord': ['emma12#5678', 'N/A', 'N/A', 'johnnybrown#5678']*5,
        'LinkedIn': ['N/A', 'David Smith', 'N/A', 'Johnny Brown']*5
    },
    'DEX Users Example Leads': {
        'Wallet/User': ['0x' + ''.join(random.choices('0123456789ABCDEF', k=40)) for _ in range(20)],
        'Wallet Value (USD)': random.choices(range(1000, 5000), k=20),
        'Gambling User Y/N': random.choices(['N', 'Y'], k=20),
        'Deposit Value': random.choices(range(100, 2000), k=20),
        'TLV': random.choices(range(1000, 5000), k=20),
        'Last Transaction Date': pd.date_range(start='2023-06-01', periods=20),
        'Email': ['John33@gmail.com', 'Allenkjb@gmail.com', 'Opal@gmail.com', 'CryptoJacob@hotmail.com'] * 5,
        'Twitter': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob'] * 5,
        'Telegram': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob'] * 5,
        'Discord': ['John33#1234', 'Allenkjb#1234', 'Opal#1234', 'CryptoJacob#1234'] * 5,
        'linkedin': ['John33', 'Allenkjb', 'Opal', 'CryptoJacob'] * 5
    },
    'Perpetual Traders Example Leads': {
        'Wallet/User': ['0x' + ''.join(random.choices('0123456789ABCDEF', k=40)) for _ in range(20)],
        'Wallet Value (USD)': random.choices(range(1000, 10000000), k=20),
        'Trades': random.choices(range(1, 5000), k=20),
        'Volume': random.choices(range(100, 1000000000), k=20),
        'Avg. Size': random.choices(range(1, 6000000), k=20),
        'Fees': random.choices(range(1, 17000000), k=20),
        'PnL': random.choices(range(-5000000, 5000000), k=20),
        'Last Transaction Date': pd.date_range(start='2023-06-01', periods=20),
        'Email': ['John33@gmail.com', 'N/A', 'Opal@gmail.com', 'CryptoJacob@hotmail.com'] * 5,
        'Twitter': ['N/A', '@Allenkjb', '@Opal', '@CryptoJacob'] * 5,
        'Telegram': ['@John33', 'N/A', 'N/A', '@CryptoJacob'] * 5,
        'Discord': ['John33#1234', 'Allenkjb#1234', 'Opal#1234', 'N/A'] * 5,
        'linkedin': ['N/A', 'N/A', 'Opal', 'CryptoJacob'] * 5
    }
}

Metrics = {
    'Arrel Example Leads': {
        'Total Wallets Tracked': 'TBD',
        'Leads Available': 'TBD',
        'Fees Generated': 'TBD',
        'Trades Completed': 'TBD'
    },
    'Gambling Example Leads': {
        'Total Wallets Tracked': '1.4m',
        'Leads Available': '27k',
        'Fees Generated': '$1',
        'Trades Completed': '$1'
    },
    'Liquidity Provider Example Leads': {     
        'Total Wallets Tracked': 'TBD',
        'Leads Available': 'TBD',
        'Fees Generated': 'TBD',
        'Trades Completed': 'TBD'
    },  
    'NFT Lending Example Leads': {     
        'Total Wallets Tracked': 'TBD',    
        'Leads Available': 'TBD',     
        'Fees Generated': 'TBD',     
        'Trades Completed': 'TBD'    
    },    
    'DEX Users Example Leads': {     
        'Total Wallets Tracked': 'TBD',     
        'Leads Available': 'TBD',     
        'Fees Generated': 'TBD',     
        'Trades Completed': 'TBD'    
        },    
    'Perpetual Traders Example Leads': {     
        'Total Wallets Tracked': '667,453',     
        'Leads Available': '13,215',     
        'Fees Generated': '$281m',     
        'Volume': '$244m'
    }
                                                                                                                                                                                                                                                                                                                        
}


def main():
    # Set page configuration
    st.set_page_config(
        page_title='Arrel Example Leads',
        page_icon='💰',
        layout='wide',
        initial_sidebar_state='expanded'
    )

    # Title
    st.markdown("<h1 style='text-align: center;'>Example Leads</h1>", unsafe_allow_html=True)

    # Add logo
    logo_path = 'slice_logo_clear.png'  # Replace with the path to your logo image
    st.sidebar.image(logo_path, use_column_width=True)

    # Create a dropdown selector in the sidebar
    table_selection = st.sidebar.selectbox('Select Sector', list(tables.keys()))
    
#     # Create a dropdown selector in the sidebar
#     wallet_value_selection = st.sidebar.selectbox('Wallet Value', ['Wallet Value over $10m', 'Wallet Value over $1m', 'Wallet Value over $100k', 'Wallet Value over $10k'])

#     # Create a dropdown selector in the sidebar
#     activity_by_chain_selection = st.sidebar.selectbox('Activity by Chain', ['Active on Ethereum', 'Active on Polygon', 'Active on Arbitrum', 'Active on BNB', 'Active on Avalanche', 'All Others'])

#     # Search for contact by address
#     search_address = st.sidebar.text_input('Search for Contact by Address', value='0x...')


    cols_titles = ['Total Wallets', 'Life Time Value', 'Fees Generated', 'Trades Completed']
    cols_data = [Metrics.get(table_selection,{}).get('Total Wallets','NA'), Metrics.get(table_selection,{}).get('Life Time Value','NA'), Metrics.get(table_selection,{}).get('Fees Generated','NA'), Metrics.get(table_selection,{}).get('Trades Completed','NA')]
    cols = st.columns(len(cols_titles))

    for i in range(len(cols_titles)):
        with cols[i]:
            st.metric(label=cols_titles[i], value=cols_data[i])

    # Display the selected table in wide mode
    df = pd.DataFrame(tables[table_selection])
    st.dataframe(df, width=1800)
    
     # Download button
    csv = df.to_csv(index=False)
    download_filename = f"{table_selection}_data.csv"
    st.download_button("Download Data", data=csv, file_name=download_filename, mime='text/csv')

if __name__ == '__main__':
    main()
