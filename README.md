# GithubReadmeGenerator

A webApp that builds beautiful readme files for your github profile and repositories.
This app is still in development stage.

## Backend Setup

To set up this project on your local machine, follow these steps:

1. Clone the repository: git clone https://github.com/your-username/GithubReadmeGenerator.git
2. In the server folder Install dependencies using:  `pip install -r requirements.txt`
3. Run the application in the terminal by typing: `python main.py`
4. Then make a post request to: http://localhost:5000/generate_readme, with request body like this: `{
    "username": "Adi-ty",
    "interests": "Web dev, dsa, ml, data science",
    "experiences": "web dev, ml, SDE intenship",
    "email": "chaitanyarai899@gmail.com",
    "social_handles": [
        {
            "handle": "twitter",
            "link": "https://twitter.com/"
        },
        {
            "handle": "linkedin",
            "link": "https://linkedin.com/"
        }
    ],
    "languages": "java,python,tenserflow,pytorch,javascript"
}`

