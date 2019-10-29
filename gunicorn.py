from os import environ

bind = "0.0.0.0:5000"
workers = 1
accesslog = "-"
loglevel = "debug"
capture_output = True
enable_stdio_inheritance = True
timeout = 3000
graceful_timeout = 3000
limit_request_line = 0
