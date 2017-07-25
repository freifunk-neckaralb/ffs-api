# ffs-api

ffs-api ist eine simple webbasierte API, die das Abfragen von einzelnen Eigenschaften der Nodes erlaubt. Sie ist auf einer Dateisystemebene implementiert, was die Flexibilität und Performance der API deutlich einschränkt. Ein Vorteil der Implementation ist, dass Benutzer\*innen der API kein `JSON` oder `XML` parsen müssen. Dadurch wird die Integration in Shellskripte vereinfacht.

Abfragen funktionieren nach folgendem Prinzip:

*Wichtig:* Die URL wird sich in den nächsten Tagen noch ändern, sobald das Mapping von IPFS auf DNS vollzogen ist. Sie wird dann deutlich schlanker sein, weil dann der lange Hash fehlt.

```sh
$ curl https://ipfs.io/ipns/Qmea9dCZu6iB1yKb6pDYvBDyKuix1gRNpzUK1W3X2cqufK/ffs-api/v0/802aa8695bfe/hostname
ffs-tue-fablab-neckar-alb
```

Die Abfrage ist sehr langsam, allerdings kann sie durch ein paar Kniffe beschleunigt werden. Da es hier um nicht mehr als Dateisystemzugriff geht, gibt es die Möglichkeit, Teile des Verzeichnisses herunterzuladen und lokal darauf zuzugreifen.


## Motivation



