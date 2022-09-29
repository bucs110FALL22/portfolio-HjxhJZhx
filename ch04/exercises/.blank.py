text = """"
Many investors see the dollar as a safe place to put their money in times of trouble.
That has helped to drive up its value against other currencies, including the British pound - which hit an all-time low against the dollar on Monday.
Also on Wednesday, the dollar reached a fresh 20-year high against a closely-watched group of leading global currencies.
The yuan's slide is yet another example of a currency weakening as a result of the strong dollar.

substitutions = 
{ "white house":"Pit of Despair",
    "allegedly":"totally",
    "bill":"snap I didn’t screenshot",
    "dollar":"puppy",
    "congressional":"spaaaaace",
    "republican":"piano accordionist",
    "democrat":"chromatic button accordionist",
    "senator": "magical wizard",
    "representative": "unmagical wizard",
    "secretary":"eating champion",
    "leaders":"goblins",
    "washington":"Mount Doom",
    "president": "you know, the guy"
}

for key, value in substitutions.items()
  article = article. replace. replace(key value)
  print(article)
  