import unittest
from werkzeug.exceptions import NotFound
from app import create_app
import os.path
from shutil import copyfile
from .test_client import TestClient
UPLOAD_DIRECTORY = '/var/hotmaps/cm_files_uploaded'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)
    os.chmod(UPLOAD_DIRECTORY, 0o777)


class TestAPI(unittest.TestCase):


    def setUp(self):
        self.app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
        self.ctx = self.app.app_context()
        self.ctx.push()

        self.client = TestClient(self.app,)

    def tearDown(self):

        self.ctx.pop()





    def test_compute(self):
        raster_file_path = 'tests/data/output_vrt.vrt'

        save_path = UPLOAD_DIRECTORY+"/output_vrt.vrt"
        copyfile(raster_file_path, save_path)
        # register the calculation module a
        payload = {"filename": "output_vrt.vrt",
                   "url_file": "http://127.0.0.1:5001/computation-module/files/output_vrt.vrt",
                   "pix_threshold": 3,"DH_threshold": 30}


        rv, json = self.client.post('computation-module/compute/', data=payload)

        self.assertTrue(rv.status_code == 200)


""" def test_register(self):
      # register the calculation module a
      rv, json = self.client.post('computation-module/register/', data={'name': 'prod1'})

      self.assertTrue(rv.status_code == 200)

      # get list of products"""




