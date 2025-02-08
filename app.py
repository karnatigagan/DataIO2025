import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from streamlit.components.v1 import html

final = pd.read_csv('Dataset/AQI and Lat Long of Countries.csv')
final.dropna(inplace=True)

def range_particulate_matter():
    st.subheader('Range of the particulate matter')

    data = {
    'Pollutant': ['PM2.5', 'PM10', 'Ozone', 'CO', 'NO2'],
    # 'Description': [
    #     'Particulate Matter with a diameter of 2.5 micrometers or less',
    #     'Particulate Matter with a diameter of 10 micrometers or less',
    #     'Ozone gas concentration in the air',
    #     'Carbon monoxide gas concentration in the air',
    #     'Nitrogen dioxide gas concentration in the air'
    # ],
    'Good': ['0-12 μg/m³', '0-54 μg/m³', '0-54 ppb', '0-4.4 ppm', '0-53 ppb'],
    'Moderate': ['12.1-35.4 μg/m³', '55-154 μg/m³', '55-70 ppb', '4.5-9.4 ppm', '54-100 ppb'],
    'Unhealthy for Sensitive Groups': ['35.5-55.4 μg/m³', '155-254 μg/m³', '71-85 ppb', '9.5-12.4 ppm', '101-360 ppb'],
    'Unhealthy': ['55.5-150.4 μg/m³', '255-354 μg/m³', '86-105 ppb', '12.5-15.4 ppm', '361-649 ppb'],
    'Very Unhealthy': ['150.5-250.4 μg/m³', '355-424 μg/m³', '106-200 ppb', '15.5-30.4 ppm', '650-1249 ppb'],
    'Hazardous': ['250.5+ μg/m³', '425+ μg/m³', '201+ ppb', '30.5+ ppm', '-']
    }

    df = pd.DataFrame(data)

    st.write(df)


def plot_by_country(dataframe, country, param1, param2):
    temp_df = dataframe[dataframe['Country'] == country]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20,   mapbox_style='carto-positron', color_continuous_scale= px.colors.sequential.Agsunset_r,
    hover_name=temp_df['City'], height=800, width=900, zoom=4, title='{} vs {} for {}'.format(param1, param2, country))

    st.plotly_chart(fig, use_container_width=True)

    range_particulate_matter()
    st.markdown('---')

    st.subheader('Line chart of {} vs {} for top cities in {}'.format(param1, param2, country))

    col1, col2 =st.columns(2)
    top1 = dataframe[dataframe['Country'] == country][['City',param1]].sort_values(by = param1, ascending=False).head(25)
    top2 = dataframe[dataframe['Country'] == country][['City',param2]].sort_values(by = param2, ascending=False).head(25)

    with col1:
        st.write('Top cities in {} for {}'.format(country, param1))
        st.dataframe(top1)
        # fig1 = px.bar(top1, 'City', param1)
        # st.plotly_chart(fig1)
        
    with col2:
        st.write('Top cities in {} for {}'.format(country, param2))
        st.dataframe(top2)
        
    
    fig1 = px.bar(top1, 'City', param1, title='{} in top cities in {}'.format(param1, country), color=param1, color_continuous_scale=px.colors.sequential.Oryel)
    st.plotly_chart(fig1)
    fig2 = px.bar(top2, 'City', param2, title='{} in top cities in {}'.format(param2, country), color=param2, color_continuous_scale=px.colors.sequential.Pinkyl)
    st.plotly_chart(fig2)



def plot_by_country2(dataframe, country, param1, param2):
    temp_df = dataframe[dataframe['Country'] == country]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20,   mapbox_style='stamen-toner', color_continuous_scale= px.colors.sequential.Agsunset_r,
    hover_name=temp_df['City'], height=800, width=900, zoom=4, title='{} vs {} for {}'.format(param1, param2, country))

    st.plotly_chart(fig, use_container_width=True)

    range_particulate_matter()
    st.markdown('---')


    st.subheader('Line chart of {} vs {} for top cities in {}'.format(param1, param2, country))

    col1, col2 =st.columns(2)
    top1 = dataframe[dataframe['Country'] == country][['City',param1]].sort_values(by = param1, ascending=False).head(25)
    top2 = dataframe[dataframe['Country'] == country][['City',param2]].sort_values(by = param2, ascending=False).head(25)

    with col1:
        st.write('Top cities in {} for {}'.format(country, param1))
        st.dataframe(top1)
        # fig1 = px.bar(top1, 'City', param1)
        # st.plotly_chart(fig1)
        
    with col2:
        st.write('Top cities in {} for {}'.format(country, param2))
        st.dataframe(top2)
        
    
    fig1 = px.bar(top1, 'City', param1, title='{} in top cities in {}'.format(param1, country),color=param1, color_continuous_scale=px.colors.sequential.Oryel)
    st.plotly_chart(fig1)
    fig2 = px.bar(top2, 'City', param2, title='{} in top cities in {}'.format(param2, country), color=param2, color_continuous_scale=px.colors.sequential.Pinkyl)
    st.plotly_chart(fig2)




def plot_by_country_city(dataframe, country,city, param1, param2):
    temp_df = dataframe[(dataframe['Country'] == country) & (dataframe['City'] == city)]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20, mapbox_style='carto-positron',
    hover_name=temp_df['City'], height=500, width=700, zoom=4)


    col1, col2, col3, col4 = st.columns(4)
    st.plotly_chart(fig, use_container_width=True)
    with col1:
        st.metric('Value of {} in {}'.format(param1, city), value=temp_df[param1])
    with col2:
        st.metric('Value of {} in {}'.format(param2, city), value=temp_df[param2])
    with col3:
        st.metric('Latitude of {}'.format(city), value=temp_df['lat'])
    with col4:
        st.metric('Longitude of {}'.format(city), value=temp_df['lng'])

    range_particulate_matter()
    st.markdown('---')


def plot_by_country_city2(dataframe, country,city, param1, param2):
    temp_df = dataframe[(dataframe['Country'] == country) & (dataframe['City'] == city)]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20, mapbox_style='stamen-toner',
    hover_name=temp_df['City'], height=500, width=700, zoom=4)
    
    col1, col2, col3, col4 = st.columns(4)
    st.plotly_chart(fig, use_container_width=True)
    with col1:
        st.metric('Value of {} in {}'.format(param1, city), value=temp_df[param1])
    with col2:
        st.metric('Value of {} in {}'.format(param2, city), value=temp_df[param2])
    with col3:
        st.metric('Latitude of {}'.format(city), value=temp_df['lat'])
    with col4:
        st.metric('Longitude of {}'.format(city), value=temp_df['lng'])

    range_particulate_matter()
    st.markdown('---')



st.set_page_config(page_title='AQI Globe', layout='wide')
st.sidebar.header('AQI Globe')
st.header('AQI Globe')
st.markdown("*Explore air quality index values across different cities worldwide*")

st.markdown("---")





# st.sidebar.markdown(
#     """
#     <a href="https://twitter.com/YOUR_TWITTER_USERNAME" target="_blank">
#         <img src="https://img.icons8.com/color/48/000000/twitter--v1.png"/>
#     </a>
#     """
#     , unsafe_allow_html=True)



option = st.sidebar.radio('Choose', ['AQI Explorer', 'Learn about AQI Globe'])
if option == 'AQI Explorer':
    st.markdown('###### NOTE: *Primary Parameter --- the size of the marker*  AND  *Secondary Parameter --- the color of the marker*')
    country = st.sidebar.selectbox('Select Country', list(sorted(final['Country'].unique())))

    temp_df = final[final['Country'] == country]
    l = list(sorted(temp_df['City'].unique()))
    l.insert(0,'-')
    city = st.sidebar.selectbox('Select a city in {}'.format(country), l)

    primary = st.sidebar.selectbox('Choose primary parameter', final.columns[2:12:2])
    secondary = st.sidebar.selectbox('Choose secondary parameter' ,[cols for cols in final.columns[2:12:2]if cols != primary])
    st.sidebar.markdown('##### *Graph is auto-plotted after parameter selection* ')
    # st.sidebar.markdown('##### *Click View Help for instructions* ')


    btn = st.sidebar.button('View Help',on_click=None)
    if btn == True:
        st.subheader('How to use?')
        st.write('* Select the country from the dropdown.')
        st.write('* For the country overall, select "-" in the city dropdown.')
        st.write('* You can also choose a specific city from the selected country in the city dropdown.')
        st.write('* Select the primary and secondary parameters from their respective dropdowns.')
        st.write('* The primary parameter represents the size of the bubble, and the secondary parameter represents the color of the bubble.')
        st.write('* Scroll below the graph to see more stats of the selected country')

        btn = st.sidebar.button('Hide Help',on_click=None)
        st.markdown("---")

    st.radio('Choose style of graph',['Carto Positron', 'Stamen Toner'], key='graph')
    if st.session_state['graph'] == 'Carto Positron':
        if city == '-':
            plot_by_country(final, country, primary, secondary)
        else:
            plot_by_country_city(final, country,city,primary, secondary)
    else:
        if city == '-':
            plot_by_country2(final, country, primary, secondary)
        else:
            plot_by_country_city2(final, country,city,primary, secondary)


if option == 'Learn about AQI Globe':
    st.subheader('About')
    st.write('AQI Globe is an interactive web application that allows users to explore the air quality index (AQI) values of different cities worldwide. The AQI is a measure of how polluted the air is, and it takes into account several pollutants, such as carbon monoxide, ozone, and particulate matter. The higher the AQI value, the more polluted the air is and the more harmful it can be to human health.')
    st.write('The app uses data from two datasets obtained from Kaggle, which were merged to provide a comprehensive view of AQI values across various countries and cities. The data is presented using Plotly, a Python library for creating interactive data visualizations.')
    st.write('Users can select a country from a dropdown menu and choose between two options: viewing the overall AQI value for the country or selecting a specific city within the country. They can then select primary and secondary parameters from the dropdown menus to customize the graph. The primary parameter is represented by the size of the bubble, while the secondary parameter is represented by the color of the bubble.')
    st.write('The application provides a simple and intuitive way for users to explore AQI values and gain insights into air pollution levels worldwide.')
    st.markdown('---')

    st.subheader('Explanation of common AQI terms')
    st.write('* PM2.5: PM2.5 refers to tiny particles or droplets in the air that are 2.5 micrometers or less in width. They can be harmful to human health when inhaled, especially in high concentrations.')
    st.write('* PM10: PM10 refers to particles or droplets in the air that are 10 micrometers or less in width. They can also be harmful to human health when inhaled, but generally to a lesser extent than PM2.5.')
    st.write('* Ozone: Ozone is a gas that can form in the atmosphere through a chemical reaction between sunlight and other pollutants. High levels of ozone can be harmful to human health, particularly for those with respiratory issues.')
    st.write('* Carbon Monoxide (CO): CO is a colorless, odorless gas that is produced by the incomplete burning of fossil fuels. High levels of CO can be toxic to humans and can cause headaches, dizziness, and nausea')
    st.markdown('---')

    st.subheader('Connect with me!')

    st.markdown('[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/yourusername/)](https://www.linkedin.com/in/aditya-ramachandran-27b2ab24a/) ''   [![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github&link=https://github.com/Aditya-Ramachandran)](https://github.com/Aditya-Ramachandran)')

    st.write('\n')
    st.write('\n')
    st.write('\n')

# with st.form("my_form", clear_on_submit=True):
#     st.write("Enter your contact details below:")
#     name = st.text_input("Enter your name:")
#     email = st.text_input("Enter your email:")
#     message = st.text_area("Enter your message:")

#     submitted = st.form_submit_button("Submit")

#     if submitted:
#         if len(name)== 0 and len(email) == 0 and len(message)== 0:
#             st.warning('Please don\'t leave any field blank')

#     if len(name)>0 and len(email)>0 and len(message)>0:
#     # If the form is submitted, print the details to the console
#         if submitted:
#             st.write("Name:", name)
#             st.write("Email:", email)
#             st.write("Message:", message)


# st.markdown("""
# <form>
#     <label for="name">Name:</label><br>
#     <input type="text" id="name" name="name"><br>
#     <label for="email">Email:</label><br>
#     <input type="email" id="email" name="email"><br>
#     <label for="message">Message:</label><br>
#     <textarea id="message" name="message"></textarea><br>
#     <input type="submit" value="Submit">
# </form>
# """, unsafe_allow_html=True)
            



# st.markdown(
#     """
#     <div style="display:flex; justify-content:center; align-items:center;">
#         <p justify-content:center>Reach Out To Me On </p>
#             <a href="https://twitter.com/YOUR_TWITTER_USERNAME" target="_blank">
#                 <img src="https://img.icons8.com/color/48/000000/github.png"/>
#             </a>
#             <a href="https://www.linkedin.com/in/YOUR_LINKEDIN_PROFILE" target="_blank">
#                 <img src="https://img.icons8.com/color/48/000000/linkedin.png"/>
#             </a>
#         </div>
#         """
#         , unsafe_allow_html=True)
