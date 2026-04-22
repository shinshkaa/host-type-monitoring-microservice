from prometheus_client import start_http_server, Gauge
import time
import os

host_type = Gauge('host_type','Host type', ['type'])
machine_types = ["vm","container","physical"]

def is_container():
	try:
		env_file = os.environ.get("container")
		containers = ["docker","podman","container"]
		return any(container in env_file for container in containers) | os.path.exists('/.dockerenv')
	except: return False

def is_vm():
    paths = ["/sys/class/dmi/id/product_name",
             "/sys/class/dmi/id/board_vendor",
             "/sys/class/dmi/id/sys_vendor"]
    vm_names = ["parallels", "virtualbox", "vmware", "qemu", "hyper-v"]
    for path in paths:
        try:
            file_content = open(path).read().lower()
            if any(vm_name in file_content for vm_name in vm_names): return True
        except: continue

def detect_host_type():
    if is_container(): return "container"
    if is_vm(): return "vm"
    return "physical"

if __name__ == "__main__":
    start_http_server(8080)
    while True:
        current_type = detect_host_type()
        for _type in machine_types:
            host_type.labels(type=_type).set(1 if _type == current_type else 0)
        time.sleep(5)