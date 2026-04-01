import streamlit as st
from openai import OpenAI

# 1. إعدادات هوية التطبيق (تظهر في تبويب المتصفح)
st.set_page_config(
    page_title="تطبيق معاذ الذكي", 
    page_icon="🤖",
    layout="centered"
)

# 2. لمسة المبرمج معاذ (التصميم العلوي)
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #007bff;
        font-family: 'Arial';
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🤖 Moaz GPT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>مرحباً بك في تطبيق الدردشة الخاص بالمطور <b>معاذ</b></p>", unsafe_allow_html=True)

# 3. القائمة الجانبية لإثبات ملكيتك للتطبيق
with st.sidebar:
    st.title("👨‍💻 لوحة التحكم")
    st.success(f"المبرمج: **معاذ**")
    st.write("هذا التطبيق نسخة مخصصة من ChatGPT تعمل تحت إشراف معاذ.")
    st.markdown("---")
    if st.button("مسح ذاكرة الدردشة"):
        st.session_state.messages = []
        st.rerun()

# 4. محرك الذكاء الاصطناعي (مفتاحك الخاص)
# ملاحظة: سيتم قراءة المفتاح من الكود مباشرة كما طلبت
client = OpenAI(api_key="Sk-proj-k-x4JRd9IIU4GZvVC63_3fiZzcs2LGvHO6aSMqeJOMJkrKZ1AvwtWdSe24kpDuhqQuqadrpO72T3BlbkFJ6LI7h6nuxX4EL852bs5m3RU8o4hAoCX4QO8PfU5yaUbtyIj8FfnCYPqThxlQO4J3a4Us7QgaoA")

# 5. إدارة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. منطقة الدردشة والردود
if prompt := st.chat_input("تحدث مع ذكاء معاذ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("معاذ يحلل طلبك الآن..."):
            try:
                stream = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error("عذراً معاذ، يبدو أن هناك مشكلة في مفتاح الـ API أو الرصيد.")

# 7. حقوق الملكية الدائمة في الأسفل
st.markdown("<div class='footer'>صُنع بكل فخر بواسطة المبرمج معاذ © 2026</div>", unsafe_allow_html=True)
