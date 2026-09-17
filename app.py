import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Skill-to-Job Matching",
    page_icon="💼",
    layout="wide"
)

# =========================================================
# JOB DATASET
# =========================================================
jobs_data = [
    ["J001", "Data Entry Operator", "ABC Services", "Chennai", "12th",
     "Typing|MS Excel|Computer Basics", 15000],

    ["J002", "Office Assistant", "Local Enterprises", "Kanchipuram", "12th",
     "MS Excel|Communication|Computer Basics", 16000],

    ["J003", "Sales Executive", "Retail Solutions", "Chennai", "12th",
     "Communication|Sales|Customer Service", 18000],

    ["J004", "Computer Operator", "Digital Services", "Chengalpattu", "Diploma",
     "Typing|MS Office|Computer Basics", 17000],

    ["J005", "Junior Data Analyst", "Data Solutions", "Chennai", "Degree",
     "Python|Excel|SQL|Data Analysis", 25000],

    ["J006", "Customer Support Executive", "Support Hub", "Coimbatore", "12th",
     "Communication|English|Customer Service", 18000],

    ["J007", "Accounts Assistant", "Finance Point", "Erode", "Degree",
     "Tally|Excel|Accounting", 22000],

    ["J008", "Graphic Design Assistant", "Creative Works", "Chennai", "Diploma",
     "Canva|Graphic Design|Communication", 20000],

    ["J009", "Field Sales Associate", "Rural Connect", "Chengalpattu", "12th",
     "Communication|Sales|Driving", 17000],

    ["J010", "IT Support Assistant", "Tech Care", "Coimbatore", "Diploma",
     "Computer Basics|Networking|Troubleshooting", 20000],

    ["J011", "Digital Marketing Assistant", "Digital Hub", "Madurai", "Degree",
     "Social Media|Canva|Communication", 22000],

    ["J012", "Warehouse Assistant", "Logistics Hub", "Tiruppur", "10th",
     "Communication|Inventory|Computer Basics", 16000],

    ["J013", "Office Coordinator", "Smart Office", "Salem", "12th",
     "MS Excel|Communication|Computer Basics", 18000],

    ["J014", "Junior Web Assistant", "Web Solutions", "Coimbatore", "Diploma",
     "HTML|CSS|Computer Basics", 20000],

    ["J015", "Customer Care Assistant", "Service Point", "Trichy", "12th",
     "Communication|English|Customer Service", 17500],

    ["J016", "Data Processing Assistant", "DataWorks", "Vellore", "12th",
     "Typing|Excel|Computer Basics", 16500],

    ["J017", "Accounts Executive", "Account Solutions", "Tirunelveli", "Degree",
     "Tally|Excel|Accounting", 23000],

    ["J018", "Social Media Assistant", "Media Hub", "Coimbatore", "Degree",
     "Social Media|Canva|Communication", 21000],

    ["J019", "Inventory Assistant", "Logistics Point", "Salem", "12th",
     "Inventory|Excel|Computer Basics", 17000],

    ["J020", "Technical Support Trainee", "Tech Solutions", "Erode", "Diploma",
     "Computer Basics|Networking|Troubleshooting", 21000],
]

df = pd.DataFrame(
    jobs_data,
    columns=[
        "Job ID",
        "Job Title",
        "Company",
        "Location",
        "Education",
        "Skills",
        "Salary"
    ]
)

# =========================================================
# LOCATIONS
# =========================================================
locations = [
    "Chennai",
    "Chengalpattu",
    "Kanchipuram",
    "Coimbatore",
    "Tiruppur",
    "Erode",
    "Salem",
    "Madurai",
    "Trichy",
    "Vellore",
    "Tirunelveli"
]

# =========================================================
# EDUCATION LEVEL
# =========================================================
education_level = {
    "10th": 1,
    "12th": 2,
    "Diploma": 3,
    "Degree": 4
}

# =========================================================
# LANGUAGE
# =========================================================
if "language" not in st.session_state:
    st.session_state.language = "English"

# Language selector FIRST
st.sidebar.markdown("### 🌐 Language")

language = st.sidebar.selectbox(
    "Choose Language / மொழியை தேர்வு செய்யவும்",
    ["English", "தமிழ்"],
    index=0 if st.session_state.language == "English" else 1
)

st.session_state.language = language

is_tamil = language == "தமிழ்"

# =========================================================
# TRANSLATION FUNCTION
# =========================================================
def tr(english, tamil):
    return tamil if is_tamil else english


# =========================================================
# SESSION STATE
# =========================================================
defaults = {
    "name": "",
    "education": "12th",
    "location": "Chennai",
    "experience": "Fresher",
    "skills": [],
    "assessment_score": 0,
    "assessment_done": False,
    "saved_jobs": [],
    "resume_created": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================
st.sidebar.markdown("---")
st.sidebar.title(
    tr("💼 Career App", "💼 வேலைவாய்ப்பு செயலி")
)

page_options = [
    tr("🏠 Home", "🏠 முகப்பு"),
    tr("👤 My Profile", "👤 எனது சுயவிவரம்"),
    tr("📝 Skill Assessment", "📝 திறன் மதிப்பீடு"),
    tr("💼 Job Matching", "💼 வேலை பொருத்தம்"),
    tr("🔎 Job Filters", "🔎 வேலை வடிகட்டி"),
    tr("📚 Skill Gap & Learning", "📚 திறன் இடைவெளி & கற்றல்"),
    tr("🧭 Career Path", "🧭 தொழில் பாதை"),
    tr("❤️ Saved Jobs", "❤️ சேமித்த வேலைகள்"),
    tr("📄 Resume Generator", "📄 Resume உருவாக்கி"),
    tr("📈 Progress Tracker", "📈 முன்னேற்ற கண்காணிப்பு"),
    tr("📊 Dashboard", "📊 Dashboard")
]

page = st.sidebar.radio(
    tr("Navigation", "பக்கங்கள்"),
    page_options
)

# =========================================================
# COMMON TITLE
# =========================================================
st.title(
    tr(
        "🎯 Skill-to-Job Matching for Rural Youth",
        "🎯 கிராமப்புற இளைஞர்களுக்கான திறன் - வேலை பொருத்தம்"
    )
)

st.caption(
    tr(
        "Find suitable jobs based on your education, skills and location.",
        "உங்கள் கல்வி, திறன்கள் மற்றும் இருப்பிடத்தின் அடிப்படையில் பொருத்தமான வேலைகளை கண்டறியுங்கள்."
    )
)

# =========================================================
# MATCHING FUNCTION
# =========================================================
def calculate_job_match(job):

    user_skills = set(st.session_state.skills)

    required_skills = set(
        skill.strip()
        for skill in job["Skills"].split("|")
    )

    matched = user_skills.intersection(required_skills)
    missing = required_skills - user_skills

    if len(required_skills) > 0:
        skill_score = (
            len(matched) / len(required_skills)
        ) * 70
    else:
        skill_score = 0

    user_edu = education_level.get(
        st.session_state.education,
        2
    )

    job_edu = education_level.get(
        job["Education"],
        2
    )

    education_score = (
        15 if user_edu >= job_edu else 5
    )

    location_score = (
        15
        if st.session_state.location == job["Location"]
        else 5
    )

    total = min(
        round(
            skill_score +
            education_score +
            location_score
        ),
        100
    )

    return total, matched, missing


# =========================================================
# HOME
# =========================================================
if page == tr("🏠 Home", "🏠 முகப்பு"):

    st.subheader(
        tr("Welcome 👋", "வரவேற்கிறோம் 👋")
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            tr("💼 Available Jobs", "💼 கிடைக்கும் வேலைகள்"),
            len(df)
        )

    with col2:
        st.metric(
            tr("🏢 Companies", "🏢 நிறுவனங்கள்"),
            df["Company"].nunique()
        )

    with col3:
        st.metric(
            tr("📍 Locations", "📍 இடங்கள்"),
            df["Location"].nunique()
        )

    st.markdown("---")

    st.subheader(
        tr(
            "How this application works",
            "இந்த செயலி எப்படி செயல்படுகிறது"
        )
    )

    steps = [
        tr("1. 👤 Create your profile",
           "1. 👤 உங்கள் சுயவிவரத்தை உருவாக்கவும்"),

        tr("2. 📝 Take the skill assessment",
           "2. 📝 திறன் மதிப்பீட்டை முடிக்கவும்"),

        tr("3. 💼 Find matching jobs",
           "3. 💼 பொருத்தமான வேலைகளை கண்டறியவும்"),

        tr("4. 📚 Identify missing skills",
           "4. 📚 இல்லாத திறன்களை கண்டறியவும்"),

        tr("5. 🧭 Explore career paths",
           "5. 🧭 தொழில் பாதைகளை பார்க்கவும்"),

        tr("6. 📄 Generate your resume",
           "6. 📄 உங்கள் Resume-ஐ உருவாக்கவும்"),

        tr("7. 📈 Track your progress",
           "7. 📈 உங்கள் முன்னேற்றத்தை கண்காணிக்கவும்")
    ]

    for step in steps:
        st.write(step)

# =========================================================
# PROFILE
# =========================================================
elif page == tr("👤 My Profile", "👤 எனது சுயவிவரம்"):

    st.subheader(
        tr("👤 My Profile", "👤 எனது சுயவிவரம்")
    )

    name = st.text_input(
        tr("Name", "பெயர்"),
        value=st.session_state.name
    )

    edu_options = ["10th", "12th", "Diploma", "Degree"]

    education = st.selectbox(
        tr("Education", "கல்வி"),
        edu_options,
        index=edu_options.index(
            st.session_state.education
        )
    )

    location = st.selectbox(
        tr("Preferred Location", "விரும்பிய வேலை இடம்"),
        locations,
        index=locations.index(
            st.session_state.location
        )
    )

    experience_options = [
        "Fresher",
        "Less than 1 year",
        "1–3 years",
        "3+ years"
    ]

    experience = st.selectbox(
        tr("Experience", "அனுபவம்"),
        experience_options
    )

    all_skills = sorted(set(
        skill.strip()
        for skills in df["Skills"]
        for skill in skills.split("|")
    ))

    skills = st.multiselect(
        tr("Your Skills", "உங்கள் திறன்கள்"),
        all_skills,
        default=st.session_state.skills
    )

    if st.button(
        tr("💾 Save Profile", "💾 சுயவிவரத்தை சேமிக்கவும்")
    ):

        st.session_state.name = name
        st.session_state.education = education
        st.session_state.location = location
        st.session_state.experience = experience
        st.session_state.skills = skills

        st.success(
            tr(
                "Profile saved successfully! ✅",
                "சுயவிவரம் வெற்றிகரமாக சேமிக்கப்பட்டது! ✅"
            )
        )

    st.markdown("---")

    st.subheader(
        tr("Current Profile", "தற்போதைய சுயவிவரம்")
    )

    st.write(
        f"**{tr('Name', 'பெயர்')}:** "
        f"{st.session_state.name or tr('Not added', 'சேர்க்கப்படவில்லை')}"
    )

    st.write(
        f"**{tr('Education', 'கல்வி')}:** "
        f"{st.session_state.education}"
    )

    st.write(
        f"**{tr('Location', 'இடம்')}:** "
        f"{st.session_state.location}"
    )

    st.write(
        f"**{tr('Experience', 'அனுபவம்')}:** "
        f"{st.session_state.experience}"
    )

    st.write(
        f"**{tr('Skills', 'திறன்கள்')}:** "
        f"{', '.join(st.session_state.skills) if st.session_state.skills else tr('Not added', 'சேர்க்கப்படவில்லை')}"
    )

# =========================================================
# SKILL ASSESSMENT
# =========================================================
elif page == tr(
    "📝 Skill Assessment",
    "📝 திறன் மதிப்பீடு"
):

    st.subheader(
        tr(
            "📝 Job Readiness Assessment",
            "📝 வேலைக்கான தயார்நிலை மதிப்பீடு"
        )
    )

    questions = [

        (
            tr(
                "Q1. You find duplicate entries in Excel. What will you do?",
                "Q1. Excel-ல் duplicate entries இருந்தால் என்ன செய்வீர்கள்?"
            ),
            [
                tr("Delete the entire file", "முழு file-ஐ delete செய்வேன்"),
                tr("Check and identify duplicates", "Duplicates-ஐ சரிபார்த்து கண்டறிவேன்"),
                tr("Ignore them", "அதை ignore செய்வேன்"),
                tr("Close Excel", "Excel-ஐ close செய்வேன்")
            ],
            tr(
                "Check and identify duplicates",
                "Duplicates-ஐ சரிபார்த்து கண்டறிவேன்"
            )
        ),

        (
            tr(
                "Q2. An angry customer contacts you. What should you do?",
                "Q2. கோபமாக இருக்கும் customer ஒருவர் தொடர்பு கொண்டால் என்ன செய்வீர்கள்?"
            ),
            [
                tr("Argue with the customer", "Customer-உடன் வாதம் செய்வேன்"),
                tr("Disconnect the call", "Call-ஐ துண்டிப்பேன்"),
                tr("Listen and respond politely", "கவனமாக கேட்டு மரியாதையாக பதிலளிப்பேன்"),
                tr("Ignore the customer", "Customer-ஐ ignore செய்வேன்")
            ],
            tr(
                "Listen and respond politely",
                "கவனமாக கேட்டு மரியாதையாக பதிலளிப்பேன்"
            )
        ),

        (
            tr(
                "Q3. You don't know a software required for your job. What will you do?",
                "Q3. வேலைக்கு தேவையான software உங்களுக்கு தெரியவில்லை என்றால் என்ன செய்வீர்கள்?"
            ),
            [
                tr("Refuse to learn", "கற்றுக்கொள்ள மறுப்பேன்"),
                tr("Ask for guidance and learn it", "வழிகாட்டுதல் கேட்டு கற்றுக்கொள்வேன்"),
                tr("Leave the job", "வேலையை விட்டுவிடுவேன்"),
                tr("Ignore the requirement", "அந்த தேவையை ignore செய்வேன்")
            ],
            tr(
                "Ask for guidance and learn it",
                "வழிகாட்டுதல் கேட்டு கற்றுக்கொள்வேன்"
            )
        ),

        (
            tr(
                "Q4. Which information should never be shared with others?",
                "Q4. எந்த தகவலை மற்றவர்களிடம் பகிரக்கூடாது?"
            ),
            [
                tr("Your password", "உங்கள் password"),
                tr("Your job title", "உங்கள் job title"),
                tr("Your working hours", "உங்கள் வேலை நேரம்"),
                tr("Your department", "உங்கள் department")
            ],
            tr(
                "Your password",
                "உங்கள் password"
            )
        ),

        (
            tr(
                "Q5. Two tasks have the same deadline. What should you do?",
                "Q5. இரண்டு tasks-க்கும் ஒரே deadline இருந்தால் என்ன செய்வீர்கள்?"
            ),
            [
                tr("Ignore both", "இரண்டையும் ignore செய்வேன்"),
                tr("Prioritize and plan", "முக்கியத்துவம் கொடுத்து plan செய்வேன்"),
                tr("Do nothing", "எதுவும் செய்யமாட்டேன்"),
                tr("Wait until the deadline", "Deadline வரை காத்திருப்பேன்")
            ],
            tr(
                "Prioritize and plan",
                "முக்கியத்துவம் கொடுத்து plan செய்வேன்"
            )
        ),

        (
            tr(
                "Q6. Which Excel feature helps you display only selected records?",
                "Q6. குறிப்பிட்ட records-ஐ மட்டும் காட்ட Excel-ல் எந்த feature பயன்படும்?"
            ),
            [
                "Filter",
                "Print",
                "Save",
                "Close"
            ],
            "Filter"
        ),

        (
            tr(
                "Q7. A job requires a skill you don't have. What is the best approach?",
                "Q7. ஒரு வேலைக்கு உங்களிடம் இல்லாத skill தேவைப்பட்டால் என்ன செய்வது?"
            ),
            [
                tr("Give up", "விட்டுவிடுவது"),
                tr("Learn the required skill", "தேவையான skill-ஐ கற்றுக்கொள்வது"),
                tr("Avoid the job", "வேலையை தவிர்ப்பது"),
                tr("Ignore the skill", "Skill-ஐ ignore செய்வது")
            ],
            tr(
                "Learn the required skill",
                "தேவையான skill-ஐ கற்றுக்கொள்வது"
            )
        ),

        (
            tr(
                "Q8. You find an error before submitting your work. What should you do?",
                "Q8. Work submit செய்வதற்கு முன் error கண்டுபிடித்தால் என்ன செய்வீர்கள்?"
            ),
            [
                tr("Submit immediately", "உடனே submit செய்வேன்"),
                tr("Check and correct it", "சரிபார்த்து correct செய்வேன்"),
                tr("Delete everything", "எல்லாவற்றையும் delete செய்வேன்"),
                tr("Ignore the error", "Error-ஐ ignore செய்வேன்")
            ],
            tr(
                "Check and correct it",
                "சரிபார்த்து correct செய்வேன்"
            )
        ),

        (
            tr(
                "Q9. Which skill is important for teamwork?",
                "Q9. Teamwork-க்கு முக்கியமான skill எது?"
            ),
            [
                tr("Communication", "Communication"),
                tr("Silence", "அமைதி"),
                tr("Avoiding people", "மற்றவர்களை தவிர்ப்பது"),
                tr("Ignoring feedback", "Feedback-ஐ ignore செய்வது")
            ],
            tr(
                "Communication",
                "Communication"
            )
        ),

        (
            tr(
                "Q10. You receive an unknown work-related link. What should you do?",
                "Q10. தெரியாத work-related link வந்தால் என்ன செய்வீர்கள்?"
            ),
            [
                tr("Open immediately", "உடனே open செய்வேன்"),
                tr("Share it with friends", "Friends-க்கு share செய்வேன்"),
                tr("Verify before opening", "Open செய்வதற்கு முன் verify செய்வேன்"),
                tr("Download everything", "எல்லாவற்றையும் download செய்வேன்")
            ],
            tr(
                "Verify before opening",
                "Open செய்வதற்கு முன் verify செய்வேன்"
            )
        )
    ]

    answers = []

    for i, (question, options, correct) in enumerate(questions):

        answer = st.radio(
            question,
            options,
            key=f"assessment_{i}"
        )

        answers.append((answer, correct))

    if st.button(
        tr(
            "🎯 Submit Assessment",
            "🎯 மதிப்பீட்டை சமர்ப்பிக்கவும்"
        )
    ):

        score = 0

        for answer, correct in answers:

            if answer == correct:
                score += 10

        st.session_state.assessment_score = score
        st.session_state.assessment_done = True

        st.success(
            tr(
                f"Your score: {score}/100",
                f"உங்கள் மதிப்பெண்: {score}/100"
            )
        )

        if score >= 80:

            st.success(
                tr(
                    "Excellent job readiness! 🌟",
                    "வேலைக்கான தயார்நிலை மிகவும் நன்றாக உள்ளது! 🌟"
                )
            )

        elif score >= 60:

            st.info(
                tr(
                    "Good readiness. Keep improving your skills. 👍",
                    "நல்ல தயார்நிலை. உங்கள் திறன்களை தொடர்ந்து மேம்படுத்துங்கள். 👍"
                )
            )

        elif score >= 40:

            st.warning(
                tr(
                    "You can improve with more practice. 📚",
                    "மேலும் practice செய்தால் உங்கள் திறன்களை மேம்படுத்தலாம். 📚"
                )
            )

        else:

            st.warning(
                tr(
                    "Start with basic digital and workplace skills. 🌱",
                    "அடிப்படை digital மற்றும் workplace skills-ல் இருந்து தொடங்குங்கள். 🌱"
                )
            )

# =========================================================
# JOB MATCHING
# =========================================================
elif page == tr(
    "💼 Job Matching",
    "💼 வேலை பொருத்தம்"
):

    st.subheader(
        tr(
            "💼 Jobs Matching Your Profile",
            "💼 உங்கள் சுயவிவரத்துடன் பொருந்தும் வேலைகள்"
        )
    )

    if not st.session_state.skills:

        st.warning(
            tr(
                "Please add your skills in My Profile first.",
                "முதலில் My Profile-ல் உங்கள் skills-ஐ சேர்க்கவும்."
            )
        )

    else:

        results = []

        for _, job in df.iterrows():

            score, matched, missing = calculate_job_match(job)

            results.append({
                "Job": job["Job Title"],
                "Company": job["Company"],
                "Location": job["Location"],
                "Education": job["Education"],
                "Salary": job["Salary"],
                "Score": score,
                "Matched": matched,
                "Missing": missing,
                "Job ID": job["Job ID"]
            })

        results = sorted(
            results,
            key=lambda x: x["Score"],
            reverse=True
        )

        for job in results[:10]:

            with st.container(border=True):

                c1, c2 = st.columns([3, 1])

                with c1:

                    st.subheader(
                        f"💼 {job['Job']}"
                    )

                    st.write(
                        f"🏢 {job['Company']}"
                    )

                    st.write(
                        f"📍 {job['Location']}"
                    )

                    st.write(
                        f"🎓 {job['Education']}"
                    )

                    st.write(
                        f"💰 ₹{job['Salary']:,}/month"
                    )

                with c2:

                    st.metric(
                        tr("Match", "பொருத்தம்"),
                        f"{job['Score']}%"
                    )

                st.progress(
                    job["Score"] / 100
                )

                if job["Matched"]:

                    st.write(
                        "✅",
                        tr(
                            "Matched Skills:",
                            "பொருந்திய திறன்கள்:"
                        ),
                        ", ".join(
                            sorted(job["Matched"])
                        )
                    )

                if job["Missing"]:

                    st.write(
                        "❌",
                        tr(
                            "Missing Skills:",
                            "தேவையான / இல்லாத திறன்கள்:"
                        ),
                        ", ".join(
                            sorted(job["Missing"])
                        )
                    )

                st.write(
                    "🎯",
                    tr(
                        "Why this match?",
                        "இந்த வேலை ஏன் பொருந்துகிறது?"
                    )
                )

                st.caption(
                    tr(
                        f"{len(job['Matched'])} required skill(s) match your profile. Education and location are also considered.",
                        f"{len(job['Matched'])} தேவையான skill(s) உங்கள் profile-உடன் பொருந்துகிறது. Education மற்றும் location-ம் கணக்கில் எடுத்துக்கொள்ளப்படுகிறது."
                    )
                )

                if job["Job ID"] not in st.session_state.saved_jobs:

                    if st.button(
                        tr(
                            "❤️ Save Job",
                            "❤️ வேலையை சேமிக்கவும்"
                        ),
                        key=f"save_{job['Job ID']}"
                    ):

                        st.session_state.saved_jobs.append(
                            job["Job ID"]
                        )

                        st.success(
                            tr(
                                "Job saved!",
                                "வேலை சேமிக்கப்பட்டது!"
                            )
                        )

# =========================================================
# JOB FILTERS
# =========================================================
elif page == tr(
    "🔎 Job Filters",
    "🔎 வேலை வடிகட்டி"
):

    st.subheader(
        tr(
            "🔎 Find Jobs Using Filters",
            "🔎 Filter பயன்படுத்தி வேலைகளை கண்டறியவும்"
        )
    )

    selected_location = st.selectbox(
        tr("📍 Location", "📍 இடம்"),
        ["All"] + locations
    )

    selected_education = st.selectbox(
        tr("🎓 Education", "🎓 கல்வி"),
        ["All", "10th", "12th", "Diploma", "Degree"]
    )

    min_salary, max_salary = st.slider(
        tr(
            "💰 Salary Range",
            "💰 சம்பள வரம்பு"
        ),
        10000,
        30000,
        (10000, 30000),
        step=1000
    )

    search = st.text_input(
        tr(
            "🔍 Search Job / Company",
            "🔍 வேலை / நிறுவனத்தை தேடவும்"
        )
    )

    filtered = df.copy()

    if selected_location != "All":

        filtered = filtered[
            filtered["Location"] == selected_location
        ]

    if selected_education != "All":

        filtered = filtered[
            filtered["Education"] == selected_education
        ]

    filtered = filtered[
        (filtered["Salary"] >= min_salary) &
        (filtered["Salary"] <= max_salary)
    ]

    if search:

        filtered = filtered[
            filtered["Job Title"].str.contains(
                search,
                case=False,
                na=False
            )
            |
            filtered["Company"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.write(
        tr(
            f"### {len(filtered)} job(s) found",
            f"### {len(filtered)} வேலைகள் கிடைத்தன"
        )
    )

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# SKILL GAP & LEARNING
# =========================================================
elif page == tr(
    "📚 Skill Gap & Learning",
    "📚 திறன் இடைவெளி & கற்றல்"
):

    st.subheader(
        tr(
            "📚 Skill Gap Analysis",
            "📚 திறன் இடைவெளி பகுப்பாய்வு"
        )
    )

    if not st.session_state.skills:

        st.warning(
            tr(
                "Add your skills in My Profile first.",
                "முதலில் My Profile-ல் உங்கள் skills-ஐ சேர்க்கவும்."
            )
        )

    else:

        user_skills = set(
            st.session_state.skills
        )

        skill_frequency = {}

        for skills in df["Skills"]:

            for skill in skills.split("|"):

                skill = skill.strip()

                if skill not in user_skills:

                    skill_frequency[skill] = (
                        skill_frequency.get(skill, 0) + 1
                    )

        sorted_missing = sorted(
            skill_frequency.items(),
            key=lambda x: x[1],
            reverse=True
        )

        st.write(
            "### 📚",
            tr(
                "Skills You Can Learn",
                "நீங்கள் கற்றுக்கொள்ளக்கூடிய திறன்கள்"
            )
        )

        for skill, count in sorted_missing:

            st.write(
                tr(
                    f"📚 **{skill}** — useful for {count} job(s)",
                    f"📚 **{skill}** — {count} வேலைகளுக்கு பயனுள்ளதாக இருக்கும்"
                )
            )

        st.markdown("---")

        st.write(
            "### 💡",
            tr(
                "What If I Learn This Skill?",
                "இந்த skill-ஐ கற்றுக்கொண்டால்?"
            )
        )

        if sorted_missing:

            selected_skill = st.selectbox(
                tr(
                    "Choose a skill",
                    "ஒரு skill-ஐ தேர்வு செய்யவும்"
                ),
                [
                    x[0]
                    for x in sorted_missing
                ]
            )

            current_scores = []
            future_scores = []

            for _, job in df.iterrows():

                current, _, _ = calculate_job_match(job)

                current_scores.append(current)

                future_skills = set(
                    st.session_state.skills
                )

                future_skills.add(
                    selected_skill
                )

                required = set(
                    x.strip()
                    for x in job["Skills"].split("|")
                )

                matched = future_skills.intersection(
                    required
                )

                skill_score = (
                    len(matched) /
                    len(required)
                ) * 70

                edu_score = (
                    15
                    if education_level[
                        st.session_state.education
                    ] >= education_level[
                        job["Education"]
                    ]
                    else 5
                )

                location_score = (
                    15
                    if st.session_state.location ==
                    job["Location"]
                    else 5
                )

                future_score = min(
                    round(
                        skill_score +
                        edu_score +
                        location_score
                    ),
                    100
                )

                future_scores.append(
                    future_score
                )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    tr(
                        "Average Current Match",
                        "தற்போதைய சராசரி பொருத்தம்"
                    ),
                    f"{sum(current_scores)/len(current_scores):.1f}%"
                )

            with col2:

                st.metric(
                    tr(
                        "Average Match After Learning",
                        "கற்ற பிறகான சராசரி பொருத்தம்"
                    ),
                    f"{sum(future_scores)/len(future_scores):.1f}%"
                )

# =========================================================
# CAREER PATH
# =========================================================
elif page == tr(
    "🧭 Career Path",
    "🧭 தொழில் பாதை"
):

    st.subheader(
        tr(
            "🧭 Career Path Suggestions",
            "🧭 தொழில் பாதை பரிந்துரைகள்"
        )
    )

    career_paths = {

        "📊 Data Career": {
            "skills": [
                "Python",
                "Excel",
                "SQL",
                "Data Analysis"
            ],
            "jobs": [
                "Junior Data Analyst"
            ],
            "learn": [
                "Python",
                "SQL",
                "Data Analysis"
            ]
        },

        "💻 IT Support Career": {
            "skills": [
                "Computer Basics",
                "Networking",
                "Troubleshooting"
            ],
            "jobs": [
                "IT Support Assistant",
                "Technical Support Trainee"
            ],
            "learn": [
                "Networking",
                "Troubleshooting"
            ]
        },

        "☎️ Customer Service Career": {
            "skills": [
                "Communication",
                "English",
                "Customer Service"
            ],
            "jobs": [
                "Customer Support Executive",
                "Customer Care Assistant"
            ],
            "learn": [
                "English",
                "Customer Service"
            ]
        },

        "🎨 Creative Career": {
            "skills": [
                "Canva",
                "Graphic Design",
                "Communication"
            ],
            "jobs": [
                "Graphic Design Assistant",
                "Social Media Assistant"
            ],
            "learn": [
                "Canva",
                "Graphic Design"
            ]
        },

        "📦 Operations Career": {
            "skills": [
                "Inventory",
                "Excel",
                "Computer Basics"
            ],
            "jobs": [
                "Warehouse Assistant",
                "Inventory Assistant"
            ],
            "learn": [
                "Inventory",
                "Excel"
            ]
        }
    }

    for career, details in career_paths.items():

        matched = set(
            st.session_state.skills
        ).intersection(
            details["skills"]
        )

        with st.container(border=True):

            st.subheader(career)

            st.write(
                "✅",
                tr(
                    "Your matching skills:",
                    "உங்களிடம் உள்ள பொருந்தும் skills:"
                ),
                ", ".join(matched)
                if matched
                else tr("None yet", "இன்னும் இல்லை")
            )

            st.write(
                "💼",
                tr(
                    "Example Jobs:",
                    "உதாரண வேலைகள்:"
                ),
                ", ".join(details["jobs"])
            )

            st.write(
                "📚",
                tr(
                    "Skills to Develop:",
                    "மேம்படுத்த வேண்டிய skills:"
                ),
                ", ".join(details["learn"])
            )

# =========================================================
# SAVED JOBS
# =========================================================
elif page == tr(
    "❤️ Saved Jobs",
    "❤️ சேமித்த வேலைகள்"
):

    st.subheader(
        tr(
            "❤️ Saved Jobs",
            "❤️ சேமித்த வேலைகள்"
        )
    )

    if not st.session_state.saved_jobs:

        st.info(
            tr(
                "You haven't saved any jobs yet.",
                "நீங்கள் இன்னும் எந்த வேலைகளையும் சேமிக்கவில்லை."
            )
        )

    else:

        saved = df[
            df["Job ID"].isin(
                st.session_state.saved_jobs
            )
        ]

        for _, job in saved.iterrows():

            with st.container(border=True):

                st.subheader(
                    f"💼 {job['Job Title']}"
                )

                st.write(
                    f"🏢 {job['Company']} | "
                    f"📍 {job['Location']} | "
                    f"💰 ₹{job['Salary']:,}"
                )

                if st.button(
                    tr(
                        "Remove",
                        "நீக்கவும்"
                    ),
                    key=f"remove_{job['Job ID']}"
                ):

                    st.session_state.saved_jobs.remove(
                        job["Job ID"]
                    )

                    st.rerun()

# =========================================================
# RESUME GENERATOR
# =========================================================
elif page == tr(
    "📄 Resume Generator",
    "📄 Resume உருவாக்கி"
):

    st.subheader(
        tr(
            "📄 Resume Generator",
            "📄 Resume உருவாக்கி"
        )
    )

    objective = st.text_area(
        tr(
            "Career Objective",
            "தொழில் நோக்கம்"
        ),
        value=(
            "Motivated student seeking an entry-level "
            "opportunity to apply skills and develop "
            "professional experience."
        )
    )

    if st.button(
        tr(
            "📄 Generate Resume",
            "📄 Resume உருவாக்கவும்"
        )
    ):

        skills_text = (
            ", ".join(
                st.session_state.skills
            )
            if st.session_state.skills
            else "Basic computer skills"
        )

        resume = f"""
RESUME
================================

Name: {st.session_state.name or "Your Name"}

Career Objective:
{objective}

Education:
{st.session_state.education}

Preferred Location:
{st.session_state.location}

Experience:
{st.session_state.experience}

Skills:
{skills_text}

Job Readiness Assessment:
{st.session_state.assessment_score}/100

================================
Generated using Skill-to-Job Matching
"""

        st.session_state.resume_created = True

        st.text_area(
            tr(
                "Resume Preview",
                "Resume முன்னோட்டம்"
            ),
            resume,
            height=400
        )

        st.download_button(
            tr(
                "⬇️ Download Resume",
                "⬇️ Resume-ஐ Download செய்யவும்"
            ),
            resume,
            file_name="my_resume.txt",
            mime="text/plain"
        )

# =========================================================
# PROGRESS TRACKER
# =========================================================
elif page == tr(
    "📈 Progress Tracker",
    "📈 முன்னேற்ற கண்காணிப்பு"
):

    st.subheader(
        tr(
            "📈 Career Progress Tracker",
            "📈 தொழில் முன்னேற்ற கண்காணிப்பு"
        )
    )

    profile_complete = (
        bool(st.session_state.name)
        and
        bool(st.session_state.skills)
    )

    assessment_complete = (
        st.session_state.assessment_done
    )

    matching_complete = bool(
        st.session_state.skills
    )

    learning_complete = bool(
        st.session_state.skills
    )

    resume_complete = (
        st.session_state.resume_created
    )

    profile_score = 20 if profile_complete else 0
    assessment_score = 20 if assessment_complete else 0
    matching_score = 20 if matching_complete else 0
    learning_score = 20 if learning_complete else 0
    resume_score = 20 if resume_complete else 0

    total_progress = (
        profile_score +
        assessment_score +
        matching_score +
        learning_score +
        resume_score
    )

    st.metric(
        tr(
            "🎯 Overall Career Readiness",
            "🎯 மொத்த தொழில் தயார்நிலை"
        ),
        f"{total_progress}%"
    )

    st.progress(
        total_progress / 100
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            "👤",
            tr(
                "Profile:",
                "சுயவிவரம்:"
            ),
            "✅" if profile_complete
            else "⏳"
        )

        st.write(
            "📝",
            tr(
                "Assessment:",
                "மதிப்பீடு:"
            ),
            "✅" if assessment_complete
            else "⏳"
        )

        st.write(
            "💼",
            tr(
                "Job Matching:",
                "வேலை பொருத்தம்:"
            ),
            "✅" if matching_complete
            else "⏳"
        )

    with col2:

        st.write(
            "📚",
            tr(
                "Skill Learning:",
                "திறன் கற்றல்:"
            ),
            "✅" if learning_complete
            else "⏳"
        )

        st.write(
            "📄",
            tr(
                "Resume:",
                "Resume:"
            ),
            "✅" if resume_complete
            else "⏳"
        )

    st.markdown("---")

    st.info(
        tr(
            "Complete your profile, assessment, learning and resume to improve your career readiness.",
            "உங்கள் profile, assessment, learning மற்றும் resume-ஐ complete செய்து career readiness-ஐ மேம்படுத்துங்கள்."
        )
    )

# =========================================================
# DASHBOARD
# =========================================================
elif page == tr(
    "📊 Dashboard",
    "📊 Dashboard"
):

    st.subheader(
        tr(
            "📊 Career Dashboard",
            "📊 தொழில் Dashboard"
        )
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            tr(
                "💼 Total Jobs",
                "💼 மொத்த வேலைகள்"
            ),
            len(df)
        )

    with col2:

        st.metric(
            tr(
                "🏢 Companies",
                "🏢 நிறுவனங்கள்"
            ),
            df["Company"].nunique()
        )

    with col3:

        st.metric(
            tr(
                "📍 Locations",
                "📍 இடங்கள்"
            ),
            df["Location"].nunique()
        )

    with col4:

        st.metric(
            tr(
                "📝 Assessment",
                "📝 மதிப்பீடு"
            ),
            f"{st.session_state.assessment_score}/100"
        )

    st.markdown("---")

    st.write(
        "### 📍",
        tr(
            "Jobs by Location",
            "இடம் வாரியாக வேலைகள்"
        )
    )

    location_count = (
        df["Location"]
        .value_counts()
        .sort_values(ascending=False)
    )

    st.bar_chart(
        location_count
    )

    st.write(
        "### 💰",
        tr(
            "Salary by Job",
            "வேலை வாரியாக சம்பளம்"
        )
    )

    salary_data = df[
        ["Job Title", "Salary"]
    ].set_index(
        "Job Title"
    )

    st.bar_chart(
        salary_data
    )

    st.write(
        "### 🎓",
        tr(
            "Jobs by Education",
            "கல்வி அடிப்படையில் வேலைகள்"
        )
    )

    education_count = (
        df["Education"]
        .value_counts()
    )

    st.bar_chart(
        education_count
    )

    st.write(
        "### 💼",
        tr(
            "Available Jobs",
            "கிடைக்கும் வேலைகள்"
        )
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.write(
        "### 👤",
        tr(
            "Your Summary",
            "உங்கள் சுருக்கம்"
        )
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.write(
            f"**{tr('Education', 'கல்வி')}:**",
            st.session_state.education
        )

    with c2:

        st.write(
            f"**{tr('Location', 'இடம்')}:**",
            st.session_state.location
        )

    with c3:

        st.write(
            f"**{tr('Skills', 'திறன்கள்')}:**",
            len(st.session_state.skills)
        )

# =========================================================
# SIDEBAR FOOTER
# =========================================================
st.sidebar.markdown("---")

st.sidebar.caption(
    tr(
        "💼 Skill-to-Job Matching for Rural Youth",
        "💼 கிராமப்புற இளைஞர்களுக்கான திறன் - வேலை பொருத்தம்"
    )
)

st.sidebar.caption(
    tr(
        "Helping youth discover suitable career opportunities.",
        "இளைஞர்கள் பொருத்தமான தொழில் வாய்ப்புகளை கண்டறிய உதவுகிறது."
    )
)