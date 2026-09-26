import streamlit as st

# Session State shuru karna page navigation ke liye
if 'page' not in st.session_state:
    st.session_state.page = 1

st.title("🩺 Advanced Medical MCQs Portal")
st.write("Subject search karein aur page-by-page test complete karein!")

# 10-10 Sawalat ka Mukammal Data Bank
data_bank = {
    "anatomy": [
        {"q": "Insani jism mein sabse lambi haddi kaunsi hai?", "o": ["Femur", "Humerus", "Tibia", "Fibula"], "a": "Femur"},
        {"q": "Insani dil (Heart) mein kitne chambers hote hain?", "o": ["2", "3", "4", "5"], "a": "4"},
        {"q": "Jism ka kaunsa azu (organ) Bile juice paida karta hai?", "o": ["Liver", "Stomach", "Pancreas", "Gallbladder"], "a": "Liver"},
        {"q": "Insani jism ki sabse badi jild (largest organ) kaunsi hai?", "o": ["Skin", "Liver", "Brain", "Lungs"], "a": "Skin"},
        {"q": "Brain ka sabse bada hissa kaunsa hota hai?", "o": ["Cerebrum", "Cerebellum", "Brainstem", "Medulla"], "a": "Cerebrum"},
        {"q": "Red Blood Cells (RBC) jism mein kahan bante hain?", "o": ["Bone Marrow", "Heart", "Spleen", "Kidney"], "a": "Bone Marrow"},
        {"q": "Insani jism mein total kitni haddiyan (bones) hoti hain?", "o": ["206", "306", "106", "216"], "a": "206"},
        {"q": "Kaunsi blood vessel saaf khoon (oxygenated blood) dil se jism tak le jaati hai?", "o": ["Artery (Aorta)", "Vein", "Capillary", "Vena Cava"], "a": "Artery (Aorta)"},
        {"q": "Ghurde (Kidney) ke buniyadi kaam karne wale unit ko kya kehte hain?", "o": ["Nephron", "Neuron", "Alveoli", "Cell"], "a": "Nephron"},
        {"q": "Insani jism mein pasliyon (Ribs) ke kitne jore (pairs) hote hain?", "o": ["12", "10", "14", "8"], "a": "12"}
    ],
    "physiology": [
        {"q": "Normal insani blood pressure kitna hota hai?", "o": ["120/80 mmHg", "140/90 mmHg", "100/60 mmHg", "90/50 mmHg"], "a": "120/80 mmHg"},
        {"q": "Insani dil ek minute mein aam tor par kitni baar dhadakta hai?", "o": ["72 times", "60 times", "90 times", "100 times"], "a": "72 times"},
        {"q": "Khoon mein oxygen carry karne wale protein ka naam kya hai?", "o": ["Hemoglobin", "Insulin", "Albumin", "Globulin"], "a": "Hemoglobin"},
        {"q": "Kaunsa hormone khoon mein sugar level ko control karta hai?", "o": ["Insulin", "Thyroxine", "Adrenaline", "Estrogen"], "a": "Insulin"},
        {"q": "Lungs mein gas exchange (Oxygen/CO2) kahan hoti hai?", "o": ["Alveoli", "Bronchi", "Trachea", "Pleura"], "a": "Alveoli"},
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
        {"q": "Kaunsi dawa khali pet maade (Stomach) ki acidity ke liye di jaati hai?", "o": ["Omeprazole", "Aspirin", "Diazepam", "Paracetamol"], "a": "Omeprazole"},
        {"q": "Insulin kis marz ke ilaj ke liye lagayi jaati hai?", "o": ["Diabetes (Shakar)", "Asthma (Dama)", "Malaria", "Typhoid"], "a": "Diabetes (Shakar)"},
        {"q": "Khoon ko patla karne wali ahem dawa (Blood thinner) kaunsi hai?", "o": ["Aspirin/Warfarin", "Paracetamol", "Amoxicillin", "Insulin"], "a": "Aspirin/Warfarin"},
        {"q": "Achanak severe Allergy (Anaphylaxis) mein kaunsa injection lagaya jata hai?", "o": ["Epinephrine (Adrenaline)", "Atropine", "Furosemide", "Digoxin"], "a": "Epinephrine (Adrenaline)"},
        {"q": "Khansi (Cough) ke liye aam tor par kaunsi class ki dawa di jaati hai?", "o": ["Antitussive", "Antipyretic", "Analgesic", "Antibiotic"], "a": "Antitussive"}
    ]
}

# --- SEARCH SYSTEM ---
search_query = st.text_input("🔍 Subject Search Karein (e.g., anatomy, physiology, pharmacology):"). lower().strip()

# Page logic set karna based on search or manual next buttons
if search_query == "anatomy":
    st.session_state.page = 1
elif search_query == "physiology":
    st.session_state.page = 2
elif search_query == "pharmacology":
    st.session_state.page = 3

# --- PAGE ROUTING SYSTEM ---
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
st.write("Niche diye gaye 10 sawalat ke sahi jawab chunie:")

# 10 Sawalat ko loop ke zariye ek hi page par dikhana
score = 0
user_answers = {}

for i, mcq in enumerate(data_bank[current_subject]):
    st.markdown(f"--- \n**Q{i+1}: {mcq['q']}**")
    user_answers[i] = st.radio(f"Options for Q{i+1}", mcq['o'], key=f"{current_subject}_{i}", label_visibility="collapsed")
    if user_answers[i] == mcq['a']:
        score += 1

# Score and Navigation Buttons
st.markdown("---")
if st.button("Submit This Page Test 🎯"):
    st.balloons()
    st.success(f"Aapne is page par 10 mein se **{score}/10** sawal sahi kiye!")

# Next aur Previous Pages ke buttons
col1, col2 = st.columns(2)
with col1:
    if st.session_state.page > 1:
        if st.button("⬅️ Go to Previous Subject Page"):
            st.session_state.page -= 1
            st.rerun()

with col2:
    if st.session_state.page < 3:
        if st.button("Go to Next Subject Page ➡️"):
            st.session_state.page += 1
            st.rerun()