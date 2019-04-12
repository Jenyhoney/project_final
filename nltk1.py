from libindic.stemmer import Stemmer
stemmer = Stemmer()
result = stemmer.stem(language='malayalam', text='രാമന്റെ വീട്ടിലേക്ക്')
for word, output in result.items():
                          print (word, " : ", output['stem'], " : ", output['inflection'])
