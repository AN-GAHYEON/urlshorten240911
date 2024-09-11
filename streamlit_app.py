import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pyshorteners

# 앱 제목
st.title("URL 단축기")

# URL 입력 받기
url = st.text_input("단축할 URL을 입력하세요:")

if url:
    # URL 단축기 생성
    s = pyshorteners.Shortener()
    
    # URL 단축
    try:
        short_url = s.tinyurl.short(url)
        st.write("단축된 URL:")
        st.write(short_url)
        st.markdown(f"[여기서 확인하기]({short_url})", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"URL 단축 중 오류가 발생했습니다: {e}")
