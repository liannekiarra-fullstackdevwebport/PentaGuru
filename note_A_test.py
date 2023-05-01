#creating a program to learn where all the notes are in the guitar 
#declaring all the distinct notes in the guitar. I am declaring the notes of the guitar below.

''''
There are 12 distinct notes in the guitar which are:
- A
- A#/Bb
- B
- C
- C#/Db
- D
- D#/Eb
- E
- F
- F#/Gb
- G
- G#/Ab

The main objectives for this program is to determine where all the notes are located in the fretboard.
For example the note A occurs in several locations in the fretboard which are 
- open fifth string (5th string)
- 5th fret of sixth string
- 7th fret of D string
- 2nd fret of third string
- 5th fret of first string
- 10th fret of second string
- 12th fret of fifth string 
---------- This pattern repeats after the 12th fret--------------------
This means that the 
- 12th fret of fifth string 
- 17th fret of sixth string
- 14th fret of third string
- 17th fret of first string
- 22th fret of second string
- 24th fret of fifth string

Since the patterns repeat, the pattern should be learned before the 12th fret and 
dus to frets available in the guitar for example some guitars only might have 
- 22 frets (Epiphone SG Pro G400)
- 24 frets
- 20 frets (GS Mini Koa - my guitar )


'''

class A:

    #setting attributes of the A note

    # the A note occurs in 7  differnet locations in the fretboard,
    # 7 differnet lcoations before the pattern repeats at the 12th fret. this means that if the guitar has 24 frets,
    # the patterns repeat, which means that the note A ocurs in 14 distint locations within the fretboard, which has 24 frets.
    # This makes the 12th fret by default the octaves of all the open notes in the guitar in standard tuning.
    # some notes such as the E note occurs in 8 different locations before the 12th fret.
    # however the G note also occurs in 7 different positions before the 12th fret.


    loc_one = ("5th fret of 6th string") # also 17th fret of the 6th string 
    loc_two = ("0th fret of the 5th string") # also the 12th fret of the 5th string
    loc_three = ("12th fret of the 5th string") # also the 24th fret of the 5th string
    loc_four = ("7th fret of the 4th string") # also the 19th fret of the 4th string 
    loc_five = ("2nd fret of the 3rd string") # also the 14th fret of the 3rd string
    loc_six = ("10th fret of the 2nd string") # also the 22nd fret of the 2nd string
    loc_seven = ("5th fret of the 1st string") # also the 17th fret of the 1st string


    def give_information():

        print("The A note occurs in 7 different positions in teh fretboard")
        print("The 7 patterns repeat themselves after the 12th fret")
        print ("The A note has frequency 440Hz")
        print("The frequency of the A note when doubled or tripled are the octave frequencies such as 880Hz and 1760Hz")
        print("The note before A is always a G# or Ab.")
        print("The nore after A is always an A# or a Bb")
    

    #this function shows all locations for the A note in the fretboard 
    #this shows all locations from zero fret to 12th fret before the patterns repeat
    

    def show_all():

        print("5th fret of 6th string")
        print ("0th fret 5th string")
        print("12th fret of 5th string")
        print ("7th fret of 4th string")
        print("2nd fret of 3rd string")
        print("10th fret of 2nd string")
        print("5th fret of 1st string")

    def test_user(self):

        left_note = "Ab or G#"
        left_note_G = "G#"
        right_note = "A# or Bb"
        right_note_B = "Bb"
        distinct_positions = 7
        loc_one = [5,6]
        loc_two = [0,5]
        loc_three = [12,5]
        loc_four = [7, 4]
        loc_five = [2,3]
        loc_six = [10,2]
        loc_seven = [5,1]

        quest_one = int(input("how many distinct locations of the note A just before and in 12th fret:  "))
        if quest_one == distinct_positions:
            print("correct, next question")
        else:
            print("wrong, there are 7 distinct positions of the A Note before and just at the 12th fret")
        
        quest_two = str(input("What is the note always located before the A note:   "))
        if quest_two == "Ab" and "G#":
            print("Correct")
            if quest_two == "Ab":
                alt_ans = str(input("What is another name for Ab: "))
                if alt_ans == "G#":
                    print("correct")
                else:
                    print("wrong it is the G#")
            else:
                ("next quesetion")
        else:
            print("Incorrect.The note always before A is the Ab or the G#.")

        quest_three = str(input("What is the note always located after the A note: "))
        if quest_three == "A#" and "Bb":
            print("Correct")
            if quest_three == "A#":
                alt_ans = str(input("What is another name for A#: "))
                if alt_ans == "Bb":
                    print("Correct")
                else:
                    print("The correct note is the Bb")
            else:
                print("Next question")
        else:
            print("Incorrect")



if __name__ == '__main__':
    print ("-------- FRETBOARD MASTER --------------")
    print('Please ensure your guitar is in Standard Tuning, web app is not useful if instrument is not in standard tuning.')
    note = A()
    note.test_user()
    print("Thats all the questions")
    

    

    



        




        
    



