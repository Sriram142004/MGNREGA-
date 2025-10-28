# 🌾 MGNREGA District Performance Dashboard

This project is a **data visualization dashboard** built using **Django**, **Chart.js**, and **Bootstrap**, designed to monitor and analyze the performance of various districts under the **Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA)**.  
It provides real-time insights into **workers employed, funds spent**, and **district-level performance** through **interactive charts** and **3D visual analytics**.

---

## 🚀 Features

- 📊 **Interactive Dashboard** – Visualizes district-level performance metrics.
- 💰 **3D Bar & Pie Charts** – Shows funds spent and worker distribution.
- ⚙️ **Django REST Framework API** – Fetches real-time JSON data dynamically.
- 💾 **SQLite Database Integration** – Stores district data locally.
- ✨ **Modern UI with Animations** – Includes glowing buttons and responsive design.
- 🌐 **Light/Dark Auto Theme** – Adapts UI automatically for the best viewing experience.

---

## 🏗️ Tech Stack

| Component | Technology Used |
|------------|----------------|
| Backend | Django 5, Django REST Framework |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Charts & Visualization | Chart.js, Chart.js 3D plugin |
| Database | SQLite |
| Hosting | Local / GitHub Deployment Ready |

---

## ⚡ How It Works

1. The **backend (Django)** retrieves district performance data from the database model `DistrictPerformance`.
2. The **REST API endpoint** `/dashboard/districts/` serves this data as JSON.
3. The **frontend (index.html)** fetches this JSON asynchronously using JavaScript.
4. **Chart.js** processes the JSON and visualizes:
   - Workers employed per district.
   - Funds spent (in ₹).
   - Overall distribution using 3D charts.
5. The dashboard provides **real-time interactive analysis** of MGNREGA’s progress and efficiency across districts.

---

## 🧠 Database Schema

**Model: DistrictPerformance**
| Field | Type | Description |
|--------|------|-------------|
| `district_name` | CharField | Name of the district |
| `year` | IntegerField | Year of performance data |
| `workers` | IntegerField | Total workers employed |
| `funds_spent` | FloatField | Total funds utilized in ₹ |

---
🧱 Project Setup:

# 1️⃣ Clone the repository
git clone https://github.com/Sriram142004/MGNREGA-.git
cd mgnrega-app
# 2️⃣ Create & activate virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# 3️⃣ Install dependencies
pip install -r requirements.txt
# 4️⃣ Run the server
python manage.py runserver
# 5️⃣ Open in browser
http://127.0.0.1:8000/dashboard/

🎯 Project Purpose:
The MGNREGA Dashboard aims to help:
Government officials track fund allocation and employment metrics.
Administrators identify underperforming districts.
Citizens visualize MGNREGA’s real impact transparently.
It acts as a decision-support system for policy evaluation and planning.

🧭 Future Enhancements:

📅 Add filters by year, state, and region.
🛰️ Integrate live API data from official MGNREGA portals.
📈 Export dashboard reports in PDF or Excel.
🗺️ Display district-level maps using GeoDjango.

🧑‍💻 Author:
👤 Govinda Maruthi Sriram Valluri


## 🧩 Example API Response

```json
[
  {
    "district_name": "Lucknow",
    "workers": 20,
    "funds_spent": 100000000.0
  },
  {
    "district_name": "UP",
    "workers": 10,
    "funds_spent": 10920391.0
  }
]

