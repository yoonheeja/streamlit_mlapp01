import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# 데이터 불러오기
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# 텍스트 요소 생성. 사용자에게 데이터가 로드 되고 있음을 알린다.
data_load_state = st.text('Loading data...')

# 10000개의 행의 데이터를 로드한다.
data = load_data(10000)

# 데이터가 성공적으로 로드 되었음을 알린다.
data_load_state.text('Loading data...done!')

# 부제목 만들기
st.subheader('Raw data')
st.write(data)

# seaborn을 사용하여 히스토그램 그리기
st.subheader('Number of pickups by hour')

# Seaborn을 사용하여 히스토그램 그리기
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x=data[DATE_COLUMN].dt.hour, bins=24, kde=False)
plt.xlabel('Hour')
plt.ylabel('Number of Pickups')
plt.title('Number of Pickups by Hour')
fig, ax = plt.subplots()
ax.hist(data[DATE_COLUMN].dt.hour, bins=24)
st.pyplot(fig)