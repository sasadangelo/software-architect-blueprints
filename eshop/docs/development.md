# How to Run the eShop Prototype

This guide explains how to start both the backend and the UI for the eShop prototype.

---

## 1. Backend

1. Open a terminal and go to the `backend` folder:

```bash
cd backend
```

2. Install dependencies:

```bash
npm install
```

3. Start the backend server (runs on port 3000 by default):

```bash
npm run dev
```

You should see output indicating that the backend is running.

## 2. UI (Frontend)

1. Go to the ui folder:

```bash
cd ui
```

2. Create a `.env` file in the ui folder with the following content:

```bash
PORT=3001
```

This ensures the frontend runs on port 3001.

3. Install dependencies:

```bash
npm install
```

4. Start the UI:

```bash
npm start
```

The frontend will be available at: http://localhost:3001

All API calls to /api/... will automatically be proxied to the backend running on port 3000.

* **Notes**:
* Make sure the backend is running before starting the UI.
* If the default ports are already in use, you can change them in the .env file for the UI or in the backend configuration.
* This setup uses an in-memory store; all data is lost when the servers stop.