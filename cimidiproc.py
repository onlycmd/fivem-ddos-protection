import os
import time

# Bu kod, bir slowloris DDoS saldırısına karşı koruma sağlar.
# Bağlantıları kontrol etmek için connectionTotal değişkenini düzenleyin.
# Scriptin yeniden çalıştırılması için refreshRate süresini düzenleyin.
# Bu script, UFW arayüzünü kullanarak IP'leri otomatik olarak yasaklar ve güvenlik duvarı kurallarını yeniden yükler.
# Engellenen IP'leri blockedIPs.txt adlı bir metin belgesinde saklar.


connectionTotal = 100
refreshRate = 3

blockedips = []
connums = []
ips = []

while True:
    f = open('blockedIPs.txt','a')
    ns = os.popen("netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r")
    ipl = ns.read()
    l = list(ipl.split())
    for x in range(len(l)):
        if x % 2 == 0:
            connums.append(l[x])
        else:
            ips.append(l[x])
    for x, y in enumerate(connums):
        if int(y) > connectionTotal:
            if ips[x] not in blockedips:
                print('%s IP adresi %d bağlantı ile engelleniyor' % (ips[x], int(y)))
                os.system(str('ufw içine 2 numaralı sıraya %s adresinden gelen bağlantıyı redde' % ips[x]))
                os.system(str('ufw yeniden başlatılıyor.'))
                blockedips.append(ips[x])
                f.write(ips[x] + '\n')   
    f.close()
    time.sleep(refreshRate)