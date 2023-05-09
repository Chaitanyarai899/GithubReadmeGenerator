
def generate_markdown_template(username: str, interests: str, experiences: str, email: str, social_handles, languages: str) -> str:

    language_list = languages.split(",")
    language_badges = ""

    for language in language_list:
        lang_name = language.strip()
        lang_icon = lang_name.lower()
        language_badges += f"![{lang_name}](https://img.shields.io/badge/{lang_name}-{lang_icon}?style=for-the-badge&logo={lang_icon}&logoColor=white)"

    language_badges.replace(" ", "")

    social_links = ""

    for social_handle, link in social_handles:
        social_links += f"[![{social_handle}](https://img.shields.io/badge/{social_handle}-%231DA1F2.svg?logo={social_handle.lower()}&logoColor=white)]({link}) "

    markdown_template = f"""💫 About Me:
- 👋 Hi, I’m @{username}
- 👀 I’m interested in {interests} and many more things.
- 🌱 I’m experienced in {experiences}.
- 💞️ I’m looking to collaborate on open source projects that will boost my skills and help me contribute to the open source ecosystem.
- 📫 Reach me at {email}

## 🌐 Socials:
{social_links}
# 💻 Tech Stack:
{language_badges}
# 📊  Language Stats:
![](https://github-readme-stats.vercel.app/api/top-langs/?username={username}&theme=dark&hide_border=false&include_all_commits=false&count_private=false&layout=compact)
"""
    return markdown_template
