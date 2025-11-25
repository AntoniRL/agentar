import threading
import time
import psutil
import os
import csv

class ResourceMonitor(threading.Thread):
    def __init__(self, time_interval=1, system=None):
        super().__init__()
        self.system = system
        self.time_interval = time_interval  # seconds
        self.cpu_usage = []
        self.cpu_usage_total = []
        self.memory_usage = []
        self.memory_percent = []
        self.time_cpu = []
        self.time_wall = []
        self.process = psutil.Process(os.getpid())
        self.logical_cores = psutil.cpu_count(logical=True)
        self.total_memory = psutil.virtual_memory().total / (1024 ** 2)  # MB

        self.num_of_agents = []

    def run(self):
        self.start_cpu_time = time.process_time()
        self.start_wall_time = time.time()
        while not self.system.terminated.is_set():
            cpu_raw = self.process.cpu_percent(interval=3.0)
            cpu_total = cpu_raw / self.logical_cores
            mem_used = self.process.memory_info().rss / (1024 ** 2)  # MB
            mem_percent = (mem_used / self.total_memory) * 100

            self.cpu_usage.append(cpu_raw)
            self.cpu_usage_total.append(cpu_total)
            self.memory_usage.append(mem_used)
            self.memory_percent.append(mem_percent)
            self.time_cpu.append(time.process_time()-self.start_cpu_time)
            self.time_wall.append(time.time()-self.start_wall_time)
            self.num_of_agents.append(len(self.system.threads))

            # print(f"CPU: {self.cpu_usage_total[-1]:.5f}% | RAM: {self.memory_percent[-1]:.5f}% | Time: {self.time[-1]:.2f}s")
            # time.sleep(self.time_interval)
        
        self.save_data("logs/resource_usage.csv")


    def save_data(self, file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Time wall(s)", "Time cpu(s)", "CPU(%)", "RAM(MB)", "RAM(%)", "agents"])
            for tw, tc, cpu, mem, memp, agents in zip(self.time_wall, self.time_cpu, self.cpu_usage_total, self.memory_usage, self.memory_percent, self.num_of_agents):
                writer.writerow([f"{tw:.2f}", f"{tc:.2f}", f"{cpu:.5f}", f"{mem:.5f}", f"{memp:.5f}", agents])
    
