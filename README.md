# Diatonic-Chords-Identifier
A script that generate all the diatonic chords on a chosen scale

the main function chord() take 4 possible arguments:

chord(

note: This is the note you want the key too, it's a letter from the ionic scale [C,C#,D,D#,E,F,F#,G,G#,A,A#,B]
type: Takes only two possible arguments, "maj", short for Major, and "min", short for Minor, determines the type of your scale.
Flat: A boolean hidden argument, it converts all the Sharps to flat (E.g D# will be Eb)
Number of notes: An integer hidden argument, The number of generated notes is based on this argument (E.g to get a Cmaj7 chord, you'll have to set it to 4)
)
