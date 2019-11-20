### Pgsql数据库的备份还原

---

#### 1. 数据备份

* 进入到数据库的bin目录

```
pg_dump -h localhost -p 5434 -U postgres ydylxm > D:/ydylxm20191120.bak
```

#### 2. 数据还原

* 进入到数据库的bin目录
* 新建数据库名为ydylxm的数据库名称

```
psql -h localhost -p 5434 -U postgres -d ydylxm < D:\ydyl\ydylxm20191120.bak
```

