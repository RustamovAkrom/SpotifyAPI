# SpotifyAPI

__A REST API built with Django for working with Spotify data. Provides endpoints to access, store, and manage tracks, playlists, and user information. Supports asynchronous tasks, authentication, and automatic API documentation.__

---

## ⚡ Key Features

1. **Spotify Data Access:** Retrieve information about tracks, playlists, and users through structured API endpoints.
2. **JWT Authentication:** Secure your API with JSON Web Tokens for user login and access control.
3. **Asynchronous Tasks:** Background tasks using Celery for periodic data updates or heavy processing.
4. **Database Integration:** Uses PostgreSQL for efficient storage and management of Spotify data.
5. **Interactive API Docs:** Includes Swagger/OpenAPI interface for testing and exploring endpoints.
6. **Responsive Design:** API documentation and interface are fully usable on desktop and mobile devices.

---

## 🏁 Getting Started

* **Requirements:** Python 3.8+, Django, PostgreSQL, Redis (for Celery tasks)
* **Installation:** Install dependencies from `requirements.txt`.
* **Configuration:** Set up PostgreSQL database, environment variables, and Celery if using asynchronous tasks.
* **Running the Project:** Start Django server to access API and interactive documentation.

---

## 🛠 How to Use

1. **Authenticate Users:** Obtain JWT tokens to access protected endpoints.
2. **Query Spotify Data:** Use endpoints to get tracks, playlists, or user information.
3. **Manage Background Tasks:** Optional Celery integration for updating data automatically.
4. **Explore & Test API:** Use Swagger UI or OpenAPI docs to interact with the API in a browser.

---

## 🌐 API Documentation

* **Swagger UI / OpenAPI:** Fully interactive, responsive documentation available in the project for testing endpoints.
* **Mobile-Friendly:** Works perfectly on any device.

---

## 🎯 Summary

SpotifyAPI is a **powerful and flexible API** for developers who want to integrate Spotify data into applications, perform automated tasks, and explore API endpoints easily through a responsive interface.
