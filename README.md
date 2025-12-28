# 📦 Shipping Optimizer (集貨費用最佳化計算機)

A professional web application designed to find the most cost-effective way to split multiple items into separate shipping parcels. It utilizes **Dynamic Programming (DP)** to balance the trade-off between "base shipping rates" and "excess item surcharges."

## 🚀 Why This Exists?
In most consolidated shipping (集運) services, there is a **base rate** for the first kilogram and a **surcharge** if a single parcel contains too many items. 

If you have many lightweight items, merging them all into one parcel might trigger high surcharges that exceed the cost of simply opening a second parcel. This calculator solves that math for you instantly.

## ✨ Key Features
- **Smart Optimization**: Uses a Dynamic Programming algorithm to guarantee the global minimum shipping cost.
- **Customizable Rates**: Configure first-kg cost, next-kg cost, surcharge thresholds, and weight limits via the UI.
- **Detailed Cost Breakdown**: View the base weight fee and surcharge for every suggested parcel.
- **Data Portability**: Import/Export your item list via CSV files.
- **Shareable Results**: One-click to generate and download a professional summary image for sharing via SMS.
- **Responsive Design**: Mobile-friendly dashboard built with Bootstrap 5.

## 🛠️ Technical Stack
- **Backend**: Python 3 (Flask)
- **Algorithm**: Dynamic Programming (O(n²) time complexity)
- **Frontend**: HTML5, CSS3, JavaScript (Bootstrap 5)
- **Libraries**: 
  - `html2canvas`: For generating result images.
  - `PapaParse`: For CSV processing.
  - `Gunicorn`: Production-grade WSGI server (for deployment).

## 💻 Installation & Local Setup

1. **Clone the repository:**
```bash
   git clone [https://github.com/yourusername/shipping-optimizer.git](https://github.com/yourusername/shipping-optimizer.git)
   cd shipping-optimizer

```

2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the app:**
```bash
python app.py

```


The app will be available at `http://127.0.0.1:5000`.

## ☁️ Deployment on Render

This app is ready for deployment on [Render](https://render.com).

1. Create a new **Web Service**.
2. Connect your GitHub repository.
3. Use the following settings:
* **Environment**: `Python`
* **Build Command**: `pip install -r requirements.txt`
* **Start Command**: `gunicorn app:app`



## 📄 License

This project is open-source and available under the MIT License.