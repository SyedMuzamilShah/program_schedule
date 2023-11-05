from globle.gantt_chart import gantt_chart
def non_premptive_scheduling(processes):
    processes.sort(key=lambda x: x["Arrival Time"])
    FirstArrivalTime = processes[0]["Arrival Time"]
    ProcessName, ProcessRunTime, ProcessCompleteTime = [], [], []

    CalculationArray = []
    current_time = FirstArrivalTime
    ProcessCompleteTime.append(current_time)

    while processes:
        process_reach = [i for i in processes if i["Arrival Time"] <= current_time]
        if not process_reach:
            next_arrival_time = min(i["Arrival Time"] for i in processes)
            idle_time = next_arrival_time - current_time

            Pname = "*"
            Brust = idle_time
            current_time+=Brust

            ProcessName.append(Pname)
            ProcessRunTime.append(Brust)
            ProcessCompleteTime.append(current_time)

        else:
            shortest_process = min(process_reach, key=lambda x: x["Priority"])
            processes.remove(shortest_process)

            Pname = shortest_process["Process"]
            Brust = shortest_process["Burst Time"]
            current_time+=Brust
            ProcessName.append(Pname)
            ProcessRunTime.append(Brust)
            ProcessCompleteTime.append(current_time)

            CalculationData = {
            "ProcessName"       : Pname,
            "CompletionTime"    : current_time,
            "Arrival Time"      : shortest_process["Arrival Time"],
            "Burst Time"        : shortest_process["Burst Time"]
            }
            CalculationArray.append(CalculationData)
    gantt_chart(ProcessRunTime=ProcessRunTime,ProcessName=ProcessName,ProcessCompletedTime=ProcessCompleteTime)
    return CalculationArray,current_time






