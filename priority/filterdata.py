def FilterData(name,comple,fulldata):
    ClearData = []
    TotalTimeForThroughPut = 0
    del comple[0]
    DeletIndex = [i for i,v in enumerate(name) if v=="*"]

    DeletIndex.reverse()

    for i in range(len(DeletIndex)):
        del name[DeletIndex[i]]
        del comple[DeletIndex[i]]

    TotalTime = 0
    TotalTimeGating = True
    TotalTimeForThroughPut = comple[-1]
    while (name):
        lastname = name[-1]
        lastvalue = comple[-1]

        if (TotalTimeGating):
            # Store The Full Time Which Help To FInd ThroughPut
            TotalTime = lastvalue
            TotalTimeGating = False

        # Gating Arrival,Brust time From User input Dictonery
        DataArrivalTime = [(i["Arrival Time"],i["Burst Time"]) for i in fulldata if i["Process"]==lastname]
        CalculationForSjfpre = {
            "ProcessName"       : lastname,
            "CompletionTime"    : lastvalue,
            "Arrival Time"      : DataArrivalTime[0][0],
            "Burst Time"        : DataArrivalTime[0][1]
        }
        ClearData.append(CalculationForSjfpre)
        DeletIndex = [i for i,v in enumerate(name) if v == lastname]
        DeletIndex.reverse()

        for i in range(len(DeletIndex)):
            if (i<=len(lastname)):    
                del name[DeletIndex[i]]
                del comple[DeletIndex[i]]
    
    return ClearData,TotalTimeForThroughPut