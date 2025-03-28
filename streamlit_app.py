import streamlit as st

st.title("User Feedbacks' Form :book:" )
st.write(
    "Please, answer and submit this form to give us "
    "information about your experience with Streamlit web-app forms!"
)


# Form-dedicated window
with st.form('User Information & Feedbacks', clear_on_submit=False):
    # User Info
    user_name = st.text_input('_Your name:_ ', placeholder="Write here your name...")
    user_surname = st.text_input('_Your surname:_ ', placeholder="Write here your surname...")
    user_sex = st.selectbox('_Your gender:_',["Select an option", "Male", "Female", "Other"])
    user_age = st.number_input('_Your age:_ ', 
                               min_value = 10,
                               max_value = 90,
                               value = 24,
                               step = 1)
    
    # Slider for rating the web-app and additional info
    rank = st.slider('_Rank your satisfaction for the site:_', 1, 5, 3)
    #st.write(f'You are selecting :red[**{rank}**] as rank') # Non si aggiorna in real-time tanto
    range_of_hours = st.slider('_Select hour-range in which you usually use this app:_', 0, 24, (7,9))
    #st.write(f'You are selecting that you usually use the site from :red[**{range_of_hours[0]}**] to :red[**{range_of_hours[1]}**]') # Non si aggiorna in real-time tanto

    # Comment section
    comments = st.text_input('_Write here all possibile additional comments:_ ', placeholder="Write here your comment...")

    # Submit Button
    submitted = st.form_submit_button('**Submit it!**', type="primary")

if submitted:
    if user_name and user_surname and user_sex != "Select an option":
        st.success(f'Form submitted! :white_check_mark: \n\n')
        st.write(f'**Name:** {user_name}\n\n **Surname:** {user_name}\n\n **Age:** {user_age} years\n\n **Gender:** {user_sex}\n\n')
        st.write(f'**Use Hours:** {range_of_hours[1]-range_of_hours[0]}\n\n **Rank:** {rank}\n\n')
        
        if rank <= 2:
            st.warning(":orange[**Low Rank!**] :warning:\n")
        if rank >= 4:
            st.success(":green[**High Rank!**] :100:\n")
        
        st.write(f'**Comments:** {comments}\n')
    else:
        st.warning(f'Please fill out all the fields correctly! :warning:')