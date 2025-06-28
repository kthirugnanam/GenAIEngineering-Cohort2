import streamlit as st
import requests
import json
import datetime

st.set_page_config(layout="centered")  # or "centered" for better mobile view
st.title("Weekly Dairy Order Form")
col1, col2 = st.columns(2)
with col1: 
    # Function to get the current or next Thursday
    def get_current_thursday():
        """Returns the current or next Thursday's date."""
        # Get today's date and calculate the next Thursday
        today = datetime.date.today()
        offset = (3 - today.weekday()) % 7  # 3 = Thursday
        return today + datetime.timedelta(days=offset)

    # Get default date (current or next Thursday)
    default_thursday = get_current_thursday()

    # Show calendar input with default set to Thursday
    selected_date = st.date_input("Pick a Thursday:", value=default_thursday)

    # Check if the selected date is a Thursday
    if selected_date.weekday() != 3:
        st.error("Please select a Thursday.")

with col2:
    options = ['Select your Registered Phone Number:', 'Preethi', 'Kriti', 'Shyam', 'Pavani', 'Varshini', 'Megna', 'Sreeja']
    # Create a combobox (selectbox) for single selection
    selected = st.selectbox("Registered Phone Number:", options, key="phone_number")
    # if selected == 'Select your Registered Phone Number:':
    #     st.warning("Please select a valid option.")
# Add a header for the app
st.header("Weekly Dairy Order Form")        
# Add a subheader for the order form
st.markdown("---")  # horizontal line   
st.subheader("Please input your weekly dairy order below:")

# Define the API base URL
api_url = "http://0.0.0.0:9321"
#api_url = "https://genaiengineering-cohort2-1-67ib.onrender.com"

with st.expander("Order Details", expanded=True):
    st.markdown("""
        <style>
        .expander-header {
            font-size: 20px;
            font-weight: bold;
            color: blue;
        }
        </style>
    """, unsafe_allow_html=True)
    #number input for milk
    milk = st.number_input("Milk (gallons)", min_value=0, step=1, format="%d", key="milk QTY")
    #number input for eggs
    eggs = st.number_input("Eggs (dozen)", min_value=0, step=1, format="%d", key="eggs QTY")
    #number input for butter
    butter = st.number_input("Butter (Qt)", min_value=0, step=1, format="%d", key="butter QTY")
    #number input for panneer
    paneer = st.number_input("Paneer (12 oz)", min_value=0, step=1, format="%d", key="paneer QTY")

#print line
st.markdown("---")  # horizontal line

#estimated total sub header
st.subheader("Estimated Total Cost:")
# estimated total cost
total_cost = (milk * 5.5) + (eggs * 5.0) + (butter * 10) + (paneer * 3.5)
st.write(f"Estimated Total Cost: ${total_cost:.2f}")  
# Form for submitting the order
st.markdown("---")  # horizontal line
st.subheader("Submit Your Order")   
with st.form(key="my_form"):
    st.markdown("""
        <style>
        .custom-button {
            background-color: white;
            color: blue;
            font-size: 18px;
            border: 2px solid #ccc;
            padding: 10px;
            width: 100%;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Button rendered by Streamlit
    submitted = st.form_submit_button("🚀 Place Order")

    if submitted:
        if selected == 'Select your Registered Phone Number:':
            st.warning("Please select a valid Registered Phone Number.")
        elif selected_date.weekday() != 3:
            st.error("Please select a Thursday.")
        else:
            # continue with successful submission
            st.success("Order placed successfully!")
            with st.expander("Order Summary", expanded=False):
                st.markdown("""
                    <style>
                    .expander-header {
                        font-size: 20px;
                        font-weight: bold;
                        color: blue;
                    }
                    </style>
                """, unsafe_allow_html=True)
                # Display the order summary
                st.write("Your Order Summary...")
                st.write(f"Milk: {milk} gallons")
                st.write(f"Eggs: {eggs} dozen")
                st.write(f"Butter: {butter} Qt")
                st.write(f"Paneer: {paneer} 12 oz")
                st.write(f"**Estimated Total Cost: ${total_cost:.2f}**")

                # # Here you can add logic to send the order data to your API
                # order_data = {
                #     "milk": milk,
                #     "eggs": eggs,
                #     "butter": butter,
                #     "paneer": paneer,
                #     "phone_number": selected,
                #     "order_date": str(datetime.date.today()),
                #     "delivery_date": str(selected_date)
                # }
                # try:
                #     response = requests.post(f"{api_url}/order", json=order_data)
                #     if response.status_code == 200:
                #         st.success("Order placed successfully!")
                #         st.write(response.json())
                #     else:
                #         st.error(f"Error placing order: {response.status_code} - {response.text}")
                # except Exception as e:
                #     st.error(f"An error occurred: {e}")
        # simulate logic
        # order_data = {
        #     "milk": milk,
        #     "eggs": eggs,
        #     "butter": butter,
        #     "paneer": paneer
        # }
        # try:
        #     response = requests.post(f"{api_url}/order", json=order_data)
        #     if response.status_code == 200:
        #         st.success("Order placed successfully!")
        #         st.write(response.json())
        #     else:
        #         st.error(f"Error placing order: {response.status_code} - {response.text}")
        # except Exception as e:
        #     st.error(f"An error occurred: {e}")
# Uncomment the following lines to use a custom HTML button
# st.markdown("""
#     <style>
#     .custom-button {
#         display: inline-block;
#         padding: 1em 2em;
#         font-size: 1.1em;
#         color: blue;
# with st.form(key="my_form"):
#     st.markdown("""
#         <style>
#         .custom-button {
#             background-color: white;
#             color: blue;
#             font-size: 18px;
#             border: 2px solid #ccc;
#             padding: 10px;
#             width: 100%;
#             border-radius: 8px;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     submitted = st.form_submit_button("🚀 Click Me – Blue Text")

#     if submitted:
#         st.success("Styled button clicked!")
# import streamlit as st

# with st.form(key="my_form"):
#     # Button rendered by Streamlit
#     submitted = st.form_submit_button("submit")
    
#     def place_order():
#         order_data = {
#             "milk": milk,
#             "eggs": eggs,
#             "butter": butter,
#             "paneer": paneer
#         }
#         try:
#             response = requests.post(f"{api_url}/order", json=order_data)
#             if response.status_code == 200:
#                 st.success("Order placed successfully!")
#                 st.write(response.json())
#             else:
#                 st.error(f"Error placing order: {response.status_code} - {response.text}")
#         except Exception as e:
#             st.error(f"An error occurred: {e}") 

#     if submitted:
#         # 🟦 THIS IS YOUR CLICK ACTION
#         st.success("Order Placed!")
#         st.balloons()

        
# st.markdown("""
#     <style>
#     .blue-button {
#         display: inline-block;
#         padding: 1em 2em;
#         font-size: 1.1em;
#         color: blue;
#         background-color: white;
#         border: 2px solid #ccc;
#         border-radius: 8px;
#         width: 100%;
#         text-align: center;
#         cursor: pointer;
#     }
#     .blue-button:hover {
#         background-color: #f0f0f0;
#     }
#     </style>

#     <form action="#">
#         <button class="blue-button" type="submit">Place Order</button>
#     </form>
# """, unsafe_allow_html=True)

# submitted =("🚀 Place Order", key="submit_order")

# if submitted:
#         st.success("Styled button clicked!")


# Buttons
#if 
#st.button("Place Order")
    # order_data = {
    #     "milk": milk,
    #     "eggs": eggs,
    #     "butter": butter,
    #     "paneer": paneer
    # }
    # try:
    #     response = requests.post(f"{api_url}/order", json=order_data)
    #     if response.status_code == 200:
    #         st.success("Order placed successfully!")
    #         st.write(response.json())
    #     else:
    #         st.error(f"Error placing order: {response.status_code} - {response.text}")
    # except Exception as e:
    #     st.error(f"An error occurred: {e}")        
