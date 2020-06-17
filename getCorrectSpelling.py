from spellchecker import SpellChecker
spell = SpellChecker()

class getCorrectSpelling:
    def __init__(self):
        self.finalSentence=""

    def correctStatement(self,sentence):
        self.finalSentence=sentence
        misspelled = spell.unknown(sentence.split())
        for word in misspelled:
            self.finalSentence=sentence.replace(word,spell.correction(word))
        return ("Did you mean \n"+self.finalSentence+"\n Please Re enter the Correct Spelling/Rephrased Query to get correct results")



