from music21 import note, stream, tempo

def tempoFunc(pent):
    temp = tempo.MetronomeMark(number=74)
    pent.append(temp)

# Mano izquierda de la canción
def first_part(pent):
    la_2 = note.Note('A2')
    la_2.duration.quarterLength = 0.5
    pent.append(la_2)

    do_sos2 = note.Note('C#3')
    do_sos2.duration.quarterLength = 0.5
    pent.append(do_sos2)

    la = note.Note('A3')
    la.duration.quarterLength = 0.5
    pent.append(la)
    
    si = note.Note('B3')
    si.duration.quarterLength = 0.5
    pent.append(si)
    
    do_sos = note.Note('C#')
    do_sos.duration.quarterLength = 0.5
    pent.append(do_sos)
    
    si2 = note.Note('B3')
    si2.duration.quarterLength = 0.5
    pent.append(si2)
    
    la3 = note.Note('A3')
    la3.duration.quarterLength = 0.5
    pent.append(la3)
    
    mi = note.Note('E3')
    mi.duration.quarterLength = 0.5
    pent.append(mi)

def second_part(pent):
    re = note.Note('D3')
    re.duration.quarterLength = 0.5
    pent.append(re)

    fa_sos = note.Note('F#3')
    fa_sos.duration.quarterLength = 0.5
    pent.append(fa_sos)

    do_sos1 = note.Note('C#')
    do_sos1.duration.quarterLength = 0.5
    pent.append(do_sos1)

    mi = note.Note('E')
    mi.duration.quarterLength = 0.5
    pent.append(mi)

    do_sos2 = note.Note('C#')
    do_sos2.duration.quarterLength = 0.5
    pent.append(do_sos2)

    la = note.Note('A3')
    la.duration.quarterLength = 1.5
    pent.append(la)

def wet_hands_left(pent):
    first_part(pent)
    second_part(pent)

# Mano derecha de la cancion
def first_part_right(pent):
    total_duration = (8 * 0.5) + (5 * 0.5) + 1.5
    silencio = note.Rest()
    silencio.duration.quarterLength = total_duration
    pent.append(silencio)

def second_part_right(pent):
    sol_sos = note.Note('G#4')
    sol_sos.duration.quarterLength = 3
    pent.append(sol_sos)

def wet_hands_right(pent):
    for i in range(2):
        first_part_right(pent)
    second_part_right(pent)

pentagramaIzq = stream.Part()
pentagramaDer = stream.Part()

tempoFunc(pentagramaIzq)
tempoFunc(pentagramaDer)

for i in range(2):
    wet_hands_left(pentagramaIzq)

wet_hands_right(pentagramaDer) 
       


score = stream.Score()
score.append(pentagramaIzq)
score.append(pentagramaDer)

score.show()

#score.write('midi', 'wet_hands.mid')