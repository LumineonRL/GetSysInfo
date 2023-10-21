import platform
import psutil
import GPUtil

# CPU information
cpu_info = platform.processor()
cpu_count = psutil.cpu_count(logical=False)
cpu_freq = psutil.cpu_freq().current
print(f"CPU: {cpu_info}")
print(f"CPU Cores: {cpu_count}")
print(f"CPU Frequency: {cpu_freq} MHz")

# RAM information
ram_info = psutil.virtual_memory()
ram_total_gb = ram_info.total / (1024**3)
print(f"RAM: {ram_total_gb} GB")

# Virtual Memory information
vm_info = psutil.swap_memory()
vm_total_gb = vm_info.total / (1024**3)
print(f"Virtual Memory: {vm_total_gb} GB")

# GPU information
gpus = GPUtil.getGPUs()
for gpu in gpus:
    gpu_total_mb = gpu.memoryTotal / 1024
    print(f"GPU: {gpu.name}, Memory: {gpu_total_mb} GB")