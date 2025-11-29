# Stake Claimer Backend (Telegram + Extension API)

Simple webhook server to collect Stake bonus codes from Telegram and deliver them to a browser extension.

## Endpoints
- `/webhook` - Telegram webhook receiver
- `/get-code` - Extension fetches latest bonus code

## Deploy to Render
1. Upload to GitHub
2. Go to Render → "New Web Service"
3. Connect repository
4. Build command:
