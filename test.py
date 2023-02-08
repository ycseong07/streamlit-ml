import streamlit as st

def main():
    st.title("제목입니다")
    st.text("텍스트입니다")
    st.header("헤더입니다")
    st.subheader("서브헤더입니다")

    st.markdown("# 큰 글자")
    st.markdown("## 중간 글자")
    st.markdown("### 작은 글자")

    st.success("성공")
    st.warning("경고")
    st.info("인포")
    st.error("에러")
    st.exception("예외")

if __name__ == "" '__main__':
    main()

