import json
import requests
from requests.auth import HTTPBasicAuth
import streamlit as st
import re
from PIL import Image


def main():

    image = Image.open('wokway.jpg')
    if image.mode != 'RGB':
        image = image.convert('RGB')
    st.image(image, caption='WokWay Fried Rice')

    st.title('WokWay Online Site')

    getMenu = requests.get('https://wokway-api.herokuapp.com/menu',
                           auth=HTTPBasicAuth('cust', '9EE6149A78857991D5F2EE2A1AB28'))

    json_output = getMenu.json()
    # st.json(json_output)
    json_list = json.loads(json_output)
    # print(json_list)

    itemList = []
    priceList = []
    for item in json_list:
        itemList.append(item['itemName'])
        priceList.append(item['itemPrice'])

    st.subheader("WokWay Menu Items")
    print(itemList)
    print(priceList)

    # st.write(itemList)
    # st.write(priceList)

    for i, p in zip(itemList, priceList):
        print("{} : ${}".format(i, p))
        st.write("{} : ${}".format(i, p))

    st.subheader("Order Cart")
    st.write("Please select items for your order:")
    choiceList = []
    orderList = []
    for index, choice in enumerate(itemList, start=0):
        option = st.checkbox(choice)
        if option:
            print(choice, index)
            choiceList.append(index)
            orderList.append(itemList[index])
    # choice = st.radio(
    #     "Here are the list of our menu items",
    #      itemList)

    total = 0
    for selected in choiceList:
        total = total + priceList[selected]

    st.write("Total Cost: $", total)

    # st.multiselect('Multiselect', itemList)
    st.write("Order List ", orderList)

    custName = st.text_input('Customer First Name (with no spacing) :')
    if not custName or custName.isalpha() == False:
        # if not custName or re.match(r"[\s\w]+$", custName) == False:
        st.warning('Please input a valid name.')
        st.stop()
    st.success('Thank you for inputting a name.')

    custPhone = st.number_input('Contact Number', value=80000000)
    if not custPhone or custPhone < 80000000 or custPhone > 99999999:
        st.warning('Please input a valid Phone Number.')
        st.stop()
    st.success('Thank you for inputting a valid Phone Number.')

    submit_button = st.button('Submit')

    if submit_button and total == 0:
        st.error(f'{custName}, Please select items to add to your order.')

    if submit_button and total != 0:
        requests.post('https://wokway-api.herokuapp.com/addOrder', auth=HTTPBasicAuth('cust', '9EE6149A78857991D5F2EE2A1AB28'), json={
                      'custName': custName, 'orderItems': orderList, 'custPhone': str(custPhone), 'price': total})
        st.success(
            f'{custName}, thank you for your order. Please pick up your order from our store in 10 minutes.')


if __name__ == "__main__":
    main()
