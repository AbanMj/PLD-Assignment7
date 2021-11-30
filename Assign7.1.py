#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#input: Bahala kayo dyan, #output:, #words: 3, #vowels: 6, #consonants: 

sentence =input("What do you want to say to me?(2 sentences): \n     ")
vowels=0

for i in sentence:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1


print(f"Vowels: \n     The sentences have {vowels} vowels.")