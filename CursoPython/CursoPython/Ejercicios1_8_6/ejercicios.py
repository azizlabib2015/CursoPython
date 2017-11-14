agenda_Personal={"9:00":"Quedar con Ana",
                 "11:30":"Reunion con josé",
                 "14:30":"Almorzar con Alba",
                 "19:00":"Ir al taller"}

def imprimeAgenda():
    datos=""
    for i in agenda_Personal:
        datos+=(str(i)+" -> "+str(agenda_Personal[i])+"\n")

    return datos
    
