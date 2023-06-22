
import streamlit as st
import pandas as pd
import random


# Define the tables
tables = {

    'NFT Lending Users': {
        'Wallet/User': ['0x' + ''.join(random.choices('0123456789ABCDEF', k=12))+ '.....' for _ in range(20)],
        'Wallet Value ($)': random.choices(range(1000, 50000000), k=20),
        'Borrower/Lender': random.choices(['Borrower', 'Lender', 'Both', 'NFT Holder'], k=20),
        'Volume ($)': random.choices(range(100, 2000000), k=20),
        'Protocols Used': random.choices(['NFTfi, Blend', 'NFTfi, BendDAO, Paraspace', 'Blend', 'Arcade, x2y2', 'NFTfi'], k=20),
        'NFTs Held': random.choices(['BAYC(1)','MAYC(1)','Doodles(1)','BAYC(6), Punk(2)', 'Punk(1), Azuki(1)', 'Azuki(2), Otherside(34)', 'MAYC(4)', 'Art Blocks(16)'], k=20),
        #'Last Transaction Date': pd.date_range(start='2023-06-01', periods=20),
        'Twitter': ['N/A', '**********', '**********', '**********'] * 5,
        'Email': ['**********', 'N/A', '**********', '**********'] * 5,
        'Telegram': ['**********', 'N/A', 'N/A', '**********'] * 5,
        'Discord': ['**********', '**********', '**********', 'N/A'] * 5,
        #'LinkedIn': ['N/A', 'David Smith', 'N/A', 'Johnny Brown']*5
    },

}

Metrics = {


    'NFT Lending Users': {     
        # 'Total NFT Holders': 'TBD',    
        # 'Total NFT Borrowers': 'TBD',
        'Total Users': '222,825',
        'Total Fees Generated': '$1.8m',
        'Starting Pricing': '55 for $100',     
        'Average Value/Lead': 'TBD',     
        'Estimated Profit Margin': '90%'   
    }

                                                                                                                                                                                                                                                                                         
}


def main():
    # Set page configuration
    st.set_page_config(
        page_title='Leads by Slice Analytics',
        page_icon='📊',
        layout='wide',
        initial_sidebar_state='expanded'
    )

    # # Title
    # st.markdown("<h1 style='text-align: center;'>Example Leads</h1>", unsafe_allow_html=True)

    # Title
    # title_style = "text-align: center; font-family: 'Roboto'; font-weight: bold; color: #000000;"
    # st.markdown(f"<h1 style='{title_style}'>Start More Conversations, Close More Deals</h1>", unsafe_allow_html=True)

    title_style = "text-align: center; font-family: 'Roboto'; font-weight: bold; color: #000000;"
    st.markdown(f"<h1 style='{title_style}'>On-chain Leads</h1>", unsafe_allow_html=True)
    
    st.markdown("---")  # Insert a horizontal rule

    # Add logo
    logo_path = 'slice_logo_clear.png'  # Replace with the path to your logo image
    st.sidebar.image(logo_path, use_column_width=True)

    st.sidebar.markdown("---")  # Insert a horizontal rule
    
    # Create a dropdown selector in the sidebar
    table_selection = st.sidebar.selectbox('Select Database', list(tables.keys()))

    cols_titles = ['Total Users', 'Total Fees Generated', 'Starting Pricing', 'Average Value/Lead', 'Estimated Profit Margin']
    cols_data = [Metrics.get(table_selection,{}).get('Total Users','NA'), Metrics.get(table_selection,{}).get('Total Fees Generated','NA'), Metrics.get(table_selection,{}).get('Starting Pricing','NA'), Metrics.get(table_selection,{}).get('Average Value/Lead','NA'), Metrics.get(table_selection,{}).get('Estimated Profit Margin','NA')]
    #cols_titles = ['Total Wallets Tracked', 'Leads Available', 'Fees Generated', 'Trades Completed']
    #cols_data = [Metrics.get(table_selection,{}).get('Total Wallets Tracked','NA'), Metrics.get(table_selection,{}).get('Leads Available','NA'), Metrics.get(table_selection,{}).get('Fees Generated','NA'), Metrics.get(table_selection,{}).get('Trades Completed','NA')]
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

    
     #request_button = st.sidebar.button('Request Custom Leads List')
    if st.sidebar.button('Need a Custom Dataset? Contact Us'):
        st.sidebar.markdown("[Click here to visit the website](https://www.sliceanalytics.xyz)")
    


if __name__ == '__main__':
    main()
