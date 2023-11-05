from globle.gantt_chart import gantt_chart
def sjf_premptive(processes):
    ProcessName = []
    ProcessCompleteTime = []
    RunTime = []

    I = 0
    processes.sort(key=lambda x: x["Arrival Time"])
    remaining_burst_time = [process["Burst Time"] for process in processes]
    oldname = processes[0]["Process"]

    FirstArrivalTime = processes[0]["Arrival Time"]
    current_time = FirstArrivalTime
    ProcessCompleteTime.append(FirstArrivalTime)
    ProcessName.append(processes[0]["Process"])

    while any(remaining_burst_time):
        available_processes = [i for i, time in enumerate(remaining_burst_time) if time > 0 and processes[i]["Arrival Time"] <= current_time]

        if not available_processes:
            next_arrival_time = min(process["Arrival Time"] for process in processes if process["Arrival Time"] > current_time)
            idle_time = next_arrival_time - current_time

            # Add a single "*" and the idle time to the Demo Data arrays
            ProcessName.append("*")
            ProcessCompleteTime.append(current_time)
            # RunTime.append(Run)
            RunTime.append(ProcessCompleteTime[I+1]-ProcessCompleteTime[I])
            I+=1
            # current_time = next_arrival_time
            current_time = current_time+idle_time

        else:
            # Find the process with the shortest remaining burst time among the available processes
            shortest_process = min(available_processes, key=lambda i: remaining_burst_time[i])
            Pname = processes[shortest_process]["Process"]

            if oldname != Pname:
                oldname = Pname
                ProcessName.append(oldname)
                ProcessCompleteTime.append(current_time)
                RunTime.append(ProcessCompleteTime[I+1]-ProcessCompleteTime[I])
                I+=1

            # Run for one unit of burst time for the selected process
            remaining_burst_time[shortest_process] -= 1
            current_time += 1

    ProcessCompleteTime.append(current_time)
    RunTime.append(ProcessCompleteTime[I+1]-ProcessCompleteTime[I])

    # Generate the Gantt chart
    gantt_chart(ProcessCompletedTime=ProcessCompleteTime, ProcessRunTime=RunTime, ProcessName=ProcessName)
    return Filter(name=ProcessName,comple=ProcessCompleteTime,fulldata=processes)

def Filter(name,comple,fulldata):
    del comple[0]
    DeletIndex = [i for i,v in enumerate(name) if v=="*"]
    DeletIndex.reverse()

    for i in range(len(DeletIndex)):
        del name[DeletIndex[i]]
        del comple[DeletIndex[i]]

    data = []
    TotalTime = 0
    TotalTimeGating = True

    while (name):
        lastname = name[-1]
        lastvalue = comple[-1]

        if (TotalTimeGating):
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
        data.append(CalculationForSjfpre)
        DeletIndex = [i for i,v in enumerate(name) if v == lastname]
        DeletIndex.reverse()

        for i in range(len(DeletIndex)):
            if (i<=len(lastname)):    
                del name[DeletIndex[i]]
                del comple[DeletIndex[i]]

    return (data,TotalTime)