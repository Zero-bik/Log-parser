import sys
log_file = sys.argv[1] # Получаем имя файла из аргумента треминала
with open(log_file, "r") as f: # Читаем лог и считаем ip
    ip_count = {}
    for log in f:
        ip = log.split()[0]
        ip_count[ip] = ip_count.get(ip, 0) + 1
# Сортируем по количеству на убывание и берём top-10 ip
sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)
for ip, count in sorted_ips[:10]:
    print(ip, count)
