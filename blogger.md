### Create a Google App from the Developers Console with Blogger API Enabled

1. Login to https://console.developers.google.com
2. Create a new application.
3. Navigate to your application's dashboard.
4. Click "Enable and manage APIs".
5. Click on "Blogger API" under "Social APIs".
6. Click "Enable API". You will now see: "This API is enabled, but you can't use it in your project until you create credentials."
7. Click "Go to Credentials".
8. Use the default option for "Which API are you using?" (Blogger API v3).
9. For "Where will you be calling this API from?" choose "Web server".
10. For "What data will you be accessing?" choose "User data".
11. Click "What credentials do I need?"
12. Give the OAuth 2.0 client ID a name ("Test Blog Coders Clan").
13. Set the "Authorized JavaScript origins" to "http://localhost:8080".
14. Set the "Authorized redirect URIs" to "http://localhost:8080/".
15. Set the email address and the Product Name shown to users ("Test Blog Coders Clan").
16. Feel free to set more customization options such as the hompage, logo, etc.
17. Download the credential information in JSON format. Rename it to "credentials.json".
18. Click Done.