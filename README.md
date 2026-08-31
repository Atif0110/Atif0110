<h1 align="center">Mohd Atif</h1>

<p align="center">
  <strong>Data Scientist · AI Software Engineer</strong>
</p>

<p align="center">
  I build data-driven systems that go beyond notebooks,<br>
  from forecasting and ML models to production APIs and LLM-powered applications.
</p>

<p align="center">
  <a href="https://atif0110.github.io/Portfolio/">
    <img src="https://img.shields.io/badge/Portfolio-atif0110.github.io-d01117?style=flat&logo=vercel&logoColor=white&labelColor=0d1117" alt="Portfolio"/>
  </a>
  <a href="https://linkedin.com/in/mohd-atif01">
    <img src="https://img.shields.io/badge/LinkedIn-Mohd_Atif-d01117?style=flat&logo=linkedin&logoColor=white&labelColor=0d1117" alt="LinkedIn"/>
  </a>
  <a href="mailto:data.atif001@gmail.com">
    <img src="https://img.shields.io/badge/Email-data.atif001%40gmail.com-d01117?style=flat&logo=gmail&logoColor=white&labelColor=0d1117" alt="Email"/>
  </a>
</p>

<p align="center">
  <img src="https://github.com/Atif0110/Atif0110/raw/main/assets/data-engineering-animation.svg" alt="Data science and software engineering animation" width="850">
</p>

---

## `atif@github ~ $ whoami`

I'm a Data Scientist and AI Software Engineer working across the full lifecycle of data products.

My work spans data engineering, feature engineering, machine learning, time-series forecasting, experimentation, LLM integration, backend development, and deployment.

I particularly enjoy taking something that works in a notebook and turning it into a system that can actually run in production. That means thinking about validation, API design, failure handling, caching, monitoring, and what happens when an external dependency goes down.

Some of the results I've worked toward:

* 20–35% improvement over baseline in electricity price forecasting
* 20% reduction in food waste through demand forecasting
* 15% improvement in gross margin through A/B-tested pricing
* 95% classification accuracy in a deployed customer churn system
* 99% data availability in a real-time urban analytics pipeline
* 100K+ records processed across analytics and forecasting workflows

I studied **Data Science and Applications at IIT Madras (2022–2025)**.

---

## `atif@github ~ $ ls projects/`

### 01. European Power Market Forecasting System

`Python` `XGBoost` `FastAPI` `ENTSO-E API` `LLM` `Backtesting` `PnL Simulation`

An electricity price forecasting system built around real European energy-market data.

I engineered 12+ time-series features including lagged prices, rolling volatility, calendar effects, and multi-period dependencies. The XGBoost model improved forecasting performance by **20–35% over baseline** and outperformed three alternative approaches.

The system goes beyond prediction. Historical forecasts feed into a backtesting and PnL simulation framework covering 12+ months of market data. An LLM layer converts model output into trader-oriented briefs, removing more than three hours of recurring manual reporting each week.

Data quality is handled through an eight-point validation pipeline covering schema checks, anomaly detection, correlations, freshness, and other consistency checks.

**What I worked on**

* Time-series feature engineering
* XGBoost forecasting
* Historical backtesting
* PnL simulation
* Data-quality validation
* FastAPI services
* Programmatic LLM integration
* Automated reporting

[View source on GitHub](https://github.com/Atif0110)

---

### 02. AI Customer Churn Prediction & Retention Engine

`Python` `FastAPI` `Scikit-learn` `LLM APIs` `Streamlit`

A production-style churn prediction system that combines classical machine learning with an LLM-powered recommendation layer.

The backend serves a logistic-regression classifier with **95% accuracy**, supporting both real-time inference and batch CSV processing.

Instead of returning only a probability score, the system explains the prediction by surfacing the customer's three strongest churn drivers. An LLM agent then converts those signals into multi-step retention recommendations.

The application also includes a What-If simulation layer so users can explore potential intervention outcomes without requesting a new analysis.

The GenAI layer includes **exponential-backoff retries and rule-based fallback logic**, allowing the application to remain useful when an external LLM service fails.

**What I worked on**

* Classification
* Feature importance and explainability
* Real-time inference
* Batch prediction
* LLM agent integration
* Retention recommendations
* What-If simulations
* API reliability
* FastAPI backend

[Live application](https://ai-customer-churn-intelligence.streamlit.app/) · [View source on GitHub](https://github.com/Atif0110)

---

### 03. Meteograph

`Python` `FastAPI` `JavaScript` `OpenWeatherMap` `TomTom` `OpenStreetMap`

A weather dashboard that combines traditional forecasting with smart-city analytics.

Meteograph brings weather, air quality, traffic, alerts, and trend information into a single interface. The application supports both live API data and deterministic mock data, allowing the entire system to run without API keys.

The backend keeps external API calls server-side, adds short-lived caching, and aggregates multiple data sources into a consistent frontend response.

The frontend intentionally avoids a JavaScript framework or build system. It is built with plain HTML, CSS, and modular JavaScript.

**What I worked on**

* FastAPI backend architecture
* External API integration
* Weather and air-quality aggregation
* Traffic data processing
* API caching
* Mock-data fallback
* Interactive dashboard
* Animated weather scenes
* REST API design

[View source on GitHub](https://github.com/Atif0110)

---

### 04. Real-Time Urban Analytics Dashboard

`Python` `REST APIs` `ARIMA` `Anomaly Detection` `Streamlit` `PyDeck`

A real-time analytics system combining traffic, weather, and air-quality data from three external APIs.

The pipeline validates incoming schemas, handles API failures, caches responses for three minutes, and maintains approximately **99% data availability**.

Forecasting and anomaly-detection modules identify unusual conditions while the dashboard provides multi-city comparison, geospatial visualization, and real-time alerts.

**What I worked on**

* Multi-source API integration
* Data validation
* Error handling
* Real-time caching
* ARIMA forecasting
* Anomaly detection
* Geospatial analytics
* Interactive dashboards

[Live application](https://smart-city-analytics.streamlit.app/) · [View source on GitHub](https://github.com/Atif0110)

---

### 05. Shravan

`Flutter` `Flask` `Groq` `Selenium`

A voice-first health companion application built around conversational interaction, medicine reminders, and hospital discovery.

The project placed **5th out of 30 teams at IIT Madras**.

I later revisited the application from a security perspective and fixed several architectural issues, including exposed API keys, overly permissive CORS, missing authentication checks, and a root-cause session-credential issue where frontend requests were not sending authentication information.

**What I worked on**

* Flask backend
* Flutter application
* LLM integration
* Voice interaction
* Web scraping
* Authentication
* API security
* CORS configuration

[View source on GitHub](https://github.com/Atif0110/Shravan-Application)

---

## `atif@github ~ $ cat stack.md`

### Machine Learning

<p>
  <img src="https://img.shields.io/badge/Python-0d1117?style=flat&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/XGBoost-0d1117?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-0d1117?style=flat&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-0d1117?style=flat&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-0d1117?style=flat&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/statsmodels-0d1117?style=flat&logoColor=white" />
</p>

Time-series forecasting, feature engineering, classification, cross-validation, A/B testing, anomaly detection, backtesting, PnL simulation.

### AI and LLM Systems

<p>
  <img src="https://img.shields.io/badge/OpenAI_API-0d1117?style=flat&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Anthropic_API-0d1117?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-0d1117?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-0d1117?style=flat&logoColor=white" />
</p>

Programmatic LLM integration, agent development, RAG, embeddings, vector search, prompt engineering, structured outputs, tool calling, retry logic, fallback systems.

### Backend and Infrastructure

<p>
  <img src="https://img.shields.io/badge/FastAPI-0d1117?style=flat&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-0d1117?style=flat&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-0d1117?style=flat&logo=amazonaws&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-0d1117?style=flat&logo=git&logoColor=white" />
</p>

REST APIs, Docker, AWS EC2, AWS Lambda, CI/CD, Kubernetes fundamentals, Render, Streamlit Cloud.

### Data

<p>
  <img src="https://img.shields.io/badge/SQL-0d1117?style=flat&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/R-0d1117?style=flat&logo=r&logoColor=white" />
  <img src="https://img.shields.io/badge/Power_BI-0d1117?style=flat&logo=powerbi&logoColor=white" />
  <img src="https://img.shields.io/badge/Tableau-0d1117?style=flat&logo=tableau&logoColor=white" />
</p>

SQL, CTEs, window functions, query optimization, database design, data pipelines, analytics, visualization.

---

## `atif@github ~ $ cat experience.md`

### Data Scientist · Arabania Indo Arabic Restaurant

**Lucknow, India**

* Built demand-forecasting models across **100K+ inventory records**, reducing food waste by 20% and procurement cost by 12%.
* Designed and analyzed end-to-end A/B pricing experiments, resulting in a **15% gross-margin improvement** within two months.
* Developed supervised classification models for SKU performance using transactional and behavioral features, contributing to a 12% operational improvement.
* Built automated SQL analytics pipelines using CTEs and window functions across 100K+ records, reducing manual reporting time by 40%.

---

## `atif@github ~ $ cat education.md`

**Indian Institute of Technology Madras**
B.S. in Data Science and Applications · 2022–2025

**Google Data Analytics Professional Certificate**

---

## `atif@github ~ $ cat currently.md`

I'm particularly interested in building systems at the intersection of:

```text
Machine Learning
      +
Data Engineering
      +
LLM Applications
      +
Backend Engineering
      +
Production Systems
```

I like problems where the interesting part isn't just training the model, but making the whole system reliable enough to use.

---

## `atif@github ~ $ contact`

If you're working on something involving machine learning, data products, AI applications, or backend systems, I'd be happy to talk.

<p>
  <a href="https://atif0110.github.io/Portfolio/">Portfolio</a> ·
  <a href="https://linkedin.com/in/mohd-atif01">LinkedIn</a> ·
  <a href="mailto:data.atif001@gmail.com">Email</a>
</p>
