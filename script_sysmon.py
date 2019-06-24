import psutil

cpu = psutil.cpu_times(True)
print("CPU usage: \n", cpu, "\n")

mem = psutil.virtual_memory()  # [0]/2.**30
print("Memory usage: \n", mem, "\n")

disk = psutil.disk_usage('/')
print("Disk usage: \n", disk, "\n")

network = psutil.net_if_stats()
print("Network usage: \n", network, "\n")
