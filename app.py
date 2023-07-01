import pandas as pd
import streamlit as st
import joblib
from streamlit_star_rating import st_star_rating
import base64
from random import randint
def process_main_page():
    show_main_page()
    sidebar_input_features()

def get_base64(bin_file):
    # функция для бэкграунда
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    # функция для бэкграунда
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
def show_main_page():
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Demo Titanic",
    )

    st.write(
        """
        # Оставьте ваш отзыв о нашей компании
        Помогите нам стать лучше!
        """
    )
    set_background('img/emoji_def.png')


def process_side_bar_inputs(user_input_df):
    my_model = joblib.load('model')
    prediction = my_model.predict(user_input_df)
    if prediction == 1:
        st.warning('Спасибо за ваш позитивный отзыв!', icon="💗")
        set_background('img/emoji_pos.png')
    else:
        st.warning('Мы сожалеем о вашем неприятном опыте.', icon="⚠️")
        set_background(f'img/emoji_neg{randint(1, 5)}.png')

def sidebar_input_features():
    st.sidebar.header('Параметры')
    gender = st.sidebar.selectbox("Пол", ("Мужской", "Женский"))
    age = st.sidebar.slider("Возраст", min_value=1, max_value=100, value=20, step=1)
    customer_type = st.sidebar.selectbox("Класс", ("Лояльный", "Нелояльный"))
    type_of_travel = st.sidebar.selectbox("Тип поездки", ("Бизнес поездка", "Персональная поездка"))
    passenger_class = st.sidebar.selectbox("Класс", ("Бизнес", "Эконом", "Эконом+"))
    flight_distance = st.sidebar.number_input('Flight distance', min_value=1)
    departure_delay_in_minutes = st.sidebar.number_input('Departure delay in minutes', min_value=0)
    arrival_delay_in_minutes = st.sidebar.number_input('Arrival delay in minutes', min_value=0)
    inflight_wifi_service = st_star_rating('Arrival delay in minutes', 5, 3)
    departure_or_arrival_time_convenient = st_star_rating('Departure/Arrival time convenient', 5, 3)
    ease_of_online_booking = st_star_rating('Ease of Online booking', 5, 3)
    gate_location = st_star_rating('Gate location', 5, 3)
    food_and_drink = st_star_rating('Food and drink', 5, 3)
    online_boarding = st_star_rating('Online boarding', 5, 3)
    seat_comfort = st_star_rating('Seat comfort', 5, 3)
    inflight_entertainment = st_star_rating('Inflight entertainment', 5, 3)
    on_board_service = st_star_rating('On-board service', 5, 3)
    leg_room_service = st_star_rating('Leg room service', 5, 3)
    baggage_handling = st_star_rating('Baggage handling', 5, 3)
    checkin_service = st_star_rating('Checkin service', 5, 3)
    inflight_service = st_star_rating('Inflight service', 5, 3)
    cleanliness = st_star_rating('Cleanliness', 5, 3)
    translatetion = {
        "Мужской": 1,
        "Женский": 0,
        "Бизнес поездка": 1,
        "Персональная поездка": 0,
        "Лояльный": 1,
        "Нелояльный": 0,
        "Бизнес":0,
        "Эконом":1,
        "Эконом+": 2,
    }
    data = {
         'Gender' : translatetion[gender],
         'Age' : age,
         'Customer Type' : translatetion[customer_type],
         'Type of Travel' : translatetion[type_of_travel],
         'Class' : translatetion[passenger_class],
         'Flight Distance' : flight_distance,
         'Departure Delay in Minutes' : departure_delay_in_minutes,
         'Arrival Delay in Minutes' : arrival_delay_in_minutes,
         'Inflight wifi service' : inflight_wifi_service,
         'Departure/Arrival time convenient' : departure_or_arrival_time_convenient,
         'Ease of Online booking' : ease_of_online_booking,
         'Gate location' : gate_location,
         'Food and drink' : food_and_drink,
         'Online boarding' : online_boarding,
         'Seat comfort' : seat_comfort,
         'Inflight entertainment' : inflight_entertainment,
         'On-board service' : on_board_service,
         'Leg room service' : leg_room_service,
         'Baggage handling' : baggage_handling,
         'Checkin service' : checkin_service,
         'Inflight service' : inflight_service,
         'Cleanliness' : cleanliness}
    if st.button('Отправить'):
        df = pd.DataFrame(data, index=[0])
        process_side_bar_inputs(df)

if __name__ == "__main__":
    process_main_page()