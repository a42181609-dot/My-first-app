import streamlit as st

# Session States ko shuru karna navigation aur modes ke liye
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0

st.title("🩺 Advanced Medical MCQs Portal")
st.write("Subject search karein aur apni pasand ke mutabiq test complete karein!")

# 10-10 Sawalat ka Data Bank
data_bank = {
    "anatomy": [
        {"q": "Insani jism mein sabse lambi haddi kaunsi hai?", "o": ["Femur", "Humerus", "Tibia", "Fibula"], "a": "Femur"},
        {"q": "Insani dil (Heart) mein kitne chambers hote hain?", "o": ["2", "3", "4", "5"], "a": "4"},
        {"q": "Jism ka kaunsa azu (organ) Bile juice paida karta hai?", "o": ["Liver", "Stomach", "Pancreas", "Gallbladder"], "a": "Liver"},
        {"q": "Insani jism ki sabse badi jild (largest organ) kaunsi hai?", "o": ["Skin", "Liver", "Brain", "Lungs"], "a": "Skin"},
        {"q": "Brain ka sabse bada hissa kaunsa hota hai?", "o": ["Cerebrum", "Cerebellum", "Brainstem", "Medulla"], "a": "Cerebrum"},
        {"q": "Red Blood Cells (RBC) jism mein kahan bante hain?", "o": ["Bone Marrow", "Heart", "Spleen", "Kidney"], "a": "Bone Marrow"},
        {"q": "Insani jism mein total kitni haddiyan (bones) hoti hain?", "o": ["206", "306", "106", "216"], "a": "206"},
        {"q": "Kaunsi blood vessel saaf khoon dil se jism tak le jaati hai?", "o": ["Artery (Aorta)", "Vein", "Capillary", "Vena Cava"], "a": "Artery (Aorta)"},
        {"q": "Ghurde (Kidney) ke buniyadi kaam karne wale unit ko kya kehte hain?", "o": ["Nephron", "Neuron", "Alveoli", "Cell"], "a": "Nephron"},
        {"q": "Insani jism mein pasliyon (Ribs) ke kitne jore (pairs) hote hain?", "o": ["12", "10", "14", "8"], "a": "12"}
    ],
    "physiology": [
        {"q": "Normal insani blood pressure kitna hota hai?", "o": ["120/80 mmHg", "140/90 mmHg", "100/60 mmHg", "90/50 mmHg"], "a": "120/80 mmHg"},
        {"q": "Insani dil ek minute mein aam tor par kitni baar dhadakta hai?", "o": ["72 times", "60 times", "90 times", "100 times"], "a": "72 times"},
        {"q": "Khoon mein oxygen carry karne wale protein ka naam kya hai?", "o": ["Hemoglobin", "Insulin", "Albumin", "Globulin"], "a": "Hemoglobin"},
        {"q": "Kaunsa hormone khoon mein sugar level ko control karta hai?", "o": ["Insulin", "Thyroxine", "Adrenaline", "Estrogen"], "a": "Insulin"},
        {"q": "Lungs mein gas exchange kahan hoti hai?", "o": ["Alveoli", "Bronchi", "Trachea", "Pleura"], "a": "Alveoli"},
        {"q": "Insani jism mein khana hazam karne ka ahem kaam kahan hota hai?", "o": ["Small Intestine", "Stomach", "Large Intestine", "Esophagus"], "a": "Small Intestine"},
        {"q": "Universal Donor blood group kaunsa hai?", "o": ["O Negative", "AB Positive", "A Positive", "B Positive"], "a": "O Negative"},
        {"q": "Jism ka normal temperature Fahrenheit mein kitna hota hai?", "o": ["98.6°F", "37°F", "96.4°F", "100°F"], "a": "98.6°F"},
        {"q": "Aankh ka kaunsa hissa roshni ko control karta hai aur rang deta hai?", "o": ["Iris", "Retina", "Cornea", "Lens"], "a": "Iris"},
        {"q": "Muscle contraction ke liye kaunsa mineral sabse zaroori hai?", "o": ["Calcium", "Iron", "Sodium", "Potassium"], "a": "Calcium"}
    ],
    "pharmacology": [
        {"q": "Amoxicillin kis qism ki dawa hai?", "o": ["Antibiotic", "Painkiller", "Antiviral", "Antifungal"], "a": "Antibiotic"},
        {"q": "Paracetamol ka ahem kaam kya hai?", "o": ["Fever & Pain reduction", "Infection cure", "Blood pressure control", "Sleep aid"], "a": "Fever & Pain reduction"},
        {"q": "Penicillin kisne dariaft (discover) ki thi?", "o": ["Alexander Fleming", "Louis Pasteur", "Robert Koch", "Edward Jenner"], "a": "Alexander Fleming"},
        {"q": "Dil ke marz mein di jaane wali emergency dawa kaunsi hai?", "o": ["Nitroglycerin", "Metformin", "Atorvastatin", "Omeprazole"], "a": "Nitroglycerin"},
        {"q": "Hypertension (High BP) ko kam karne wali dawa kaunsi hai?", "o": ["Lisinopril", "Amoxicillin", "Ibuprofen", "Metformin"], "a": "Lisinopril"},
        {"q": "Kaunsi dawa khali pet maade ki acidity ke liye di jaati hai?", "o": ["Omeprazole", "Aspirin", "Diazepam", "Paracetamol"], "a": "Omeprazole"},
        {"q": "Insulin kis marz ke ilaj ke liye lagayi jaati hai?", "o": ["Diabetes (Shakar)", "Asthma (Dama)", "Malaria", "Typhoid"], "a": "Diabetes (Shakar)"},
        {"q": "Khoon ko patla karne wali ahem dawa kaunsi hai?", "o": ["Aspirin/Warfarin", "Paracetamol", "Amoxicillin", "Insulin"], "a": "Aspirin/Warfarin"},
        {"q": "Achanak severe Allergy mein kaunsa injection lagaya jata hai?", "o": ["Epinephrine (Adrenaline)", "Atropine", "Furosemide", "Digoxin"], "a": "Epinephrine (Adrenaline)"},
        {"q": "Khansi ke liye aam tor par kaunsi class ki dawa di jaati hai?", "o": ["Antitussive", "Antipyretic", "Analgesic", "Antibiotic"], "a": "Antitussive"}
    ]
}

# --- SEARCH SYSTEM ---
search_query = st.text_input("🔍 Subject Search (anatomy, physiology, pharmacology):").lower().strip()

if search_query == "anatomy":
    st.session_state.page = 1
    st.session_state.q_index = 0
elif search_query == "physiology":
    st.session_state.page = 2
    st.session_state.q_index = 0
elif search_query == "pharmacology":
    st.session_state.page = 3
    st.session_state.q_index = 0

# Page Routing setup
if st.session_state.page == 1:
    current_subject = "anatomy"
    display_title = "🦴 Page 1: Anatomy (Insani Jism)"
elif st.session_state.page == 2:
    current_subject = "physiology"
    display_title = "🫁 Page 2: Physiology (Afaal-e-Aza)"
else:
    current_subject = "pharmacology"
    display_title = "💊 Page 3: Pharmacology (Adviyat)"

st.header(display_title)

# --- NEW VIEW MODE SYSTEM ---
view_mode = st.radio("🧐 Dikhane ka Tareeqa (View Mode):", ["Ikhtay (Saare sawal ek sath)", "Aik Aik Sawal (Single Mode)"], horizontal=True)

mcqs_list = data_bank[current_subject]

# --- MODE 1: IKHTAY (ALL MCQS TOGETHER) ---
if view_mode == "Ikhtay (Saare sawal ek sath)":
    score = 0
    user_answers = {}
    for i, mcq in enumerate(mcqs_list):
        st.markdown(f"--- \n**Q{i+1}: {mcq['q']}**")
        user_answers[i] = st.radio(f"Options for Q{i+1}", mcq['o'], key=f"all_{current_subject}_{i}", label_visibility="collapsed")
        if user_answers[i] == mcq['a']:
            score += 1
            
    st.markdown("---")
    if st.button("Submit This Page Test 🎯", key="submit_all"):
        st.balloons()
        st.success(f"Aapne is page par 10 mein se **{score}/10** sawal sahi kiye!")

# --- MODE 2: AIK AIK SAWAL (SINGLE MCQ MODE) ---
else:
    q_idx = st.session_state.q_index
    mcq = mcqs_list[q_idx]
    
    st.markdown(f"--- \n### Sawal {q_idx + 1} of 10")
    st.subheader(mcq['q'])
    
    user_choice = st.radio("Sahi jawab chunein:", mcq['o'], key=f"single_{current_subject}_{q_idx}")
    
    # Check button for single question
    if st.button("Jawab Check Karein ✔️"):
        if user_choice == mcq['a']:
            st.success("🎉 Perfect Answers!")
        else:
            st.error(f"❌ Wrong Answer! this is corect Answer: **{mcq['a']}**")
            
    # Single mode navigation buttons
    col_q1, col_q2 = st.columns(2)
    with col_q1:
        if q_idx > 0:
            if st.button("⬅️ Previous question"):
                st.session_state.q_index -= 1
                st.rerun()
    with col_q2:
        if q_idx < 9:
            if st.button("Next question ➡️"):
                st.session_state.q_index += 1
                st.rerun()
        else:
            st.info("Aapne is subject ke saare sawal dekh liye hain! Niche se agla page badlein.")

# --- MAIN PAGE NAVIGATION BUTTONS ---
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.session_state.page > 1:
        if st.button("⬅️ Go to Previous Subject Page", key="prev_page"):
            st.session_state.page -= 1
            st.session_state.q_index = 0
            st.rerun()

with col2:
    if st.session_state.page < 3:
        if st.button("Go to Next Subject Page ➡️", key="next_page"):
            st.session_state.page += 1
            st.session_state.q_index = 0
            st.rerun()