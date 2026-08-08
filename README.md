<h1 align="center">Mohd Atif</h1>
<h3 align="center">Data Scientist</h3>

<p align="center">
  <a href="https://atif0110.github.io/Portfolio/"><img src="https://img.shields.io/badge/Portfolio-atif0110.github.io-d01117?style=flat&logo=vercel&logoColor=white&labelColor=0d1117" alt="Portfolio"/></a>
  <a href="https://linkedin.com/in/mohd-atif01"><img src="https://img.shields.io/badge/LinkedIn-Mohd_Atif-d01117?style=flat&logo=linkedin&logoColor=white&labelColor=0d1117" alt="LinkedIn"/></a>
  <a href="mailto:data.atif001@gmail.com"><img src="https://img.shields.io/badge/Email-data.atif001%40gmail.com-d01117?style=flat&logo=gmail&logoColor=white&labelColor=0d1117" alt="Email"/></a>
</p>

[![Contribution heatmap for Atif0110, refreshed daily](https://github.com/Atif0110/Atif0110/raw/main/contribheatmap.svg)](/Atif0110/Atif0110/blob/main/contribheatmap.svg)
[![Recent releases and commits for Atif0110, newest first, refreshed daily](https://github.com/Atif0110/Atif0110/raw/main/shiplog.svg)](/Atif0110/Atif0110/blob/main/shiplog.svg)

<p align="center">
  <a href="/Atif0110/Atif0110/blob/main/infocard.svg"><img src="https://github.com/Atif0110/Atif0110/raw/main/infocard.svg" alt="Terminal card summarizing Mohd Atif as a Data Scientist"/></a>
</p>

## `atif@github ~ $ cat about.md`

I am a Data Scientist based in Lucknow, working across the full model lifecycle: data engineering, feature engineering, model development, validation, and deployment. My work leans heavily on time series forecasting and programmatic LLM integration, and I build systems that carry their own retry and fallback logic so they hold up outside a notebook.

A year of applied work behind me has translated into numbers I can point to: a 20 to 35% lift in forecast accuracy, a 15% improvement in gross margin, and a classifier running at 95% accuracy in a live deployed system. I studied Data Science and Applications at IIT Madras (2022 to 2025).

Reach me on [LinkedIn](https://linkedin.com/in/mohd-atif01) or by [email](mailto:data.atif001@gmail.com).

## `atif@github ~ $ cat experience.md`

**Data Scientist, Arabania Indo Arabic Restaurant** (Lucknow)

* Built demand forecasting models in Python (statsmodels, scikit learn) across 100K+ inventory records, cutting food waste by 20% and procurement cost by 12%
* Ran end to end A/B pricing experiments with formal hypothesis testing, landing a pricing strategy that improved gross margin by 15% within two months
* Trained supervised classification models for SKU performance on transactional and behavioral features, driving a 12% operational improvement
* Built SQL analytics pipelines using CTEs and window functions across 100K+ records, cutting manual reporting time by 40% through full automation

## `atif@github ~ $ ls -l projects/`

### European Power Market Forecasting System
`Python` `XGBoost` `FastAPI` `ENTSO E API` `LLM Integration` `Prompt Engineering` `PnL Simulation`

An electricity price forecasting pipeline built on real ENTSO E European market data. I engineered 12+ features (lag 1/24/168h, rolling volatility, calendar effects) and trained an XGBoost model that outperformed three alternative architectures with a 20 to 35% improvement over baseline. An LLM agent reads the model output and writes trader briefs automatically, removing 3+ hours a week of manual reporting across five recurring report types. An 8 point QA pipeline (schema validation, anomaly detection, correlation checks, freshness monitoring) has held data quality incidents at zero, alongside a backtesting and PnL simulation framework spanning 12+ months of historical data.

[Source on GitHub](https://github.com/Atif0110)

### AI Customer Churn Prediction and Retention Engine
`Python` `FastAPI` `Scikit learn` `LLM API Integration` `Streamlit`

A production FastAPI backend serving a logistic regression classifier at 95% accuracy, with real time inference for 100+ customers and batch CSV processing. A custom LLM agent reads churn scores and feature importances and turns them into multi step retention recommendations, with an explainability layer surfacing the top three churn drivers behind each prediction. A What If simulation layer lets stakeholders test intervention ROI on their own instead of filing a request. The GenAI service underneath handles retries with exponential backoff and drops to rule based logic if the LLM call fails.

[Live App](https://ai-customer-churn-intelligence.streamlit.app/) · [Source on GitHub](https://github.com/Atif0110)

### Real Time Urban Analytics Dashboard
`Python` `REST APIs` `ARIMA` `Anomaly Detection` `Streamlit` `PyDeck`

A pipeline pulling from three live REST APIs (traffic, weather, air quality) with schema validation, error handling, and a three minute refresh cache, holding 99% data availability. Statistical forecasting and anomaly detection modules feed an interactive dashboard with real time alerts and multi city comparison, tracking five or more operational metrics at once with geospatial visualization.

[Live App](https://smart-city-analytics.streamlit.app/) · [Source on GitHub](https://github.com/Atif0110)

### Shravan, a voice first health companion app
`Flutter` `Flask` `Groq` `Selenium`

A safety gated health chatbot with voice medicine reminders and a Selenium based hospital scraper. Placed fifth out of thirty at IIT Madras. Later went through a full security overhaul: fixed exposed API keys, an open CORS policy, missing auth checks, and a root cause bug where no frontend call was sending session credentials.

[Source on GitHub](https://github.com/Atif0110/Shravan-Application)

## `atif@github ~ $ which python sql llm`

<p align="left">
  <img src="https://img.shields.io/badge/Python-0d1117?style=flat&logo=python&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/FastAPI-0d1117?style=flat&logo=fastapi&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/SQL-0d1117?style=flat&logo=postgresql&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/XGBoost-0d1117?style=flat&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/scikit_learn-0d1117?style=flat&logo=scikitlearn&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/LangChain-0d1117?style=flat&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/OpenAI_API-0d1117?style=flat&logo=openai&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Anthropic_API-0d1117?style=flat&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Groq-0d1117?style=flat&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Streamlit-0d1117?style=flat&logo=streamlit&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Docker-0d1117?style=flat&logo=docker&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/AWS-0d1117?style=flat&logo=amazonaws&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Git-0d1117?style=flat&logo=git&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Power_BI-0d1117?style=flat&logo=powerbi&logoColor=white&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Tableau-0d1117?style=flat&logo=tableau&logoColor=white&labelColor=0d1117" />
</p>

**ML and statistics:** XGBoost, scikit learn, logistic regression, time series forecasting, feature engineering, cross validation, A/B testing, anomaly detection, backtesting, PnL simulation
**LLMs and agents:** programmatic LLM API integration (OpenAI, Anthropic, Groq), LangChain, RAG pipelines, custom agent development, prompt engineering, structured output validation, retry and fallback reliability layers
**Backend and cloud:** FastAPI, REST APIs, Docker, AWS (EC2, Lambda), Kubernetes fundamentals, Render, Streamlit Cloud, CI/CD
**Data:** Python (Pandas, NumPy, statsmodels), SQL (CTEs, window functions, query optimization), R

## `atif@github ~ $ cat education.md`

**Indian Institute of Technology, Madras**, B.S. in Data Science and Applications, 2022 to 2025
**Google Data Analytics Professional Certificate**

## `atif@github ~ $ make readme`

The heatmap, the ship log, and the terminal card above are not hosted widgets. They are SVGs generated in this repo, so nothing here can rate limit or go down and leave a broken image on my profile.

| Piece | Script | Refreshed |
|---|---|---|
| `contribheatmap.svg` | `scripts/fetch_contributions.py` + `scripts/render_heatmap_svg.py` | Daily, by GitHub Actions |
| `shiplog.svg` | `scripts/fetch_shiplog.py` + `scripts/render_shiplog_svg.py` | Daily, by GitHub Actions |
| `infocard.svg` | `scripts/make_info_card.py` | By hand, when the facts change |

GitHub strips `<script>` tags from a README but still renders SVG through `<img>` and still runs CSS keyframes inside it, so the animation lives entirely in the files. Python standard library only, no dependencies.

```
python3 scripts/fetch_contributions.py
python3 scripts/render_heatmap_svg.py
python3 scripts/fetch_shiplog.py
python3 scripts/render_shiplog_svg.py
python3 scripts/make_info_card.py
```

## `atif@github ~ $ exit`

Full writeups for these live at [my portfolio](https://atif0110.github.io/Portfolio/). If any of this overlaps with something you are building, reach out on [LinkedIn](https://linkedin.com/in/mohd-atif01) or by [email](mailto:data.atif001@gmail.com).
