# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
while True:
    user_word = input('please enter a word or phrase: ')
    word_length = len(user_word)

    if(user_word == 'quit'):
        print('goodbye')
        break

    print(f'what you entered is {word_length} characters long')
