#app.py
import falcon
import json

from db_client import *

class ReportResource:

    def on_get(self, req, resp):
        """ HANDLES GET REQUESTS """
        # Return note for particular ID
        if req.get_param("id"):
            result = {'report': r.db(PROJECT_DB).table(PROJECT_TABLE).get(req.get_param("id")).run(db_connection)}
        else:
            report_cursor = r.db(PROJECT_DB).table(PROJECT_TABLE).run(db_connection)
            result = {'reports': [i for i in report_cursor]}
        resp.body = json.dumps(result)

    def on_post(self, req, resp):
        """ HANDLES POST REQUESTS """
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

        try:
            result = json.loads(raw_json, encoding='utf-8')
            sid = r.db(PROJECT_DB).table(PROJECT_TABLE).insert(
                {"reporter_email": result['reporter_email'],
                 "date": result['date'],
                 "coordinates": result['coordinates'],
                 }
            ).run(db_connection)
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON', 'Could not decode request body. The ''JSON was incorrect.')

    def on_delete(self, req, resp):
        """ HANDLES DELETE REQUESTS """
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

        try:
            result = json.loads(raw_json, encoding='utf-8')
            sid = r.db(PROJECT_DB).table(PROJECT_TABLE).filter({"id": result['id']}).delete().run(db_connection)
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON', 'Could not decode request body. The ''JSON was incorrect.')

api = falcon.API()
api.add_route('/reports', ReportResource())