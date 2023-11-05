def gantt_chart(ProcessRunTime,ProcessName,ProcessCompletedTime):
    for i in range(4):
        if((i==0) or (i==2)):
            print(" ",end="")
            for j in range(len(ProcessRunTime)):
                for _ in range(ProcessRunTime[j]):
                    print("--",end="")
                print(" ",end="")
            print()
        elif (i==1):
            print("|",end="")
            for i in range(len(ProcessRunTime)):
                print(ProcessName[i].center(ProcessRunTime[i]*2),end="|")
            print()
        else:
            for i in range(len(ProcessRunTime)):
                print(ProcessCompletedTime[i],end="")
                for _ in range(ProcessRunTime[i]):
                    print(end="  ")
            print(ProcessCompletedTime[i+1])