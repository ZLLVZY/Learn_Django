# coding:utf-8

def simple_app(environ,start_response):
    """Simplest possible application object"""
    status='200 OK'
    response_headers=[('Content-type','text/plain')]
    start_response(status,response_headers)
    return [b'Hello world! -by the5fire \n']