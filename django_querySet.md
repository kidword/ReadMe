### 查找

```python
all() 方法来查询所有内容
models.Book.objects.all() 

filter() 方法用于查询符合条件的数据
models.Book.objects.filter(publish='菜鸟出版社', price=300)

exclude() 方法用于查询不符合条件的数据
models.Book.objects.exclude(publish='菜鸟出版社', price=300)

get() 方法用于查询符合条件的返回模型类的对象符合条件的对象只能为一个，如果符合筛选条件的对象超过了一个或者没有一个都会抛出错误
models.Book.objects.get(pk=5)

order_by() 方法用于对查询结果进行排序
models.Book.objects.order_by("price")
models.Book.objects.order_by("-price")  # 降序

reverse() 方法用于对查询结果进行反转
models.Book.objects.order_by("-price").reverse()

count() 方法用于查询数据的数量返回的数据是整数
models.Book.objects.count()
models.Book.objects.filter(price=200).count()

first() 方法返回第一条数据返回的数据是模型类的对象也可以用索引下标 [0]
models.Book.objects.first()

last() 方法返回最后一条数据返回的数据是模型类的对象不能用索引下标 [-1]，ORM 没有逆序索引
models.Book.objects.last()

exists() 方法用于判断查询的结果 QuerySet 列表里是否有数据
models.Book.objects.exists()

values() 方法用于查询部分字段的数据
models.Book.objects.values("pk","price")  # 查询所有的id字段和price字段的数据

values_list() 方法用于查询部分字段的数据
models.Book.objects.values_list("price","publish")

distinct() 方法用于对数据进行去重
对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在
distinct() 一般是联合 values 或者 values_list 使用
models.Book.objects.values_list("publish").distinct()

filter() 方法基于双下划线的模糊查询（exclude 同理）
models.Book.objects.filter(price__in=[200,300])  # 查询价格为200或者300的数据
__gt 大于号 ，= 号后面为数字。
models.Book.objects.filter(price__gt=200)   # 查询价格大于200的数据

__gte 大于等于，= 号后面为数字。
books = models.Book.objects.filter(price__gte=200)

__lt 小于，=号后面为数字
models.Book.objects.filter(price__lt=300)  # 查询价格小于300的数据 

__lte 小于等于，= 号后面为数字
models.Book.objects.filter(price__lte=300)

__range 在 ... 之间，左闭右闭区间，= 号后面为两个元素的列表
models.Book.objects.filter(price__range=[200,300])

__contains 包含，= 号后面为字符串
models.Book.objects.filter(title__contains="菜")

__icontains 不区分大小写的包含，= 号后面为字符串
models.Book.objects.filter(title__icontains="python") # 不区分大小写

__startswith 以指定字符开头，= 号后面为字符串
models.Book.objects.filter(title__startswith="菜")

__endswith 以指定字符结尾，= 号后面为字符串
models.Book.objects.filter(title__endswith="教程")

__year 是 DateField 数据类型的年份，= 号后面为数字
models.Book.objects.filter(pub_date__year=2008) 

```

### 删除

```
delete() 删除
models.Book.objects.filter(pk=8).first().delete()

models.Book.objects.filter(pk__in=[1,2]).delete()

models.Book.objects.delete()  # 报错
models.Book.objects.all().delete()  # 删除成功

```

### 修改

```
模型类的对象.属性 = 更改的属性值
模型类的对象.save()

books = models.Book.objects.filter(pk=7).first() 
books.price = 400 
books.save()

QuerySet 类型数据.update(字段名=更改的数据)
models.Book.objects.filter(pk__in=[7,8]).update(price=888)
```





