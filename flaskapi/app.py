from flask import Flask, request
from flask_restx import Resource, Api, reqparse
import werkzeug
import cloudinary
from cloudinary.uploader import upload
import cloudinary.api


# Cloudainerry configuration
cloudinary.config(
    cloud_name =  "dzxyqmygj",
    api_key =  "379288986521871",
    api_secret = "oUwaSB4zZExC7y_qpejm7I6ShwM",
    secure = True
)

parser = reqparse.RequestParser()
app = Flask(__name__)
api = Api(app)

# Request Parser
parser.add_argument('name', type=str, location='form')
parser.add_argument('last_name', type=str, location='form')
parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')



@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/upload')
class Upload(Resource):
    @api.expect(parser, code=201)
    def post(self):
        file_to_upload = request.files['picture']
        data = request.form.to_dict()

        if file_to_upload:
            upload_result = upload(file_to_upload)
            url = upload_result.get("url")
            return {'Successfull': 200,
                    'data':data, 
                    'image':url
                   }
    

if __name__ == '__main__':
    app.run(debug=True)
