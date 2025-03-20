from music21 import note, stream, tempo

# Mano izquierda de la canción
def tempoFunc(pent):
    temp = tempo.MetronomeMark(number=74)
    pent.append(temp)

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

pentagrama = stream.Stream()

tempoFunc(pentagrama)

for i in range(3):
    wet_hands_left(pentagrama)

pentagrama.show()

pentagrama.write('midi', 'wet_hands.mid')