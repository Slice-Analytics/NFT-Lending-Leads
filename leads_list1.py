# import streamlit as st
# import pandas as pd

# def generate_table():
#     data = {
#         'Wallet/User': ['0x29ab82Ec552573b1B7d4933B2AaA3C568be9C6D1', '0xBE7CE5358977B00868C52045fb6c2790514efE68', '0xc9a648CF30D16079e48404F6Fd1Fd7Be83650C4d', '0xB5A16b3962BAcEB2CB292047333b58AaD1E060EE'],
#         'Wallet Value (USD)': [1000, 500, 2000, 1500]*5,
#         'Gambling User Y/N': ['N', 'Y', 'N', 'Y']*5,
#         'Deposit Value': [500, 1000, 1500, 200]*5,
#         'TLV': [1500, 1500, 3500, 1700]*5,
#         'Last Transaction Date': ['2022-05-01', '2023-03-15', '2023-04-20', '2023-05-25']*5,
#         'Email': ['John33@gmail.com', 'Allenkjb@gmail.com', 'Opal@gmail.com', 'CryptoJacob@hotmail.com']*5,
#         'Twitter': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
#         'Telegram': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
#         'Discord': ['John33#1234', 'Allenkjb#1234', 'Opal#1234', 'CryptoJacob#1234']*5,
#         'linkedin': ['John33', 'Allenkjb', 'Opal', 'CryptoJacob']*5,
#     }

#     df = pd.DataFrame(data)
#     return df

# def main():
#     st.title('Leads List - Gambling Users')
#     df = generate_table()
#     st.dataframe(df)

# if __name__ == '__main__':
#     main()




# import streamlit as st
# import pandas as pd


# # Define the tables
# tables = {
#     'Gambling Leads': {
#         'Wallet/User': ['0x29ab82Ec552573b1B7d4933B2AaA3C568be9C6D1', '0xBE7CE5358977B00868C52045fb6c2790514efE68', '0xc9a648CF30D16079e48404F6Fd1Fd7Be83650C4d', '0xB5A16b3962BAcEB2CB292047333b58AaD1E060EE']*5,
#         'Wallet Value (USD)': [1000, 500, 2000, 1500]*5,
#         'Gambling User Y/N': ['N', 'Y', 'N', 'Y']*5,
#         'Deposit Value': [500, 1000, 1500, 200]*5,
#         'TLV': [15000, 1500, 350000, 17000]*5,
#         'Last Transaction Date': ['2022-05-01', '2023-03-15', '2023-04-20', '2023-05-25']*5,
#         'Email': ['John33@gmail.com', 'Allenkjb@gmail.com', 'Opal@gmail.com', 'CryptoJacob@hotmail.com']*5,
#         'Twitter': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
#         'Telegram': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
#         'Discord': ['John33#1234', 'Allenkjb#1234', 'Opal#1234', 'CryptoJacob#1234']*5,
#         'linkedin': ['John33', 'Allenkjb', 'Opal', 'CryptoJacob']*5,
#     },
#     'Liquidity Provider Leads': {
#         'Wallet/User': ['0x29ab82Ec552573b1B7d4933B2AaA3C568be9C6D1', '0xBE7CE5358977B00868C52045fb6c2790514efE68', '0xc9a648CF30D16079e48404F6Fd1Fd7Be83650C4d', '0xB5A16b3962BAcEB2CB292047333b58AaD1E060EE']*5,
#         'Wallet Value (USD)': [1000, 500, 2000, 1500]*5,
#         'Liquidity Provider Y/N': ['N', 'Y', 'N', 'Y']*5,
#         'Deposit Value': [500, 1000, 1500, 200]*5,
#         'TLV': [1500, 1500, 3500, 1700]*5,
#         'Last Transaction Date': ['2022-05-01', '2023-03-15', '2023-04-20', '2023-05-25']*5,
#         'Email': ['John33@gmail.com', 'Allenkjb@gmail.com', 'Opal@gmail.com', 'CryptoJacob@hotmail.com']*5,
#         'Twitter': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
#         'Telegram': ['@John33', '@Allenkjb', '@Opal', '@CryptoJacob']*5,
#         'Discord': ['John33#1234', 'Allenkjb#1234', 'Opal#1234', 'CryptoJacob#1234']*5,
#         'linkedin': ['John33', 'Allenkjb', 'Opal', 'CryptoJacob']*5,
#     }
# }

# def main():
#     st.title('Wallet Information')

#     # Create a dropdown selector in the sidebar
#     table_selection = st.sidebar.selectbox('Select Table', list(tables.keys()))

#     # Display the selected table in wide mode
#     df = pd.DataFrame(tables[table_selection])
#     st.dataframe(df, width=800)

# if __name__ == '__main__':
#     main()


import streamlit as st
import pandas as pd
import random

# Define the tables
tables = {
 'Gambling Leads': {
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
    'Liquidity Provider Leads': {
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
    'NFT Lending Users': {
        'Wallet/User': ['0x' + ''.join(random.choices('0123456789ABCDEF', k=40)) for _ in range(20)],
        'Wallet Value (USD)': random.choices(range(1000, 5000), k=20),
        'Gambling User Y/N': random.choices(['N', 'Y'], k=20),
        'Deposit Value': random.choices(range(100, 2000), k=20),
        'TLV': random.choices(range(1000, 5000), k=20),
        'Last Transaction Date': pd.date_range(start='2023-06-01', periods=20),
        'Email': ['emma12@gmail.com', 'david.smith23@gmail.com', 'cryptoconnect@gmail.com', 'johnny.brown@gmail.com']*5,
        'Twitter': ['@emma12', '@davidsmith23', '@cryptoconnect', '@johnnybrown']*5,
        'Telegram': ['@emma12', '@davidsmith23', '@cryptoconnect', '@johnnybrown']*5,
        'Discord': ['emma12#5678', 'davidsmith23#5678', 'cryptoconnect#5678', 'johnnybrown#5678']*5,
        'LinkedIn': ['Emma Johnson', 'David Smith', 'Crypto Connect', 'Johnny Brown']*5
    },
    'DEX Users': {
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
    'Perpetual Traders': {
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
    }
}

def main():
    # Set page configuration
    st.set_page_config(
        page_title='Leads Lists by Sector',
        page_icon='💰',
        layout='wide',
        initial_sidebar_state='expanded'
    )

    # Title
    st.markdown("<h1 style='text-align: center;'>Leads Lists by Sector</h1>", unsafe_allow_html=True)

    # Add logo
    logo_path = 'slice_logo_clear.png'  # Replace with the path to your logo image
    st.sidebar.image(logo_path, use_column_width=True)

    # Create a dropdown selector in the sidebar
    table_selection = st.sidebar.selectbox('Select Sector', list(tables.keys()))

    # Display the selected table in wide mode
    df = pd.DataFrame(tables[table_selection])
    st.dataframe(df, width=1800)

if __name__ == '__main__':
    main()
