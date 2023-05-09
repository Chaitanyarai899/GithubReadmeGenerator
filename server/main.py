from flask import Flask, request, send_file
from flask_restful import Api, Resource
from typing import List
from helper import generate_markdown_template

app = Flask(__name__)
api = Api(app)

class GitHubAPI(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        interests = data["interests"]
        experiences = data["experiences"]
        email = data["email"]
        social_handles = data["social_handles"]
        languages = data["languages"]
        
        markdown_template = generate_markdown_template(username, interests, experiences, email, social_handles, languages)
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(markdown_template)

        return send_file('README.md', mimetype='text/markdown')

api.add_resource(GitHubAPI, "/generate_readme")

if __name__ == "__main__":
    app.run(debug=True)
