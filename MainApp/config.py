# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-22 02:45:44
# @Last Modified by:   ahmedkammorah
# @Last Modified time: 2018-12-11 12:16:07

import os

# AUTH
AK_API_JWT_SECRET_KEY = ''
AK_JWT_ALGORITHM = 'HS256'

# RPC Service
AK_RPC_URI = ''
TSCORE_USERNAME = ''
TSCORE_PASSWORD = ''

if os.environ.get('AK_APP_ENV') == 'pro':
    print 'Prodction environment'
    # AUTH
    AK_API_JWT_SECRET_KEY = ''
    AK_JWT_ALGORITHM = 'HS256'


elif os.environ.get('AK_APP_ENV') == 'dev':
    print 'development environment'
    # AUTH
    AK_API_JWT_SECRET_KEY = ''
    AK_JWT_ALGORITHM = 'HS256'


