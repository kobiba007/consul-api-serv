# system_info.py
import psutil
from flask import jsonify

# checking 5 of the container's resources
def get_system_info():
    try:
        cpus = psutil.cpu_count(logical=True)
        memory_gb = psutil.virtual_memory().total / (1024 ** 3)
        disk_usage = psutil.disk_usage('/')
        disk_total_gb = disk_usage.total / (1024 ** 3)
        disk_used_gb = disk_usage.used / (1024 ** 3)
        net_io = psutil.net_io_counters()
        
        return jsonify({
            "vCpus": cpus,
            "MemoryGB": memory_gb,
            "DiskTotalGB": disk_total_gb,
            "DiskUsedGB": disk_used_gb,
            "traffic_received_KB": net_io.bytes_recv / 1024
        })
    except Exception as e:
        return jsonify({"error": str(e)})
