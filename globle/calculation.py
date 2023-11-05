compersion_data = []

def sort_data_for_calculation(CalculatingDataArray,TotalPassedTime,name):
    global AlgoritumName
    AlgoritumName = name
    sorted_data = sorted(CalculatingDataArray, key=lambda x: x["ProcessName"])
    turnaround_time(sorted_data,TotalPassedTime)
    

# Formula : TA = Completion Time - Arrival Time
def turnaround_time(sorted_data,TotalPassedTime):
    global TaAvg

    ForWatingCalculArray = []

    turnaround_time_array = []
    print("turnaround_time :-")
    for i in range(len(sorted_data)):
        turnaround_time = sorted_data[i]["CompletionTime"] - sorted_data[i]["Arrival Time"]
        turnaround_time_array.append(turnaround_time)
        print(f"{sorted_data[i]['ProcessName']} : {turnaround_time}",end="\t"*2)

        #set sorted_data 
        ForWatingCalDic = {"PN" : sorted_data[i]['ProcessName'], "TA" : turnaround_time,"BT" : sorted_data[i]["Burst Time"]}

        ForWatingCalculArray.append(ForWatingCalDic)
    TaAvg = sum(turnaround_time_array)/len(sorted_data)
    print(f"Ta Avg : {TaAvg}")

    wating_time(ForWatingCalculArray,TotalPassedTime)

# Formula : TurnAroundTime - BrustTime 
def wating_time(Data,TotalPassedTime):
    global WtAvg
    global WtAvg
    Da = []
    print("Waiting Time :-")
    for i in range(len(Data)):
        WT = Data[i]["TA"] - Data[i]["BT"]
        Da.append(WT)
        print(f"{Data[i]['PN']} : {WT}",end="\t"*2)
    WtAvg = sum(Da)/len(Data)
    print(f"Wt Avg : {WtAvg}")
    (ThroughPut(TotalPassedTime,len(Data)))


# Formula : Total Completion Time
def ThroughPut(Data,L):
    print(f"Through Put     : {Data}",end="\t\t\t")
    print(f"Through Put Avg : {Data/L}")
    # Data/L
    DataIsStoreForCompersion = {
        "processname"       : AlgoritumName,
        "turnaroundtime"    : TaAvg,
        "watingtime"        : WtAvg,
        "throughput"        : Data/L
    }   
    compersion_data.append(DataIsStoreForCompersion)

def compersion_alg():
    if (len(compersion_data)):
        min_combined_process = min(compersion_data, key=lambda x: (x['turnaroundtime'], x['watingtime'], x['throughput']))
        print(f"The process with the minimum values in all aspects is '{min_combined_process['processname']}' with the following metrics:")
        print(f"Turnaround Time: {min_combined_process['turnaroundtime']}")
        print(f"Wating Time: {min_combined_process['watingtime']}")
        print(f"Throughput: {min_combined_process['throughput']}")
    else:
        return print("Please insert two or more process with timing.")
