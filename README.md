# Streamlit Crash Course with Showcase Projects

This repository contains a structured learning path to master Streamlit using modern Python tools like `uv`. It starts from the basics and builds up to professional-level dashboards, using only core libraries such as Streamlit, pandas, and numpy.

You will learn how to build data apps, create interactive user interfaces, work with real datasets, and deploy your apps to the web — all from a single Python file per app.

## 🎯 Learning Objectives

- Set up and run Streamlit projects using `uv`
- Build interactive interfaces with forms, sliders, buttons, and dropdowns
- Structure apps with layouts like columns, sidebars, and expanders
- Load, filter, and display real data using pandas
- Build dashboards with KPI cards and charts using only built-in Streamlit features
- Learn how to deploy your app to Streamlit Cloud

## 📋 Prerequisites

- Basic knowledge of Python
- Familiarity with HTML, CSS, and JavaScript

## 📚 Table of Contents

1. **chapter-one.py** - Introduction to Streamlit
2. **chapter-two.py** - Widgets and Inputs
3. **chapter-three.py** - Layouts and Styling
4. **chapter-four.py** - Working with Data
5. **chapter-five.py** - API Integration
6. **demo-dashboard.py** - Dashboards with KPI cards and charts

## 🚀 Getting Started

### Using `uv` (Recommended)

1. **Install uv**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and setup**
   ```bash
   git clone https://github.com/mbe-waqar/streamlit-crash-course.git
   cd streamlit-crash-course
   uv venv
   source .venv/bin/activate
   uv pip install streamlit pandas numpy plotly
   ```

3. **Run any chapter**
   ```bash
   streamlit run chapter-one.py
   ```

### Using pip

```bash
git clone https://github.com/mbe-waqar/streamlit-crash-course.git
cd streamlit-crash-course
python -m venv venv
source venv/bin/activate
pip install streamlit pandas numpy plotly
streamlit run chapter-one.py
```

## 📖 What You'll Learn

- **Chapter 1**: Basic Streamlit setup and text elements
- **Chapter 2**: Interactive widgets and forms
- **Chapter 3**: Layouts, columns, and styling
- **Chapter 4**: Data loading and display
- **Chapter 5**: API integration and real-time data
- **Chapter 6**: Professional dashboard with KPIs and charts

## 🚀 Deployment

Deploy to Streamlit Cloud:
1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect repository and deploy

## 📁 Project Structure

```
streamlit-crash-course/
├── chapter-one.py          # Introduction to Streamlit
├── chapter-two.py          # Widgets and Inputs
├── chapter-three.py        # Layouts and Styling
├── chapter-four.py         # Working with Data
├── chapter-five.py         # API Integration
├── demo-dashboard.py       # Professional Dashboard
├── data/                   # Sample datasets
└── requirements.txt        # Dependencies
```

## 🛠️ Quick Tips

- Use `@st.cache_data` for performance
- Keep each app in a single Python file
- Test with different screen sizes
- Use `streamlit run app.py --server.port 8502` if port 8501 is busy

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Community Forum](https://discuss.streamlit.io/)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push and submit pull request

---

**⭐ If you find this crash course helpful, please give it a star!**

**Made with ❤️ by [Waqar Ali](https://www.linkedin.com/in/waqar-ali-b70976322/) using Streamlit and Python**