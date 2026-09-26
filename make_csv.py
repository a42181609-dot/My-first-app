import pandas as pd

# Aapke Python code ke bilkul exact column names
data = {
    'subject': ['anatomy', 'anatomy', 'anatomy', 'physiology', 'pharmacology'],
    'question': [
        'Which organ pumps blood in the human body?',
        'What is the normal human body temperature?',
        'Which vitamin deficiency causes night blindness?',
        'What is the main function of red blood cells?',
        'Which of the following is an antibiotic?'
    ],
    'option1': ['Lung', '37°C', 'Vitamin A', 'Oxygen transport', 'Paracetamol'],
    'option2': ['Heart', '98°C', 'Vitamin B', 'Blood clotting', 'Amoxicillin'],
    'option3': ['Liver', '45°C', 'Vitamin C', 'Immunity', 'Ibuprofen'],
    'option4': ['Kidney', '32°C', 'Vitamin D', 'Digestion', 'Loratadine'],
    'answer': ['Heart', '37°C', 'Vitamin A', 'Oxygen transport', 'Amoxicillin']
}

df = pd.DataFrame(data)
df.to_csv('medical_data.csv', index=False)
print("🎯 Done! Perfect CSV structure created for your app.")