
# Sweet Shop Management System - Frontend

This is the React + TypeScript frontend application for the Sweet Shop Management System, built with Vite.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Available Scripts](#available-scripts)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Styling and UI](#styling-and-ui)
- [Testing](#testing)
- [Linting and Formatting](#linting-and-formatting)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This frontend application provides a Single Page Application (SPA) for managing sweets, user authentication, and admin functionalities in a sweet shop. It uses modern React with TypeScript, React Router for navigation, Axios for API communication, and a pastel-themed design system called “Sweet Serenity.”

---

## Features

- User registration and login with JWT authentication
- Browse, search, and purchase sweets
- Admin panel for adding, updating, and deleting sweets
- Responsive design with a modern pastel UI
- Context-based state management with reusable custom hooks
- Robust form validation with TypeScript typings
- API abstraction for clean backend communication

---

## Prerequisites

- Node.js v14 or higher
- npm v6 or higher (or yarn if preferred)

---

## Getting Started

1. Clone the repository:
```
git clone https://github.com/your-username/sweet-shop-frontend.git
cd sweet-shop-frontend
```

2. Install dependencies:
```
npm install
````

3. Set up environment variables:
- Create a `.env` file in the project root.
- Add your backend API URL:
  ```
  VITE_API_URL=http://localhost:8000/api
  ```

4. Run the development server:
```
npm run dev
```

5. Open `http://localhost:5173` in your browser to start using the app.

---
## Available Scripts

- `npm run dev`: Starts the development server with hot reload
- `npm run build`: Builds the app for production in the `dist/` folder
- `npm run preview`: Previews the production build locally
- `npm run lint`: Runs ESLint across the codebase
- `npm run format`: Runs Prettier to format source files
- `npm run test`: Runs unit tests using Vitest

---

## Project Structure

```

frontend/
├─ public/
│ ├─ index.html # Main HTML template
│ ├─ favicon.ico # Favicon icon
│ ├─ assets/ # Static assets like images, fonts, icons
├─ src/
│ ├─ api/ # API modules for backend interaction
│ ├─ components/ # Reusable UI components and forms
│ ├─ contexts/ # React Context providers and hooks
│ ├─ hooks/ # Custom React hooks for state and side-effects
│ ├─ pages/ # Route components representing pages
│ ├─ styles/ # CSS files with base and component styles
│ ├─ utils/ # Helper functions and validators
│ ├─ App.tsx # Root React component with routing
│ ├─ main.tsx # ReactDOM render entry point
├─ .env # Environment variables (ignored in git)
├─ package.json # Project configuration, scripts, and dependencies
├─ tsconfig.json # TypeScript configuration with project references
├─ vite.config.ts # Vite build tool configuration

```

---

## Environment Variables

- `VITE_API_URL`: The base URL for the backend API. Defaults to `http://localhost:8000/api` if not set.

---

## Styling and UI

- Uses a pastel color palette named “Sweet Serenity” for a fresh, modern look.
- Base styles and variables defined in `src/styles/base.css`.
- Component-level styles in `src/styles/components.css`.
- Fonts loaded from Google Fonts ("Poppins").
- Responsive design ensures usability across devices.

---

## Testing

- Unit tests are written with [Vitest](https://vitest.dev/).
- Test files colocated with corresponding components inside the `src` folder.
- Run tests with:
```
npm run test
```

---

## Linting and Formatting

- Code quality ensured via ESLint and Prettier.
- Run lint:
```
npm run lint
```
- Format code:
```
npm run format
```

---

## Contributing

Contributions are welcome! Please open issues or pull requests on the GitHub repository.

---

## License

This project is licensed under the MIT License.

---

*Built with care and modern best practices by the Zaud Rehman.*


