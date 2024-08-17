# LeetWrap

## Description

This project is a FastAPI-based wrapper for LeetCode's GraphQL API. It provides a set of endpoints that allow users to interact with various LeetCode features, including fetching question details, user stats, submission lists, and more.

## Features

- Fetch question details
- Retrieve user stats
- Get submission lists
- Access language information
- Fetch recent accepted submissions
- Get the Question of the Day (QOTD)
- Retrieve streak information
- Access question hints
- Manage user favorites
- Fetch panel question lists
- Track user session progress
- Manage question tags, notes, and status

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/galawaydude/LeetWrap.git
   cd LeetWrap
   ```

2. Install dependencies:
   ```
   pipenv install
   ```

3. Activate the virtual environment:
   ```
   pipenv shell


## Usage

1. Start the server:
   ```
   uvicorn app.main:app --reload
   ```

2. Access the API documentation:
   Open your browser and go to `http://localhost:8000/docs` to see the Swagger UI with all available endpoints.

## API Endpoints

Here are some of the main endpoints provided by this API wrapper:

### Question Details

- `POST /api/question`: Get details of a specific question
- `POST /api/similarQuestions`: Get similar questions for a given question

### User Stats

- `POST /api/stats`: Get question stats
- `POST /api/user-session-progress`: Get user session progress

### Submissions

- `POST /api/submissionList`: Get submission list for a question
- `POST /api/recentAc`: Get recent accepted submissions

### Question of the Day

- `GET /api/question-of-today`: Get the current Question of the Day

### Streak Information

- `POST /api/streak-counter`: Get user's streak information

### Question Hints

- `POST /api/question-hints`: Get hints for a specific question

### User Favorites

- `POST /api/user-favorites`: Get user's favorite questions

### Panel Question List

- `POST /api/panel-question-list`: Get panel question list

### Question Tags, Notes, and Status

- `POST /api/single-question-topic-tags`: Get topic tags for a question
- `POST /api/question-note`: Get or set question notes
- `POST /api/user-question-status`: Get question status for a user

## Authentication

Some endpoints require authentication using a LeetCode session cookie and a csrf token. Include the `leetcodeSession` in the request body for authenticated endpoints.

Example:
```json
{
  "titleSlug": "two-sum",
  "leetcodeSession": "your_leetcode_session_cookie;your_csrf_token"
}
```