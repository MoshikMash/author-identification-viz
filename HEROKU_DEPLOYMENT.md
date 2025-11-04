# Heroku Deployment Guide

## Important Note

Heroku removed their free tier in November 2022. You'll need a paid account ($5/month minimum) or consider free alternatives like Railway, Render, or Fly.io.

## Prerequisites

1. **Heroku account**: https://signup.heroku.com/
2. **Heroku CLI**: Install from https://devcenter.heroku.com/articles/heroku-cli
3. **Git** (already installed)

## Files Included

- `Procfile` - Tells Heroku how to run your app
- `requirements_app.txt` - Python dependencies
- `runtime.txt` - Python version
- `setup.sh` - Setup script for Streamlit config

## Deployment Steps

### Step 1: Install Heroku CLI

Download and install from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Login to Heroku

```bash
heroku login
```

This will open a browser to login.

### Step 3: Create Heroku App

```bash
cd deployment
heroku create your-app-name
```

Replace `your-app-name` with your desired app name (must be unique).

### Step 4: Deploy

```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main
```

### Step 5: Open Your App

```bash
heroku open
```

Your app will be available at: `https://your-app-name.herokuapp.com`

## Alternative: Free Deployment Options

Since Heroku isn't free, consider these alternatives:

### Railway.app (Free tier available)
- Similar to Heroku
- Free tier with limits
- Easy GitHub integration

### Render.com (Free tier available)
- Free tier for static sites and web services
- Easy deployment
- Auto-deploy from GitHub

### Fly.io (Free tier available)
- Free tier with limits
- Good for containerized apps

Would you like me to set up for Railway or Render instead? They're free and might avoid organization authorization issues.

