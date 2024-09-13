import streamlit as st


def test_func(param):
    return f"param: {param}"


st.subheader("이미지 분석")

tab_image_desc, tab_image_gen = st.tabs([
    "이미지의 설명 생성", 
    "텍스트 to 이미지"
])

with tab_image_desc:
    st.write(test_func("TEST"))
    "---"
    st.write("Result:")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab_image_gen:

    "---"
    st.write("Result:")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
