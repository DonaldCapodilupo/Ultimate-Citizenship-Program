return_dict = {
    'What is the supreme law of the land?': [

    ],
    'What does the Constitution do?': [

    ],
    'The idea of self-government is in the first three words of the Constitution. What are these words?': [

    ],
    'What is an amendment?': [

    ],
    'What do we call the first ten amendments to the Constitution?': [

    ],
    'What is one right or freedom from the First Amendment?*': [

    ],
    'How many amendments does the Constitution have?': [
        "Twenty-Seven (27)"

    ],
    'What did the Declaration of Independence do?': [

    ],
    'What are two rights in the Declaration of Independence?': [

    ],
    'What is freedom of religion?': [

    ],
    'What is the economic system in the United States?*': [

    ],
    'What is the "rule of law"?': [

    ],
    'Name one branch or part of the government.*': [

    ],
    'What stops one branch of government from becoming too powerful?': [

    ],
    'Who is in charge of the executive branch?': [

    ],
    'Who makes federal laws?': [

    ],
    'What are the two parts of the U.S. Congress?*': [

    ],
    'How many U.S. Senators are there?': [

    ],
    'We elect a U.S. Senator for how many years?': [

    ],
    "Who is one of your state's U.S. Senators now?*": [

    ],
    'The House of Representatives has how many voting members?': [

    ],
    'We elect a U.S. Representative for how many years?': [],
    'Name your U.S. Representative.': [],
    'Who does a U.S. Senator represent?': [],
    'Why do some states have more Representatives than other states?': [],
    'We elect a President for how many years?': [],
    'In what month do we vote for President?*': [],
    'What is the name of the President of the United States now?*': [],
    'What is the name of the Vice President of the United States now?': [],
    'If the President can no longer serve, who becomes President?': [],
    'If both the President and the Vice President can no longer serve, who becomes President?': [],
    'Who is the Commander in Chief of the military?': [],
    'Who signs bills to become laws?': [],
    'Who vetoes bills?': [],
    "What does the President's Cabinet do?": [],
    'What are two Cabinet-level positions?': [],
    'What does the judicial branch do?': [],
    'What is the highest court in the United States?': [],
    'How many justices are on the Supreme Court?': [],
    'Who is the Chief Justice of the United States now?': [],
    'Under our Constitution, some powers belong to the federal government. What is one power of the federal government?': [],
    'Under our Constitution, some powers belong to the states. What is one power of the states?': [],
    'Who is the Governor of your state now?': [],
    'What is the capital of your state?*': [],
    'What are the two major political parties in the United States?*': [],
    'What is the political party of the President now?': [],
    'What is the name of the Speaker of the House of Representatives now?': [],
    'There are four amendments to the Constitution about who can vote. Describe one of them.': [],
    'What is one responsibility that is only for United States citizens?*': [],
    'Name one right only for United States citizens.': [],
    'What are two rights of everyone living in the United States?': [],
    'What do we show loyalty to when we say the Pledge of Allegiance?': [],
    'What is one promise you make when you become a United States citizen?': [],
    'How old do citizens have to be to vote for President?*': [],
    'What are two ways that Americans can participate in their democracy?': [],
    'When is the last day you can send in federal income tax forms?*': [],
    'When must all men register for the Selective Service?': [],
    'What is one reason colonists came to America?': [],
    'Who lived in America before the Europeans arrived?': [],
    'What group of people was taken to America and sold as slaves?': [],
    'Why did the colonists fight the British?': [],
    'Who wrote the Declaration of Independence?': [],
    'When was the Declaration of Independence adopted?': [],
    'There were 13 original states. Name three.': [],
    'What happened at the Constitutional Convention?': [],
    'When was the Constitution written?': [],
    'The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers.': [],
    'What is one thing Benjamin Franklin is famous for?': [],
    'Who is the "Father of Our Country"?': [],
    'Who was the first President?*': [],
    'What territory did the United States buy from France in 1803?': [],
    'Name one war fought by the United States in the 1800s.': [],
    'Name the U.S. war between the North and the South.': [],
    'Name one problem that led to the Civil War.': [],
    'What was one important thing that Abraham Lincoln did?*': [],
    'What did the Emancipation Proclamation do?': [],
    'What did Susan B. Anthony do?': [],
    'Name one war fought by the United States in the 1900s.*': [],
    'Who was President during World War I?': [],
    'Who was President during the Great Depression and World War II?': [],
    'Who did the United States fight in World War II?': [],
    'Before he was President, Eisenhower was a general. What war was he in?': [],
    'During the Cold War, what was the main concern of the United States?': [],
    'What movement tried to end racial discrimination?': [],
    'What did Martin Luther King, Jr. do?*': [],
    'What major event happened on September 11, 2001, in the United States?': [],
    'Name one American Indian tribe in the United States.': [],
    'Name one of the two longest rivers in the United States.': [],
    'What ocean is on the West Coast of the United States?': [],
    'What ocean is on the East Coast of the United States?': [],
    'Name one U.S. territory.': [],
    'Name one state that borders Canada.': [],
    'Name one state that borders Mexico.': [],
    'What is the capital of the United States?*': [],
    'Where is the Statue of Liberty?*': [],
    'Why does the flag have 13 stripes?': [],
    'Why does the flag have 50 stars?*': [],
    'What is the name of the national anthem?': [],
    'When do we celebrate Independence Day?*': [],
    'Name two national U.S. holidays.': []
}

searching_answers = False
index_num = 0

spanish_dict = {}

with open("Old stuff/spanish questionbank.txt", "r", encoding="utf8") as file:
    for text_line in file:

        words_in_sentence = text_line.split()

        # Is the line a question or an answer?
        # Question
        # Skip Blank Lines
        if len(words_in_sentence) == 0:
            continue

        if words_in_sentence[0].replace(".", "").isnumeric():
            question_text = " ".join(words_in_sentence[1:]).replace("\n", "")
            print("Question Number:" + str(words_in_sentence[0].replace(".", "")))
            print("Question text: " + question_text)
            print("Passing on this line for now.")
            spanish_dict[question_text] = []
        print("********** " + words_in_sentence[0] + "************************")
        if words_in_sentence[0] == "▪":
            answer_text = " ".join(words_in_sentence[1:]).replace("\n", "")
            #return_dict[question_text].append(answer_text)
            print("This is an answer: " + answer_text)
            spanish_dict[question_text].append(answer_text)

import json
print(spanish_dict)

with open("Trivia Questions Spanish.json", "w") as outfile:
    json.dump(spanish_dict, outfile, ensure_ascii=False)




        #print("There is no number at the beginning of this:")
        #print(text_line)

    # if words_in_sentence[0] == ".":
    #    print(" ".join(words_in_sentence[1:]))
    #    return_dict[index_num].append(" ".join(words_in_sentence[1:]))
#
# else:
#    print("**********************************************************************")
#    index_num += 1
#    print(return_dict)

# print(words_in_sentence)

#

#
# except IndexError as e:
#    try:
#        return_dict[" ".join(words_in_sentence[1:])].append(words_in_sentence[1:])
#    except KeyError as e:
#        print(e)
#    continue


partially_filled_out_dict = {
    'What is the supreme law of the land?': [
        "The Constitution"
    ],
    'What does the Constitution do?': [
        "sets up the government",
        "Defines the government",
        "Protects basic rights of Americans"
    ],
    'The idea of self-government is in the first three words of the Constitution. What are these words?': [
        "We the People"
    ],
    'What is an amendment?': [
        "A change (to the Constitution"
    ],
    'What do we call the first ten amendments to the Constitution?': [
        "The Bill of Rights"
    ],
    'What is one right or freedom from the First Amendment?*': [
        "Speech",
        "Religion,"
        "Assembly",
        "Press",
        "Petition the Government"

    ],
    'How many amendments does the Constitution have?': [
        "Twenty-Seven (27)"

    ],
    'What did the Declaration of Independence do?': [

    ],
    'What are two rights in the Declaration of Independence?': [

    ],
    'What is freedom of religion?': [

    ],
    'What is the economic system in the United States?*': [

    ],
    'What is the "rule of law"?': [

    ],
    'Name one branch or part of the government.*': [

    ],
    'What stops one branch of government from becoming too powerful?': [

    ],
    'Who is in charge of the executive branch?': [

    ],
    'Who makes federal laws?': [

    ],
    'What are the two parts of the U.S. Congress?*': [

    ],
    'How many U.S. Senators are there?': [

    ],
    'We elect a U.S. Senator for how many years?': [

    ],
    "Who is one of your state's U.S. Senators now?*": [

    ],
    'The House of Representatives has how many voting members?': [

    ],
    'We elect a U.S. Representative for how many years?': [],
    'Name your U.S. Representative.': [],
    'Who does a U.S. Senator represent?': [],
    'Why do some states have more Representatives than other states?': [],
    'We elect a President for how many years?': [],
    'In what month do we vote for President?*': [],
    'What is the name of the President of the United States now?*': [],
    'What is the name of the Vice President of the United States now?': [],
    'If the President can no longer serve, who becomes President?': [],
    'If both the President and the Vice President can no longer serve, who becomes President?': [],
    'Who is the Commander in Chief of the military?': [],
    'Who signs bills to become laws?': [],
    'Who vetoes bills?': [],
    "What does the President's Cabinet do?": [],
    'What are two Cabinet-level positions?': [],
    'What does the judicial branch do?': [],
    'What is the highest court in the United States?': [],
    'How many justices are on the Supreme Court?': [],
    'Who is the Chief Justice of the United States now?': [],
    'Under our Constitution, some powers belong to the federal government. What is one power of the federal government?': [],
    'Under our Constitution, some powers belong to the states. What is one power of the states?': [],
    'Who is the Governor of your state now?': [],
    'What is the capital of your state?*': [],
    'What are the two major political parties in the United States?*': [],
    'What is the political party of the President now?': [],
    'What is the name of the Speaker of the House of Representatives now?': [],
    'There are four amendments to the Constitution about who can vote. Describe one of them.': [],
    'What is one responsibility that is only for United States citizens?*': [],
    'Name one right only for United States citizens.': [],
    'What are two rights of everyone living in the United States?': [],
    'What do we show loyalty to when we say the Pledge of Allegiance?': [],
    'What is one promise you make when you become a United States citizen?': [],
    'How old do citizens have to be to vote for President?*': [],
    'What are two ways that Americans can participate in their democracy?': [],
    'When is the last day you can send in federal income tax forms?*': [],
    'When must all men register for the Selective Service?': [],
    'What is one reason colonists came to America?': [],
    'Who lived in America before the Europeans arrived?': [],
    'What group of people was taken to America and sold as slaves?': [],
    'Why did the colonists fight the British?': [],
    'Who wrote the Declaration of Independence?': [],
    'When was the Declaration of Independence adopted?': [],
    'There were 13 original states. Name three.': [],
    'What happened at the Constitutional Convention?': [],
    'When was the Constitution written?': [],
    'The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers.': [],
    'What is one thing Benjamin Franklin is famous for?': [],
    'Who is the "Father of Our Country"?': [],
    'Who was the first President?*': [],
    'What territory did the United States buy from France in 1803?': [],
    'Name one war fought by the United States in the 1800s.': [],
    'Name the U.S. war between the North and the South.': [],
    'Name one problem that led to the Civil War.': [],
    'What was one important thing that Abraham Lincoln did?*': [],
    'What did the Emancipation Proclamation do?': [],
    'What did Susan B. Anthony do?': [],
    'Name one war fought by the United States in the 1900s.*': [],
    'Who was President during World War I?': [],
    'Who was President during the Great Depression and World War II?': [],
    'Who did the United States fight in World War II?': [],
    'Before he was President, Eisenhower was a general. What war was he in?': [],
    'During the Cold War, what was the main concern of the United States?': [],
    'What movement tried to end racial discrimination?': [],
    'What did Martin Luther King, Jr. do?*': [],
    'What major event happened on September 11, 2001, in the United States?': [],
    'Name one American Indian tribe in the United States.': [],
    'Name one of the two longest rivers in the United States.': [],
    'What ocean is on the West Coast of the United States?': [],
    'What ocean is on the East Coast of the United States?': [],
    'Name one U.S. territory.': [],
    'Name one state that borders Canada.': [],
    'Name one state that borders Mexico.': [],
    'What is the capital of the United States?*': [],
    'Where is the Statue of Liberty?*': [],
    'Why does the flag have 13 stripes?': [],
    'Why does the flag have 50 stars?*': [],
    'What is the name of the national anthem?': [],
    'When do we celebrate Independence Day?*': [],
    'Name two national U.S. holidays.': []
}
