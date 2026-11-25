import streamlit as st
import random
import pandas as pd

# 1. 제목 설정
st.title("학생들을 위한 맞춤 스트레칭 가이드")

st.write("---")

# (1) 통증 부위 선택
pain_area = st.radio("1. 통증 부위를 선택하세요", ["목", "어깨", "허리"])

# (2) 앉아있는 시간 선택 (0 ~ 24시간 슬라이더)
sitting_time = st.slider("2. 오늘 앉아있는 시간을 선택하세요 (시간)", 0, 24, 1)

# 분석하기 버튼
if st.button("분석하기"):
    st.write("---")
    st.subheader("📋 맞춤 스트레칭 분석 결과")
    
    # 앉아있는 시간이 2시간 이상일 때만 휴식 메시지 출력 (2시간 미만이면 안 나옴)
    if sitting_time >= 2:
        st.warning("자리에서 일어나 휴식을 취하세요")
    
    # 통증 부위에 따른 운동 데이터 매칭
    if pain_area == "목":
        exercise_name = "목 운동"
        method = "목 천천히 돌리기"
    elif pain_area == "어깨":
        exercise_name = "어깨 운동"
        method = "어깨 앞뒤로 돌리기"
    else: # 허리
        exercise_name = "허리 운동"
        method = "허리 돌리기"
        
    duration = "15초"
    
    # 결과 표 구성 (운동 명 | 방법 | 시간)
    result_data = {
        "운동 명": [exercise_name],
        "방법": [method],
        "시간": [duration]
    }
    
    df = pd.DataFrame(result_data)
    st.table(df)
    
    # random 라이브러리를 활용한 오늘의 응원 한마디 (기능 확장용)
    cheers = [
        "잠깐의 스트레칭이 집중력을 높여줍니다!",
        "바른 자세가 건강한 학교생활을 만듭니다.",
        "오늘도 열공하는 당신을 응원합니다!"
    ]
    st.info(f"💡 {random.choice(cheers)}")
