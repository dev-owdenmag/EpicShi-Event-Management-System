# Event Management & Guest Services System

## Overview

The **Event Management & Guest Services System** is a **luxurious, high-end** event management platform designed for seamless guest registration, RSVP tracking, and event coordination. It includes dynamic form creation, branding customization, real-time reports, and secure authentication.

## Features

**Dynamic RSVP Forms** – Clients can create custom RSVP forms with predefined data fields.  
**Guest Code Verification** – Secure guest check-ins using unique codes.  
**Admin & Client Dashboards** – Separate portals for managing events and guests.  
**JWT Authentication** – Secure login with role-based access.  
**Activity Logs & Reports** – Exportable logs in Excel, CSV, and PDF formats.  
**Branding & Customization** – Clients can upload logos and set colors for their dashboard.  
**Security Measures** – Password rules, account lockout after failed attempts, and email notifications.  
**Dockerized Deployment** – Easily deployable on **Google Cloud**.  

## Tech Stack

- **Backend**: Flask (Python), MySQL, JWT Authentication
- **Frontend**: React, Vite
- **Deployment**: Docker, Nginx, Google Cloud
- **Other Tools**: ProPresenter, vMix, Resolume (for event visuals)

## Installation

### Prerequisites
- Docker & Docker Compose installed  
- MySQL database setup  
- `.env` file configured for database credentials  

### Setup Instructions

1. **Clone the Repository**  
   ```sh
   git clone https://github.com/yourusername/event-management-system.git
   cd event-management-system
