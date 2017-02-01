from i3pystatus import Status
status = Status()

status.register("clock",
        format="%Y-%m(%B)-%d(%A) %H:%M:%S",)

status.register("disk",
        path="/mnt/Fat32",
        format="{avail}G",)
status.register("disk",
        path="/mnt/DataBackup",
        format="{avail}G",)
status.register("disk",
        path="/mnt/Data",
        format="{avail}G",)
status.register("disk",
        path="/mnt/Linux",
        format="{avail}G",)
status.register("disk",
        path="/",
        format="DISK {avail}G",)

status.register("gpu_mem",
        divisor=1024,
        format="{percent_used_mem}% {used_mem}/{total_mem}G",)

status.register("gpu_temp",
        format="GPU {temp} °C",
        display_if="1 == 1",)

status.register("disk",
        path="/mnt/RAM_disk",
        format="RAMDISK {avail}G",)

status.register("mem",
        divisor=1024*1024*1024,
        format="MEM {percent_used_mem}% {used_mem}/{total_mem}G",)

status.register("temp",)

status.register("cpu_usage",
        format="CPU {usage_all}%",)

status.register("runwatch",
        name="DHCP",
        path="/var/run/dhclinet*.pid",)

status.register("network",
        interface="enp0s25",
        format_up="{v4cidr} ⏫{bytes_sent}K/{tx_tot_Mbytes}M ⏬{bytes_recv}K/{rx_tot_Mbytes}M",)
status.register("network",
        format_up="{essid} {v4cidr} ⏫{bytes_sent}K/{tx_tot_Mbytes}M ⏬{bytes_recv}K/{rx_tot_Mbytes}M",
        interface="enx7403bd8f0492",)

status.run()

