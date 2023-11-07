from gantt_chart import gantt_chart
def fcfs_sorted(processes):
    sorted_processes  = sorted(processes, key=lambda y: y["Arrival Time"])
    Name, Run, Completion, calculation_array  = [], [], [], []

    FirstArrivalTime = sorted_processes [0]["Arrival Time"]
    Completion.append(FirstArrivalTime)
    j = 0
    for i in range(len(sorted_processes)):
        
        if ((a:=sorted_processes [i]["Arrival Time"]) > (b:=Completion[i+j])):
            Name.append("*")
            Run.append(total := (a-b))
            Completion.append(Completion[i+j]+(total))
            j += 1
        if (sorted_processes[i]["Arrival Time"] <= (v:=Completion[i+j])):
            Name.append(sorted_processes [i]["Process"])
            Run.append(sorted_processes [i]["Burst Time"])
            FirstArrivalTime = v + sorted_processes [i]["Burst Time"]
            Completion.append(FirstArrivalTime)
            CalData = {
                "ProcessName" : sorted_processes [i]["Process"],
                "CompletionTime" : FirstArrivalTime,
                "Arrival Time" : sorted_processes [i]["Arrival Time"],
                "Burst Time" : sorted_processes [i]["Burst Time"]  
            }
            calculation_array.append(CalData)

    gantt_chart(ProcessName=Name,ProcessCompletedTime=Completion,ProcessRunTime=Run)

    return calculation_array ,(Completion[-1])
