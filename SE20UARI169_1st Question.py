def fcfs(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time and turnaround time for each process
    for i in range(1, n):
        waiting_time[i] = max(0, turnaround_time[i - 1] + processes[i - 1]['burst_time'] - processes[i]['arrival_time'])
        turnaround_time[i] = waiting_time[i] + processes[i]['burst_time']

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

def sjf(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Sort processes by burst time
    processes.sort(key=lambda x: x['burst_time'])

    # Calculate waiting time and turnaround time for each process
    for i in range(1, n):
        waiting_time[i] = max(0, turnaround_time[i - 1] + processes[i - 1]['burst_time'] - processes[i]['arrival_time'])
        turnaround_time[i] = waiting_time[i] + processes[i]['burst_time']

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

def priority_scheduling(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Sort processes by priority (lower values indicate higher priority)
    processes.sort(key=lambda x: x['priority'])

    # Calculate waiting time and turnaround time for each process
    for i in range(1, n):
        waiting_time[i] = max(0, turnaround_time[i - 1] + processes[i - 1]['burst_time'])
        turnaround_time[i] = waiting_time[i] + processes[i]['burst_time']

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

def round_robin(processes, time_quantum):
    n = len(processes)
    remaining_time = [process['burst_time'] for process in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    time = 0
    queue = []

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                if remaining_time[i] > time_quantum:
                    time += time_quantum
                    remaining_time[i] -= time_quantum
                    queue.append(processes[i])
                else:
                    time += remaining_time[i]
                    waiting_time[i] = time - processes[i]['burst_time']
                    remaining_time[i] = 0
                    turnaround_time[i] = waiting_time[i] + processes[i]['burst_time']
        if done:
            break

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time

def main():
    # Define the processes with arrival time, burst time, and priority
    processes = [
        {'arrival_time': 0, 'burst_time': 24, 'priority': 3},
        {'arrival_time': 4, 'burst_time': 3, 'priority': 1},
        {'arrival_time': 5, 'burst_time': 3, 'priority': 4},
        {'arrival_time': 6, 'burst_time': 12, 'priority': 2},
    ]

    # Calculate and print results for each scheduling algorithm
    avg_waiting_time_fcfs, avg_turnaround_time_fcfs = fcfs(processes)
    avg_waiting_time_sjf, avg_turnaround_time_sjf = sjf(processes)
    avg_waiting_time_ps, avg_turnaround_time_ps = priority_scheduling(processes)
    avg_waiting_time_rr, avg_turnaround_time_rr = round_robin(processes, time_quantum=4)

    print("FCFS Scheduling:")
    print(f"Average Waiting Time: {avg_waiting_time_fcfs}")
    print(f"Average Turnaround Time: {avg_turnaround_time_fcfs}\n")

    print("SJF Scheduling:")
    print(f"Average Waiting Time: {avg_waiting_time_sjf}")
    print(f"Average Turnaround Time: {avg_turnaround_time_sjf}\n")

    print("Priority Scheduling:")
    print(f"Average Waiting Time: {avg_waiting_time_ps}")
    print(f"Average Turnaround Time: {avg_turnaround_time_ps}\n")

    print("Round Robin Scheduling:")
    print(f"Average Waiting Time: {avg_waiting_time_rr}")
    print(f"Average Turnaround Time: {avg_turnaround_time_rr}\n")

if __name__ == "__main__":
    main()
