from WebPages import *
from src.resource import *
import streamlit as st


st.markdown(
    """
    <h1 style='text-align: center; color: #00FF00; text-shadow: 2px 2px #000000;'>Github ReadMe Generator</h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
        """
        <h3 style='text-align: center; color: #FFFFFF;'>Creating ReadMe files just got simpler</h3>
        """,
        unsafe_allow_html=True
    )


def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://w.forfun.com/fetch/4e/4e3afb6cc0061d853637aff488daeea9.jpeg");
            background-attachment: fixed;
            background-size: cover;
        }}
        .stApp:before {{
            content: "";
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            background-color: rgba(0, 0, 0, 0.5);  
            z-index: -1; 
        }}
        </style>
        """,
        unsafe_allow_html=True
    )





class CreatePage:

    title = ''
    subtitle = ''
    work = ''
    badge_theme = ''
    social_media = {}
    skills = []
    supports = {}
    github_username = ''
    github_theme = ''
    banner_type = ''
    banner_height = 0
    banner_width = 0
    banner_theme = 0
    stats_card = False
    trophy = False
    count_badge = False
    top_skills = False
    streak = False
    meme = False
    quote = False
    image_banner = ""
    svgtitle = ""

    def create_page(self):

        add_bg_from_url()

        st.text("Title")
        self.title = st.text_input(label="", value=title_value)
        st.text("Subtitle")
        self.subtitle = st.text_input(label="", value=subtitle_value)
        st.text("About")
        self.work = st.text_area(label="", value=work_area_value, height=300)

        st.text("Theme:")
        badge_theme = st.selectbox("", badge_theme_list)
        self.badge_theme = badge_theme.lower().replace(" ", "-")
        # ---- based on badge_theme: badge preview ---- #
        st.image(badge_them_link_generator(preview_badge_link, self.badge_theme))

        st.text("social")
        social_media_input = st.multiselect("", options=social_media_list)
        self.social_media = {}
        for i in social_media_input:
            st.text(f"{i} profile link")
            self.social_media[i] = st.text_input(label=i)

        st.text("Skills")
        st.text("LANGUAGES")
        languages_input = st.multiselect("", options=languages_list)
        st.text("AI/ML skillset")
        ml_dl_input = st.multiselect("", options=ml_dl_list)
        st.text("FRAMEWORKS, PLATFORMS & LIBRARIES")
        frameworks_input = st.multiselect("", options=frameworks_list)
        st.text("DATABASES")
        databases_input = st.multiselect("", options=databases_list)
        st.text("SERVERS")
        servers_input = st.multiselect("", options=servers_list)
        st.text("DESIGN")
        design_input = st.multiselect("", options=designs_list)
        st.text("OTHER")
        other_input = st.multiselect("", options=other_list)

        self.github_addons()

        st.text("Random meme/quote")
        self.meme = st.checkbox(label="display random meme")
        self.quote = st.checkbox(label="display random quote")
    
        st.text("Support badge")
        support_inputs = st.multiselect("", options=support_list)
        for i in support_inputs:
            st.text(f"{i.replace('-', ' ').capitalize()} profile link")
            self.supports[i] = st.text_input(label=i)

        self.skills = languages_input + frameworks_input + ml_dl_input + databases_input + servers_input + design_input + other_input


    def readme_typo(self):
        st.text("color")
        color = st.color_picker(label="", value="#FF6263")
        st.text("Use ';' for before going to next line")
        typing_text = st.text_area(label="", value="I'm Pygitdev;\nWeb Developer;\nBlogger")
        st.text("Font Size")
        font_size = st.text_input(label="", value="20")
        st.text("Font family(select from google fonts)")
        font_family = st.text_input(label="", value="Edu VIC WA NT Beginner")
        st.text("Duration (ms per line)")
        duration = st.text_input(label="", value="5000")
        self.image_banner = readme_typo_banner(color=color,
                                               text=typing_text,
                                               font=font_family,
                                               font_size=font_size,
                                               duration=duration)

    def github_addons(self):
        st.text("Github User Name")
        self.github_username = st.text_input('')
        if len(self.github_username) == 0:
            st.warning("Please enter the github name to use addons")
        st.text("Github Stats Theme")
        self.github_theme = st.selectbox('', github_stats_theme)
        st.text("Add-ons")
        self.stats_card = st.checkbox(label="display github profile stats card")
        self.trophy = st.checkbox(label="display github trophy")
        self.streak = st.checkbox(label="display github streak stats")
        self.count_badge = st.checkbox(label="display visitors count badge")
        self.top_skills = st.checkbox(label="display top skills")