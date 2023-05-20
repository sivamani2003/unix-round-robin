import tkinter as tk
from tkinter import messagebox
def schedule_processes():
    num_processes = int(num_processes_entry.get())
    processes = []
    try:
        for i in range(num_processes):
            arrival_time = int(arrival_entries[i].get())
            burst_time = int(burst_entries[i].get())
            processes.append({
                'pid': i + 1,
                'arrival_time': arrival_time,
                'burst_time': burst_time,
                'remaining_time': burst_time,
                'waiting_time': 0,
                'turnaround_time': 0,
                'queue_level': 1
            })
        time_slice_1 = 3
        time_slice_2 = 5
        time = 0
        completed_processes = 0
        current_process = 0
        while completed_processes < num_processes:
            if processes[current_process]['remaining_time'] <= 0:
                completed_processes += 1
                processes[current_process]['turnaround_time'] = time - processes[current_process]['arrival_time']
            elif processes[current_process]['queue_level'] == 1:
                remaining_time = processes[current_process]['remaining_time']
                time_slice = min(remaining_time, time_slice_1)
                processes[current_process]['remaining_time'] -= time_slice
                time += time_slice
            else:
                remaining_time = processes[current_process]['remaining_time']
                time_slice = min(remaining_time, time_slice_2)
                processes[current_process]['remaining_time'] -= time_slice
                time += time_slice
            for i in range(num_processes):
                if i != current_process and processes[i]['arrival_time'] <= time and processes[i]['remaining_time'] > 0:
                    processes[i]['waiting_time'] += time - processes[i]['arrival_time']
            current_process = (current_process + 1) % num_processes
        total_waiting_time = sum(process['waiting_time'] for process in processes)
        total_turnaround_time = sum(process['turnaround_time'] for process in processes)
        avg_waiting_time = total_waiting_time / num_processes
        avg_turnaround_time = total_turnaround_time / num_processes
        result_text.set(f"Average Waiting Time: {avg_waiting_time:.2f}\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter integers for arrival time and burst time.")
root = tk.Tk()
root.title("Process Scheduling")
num_processes_label = tk.Label(root, text="Enter the number of processes:")
num_processes_label.pack()
num_processes_entry = tk.Entry(root)
num_processes_entry.pack()
arrival_entries = []
burst_entries = []
process_details_frame = tk.Frame(root)
process_details_frame.pack()
def create_entry_fields():
    num_processes = int(num_processes_entry.get())
    for i in range(num_processes):
        arrival_label = tk.Label(process_details_frame, text=f"Arrival time for process {i+1}:")
        arrival_label.grid(row=i, column=0, padx=5, pady=5)
        arrival_entry = tk.Entry(process_details_frame)
        arrival_entry.grid(row=i, column=1, padx=5, pady=5)
        arrival_entries.append(arrival_entry)
        burst_label = tk.Label(process_details_frame, text=f"Burst time for process {i+1}:")
        burst_label.grid(row=i, column=2, padx=5, pady=5)
        burst_entry = tk.Entry(process_details_frame)
        burst_entry.grid(row=i, column=3, padx=5, pady=5)
        burst_entries.append(burst_entry)
create_fields_button = tk.Button(root, text="Create Entry Fields", command=create_entry_fields)
create_fields_button.pack()
schedule_button = tk.Button(root, text="Schedule Processes", command=schedule_processes)
schedule_button.pack()
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.pack()
root.mainloop()