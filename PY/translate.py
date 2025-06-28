import pandas as pd
from googletrans import Translator

# Load your Excel file
df = pd.read_excel("Rajasthan_mcv_2025-06-18_rushangi_updated-village_new 1.xlsx")

# Initialize Google Translator
translator = Translator()

# Translate Hindi text in column C (index 2)
df['Translated_Village'] = df.iloc[:, 2].astype(str).apply(lambda text: translator.translate(text, src='hi', dest='en').text)

# Save the translated output
df.to_excel("translated_output.xlsx", index=False)