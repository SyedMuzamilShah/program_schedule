def get_user_input_for_simple_alg():
    process_list = []
    num_processes = int(input("Enter the number of processes: "))
    
    for i in range(1, num_processes + 1):
        process = {
            "Process": f"P{i}",
            "Arrival Time": int(input(f"Enter Arrival Time for P{i}: ")),
            "Burst Time": int(input(f"Enter Burst Time for P{i}: "))
        }
        process_list.append(process)
    return process_list

def get_user_input_for_priority():
    process_list = []
    num_processes = int(input("Enter the number of processes: "))
    
    for i in range(1, num_processes + 1):
        process = {
            "Process": f"P{i}",
            "Arrival Time": int(input(f"Enter Arrival Time for P{i}: ")),
            "Burst Time": int(input(f"Enter Burst Time for P{i}: ")),
            "Priority": int(input(f"Enter Priority for P{i}: ")),
        }
        process_list.append(process)
    return process_list
