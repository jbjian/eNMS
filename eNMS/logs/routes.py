from flask import request
from re import search

from eNMS.base.helpers import get, post, serialize
from eNMS.logs import bp
from eNMS.logs.forms import LogAutomationForm


@get(bp, '/log_management', 'View')
def log_management():
    return dict(
        fields=('source_ip', 'content'),
        logs=serialize('Log')
    )


@get(bp, '/log_automation', 'View')
def log_automation():
    return dict(
        log_automation_form=LogAutomationForm(request.form),
        fields=('name', 'source_ip', 'content'),
        log_rules=serialize('LogRule')
    )
