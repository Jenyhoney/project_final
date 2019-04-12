from __future__ import unicode_literals
from polyglot_tokenizer import Tokenizer
tk = Tokenizer(lang='ml', smt=True) #smt is a flag for social-media-text
text = "രണ്ട് വർഷംമുമ്പ് നടന്ന നിയമസഭാ തെരഞ്ഞെടുപ്പിൽ തിരിച്ചടി ലഭിച്ചതിനുശേഷം ഗുജറാത്തിൽ ബിജെപിയുടേത് ഒരുതരം ഞാണിൻമേൽക്കളിയാണ്. കഴിഞ്ഞ ലോക്സഭാ തെരഞ്ഞെടുപ്പിൽ ആകെയുള്ള 26 സീറ്റിലും വിജയിച്ച ബിജെപി ഇക്കുറി അത് നിലനിർത്താനായി  എല്ലാ വൃത്തികെട്ട കളിയും പുറത്തെടുക്കുകയാണ്."
print(tk.tokenize(text))
