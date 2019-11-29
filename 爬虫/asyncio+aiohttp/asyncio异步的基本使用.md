#### 1. 创建携程函数

```python
import asyncio

async def fetch():
	print("创建携程函数")
	return 'result'
```

#### 2.创建事件循环

```python
event_loop = asyncio.get_event_loop()
```

#### 3. 注册携程函数到循环事件中

```python
event_loop.run_until_complete(fetch())
```



#### 4. python3.5以后

```
async 关键字替代了 @asyncio.coroutine 这个装饰器, await 替代了 yield from。至此, 协程成为了一种新的语法, 而不再是一种生成器类型。
```

