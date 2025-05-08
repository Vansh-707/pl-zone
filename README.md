# Premier League Zone ⚽️

## About
**Premier League Zone** is a Spring Boot CRUD application designed to provide users with the ability to retrieve data for players and teams of the Premier League (EPL). The application also incorporates machine learning to predict match outcomes, giving users valuable insights into potential results based on historical data and various performance metrics.

The application offers:

- **CRUD operations**: Create, Read, Update, Delete data for players and teams 📝.
- **Data retrieval**: Fetch detailed information about Premier League players and teams 📊.
- **Match prediction**: Predict the outcome of upcoming matches using machine learning algorithms 🤖.

---

## Features ✨

- **Player Management**: Add, update, and delete player information (e.g., name, team, position, goals scored, etc.) 👤⚽️.
- **Team Management**: Create and modify team details (e.g., team name, coach, players) 🏆.
- **Real-time Data Scraping**: Scrape current player and team statistics from popular sports websites (e.g., BBC Sport, ESPN, or official EPL data sources) 🌐📈.
- **Match Prediction**: Using historical performance data, the app predicts match outcomes between teams 🔮.
- **RESTful API**: Exposes endpoints for retrieving player and team data, as well as triggering predictions 📡.

---

## Tech Stack 💻

- **Backend**: Spring Boot 🚀
- **Database**: MySQL 🗄️
- **Machine Learning Model**: 
  - **Random Forest Classifier** (used for predicting match outcomes) 🌳
  - **Logistic Regression** (used for predicting player ratings) 📉
- **API**: REST API built with Spring Boot 🔗
- **Web Scraping**: **BeautifulSoup** (for extracting player and team statistics from web pages) 🕸️
- **Authentication**: JWT for securing user access 🔐
- **Others**: Maven for build automation 🛠️

---

