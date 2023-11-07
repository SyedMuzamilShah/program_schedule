import copy
from gantt_chart import gantt_chart
from filterdata import FilterData
def premptive_scheduling(processes):
    ProcessName, RunTimeArray, CompletedTime = [], [], []

    processes.sort(key=lambda x: x["Arrival Time"])
    processes_copy = copy.deepcopy(processes)

    FirstArrivalTime = processes[0]["Arrival Time"]
    FirstProcessName = processes[0]["Process"]
    current_time = FirstArrivalTime


    CompletedTime.append(current_time)
    ProcessName.append(FirstProcessName)

    
    RunTime = 0

    while processes:

        available_processes = [i for i in processes if (i["Burst Time"] > 0 and i["Arrival Time"] <=current_time)]

        if not available_processes:
            Name = "*"
            next_arrival_time = min(i["Arrival Time"] for i in processes if i["Arrival Time"] > current_time)
            idle_time = next_arrival_time-current_time
            ProcessName.append(Name)
            RunTimeArray.append(idle_time)
            CompletedTime.append(current_time)
            current_time +=idle_time
        else:
            shortest_Priority = min(i["Priority"] for i in available_processes)            
            min_priority_processes = [i for i,value in enumerate(processes) if value["Priority"] == shortest_Priority]
            NewName = processes[min_priority_processes[0]]["Process"]
            processes[min_priority_processes[0]]["Burst Time"] -=1
            if (FirstProcessName !=NewName):
                ProcessName.append(NewName)
                CompletedTime.append(current_time)
                RunTimeArray.append(RunTime)


                RunTime = 0
                FirstProcessName = NewName

            if (processes[min_priority_processes[0]]["Burst Time"] == 0):
                del processes[min_priority_processes[0]]

            RunTime+=1
            current_time +=1
    
    CompletedTime.append(current_time)
    RunTimeArray.append(current_time)

    gantt_chart(ProcessName=ProcessName,ProcessRunTime=RunTimeArray,ProcessCompletedTime=CompletedTime)
    # Send The Data For Filteration For Calculation
    Responce = FilterData(name=ProcessName,comple=CompletedTime,fulldata=processes_copy)
    return Responce
