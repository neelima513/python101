def vowel(str):
    str="nandhini reddy"
    vowel=['a','e','i','o','u' or 'A','E','I','O','U']
    count=0
    for i in str:
        if i in vowel:
           count+=1
    print("No. of vowels:",count)

vowel(str)