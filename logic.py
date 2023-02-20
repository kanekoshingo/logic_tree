import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt
import time

st.title('どこの国がサッカーワールドカップで優勝すると思いますか？')

val = st.selectbox('選択してください',['','日本','ブラジル','アメリカ'])
st.write(f'選択した値: {val}')

if val == '日本':
   st.title(f"{val}を選択した場合、{val}が優勝するために何が必要ですか")
   val2 = st.selectbox('選択してください',['','監督の交代','選手の育成','個々の能力を上げる'])
   st.write(f'選択した値: { val2}')
elif val == 'ブラジル':
   st.title(f"{val}を選択した場合、{val}が優勝するために何が必要ですか")
   val2 = st.selectbox('選択してください',['','監督の交代','選手の育成','個々の能力を上げる'])
   st.write(f'選択した値: {val2}')
else:
   st.title(f"{val}を選択した場合、{val}が優勝するために何が必要ですか")
   val2 = st.selectbox('選択してください',['','監督の交代','選手の育成','個々の能力を上げる'])
   st.write(f'選択した値: {val2}')

if val2 == '監督の交代':
   st.title(f"{val2}を選択した場合、どなたがいいですか")
   val3 = st.selectbox('選択してください',['','秋元監督','小野寺監督','オレだ、オレだ、オレだ'])
   st.write(f'選択した値: {val3}')
   if val3 == '秋元監督':
      st.title(f"{val3}を選択した場合、{val3}の強みは何ですか")
      val6 = st.selectbox('選択してください',['','発想力','効率性','ユーモア'])
      st.write(f'選択した値: {val6}')
      time.sleep(3)
      st.success('確かに！！！！') 
   elif val3 == 'オレだ、オレだ、オレだ':
      st.title(f"{val3}を選択した場合ですが、、{val3}の強みは何ですか")
      time.sleep(3)
      st.success('大山さんが教えてくれますよ')
   else:
       st.title(f"{val3}を選択した場合、{val3}の強みは何ですか")
       val4 = st.selectbox('選択してください',['','ビジュアル','傾聴力','思慮深さ'])
       st.write(f'選択した値: {val4}')
       time.sleep(3)
       st.success('ごもっともです！！！！')

   
elif val2 == '選手の育成':
   st.title('選手の育成を選択した場合、何が必要ですか？')
   val4 = st.selectbox('選択してください',['','unboss','curios','inspire'])
   st.write(f'選択した値: {val4}')
   if val4 == 'unboss':
      st.title(f"あなたが考える{val4}とは何ですか？")
      val6 = st.selectbox('選択してください',['','自ら考える','プラスになることはやる','主体性'])
      st.write(f'選択した値: {val6}')
   elif val4 == 'curios':
      st.title(f"あなたが考える{val4}とは何ですか？")
      val6 = st.selectbox('選択してください',['','遊び心','何だろうと思うこと','それ、ちょっと面白そう！'])
      st.write(f'選択した値: {val6}')
   else:
      st.title(f"あなたが考える{val4}とは何ですか？")
      val6 = st.selectbox('選択してください',['','強みの掛け合わせ','自ら学ぶ','圧倒的努力'])
      st.write(f'選択した値: {val6}')
   
else:
   st.title('個々の能力を上げるを選択した場合、個々の能力を上げるためにどうすればいいですか？')
   val5 = st.selectbox('選択してください',['','食事','トレーニング','コーチング'])
   st.write(f'選択した値: {val5}')  
   if val5 == '食事':
      st.title(f"{val5}を選択した場合、何が必要ですか？")
      val7 = st.selectbox('選択してください',['','タンパク質','プロティン','アミノ酸'])
      st.write(f'選択した値: {val7}')
   elif val5 == 'トレーニング':
      st.title(f"{val5}を選択した場合、何が必要ですか？")
      val9 = st.selectbox('選択してください',['','気合い','根性','圧倒的努力'])
      st.write(f'選択した値: {val9}')
   else:
      st.title(f"{val5}を選択した場合、何が必要ですか？")
      val10 = st.selectbox('選択してください',['','発想力','効率性','ユーモア'])
      st.write(f'選択した値: {val10}')



option_button = st.button('click here')
if option_button == True: st.write('ありがとうございました')
if option_button == True: st.snow()


if option_button == True: 
   col1, col2, col3 = st.columns(3)

   with col1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg")

   with col2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg")

   with col3:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg")


st.title('みなさんのご意見を最後にお聞かせください')

age = st.slider('こちらのアプリの評価はいかがですか', 0, 100,50)
st.write("私の採点は", age, '点です')  
option_button = st.button('送信')
if option_button == True: st.write('送信はされないので、安心してください')