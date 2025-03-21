from music21 import note, stream, tempo

def tempoFunc(pent):
    temp = tempo.MetronomeMark(number=74)
    pent.append(temp)

# Mano izquierda de la canción
def first_part_left(pent):
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

def second_part_left(pent):
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

def third_part_left(pent):
    sol = note.Note('G2')
    sol.duration.quarterLength = 0.5
    pent.append(sol)

    si = note.Note('B2')
    si.duration.quarterLength = 0.5
    pent.append(si)

    re = note.Note('D3')
    re.duration.quarterLength = 0.5
    pent.append(re)

    fa_sos = note.Note('F#3')
    fa_sos.duration.quarterLength = 0.5
    pent.append(fa_sos)

    la = note.Note('A3')
    la.duration.quarterLength = 0.5
    pent.append(la)

    fa_sos2 = note.Note('F#3')
    fa_sos2.duration.quarterLength = 0.5
    pent.append(fa_sos2)

    re2 = note.Note('D3')
    re2.duration.quarterLength = 0.5
    pent.append(re2)

    si2 = note.Note('B2')
    si2.duration.quarterLength = 0.5
    pent.append(si2)

    sol2 = note.Note('G2')
    sol2.duration.quarterLength = 0.5
    pent.append(sol2)

    si3 = note.Note('B2')
    si3.duration.quarterLength = 0.5
    pent.append(si3)

    re3 = note.Note('D3')
    re3.duration.quarterLength = 0.5
    pent.append(re3)

    fa_sos3 = note.Note('F#3')
    fa_sos3.duration.quarterLength = 0.5
    pent.append(fa_sos3)

    la2 = note.Note('A3')
    la2.duration.quarterLength = 2
    pent.append(la2)

def wet_hands_left(pent):
    for i in range(4):
        first_part_left(pent)
        second_part_left(pent)
    third_part_left(pent)

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

    la = note.Note('A4')
    la.duration.quarterLength = 1
    pent.append(la)

    fa_sos = note.Note('F#4')
    fa_sos.duration.quarterLength = 3
    pent.append(fa_sos)

    mi = note.Note('E4')
    mi.duration.quarterLength = 0.5
    pent.append(mi)

    fa_sos2 = note.Note('F#4')
    fa_sos2.duration.quarterLength = 0.5
    pent.append(fa_sos2)

    sol_sos2 = note.Note('G#4')
    sol_sos2.duration.quarterLength = 3
    pent.append(sol_sos2)

    si = note.Note('B4')
    si.duration.quarterLength = 0.5
    pent.append(si)

    do_sos = note.Note('C#5')
    do_sos.duration.quarterLength = 1
    pent.append(do_sos)

    fa_sos = note.Note('F#4')
    fa_sos.duration.quarterLength = 2
    pent.append(fa_sos)


def third_part_right(pent):
    silencio = note.Rest()
    silencio.duration.quarterLength = 0.5
    pent.append(silencio)

    do_sos2 = note.Note('C#5')
    do_sos2.duration.quarterLength = 0.5
    pent.append(do_sos2)

    mi2 = note.Note('E5')
    mi2.duration.quarterLength = 0.5
    pent.append(mi2)

    sol = note.Note('G5')
    sol.duration.quarterLength = 1.5
    pent.append(sol)

    fa_sos3 = note.Note('F#5')
    fa_sos3.duration.quarterLength = 0.5
    pent.append(fa_sos3)

    re = note.Note('D5')
    re.duration.quarterLength = 1
    pent.append(re)

    la = note.Note('A5')
    la.duration.quarterLength = 0.5
    pent.append(la)

    si = note.Note('B4')
    si.duration.quarterLength = 4.5
    pent.append(si)

def wet_hands_right(pent):
    for i in range(2):
        first_part_right(pent)
    second_part_right(pent)
    third_part_right(pent)

pentagramaIzq = stream.Part()
pentagramaDer = stream.Part()

tempoFunc(pentagramaIzq)
tempoFunc(pentagramaDer)


wet_hands_left(pentagramaIzq)

wet_hands_right(pentagramaDer) 
       

score = stream.Score()
score.append(pentagramaIzq)
score.append(pentagramaDer)

score.show()

#score.write('midi', 'wet_hands.mid')