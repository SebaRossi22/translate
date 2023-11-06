from googletrans import Translator

def translate_to_italian(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='it')
    return translated.text

if __name__ == "__main__":
    text_to_translate = input("Enter the English text to translate to Italian: ")
    translated_text = translate_to_italian(text_to_translate)
    print("Translated text (Italian):", translated_text)
