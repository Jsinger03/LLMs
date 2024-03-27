import restaurant_helper
import streamlit as st
import time
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine", ("Italian", "Indian", "Spanish", "Mexican", "American", "Greek", "Chinese", "Thai", "Japanese", "French"))
print(cuisine)

# Add a delay of 5 seconds
time.sleep(5)
print("Done sleeping===========================================")


response = restaurant_helper.gen_restname_menu(cuisine)
st.header(response['restaurant_name'])
menu_items = response["menu_items"].split("\n")
st.write("** Menu Items **")
for item in menu_items[2::]:
    st.write(" -- ", item)
    print(f"item: {item}")
    im = restaurant_helper.gen_item_image(item)
    print("IM made")
    st.image(im, caption=item)
    print("IM shown")
    del im
