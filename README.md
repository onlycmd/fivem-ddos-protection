# yapımcı
```cimidi & Papazchavo.```

# Kullanım

> [!IMPORTANT]
> Normal işlem sırasında, normal bir oyuncunun kaç bağlantı kurduğunu belirlemek için ```netstat -ntu|awk '{print $5}'|cut -d: -f1 -s|sort|uniq -c|sort -nk1 -r``` komutunu çalıştırın. connectionTotal değişkenini düzenleyerek bağlantı sayısı eşiğini belirleyin. Bu değişkenden daha fazla bağlantı kuran herhangi bir IP yasaklanacak.
Bu scriptin sürekliliğini sağlamak için Linux komutu olan screen kullanarak çalıştırmanız önerilir.


# Benzer Scriptler için Star & fork atmanız yeterli olacaktır. ^^
