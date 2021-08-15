import json
import requests
from requests.auth import HTTPBasicAuth
import streamlit as st


def main():

    st.title('WokWay Admin Site')

    getOrder = requests.get('https://wokway-api.herokuapp.com/order',
                           auth=HTTPBasicAuth('admin', 'C6BF377E68B7B598B75EB94CB4C2B'))

    st.subheader("List of Orders")

    json_output = getOrder.json()
    st.json(json_output)
    json_list = json.loads(json_output)

   
    st.subheader("List of Menu Items")

    getMenu = requests.get('https://wokway-api.herokuapp.com/menu',
                           auth=HTTPBasicAuth('admin', 'C6BF377E68B7B598B75EB94CB4C2B'))
    
    json_output = getMenu.json()
    st.json(json_output)
    json_list = json.loads(json_output)



if __name__ == "__main__":
    main()