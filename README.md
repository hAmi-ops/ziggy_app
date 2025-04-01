# Ziggy - AI Social Media Assistant

Ziggy is an AI-powered social media assistant that helps you manage and optimize your social media presence. It includes features for post generation, hashtag suggestions, and comment response assistance.

## Features

- AI-powered content generation for multiple social media platforms
- Hashtag Wizard for finding relevant and trending hashtags
- Comment Assistant for crafting appropriate responses
- Modern, responsive web interface
- User authentication and data persistence
- Post scheduling capabilities

## Prerequisites

- Node.js >= 18.0.0
- Docker and Docker Compose (for local development)
- OpenAI API key
- Netlify account (for frontend hosting)
- Render account (for backend hosting)
- GitHub account

## Quick Start (Local Development)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ziggy.git
cd ziggy
```

2. Set up the frontend:
```bash
cd frontend
npm install
cp .env.example .env
```

3. Set up the backend:
```bash
cd ../
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

4. Start the development servers:

Backend:
```bash
uvicorn app.main:app --reload
```

Frontend (in a new terminal):
```bash
cd frontend
npm run dev
```

5. Access the development version:
- Frontend: http://localhost:5173
- API Documentation: http://localhost:8000/docs
- API Endpoint: http://localhost:8000/api

## Deployment

### 1. Deploy the Backend (Render)

1. Create a new Web Service on Render:
   - Sign up at https://render.com
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Configure the service:
     - Name: `ziggy-api`
     - Environment: `Python`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

2. Set up environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `DATABASE_URL`: Your PostgreSQL URL (you can use Render's PostgreSQL)
   - `SECRET_KEY`: A secure random string
   - `CORS_ORIGINS`: Your Netlify app URL (e.g., https://your-app.netlify.app)

3. Deploy the service
   - Your API will be available at `https://ziggy-api.onrender.com`

### 2. Deploy the Frontend (Netlify)

1. Update the frontend environment:
```bash
cd frontend
cp .env.production.example .env.production
# Edit .env.production with your Render API URL
```

2. Push your code to GitHub:
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

3. Deploy to Netlify:
   - Sign up at https://netlify.com
   - Click "New site from Git"
   - Select your GitHub repository
   - Configure build settings:
     - Base directory: `frontend`
     - Build command: `npm install && npm run build`
     - Publish directory: `dist`
   - Add environment variables:
     - `VITE_API_URL`: Your Render API URL

4. Your site will be live at:
   - Frontend: https://your-app.netlify.app
   - API: https://ziggy-api.onrender.com

### Verifying the Deployment

1. Visit your Netlify URL (e.g., https://your-app.netlify.app)
2. Test the API connection at https://your-app.netlify.app/api/health
3. Try generating a post or using the Hashtag Wizard

## Environment Variables

### Frontend (.env.production)
```
VITE_API_URL=https://ziggy-api.onrender.com
VITE_APP_NAME=Ziggy
VITE_APP_DESCRIPTION="AI Social Media Assistant"
```

### Backend (.env)
```
OPENAI_API_KEY=your-api-key
DATABASE_URL=postgresql://user:pass@host:5432/dbname
SECRET_KEY=your-secret-key
CORS_ORIGINS=https://your-app.netlify.app
```

## Support

For support:
1. Check the [documentation](https://your-app.netlify.app/docs)
2. Open an issue in the GitHub repository
3. Contact the maintainers at support@yourdomain.com

## License

This project is licensed under the MIT License - see the LICENSE file for details. 