# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2017-01-21 16:58:27
# @Last Modified by:   ahmedkammorah
# @Last Modified time: 2018-12-10 19:00:54
from flask import Flask
from flask import request

from flask import jsonify

from AKAPP import app,auto
from AKAuth import jwt, JWT, jwt_required, current_identity, safe_str_cmp




def _getUserId():
    if current_identity:
        return current_identity['id']
    return None

@app.route('/doc')
def documentation():
    return auto.html()
    # return auto.generate()

@app.route('/protected')
# @jwt_required()
@auto.doc()
def protected():
    print 'protected'
    return '%s' % current_identity

@app.route("/")
@auto.doc()
def helloworld():
    '''Welcome API Test'''
    return "Welcome"

@app.route('/products/<int:prod_id>/likes', methods=['GET','POST', 'DELETE'])
@auto.doc()
@jwt_required()
def productsLikes(prod_id):
    '''Product Liks API Endpoint'''
    app.logger.debug('productsLikes  /products/<prod_id=%d>/likes ',prod_id)
    return app.make_response(('prod_id'+str(prod_id), 200))
        


def _build_out(items, totoal_count, request, limit, offset):
    
    if items != None:
        # here because items already json Serialzed by TSMongoManger
        itemsJson = items #json.loads(json_util.dumps(items))
        count = totoal_count #len(itemsJson)
        
        next_url = None
        prev_url = None

        if count > 0:
            nextOffset = offset + limit
            prevOffset = offset - limit
            next_url = ''+request.url_root+request.path[1:]+'?limit='+str(limit)+'&offset='+str(nextOffset)
            prev_url = ''+request.url_root+request.path[1:]+'?limit='+str(limit)+'&offset='+str(prevOffset)
            if nextOffset >= totoal_count:
                next_url = None

        if count < limit:
            next_url = None

        if offset <= 0:
            prev_url = None


        out = { 'count':count,
                'next':next_url,
                'previous':prev_url,
                'results':itemsJson
               }
        return jsonify(out)
    else:
        app.logger.error('Error in Fetshing items')
        return app.make_response(('Error in Fetshing items', 503))




if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0')