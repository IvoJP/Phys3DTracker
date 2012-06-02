def patternrec(events,event_num,adc_tol):
    
    goodevents = []
    for i in range(len(events[event_num])):
        if events[event_num][i].wgt > adc_tol:
            goodevents.append(events[event_num][i])
    return goodevents
        
