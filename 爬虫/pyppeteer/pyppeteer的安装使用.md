#### 1.pyppeteer的安装

```python
# 下载chrom包地址
linux: https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/575458/chrome-linux.zip'

mac: 'https://storage.googleapis.com/chromium-browser-snapshots/Mac/575458/chrome-mac.zip'

win32: 'https://storage.googleapis.com/chromium-browser-snapshots/Win/575458/chrome-win32.zip'

win64: 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/575458/chrome-win32.zip'
    
pip install pyppeteer

# 在C:\Users\xbc\AppData\Local\pyppeteer中创建如下文件夹
pyppeteer\local-chromium\575458
# 将文件chrome-win32放到下面，最后执行测试代码


import asyncio
from pyppeteer import launch


async def main():
    await launch(headlees=False)
    print('休眠')
    await asyncio.sleep(10)

asyncio.get_event_loop().run_until_complete(main())
```

#### 2. pyppeteer配置项

```python
import asyncio
from pyppeteer import launch


async def main():
    width, height = 1366, 768
    # headless=False 浏览器显示
    # args=['-disable-infobars'] 请用提示
    # devtools = True 开启浏览中的控制台
    # userDataDir='./userdata' 设置用户的
    browser = await launch(headless=False, args=['-disable-infobars'], devtools=True)
    # browser.createIncogniteBrowserContext() 开启无痕浏览模式
    content = await browser.createIncogniteBrowserContext()
    # browser.newPage() 新建一个tab页面
    page = await content.newPage()
    # 配置浏览器分辨率
    await page.setViewport({'width': width, 'height': height})
    # 配置网站监测是否启动webdriver
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    await page.goto('https://antispider1.scrape.cuiqingcai.com/')
    await asyncio.sleep(20)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
```

#### 3.pyppeteer 常用的方法

```python
import asyncio
from pyppeteer import launch


async def main():
    width, height = 1366, 768
    browser = await launch(headless=False, args=['-disable-infobars'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    await page.goto('https://www.taobao.com')
    # 等待页面加载元素 可以有很多等待条件：waitForXpath  waitForFunction
    # await page.waitForSelector('.item .name')
    # 输入内容
    await page.type('#q', 'ipad')
    # 获取页面html
    html = await page.content()
    # 获取页面cookie
    html = await page.cookies()
    print(html)
    # 点击操作
    # await page.click('.item .name', options={
    #     'button': 'right',  # 鼠标的按键
    #     'clickCount': 1,  # 1 or 2
    #     'delay': 3000,  # 毫秒
    # })
    await asyncio.sleep(10)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
```

#### 4.pyppeteer 案例

```python
import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError

INDEX_URL = 'https://dynamic2.scrape.cuiqingcai.com/page/{page}'
TIMEOUT = 10
TOTAL_PAGE = 10
WINDOW_WIDTH, WINDOW_HEIGHT = 1330, 768
browser, tab = None, None


# 设置请求
async def scrape_page(url, selector):
    try:
        await tab.goto(url)
        await tab.waitForSelector(selector, options={
            'timeout': TIMEOUT * 1000
        })
    except TimeoutError:
        print('timeout')


# 初始化配置
async def init():
    global browser, tab
    browser = await launch(headless=False,
                           args=['--disable-infobars', f'--windows-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'])
    tab = await browser.newPage()
    await tab.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})


async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, '.item .name')


# 解析页面
async def parse_index():
    return await tab.querySelectorAllEval('.item .name', 'nodes => nodes.map(node => node.href)')


# 详情页方法
async def scrape_detail(url):
    await scrape_page(url, 'h2')


# 详情页面解析
async def parse_detail():
    url = tab.url
    name = await tab.querySelectorEval('h2', 'node => node.innerText')
    categories = await tab.querySelectorAllEval('.categories button span', 'nodes => nodes.map(node => node.innerText)')
    cover = await tab.querySelectorEval('.cover', 'node => node.src')
    score = await tab.querySelectorEval('.score', 'node => node.innerText')
    drama = await tab.querySelectorEval('.drama p', 'node => node.innerText')
    return {
        'url': url,
        "name": name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            for detail_url in detail_urls:
                await scrape_detail(detail_url)
                detaol_data = await parse_detail()
                print(detaol_data)
            print(detail_urls)
    finally:
        await browser.close()


asyncio.get_event_loop().run_until_complete(main())


# 碰到错误的时候找打pyppeteer包下的connection.py文件,修改为:
self._ws = websockets.client.connect(
            self._url, max_size=None, loop=self._loop, ping_interval=None, ping_timeout=None)
```



