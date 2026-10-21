# 🌦️ Weather App

A simple and responsive weather application built using **Python, Flask, HTML, and CSS** that allows users to check weather information for their desired locations using a weather API.

## 🚀 Features

- Search for weather information by city.
- Fetch weather data using a weather API.
- Display weather information through a simple user interface.
- Responsive and clean design using HTML and CSS.
- Secure API key management using environment variables.

## 🛠️ Technologies Used

- **Python** – Application logic
- **Flask** – Backend web framework
- **HTML5** – Web page structure
- **CSS3** – Styling and layout
- **Weather API** – Fetching weather data
- **python-dotenv** – Loading environment variables

## 📁 Project Structure

```text
weather-app/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

*Adjust the filenames above to match your actual project structure.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd weather-app
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
WEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key. Use the environment variable name expected by your application.

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

`http://127.0.0.1:5000`

## 🔐 Security

- API keys are stored in environment variables.
- The `.env` file should not be committed to GitHub.
- Keep your API key private.

## 📌 Future Improvements

- Display weather forecasts for upcoming days.
- Add weather icons and animations.
- Improve mobile responsiveness.
- Display additional information such as humidity, wind speed, and feels-like temperature.

## 👨‍💻 Author

**Sreehari PS**

A project developed to practice Python web development, Flask, API integration, and frontend design.
