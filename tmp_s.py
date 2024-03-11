# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
# nlp = spacy.load("en_core_web_sm")
nlp = spacy.load("sk_core_web_sm")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasnt "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

# text = ("I need to go back to duolingo")
text = ("hey levi u wanna play league of legends. I have an tool")
text = "Ahoj, byvam v bratislave"
doc = nlp(text)




# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)
