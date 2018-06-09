import orm as orm
from orm import destory_pool
from models import User,Blog, Comment
import asyncio
import sys
import time

loop = asyncio.get_event_loop()


async def test():
    await orm.create_pool(loop=loop, host='localhost', port=3306, user='www-data', password='www-data', db='awesome')
    u1 = Blog(id='1',  name='Test Blog', summary='33', created_at=time.time()-120,user_id=1,user_name='yss',user_image='none',content='ss')
    await  u1.save()
    # await u1.remove()
    r = await Blog.findAll()
    # r = await  User2.remove()
    print(r)

    # 在程序结束之前关闭进程池
    await destory_pool()


loop.run_until_complete(test())
# 关闭loop
loop.close()
if loop.is_closed():
    sys.exit(0)