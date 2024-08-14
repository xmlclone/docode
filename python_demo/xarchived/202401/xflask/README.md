# 说明

1. WSGI[1] is not a server, a python module, a framework, an API or any kind of software. It is just an interface specification by which server and application communicate. Both server and application interface sides are specified in the PEP 3333. If an application (or framework or toolkit) is written to the WSGI spec then it will run on any server written to that spec.

# 参考

1. [wsgi](https://wsgi.readthedocs.io/en/latest/)
1. [wsgi.tutorial](http://wsgi.tutorial.codepoint.net/intro)
2. [pep-333](https://peps.python.org/pep-3333/)
3. [werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/)
4. [FLask之Local、LocalStack和LocalProxy介绍](https://blog.csdn.net/weixin_45950544/article/details/103923191)

# 易混淆概念

1. wsgi: web service gateway interface, 其核心是interface，类似于一个协议，让服务器和应用程序在这个协议规范内进行开发。
2. uwsgi: 是一个web服务器，常见的还有Gunicorn,mod_wsgi等。参考: [servers](https://wsgi.readthedocs.io/en/latest/servers.html)
3. Werkzeug: 这个被wsgi定义为了libraries/middleware，参考: [libraries](https://wsgi.readthedocs.io/en/latest/libraries.html)，werkzeun官方介绍为: 

> Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility libraries

参考: [werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/)

4. flask/django: 是web开发框架，类似spring. 参考: [frameworks](https://wsgi.readthedocs.io/en/latest/frameworks.html)

> 服务器就是运行我们代码的，比如tomcat运行java。注意nginx无法直接运行java或python代码。运行python代码的服务器有uwsgi,gunicorn等。然后代码和服务器需要遵守一定的规范或者协议，就是wsgi。类似于java里面的jsp,servlet

5. 类似cookie/session等并不是http协议的内容，因为http本身是无状态的，所以wsgi也没有对cookie进行规定。wsgi提供了中间件来处理，比如[Beaker](https://wsgi.readthedocs.io/en/latest/libraries.html)，而werkzeug这个库就提供了这些功能