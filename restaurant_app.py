import restaurant_helper
import streamlit as st
#to use:
#streamlit run restaurant_app.py
#refresh page after each save to see updates


st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine", ("Italian", "Indian", "Spanish", "Mexican", "American", "Greek", "Chinese", "Thai", "Japanese", "French"))
print(cuisine)

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