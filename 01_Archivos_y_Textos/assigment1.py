from pathlib import Path
BASE_DIR = Path(__file__).parent
path_emotion = BASE_DIR / "emotion_words.txt"
path_travel = BASE_DIR / "travel_plans.txt"
path_school = BASE_DIR / "school_prompt.txt"

########  Create a list called emotions that contains the first word of every line in file

with open(path_emotion, "r") as fileR:
    num_words = len(fileR.read())
    print(num_words)


emotion = []

with open(path_emotion, "r") as file:
    for line in file:
        #file.read()
        lines = line.split()
        #print(lines)
        emotion.append(lines[0])
    print(emotion)


######### Assing the first 33 characters from file to the variable first_chars

first_chars = " "

with open(path_travel, "r") as file2:
    chars = file2.read(33)
    first_chars = chars 
    print(first_chars)    

##############  Using the file if the charcter 'p' is in a word then add the word to a list called p_word
p_word = []
with open(path_school, "r") as file3:
    for l in file3:
        lista = l.split()
        for i, w in enumerate(lista):
            if "p" in w:
                p_word.append(w)
                
    print(p_word)
        
        
    

        
    





