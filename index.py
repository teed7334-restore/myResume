import openai
import streamlit as st

# Get API key
openai.api_key = st.secrets["secret_key"]

def generate_cover_letter(prompt, language, length):
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
    gender = st.selectbox("請輸入你的性別︰", ["男", "女", "不公開"])
    email = st.text_input("請輸入你的信箱︰", "")
    phone = st.text_input("請輸入你的聯絡電話︰", "")
    job_title = st.text_input("你希望投遞的職位︰", "")
    job_description = st.text_input("你希望的工作內容︰", "")
    company_name = st.text_input("你希望投遞的公司名︰", "")
    skills = st.text_input("你的技能︰", "")
    work_experience = st.text_input("你的年資︰", "")
    project_info = st.text_area("您過去經歷的專案內容︰", "")
    length = st.slider("你希望的履歷的文字長度(中文建議拉長一點)︰", 100, 3000, 500)
    language = st.selectbox("你希望的履歷語系:", ["中文", "英文"])
    tone = st.selectbox("你希望的履歷風格:", ["專業", "友善"])

    lang_switch = {"中文": "zh_tw", "英文": "en"}
    lang = lang_switch.get(language, "中文")
    tone_switch = {"專業": "professional & concise & eye-catching", "友善": "friendly & neat & eye-catching"}
    t = tone_switch.get(tone, '專業')

    if st.button("建立"):
        prompt = (f"Please generate a {t.lower()} cover letter for a job application as a {job_title} at {company_name}. Use my name, {name}, in the letter. <br/>\n"
            f"Include the following information in the letter: <br/>\n"
            f"Gender: {gender} <br />\n"
            f"Email: {email} <br />\n"
            f"Phone number: {phone} <br />\n"
            f"Job description: {job_description} <br />\n"
            f"Skills: {skills} <br />\n"
            f"Years of experience: {work_experience} <br />\n"
            f"Project information: <br />\n"
            f"Please format the following information as a list with bullet points and line breaks, and add some highlights of industry know-how from each project: {project_info} <br />\n"
            f"(language:{lang})")
        cover_letter = generate_cover_letter(prompt, lang, length)
        st.success("新增完成!")
        st.write("---")
        st.write(cover_letter)

if __name__=="__main__":
    main()