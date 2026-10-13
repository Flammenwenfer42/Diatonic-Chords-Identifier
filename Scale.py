import argparse
notes = {"C":1,"C#":2,"D":3,"D#": 4,"E": 5,"F": 6,"F#": 7,"G": 8,"G#": 9,"A": 10,"A#": 11,"B": 12}
test = {1:"C",2:"C#",3:"D",4:"D#",5:"E",6:"F",7:"F#",8:"G",9:"G#",10:"A",11:"A#",12:"B"}

triad = 3
romanNumbers = {1:"i",2:"ii",3:"iii",4:"iv",5:"v",6:"vi",7:"vii"}
one = "i"
two = "ii"
three = "iii"
four = "iv"


Major = [2,2,1,2,2,2,1]
Minor = [2,1,2,2,1,2,2]
# maj is w,w,h,w,w,w,h
#min is w,h,w,w,h,w,w


def Maj_scale(rootNote: str, flat = False):
    scale = []
    num = 1
    idx = notes[rootNote]
    for i in Major:

        if idx > len(notes):
            idx -= len(notes) 
        curNote = test[idx]
        if flat:
            if "#" in curNote:
                curNote = test[idx+1] + "b"
        
        scale.append(curNote)
        idx += i
        num +=1
    return scale

def Min_scale(rootNote,flat=False):
    scale = []
    num = 1
    idx = notes[rootNote]
    for i in Minor:

        if idx > len(notes):
            idx -= len(notes) 
        curNote = test[idx]
        if flat:
            if "#" in curNote:
                curNote = test[idx+1] + "b"
        
        scale.append(curNote)
        idx += i
        num +=1
    return scale

def chords(note:str ,type,flat = True,notes_number = 3):
    #note = note.replace("b","#")
    num = 1
    if type == "maj":
        scale = Maj_scale(note)
        
    else:
        scale = Min_scale(note)
        
    
    idx = notes[note]

    placeholder = note
    if flat:
        placeholder = note.replace("#","b")
    if type == "maj":
        print(f"This is The {placeholder} Major Diatonics Chords :")
    else:
        print(f"This is The {placeholder} Minor Diatonics Chords :")
    if flat:
        var = [i.replace("#","b") for i in scale]
    else:
        var = scale
    print(f"\nThe Scale notes are: {', '.join(var)}\n")




    for j in scale:

        Title = ""
        chord = []
        newInd = scale.index(j)

        for i in range(notes_number):
            if newInd >= len(scale):
                newInd -= len(scale)
            chord.append(scale[newInd])
            newInd += 2

        

        if (notes[chord[1]] - notes[chord[0]] ) % 12 == 4 and (notes[chord[2]] - notes[chord[1]]) % 12 == 3:
            rom = romanNumbers[num].upper()
            Title = "maj"
        elif (notes[chord[1]] - notes[chord[0]] ) % 12 == 3 and (notes[chord[2]] - notes[chord[1]] ) % 12 == 4:
            rom = romanNumbers[num]
            Title = "min"
        elif (notes[chord[1]] - notes[chord[0]] ) % 12 == 2:
            Title = "Sus2"
        else:
            Title = "Dim"
            rom = romanNumbers[num]+"°"

        chord_number = (len(chord) * 2) - 1

        if len(chord) > 3:
            Title += f"{chord_number}"


        if flat:
            v = [i.replace("#","b") for i in chord]
            print(f'{rom}. {j.replace("#","b")}{Title}  chord: ')
            print(*v)
        else:
            print(f"{rom}. {j}{Title} chord: ")
            print(*chord)


            

        print("---------------")
        idx +=1
        num +=1
    



# chords("F" , "maj" ,flat = False,notes_number=4)




def main():
    # 1. Create the parser
    parser = argparse.ArgumentParser(description="A friendly greeting program")

    # 2. Add an optional or positional argument
    parser.add_argument(
        "--note", 
        type=str, 
        default="C", 
    )
    parser.add_argument(
        "--type", 
        type=str, 
        default="Maj", 
    )
    parser.add_argument(
        "--flat", 
        type=bool, 
        default=False, 
    )
    parser.add_argument(
        "--notes", 
        type=int, 
        default=3, 
    )
    # 3. Parse the arguments
    args = parser.parse_args()

    # 4. Use the parsed argument
    chords(args.note,args.type,flat=args.flat,notes_number=args.notes)


if __name__ == "__main__":
    main()
