# Technical Approach & Architectural Decisions

## 1. Project Overview
The goal was to build a cohesive **Crypto Portfolio Tracker** that demonstrates full-stack capabilities using Python (Django) and PostgreSQL. The application follows the MVC (Model-View-Controller) architecture, exposing a REST API for asset management and a server-side rendered dashboard for visualization.

## 2. Technology Stack Selection
*   **Django & DRF:** Selected for rapid development and built-in security features. Django REST Framework (DRF) was used to ensure the API adheres to RESTful standards (GET, POST, PUT, DELETE).
*   **PostgreSQL:** Chosen over SQLite to mimic a production environment. PostgreSQL handles concurrent data efficiently and allows for robust data typing.
*   **CoinGecko API:** Used for real-time price data because it offers a reliable public endpoint without requiring complex API key management for a demo application.
*   **Chart.js:** Selected as a lightweight, flexible frontend library to visualize data without the overhead of setting up a complex Single Page Application (React/Vue) for a simple dashboard.

## 3. Key Design Decisions

### A. Dynamic vs. Stored Valuation
**Decision:** I chose **not** to store the `current_value` of the assets in the database.
**Reasoning:** Cryptocurrency prices fluctuate constantly. Storing a "current value" would result in stale data almost immediately. Instead, I store the `quantity` and `purchase_price`. The application calculates the *Current Value* dynamically during the API Read operation (`GET`).

### B. Serializer Logic
**Decision:** Integrated the external API call directly within the Django Serializer using a `SerializerMethodField`.
**Reasoning:** This allows the API to return a cohesive JSON object that includes both the database data (Symbol, Quantity) and the computed external data (Current Value). This reduces the complexity on the frontend—the client simply consumes the JSON without needing to perform its own math or external API calls.

### C. Modular Code Structure
**Decision:** Isolated the external API logic into a separate `utils.py` file.
**Reasoning:** This adheres to the "Separation of Concerns" principle. If we switch API providers (e.g., from CoinGecko to Binance) in the future, we only need to modify `utils.py`, keeping the Views and Models untouched.

## 4. Future Improvements (Production Readiness)
If this were a production application, I would implement the following:

1.  **Caching (Redis):** Currently, every page load triggers a request to CoinGecko. In production, this would hit rate limits. I would implement Redis to cache price data for 5-10 minutes.
2.  **Environment Variables:** Sensitive data (Database credentials, `DEBUG` mode) would be moved to a `.env` file using `python-dotenv`.
3.  **Asynchronous Tasks (Celery):** For heavy portfolio updates, price fetching should be moved to a background worker to prevent blocking the main web request.