from globle.user_input import get_user_input_for_simple_alg, get_user_input_for_priority
from fcfs.fcfs import fcfs_sorted
from globle.calculation import sort_data_for_calculation, compersion_alg

from priority.premptive import premptive_scheduling
from priority.nonpremptive import non_premptive_scheduling

from sjf.nonpremptive import sjf_non_premptive
from sjf.premptive import sjf_premptive
def main():
    print('''
    1 : First Come First Serive FCFS    2 : SJF-NonPremtive     3 : SRTF    4 : Priority Non-Premtive           
    5 : Priority Premtive               6 : Compersion          7 : Exit
    ''')
    while True:
        option = (input("Select Your Option : "))
        match option:
            case "1":
                print("You select", name:="first come first serive (FCFS)")
                responce = get_user_input_for_simple_alg()
                responce = fcfs_sorted(responce)
                sort_data_for_calculation(responce[0],responce[1],name)
            case "2":
                print("You select", name:="short job first (SJF) non-premptive")
                responce = get_user_input_for_simple_alg()
                responce = sjf_non_premptive(responce)
                sort_data_for_calculation(responce[0],responce[1],name)
            case "3":
                print("You select", name:="short job first (SJF) premptive")
                responce = get_user_input_for_simple_alg()
                responce = sjf_premptive(responce)
                sort_data_for_calculation(responce[0],responce[1],name)
            case "4":
                print("You select", name:="priority non-Premtive")
                responce = get_user_input_for_priority()
                responce = non_premptive_scheduling(responce)
                sort_data_for_calculation(responce[0],responce[1],name)
            case "5":
                print("You select", name:="priority Premtive")
                responce = get_user_input_for_priority()
                responce = premptive_scheduling(responce)
                sort_data_for_calculation(responce[0],responce[1],name)
            case "6":
                compersion_alg()
            case "7":
                break
            case _:
                print("Please Enter Vaild Option")

if __name__ == '__main__':
    main()


# 1. FCFS                       /
# 2. SJF-NonPremtive            /
# 3. SRTF                       /
# 4. Priority Non-Premtive      /
# 5. Priority Premtive          /
# 6. Compare Algorithum         X
# 7. Exit                       /
