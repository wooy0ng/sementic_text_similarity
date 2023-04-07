import streamlit as st
from inference_one import inference


st.set_page_config(layout="wide")


if __name__ == '__main__':
    st.title("sementic text similarity")
    st.text("두 문장을 입력받아 서로 간의 문장 뜻 유사도를 0~5 사이로 측정하는 서비스입니다.")
    st.text("사용자가 입력한 모든 데이터는 DB에서 관리합니다.")
    
    col1, col2 = st.columns(2)
    with col1:
        sentence_1 = st.text_input("문장 1")
    with col2:
        sentence_2 = st.text_input("문장 2")
    
    inference_btn = st.button('inference', disabled=False if sentence_1 and sentence_2 else True)
    
    if inference_btn:
        prediction: float = inference(sentence_1, sentence_2)
        st.text(f"두 문장 간 유사도는 {prediction}입니다. (5에 가까울 수록 문장 간 의미가 유사합니다)")
        

    