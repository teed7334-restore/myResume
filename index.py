import openai_secret_manager
import openai
import streamlit as st

# Get API key
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

def generate_cover_letter(prompt, length):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=length,
        n=1,
        stop=None,
        temperature=0.5
    )

    message = completions.choices[0].text
    return message.strip()

def main():
    st.set_page_config(page_title="myResume", page_icon=":guardsman:", layout="wide")
    st.title("建立我的履歷")

    name = st.text_input("請輸入你的姓名︰", "")
    gender = st.text_input("請輸入你的性別︰", "")
    email = st.text_input("請輸入你的信箱︰", "")
    phone = st.text_input("請輸入你的聯絡電話︰", "")
    job_title = st.text_input("你希望投遞的職位︰", "")
    job_description = st.text_input("你希望的工作內容︰", "")
    company_name = st.text_input("你希望投遞的公司名︰", "")
    skills = st.text_input("你的技能︰", "")
    work_experience = st.text_input("你的技能︰", "")
    length = st.slider("你希望的履歷的文字長度︰", 100, 1000, 500)
    language = st.selectbox("你希望的履歷語系:", ["中文", "英文"])
    tone = st.selectbox("你希望的履歷風格:", ["專業", "友善"])

    if st.button("建立"):
        prompt = (f"Please generate a {tone.lower()} cover letter for a job application as a {job_title} at {company_name}. Use my name, {name}, in the letter.\n"
          f"Include the following information in the letter: \n"
          f"Gender: {gender} \n"
          f"Email: {email} \n"
          f"Phone number: {phone} \n"
          f"Job description: {job_description} \n"
          f"Skills: {skills} \n"
          f"Years of experience: {work_experience} \n"
          f"Resume language: {language}\n")
        cover_letter = generate_cover_letter(prompt, length)
        st.success("Cover letter generated!")
        st.write("---")
        st.write(cover_letter)

if __name__=="__main__":
    main()