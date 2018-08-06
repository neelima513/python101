def punct(str):
    punct= '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
    no_punct=""
    for i in str:
        if i not in punct:
           no_punct=no_punct+i
    print(no_punct)
str=("this is *!my  #$ Wor*l@d")
punct(str)
