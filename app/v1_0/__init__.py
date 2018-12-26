# -*- coding: utf-8 -*-
from flask import Blueprint

v1_0 = Blueprint('v1_0', __name__, url_prefix='/api')

from . import test, system
