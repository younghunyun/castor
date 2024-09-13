import streamlit as st

## 홈
pg_home_dashboard = st.Page("pgs/home_dashboard.py", title="대시보드", icon=":material/dashboard:")

## 데이터 수집
pg_data_collection = st.Page("pgs/data_collection.py", title="데이터 수집", icon=":material/downloading:")
pg_data_search = st.Page("pgs/data_search.py", title="데이터 조회", icon=":material/manage_search:")

## Gen AI 분석
pg_genai_text = st.Page("pgs/genai_text.py", title="텍스트 분석", icon=":material/library_books:")
pg_genai_image = st.Page("pgs/genai_image.py", title="이미지 분석", icon=":material/photo_library:")
pg_genai_video = st.Page("pgs/genai_video.py", title="동영상 분석", icon=":material/video_library:")
pg_genai_result = st.Page("pgs/genai_result.py", title="분석 결과 조회", icon=":material/playlist_add_check:")
pg_genai_management = st.Page("pgs/genai_management.py", title="컨텐츠 관리",  icon=":material/folder_managed:")

## 알림 설정
pg_alert_history = st.Page("pgs/alert_history.py", title="알림 이력",  icon=":material/history:")
pg_alert_group = st.Page("pgs/alert_group.py", title="수신 그룹",  icon=":material/group:")

pg = st.navigation({
    "홈": [pg_home_dashboard],
    "데이터 수집": [pg_data_collection, pg_data_search],
    "Gen AI 분석": [pg_genai_text, pg_genai_image, pg_genai_video, pg_genai_result, pg_genai_management],
    "알림 설정": [pg_alert_history, pg_alert_group]
})

pg.run()

with st.sidebar:
    st.text_input("1. Enter the GCP Project ID", key="gcp_project_id")
    # st.write("Project ID: ", st.session_state.gcp_project_id if "gcp_project_id" in st.session_state else "None1")
