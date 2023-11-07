from gantt_chart import gantt_chart
def sjf_non_premptive(processes):
    ProcessName = []
    ProcessCompleteTime = []
    ProcessRunTime = []

    CalculationArray = []
    # Sort the processes by arrival time
    processes.sort(key=lambda x: x["Arrival Time"])


    CanReach = processes[0]["Arrival Time"]
    # ProcessCompleteTime.append(processes[0]["Arrival Time"])
    ProcessCompleteTime.append(CanReach)
    # Initialize the current time
    current_time = CanReach
    # Iterate through the sorted processes
    while processes:
        # Filter processes that have already arrived
        arrived_processes = [process for process in processes if process["Arrival Time"] <= current_time]


        # print(arrived_processes)
        if not arrived_processes:
            # If no process has arrived yet, find the next arrival time
            next_arrival_time = min(process["Arrival Time"] for process in processes)
            idle_time = next_arrival_time - current_time

            # Add a single "*" and the idle time to the R array
            ProcessName.append("*")
            ProcessRunTime.append(idle_time)
            # current_time = next_arrival_time
            current_time = current_time+idle_time

            ProcessCompleteTime.append(current_time)
        else:
            # Find the process with the shortest burst time among the arrived processes
            shortest_process = min(arrived_processes, key=lambda x: x["Burst Time"])
            processes.remove(shortest_process)

            Pname = shortest_process["Process"]
            Brust = shortest_process["Burst Time"]

            completion_time = current_time + Brust

            ProcessName.append(Pname)
            ProcessRunTime.append(completion_time - current_time)  # Add the burst time
            current_time = completion_time

            ProcessCompleteTime.append(completion_time)

            
            CalculationData = {
            "ProcessName"       : Pname,
            "CompletionTime"    : completion_time,
            "Arrival Time"      : shortest_process["Arrival Time"],
            "Burst Time"        : shortest_process["Burst Time"]
            }
            CalculationArray.append(CalculationData)
            
    gantt_chart(ProcessRunTime=ProcessRunTime,ProcessName=ProcessName,ProcessCompletedTime=ProcessCompleteTime)
    return CalculationArray,current_time
