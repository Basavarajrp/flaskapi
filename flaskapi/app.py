from flask import Flask, request
from flask_restx import Resource, Api, fields, reqparse
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
parser.add_argument('picture1', type=werkzeug.datastructures.FileStorage, location='files')
parser.add_argument('picture2', type=werkzeug.datastructures.FileStorage, location='files')
parser.add_argument('picture3', type=werkzeug.datastructures.FileStorage, location='files')





@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/upload')
class Upload(Resource):
    @api.expect(parser, code=201)
    def post(self):
        try:
            file_to_upload1 = request.files['picture1']
            file_to_upload2 = request.files['picture2']
            file_to_upload3 = request.files['picture3']

            data = request.form.to_dict()

            if file_to_upload1:
                upload_result1 = upload(file_to_upload1)
                upload_result2 = upload(file_to_upload2)
                upload_result3 = upload(file_to_upload3)

                url1 = upload_result1.get("url")
                url2 = upload_result2.get("url")
                url3 = upload_result3.get("url")

                return {'Successfull': 200,
                        'data':data, 
                        'image1':url1,
                        'image2':url2,
                        'image3':url3,
                        'file_to_upload1':file_to_upload1,
                        'file_to_upload2':file_to_upload2,
                        
                    }
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app.run(debug=True)
