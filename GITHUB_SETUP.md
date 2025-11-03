# GitHub Setup Instructions

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. **Repository name**: e.g., `author-identification-viz` or `visualization-app`
3. **Description**: "Streamlit app for author identification visualizations"
4. **Visibility**: Choose Public or Private
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

## Step 2: Connect Local Repository to GitHub

After creating the repo on GitHub, you'll see commands. Use these:

```bash
# Make sure you're in the deployment folder
cd deployment

# Add the remote (replace YOUR_USERNAME and YOUR_REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Or if you prefer SSH:
# git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 3: Verify Connection

```bash
git remote -v
```

Should show your GitHub repository URL.

## Step 4: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Main file path: `visualization_app.py`
6. Branch: `main`
7. Click "Deploy!"

## Troubleshooting

If you get authentication errors:
- Use GitHub Personal Access Token instead of password
- Or use SSH keys

