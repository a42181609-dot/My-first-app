import streamlit as st

# App ka Title aur Header
st.title("🩺 Medical MCQs Practice App")
st.write("Apne medical knowledge ko test karein aur seekhein!")

# Sidebar mein Subject select karne ka option
subject = st.sidebar.selectbox(
    "Subject Chunein:",
    ["Anatomy (Insani Jism)", "Physiology (Afaal-e-Aza)", "Pharmacology (Adviyat)"]
)

# Har subject ke mutabiq MCQs ka data
questions = {
    "Anatomy (Insani Jism)": {
        "question": "Insani jism (Human Body) mein sabse lambi (longest) haddi kaunsi hai?",
        "options": ["Femur (Thigh bone)", "Humerus", "Tibia", "Fibula"],
        "answer": "Femur (Thigh bone)",
        "explanation": "Femur insani jism ki sabse lambi aur mazboot haddi hoti hai jo raan (thigh) mein paayi jaati hai."
    },
    "Physiology (Afaal-e-Aza)": {
        "question": "Ek aam insani jism mein normal blood pressure kitna hota hai?",
        "options": ["140/90 mmHg", "120/80 mmHg", "100/60 mmHg", "90/50 mmHg"],
        "answer": "120/80 mmHg",
        "explanation": "Normal insani blood pressure 120/80 mmHg hota hai, jahan 120 Systolic aur 80 Diastolic pressure hai."
    },
    "Pharmacology (Adviyat)": {
        "question": "Niche diye gaye mein se kaunsi dawa Antibiotic (bacteria ke khilaf) hai?",
        "options": ["Paracetamol", "Amoxicillin", "Ibuprofen", "Insulin"],
        "answer": "Amoxicillin",
        "explanation": "Amoxicillin ek aam Penicillin-type antibiotic dawa hai jo bacterial infections ke ilaj mein istemal hoti hai."
    }
}

# Selected subject ka sawal uthana
current_quiz = questions[subject]

st.header(f"📋 Subject: {subject}")
st.write(f"**Sawal:** {current_quiz['question']}")

# Radio buttons ke zariye options dikhana
user_choice = st.radio("Sahi jawab chunein:", current_quiz["options"])

# Answer submit karne ka button
if st.button("Submit Answer 🚀"):
    if user_choice == current_quiz["answer"]:
        st.success("🎉 Bilkul Sahi Jawab! Boht khoob.")
    else:
        st.error(f"❌ Galat Jawab! Sahi jawab yeh tha: **{current_quiz['answer']}**")
    
    # Wajah/Explanation dikhana
    st.info(f"💡 **Wajah (Explanation):** {current_quiz['explanation']}")