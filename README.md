
# 📱 Django SPA with Lazy Loading  
*A beginner-friendly Single Page Application implementing lazy loading of posts, built with Django.*

## ✨ Features  
- **Lazy Loading**: Dynamically loads posts as the user scrolls (JavaScript + Django API).  
- **SPA Architecture**: Single-page experience with no full page reloads.  

## 🛠️ Tech Stack  
- **Backend**: Django (Python)  
- **Frontend**: Vanilla JavaScript (no frameworks)  
- **Database**: SQLite (default)  

## 🚀 Setup  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/saad9797/SPA-in-Django.git  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Run migrations:  
   ```bash  
   python manage.py migrate  
   ```  
4. Start the server:  
   ```bash  
   python manage.py runserver  
   ```  
5. Open `http://localhost:8000` in your browser.  

## 🔍 How It Works  
1. **Initial Load**: Renders first 10 posts via Django template.  
2. **Lazy Loading**: On scroll, JavaScript fetches next posts via API  
3. **API Endpoint**: Returns JSON data (new posts).  
