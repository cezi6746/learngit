import www.orm as orm
import sys
import asyncio
from aiohttp import web
from coroweb import add_static, add_routes
from app import init_jinja2, datetime_filter, logger_factory,response_factory
import logging; logging.basicConfig(level=logging.INFO)
#from handlers import cookie2user, COOKIE_NAME



async def test(loop):
    await orm.create_pool(loop=loop, host='localhost', port=3306, user='root', password='1aA$2bB@', db='awesome')

    app = web.Application(loop=loop, middlewares=[logger_factory, response_factory])
    init_jinja2(app, filters=dict(datetime=datetime_filter))
    add_routes(app, 'handlers')
    add_static(app)
    srv = await  loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    # await orm.destory_pool()
    return srv


loop1 = asyncio.get_event_loop()
loop1.run_until_complete(test(loop1))
loop1.run_forever()






