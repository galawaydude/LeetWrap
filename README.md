# LeetWrap

## Description

Leetwrap is an api for leetcode, I built this using the fastapi framework. You can use this API for getting most of the information you may need from leetcode.
Use it for extensions, or any applications you are working on.

## Info you can get

- Fetch question details
- Retrieve user stats
- Get submission lists
- Access language information
- Fetch recent accepted submissions
- Get the Question of the Day
- Retrieve streak information
- Access question hints
- Manage user favorites
- Fetch panel question lists
- Track user session progress
- Manage question tags, notes, and status

## Installation and Usage

### Using Docker

1. Pull the Docker image from Docker Hub:
   ```
   docker pull galawaydude/leetwrap:latest
   ```

2. Run the container:
   ```
   docker run -d -p 8000:8000 galawaydude/leetwrap:latest
   ```

3. Access the API documentation:
   Open your browser and go to `http://localhost:8000/docs` to see the Swagger UI with all available endpoints.

### Manual Installation

If you prefer to run the application without Docker:

1. Clone the repository:
   ```
   git clone https://github.com/galawaydude/LeetWrap.git
   cd LeetWrap
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Start the server:
   ```
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

4. Access the API documentation:
   Open your browser and go to `http://localhost:8000/docs` to see the Swagger UI with all available endpoints.


## Authentication

Some endpoints require authentication using a LeetCode session cookie and a csrf token. Include the `leetcodeSession` in the request body for these requests.
Example:

```
{
  "leetcodeSession": "your_leetcode_session_cookie",
  "csrfToken": "your_csrf_token"
}
```

# note
working on hosting this on azure, till then render should do the work. here is the link: https://leetwrap-3.onrender.com
more endpoints may come.
