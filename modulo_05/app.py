import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.title('House Rocket Company')
st.markdown('House Rocket Company' )
st.markdown( 'Welcome to House Rocket Data Analysis' )

st.header('Load data')

# read data
@st.cache( allow_output_mutation=True )
def get_data( path ):
    data = pd.read_csv( path )
    data['date'] = pd.to_datetime( data['date'] )

    return data

# load data
data = get_data('/home/daniel/repos/curso_python_zero_ao_ds/datasets/kc_house_data.csv')

# define level of prices
for i in range( len( data ) ):
    if data.loc[i, 'price'] <= 321950:
        data.loc[i, 'level'] = 0

    elif ( data.loc[i,'price'] > 321950 ) & ( data.loc[i,'price'] <= 450000 ):
        data.loc[i, 'level'] = 1

    elif ( data.loc[i,'price'] > 450000 ) & ( data.loc[i,'price'] <= 645000 ):
        data.loc[i, 'level'] = 2

    else:
        data.loc[i, 'level'] = 3

# st.write( 'You choose', bedrooms[0] )
#
# df = data[data['bedrooms'].isin(bedrooms)]
# st.dataframe( df.head() )


# plot map
st.title( 'House Rocket Map' )
is_check = st.checkbox( 'Display Map')

#Filters

# filter bedrooms
bedrooms = data['bedrooms'].sort_values().unique()
bedrooms_multi = st.sidebar.multiselect('Number of Bedrooms', bedrooms)

#filters livingi room
size_living_min = int(data['sqft_living'].min())
size_living_max = int(data['sqft_living'].max())
size_living_avg = int(data['sqft_living'].median())
sqft_living_slider = st.slider('Size of living room', size_living_min, size_living_max, size_living_avg)

# filters price
price_min = int( data['price'].min() )
price_max = int( data['price'].max() )
price_avg = int( data['price'].median() )
price_slider = st.slider('Price Range', price_min, price_max, price_avg)

# filter condition
condition = data['condition'].sort_values().unique()
condition_radio = st.radio('Choose house condition', condition)

#filter year built
yr_built = data['yr_built'].sort_values().unique()
yr_built_select = st.selectbox('Choose year built', yr_built)


if is_check:
    #select rows
    houses = data[(data['sqft_living'] < sqft_living_slider) &
                  (data['price'] < price_slider) &
                  (data['condition'] == condition_radio) &
                  (data['bedrooms'].isin(bedrooms_multi) &
                  (data['yr_built'] < yr_built_select))][['id', 'lat', 'long', 'price', 'level']]

# draw map
    fig = px.scatter_mapbox(
        houses,
        lat="lat",
        lon="long",
        color="level",
        size="price",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=10 )

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart( fig )


