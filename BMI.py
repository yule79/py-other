import streamlit as st

st.title("BMI")

def bmi(height, weight):
    return weight / ((height/100) ** 2)

def laurel(height, weight):
    return weight / ((height/100)**3) * 10

h = st.number_input('身長(cm)', min_value=1.0)
w = st.number_input('体重(kg)', min_value=1.0)
o = st.selectbox(label="年代を選択", options=["中学生","高校生", "成人"])
s = st.selectbox(label="性別を選択", options=["男性", "女性"])

bmi = bmi(h, w)
laurel = laurel(h,w)

if st.button('BMIを計算'):
    if o=="中学生":
        if laurel<=114:
            st.info("やせている")
        if laurel>=115 and laurel<=144:
            st.info("平均的です")
        if laurel>=145:
            st.info("ふとっている")
    if o=="高校生":
        st.write(f'あなたのBMIは {bmi:.2f} ')
        if s=="男性":
            if bmi<=25 and bmi>=20:
                st.info("平均的です")
        if s=="女性":
            if bmi<=22 and bmi>=18:
                st.info("平均的です")
    if o=="成人":
        st.write(f'あなたのBMIは {bmi:.2f} ')
        if bmi<=25 and bmi>=18:
                st.info("平均的です")


if o=="高校生" and "成人":
    if st.button("BMIを保存"):
        with open('bmi.txt','a',encoding='utf-8') as file:
            file.write(f'{bmi:.2f}')
            file.write(' '+'\n')
            st.info("保存しました")