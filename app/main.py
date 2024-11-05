from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import questionEndpoints, userEndpoints, submissionEndpoints, miscEndpoints
import os

app = FastAPI(
    title="LeetWrap",
    description="A FastAPI wrapper for LeetCode's GraphQL API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get port from environment variable or use default
port = int(os.getenv("PORT", 8000))

@app.get("/", response_class=HTMLResponse)
def root_message():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LeetWrap</title>
        <style>
            body {
                background-color: #000;
                color: #fff;
                font-family: 'Courier New', Courier, monospace;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                padding: 20px;
                box-sizing: border-box;
            }
            .content {
                max-width: 800px;
                width: 100%;
            }
            h1, h2 {
                text-align: center;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                margin-bottom: 10px;
                overflow: hidden;
                white-space: nowrap;
                opacity: 0;
                animation: typing 1s steps(40, end) forwards, blink-caret 1s step-end infinite;
            }
            @keyframes typing {
                from { width: 0; opacity: 1; }
                to { width: 100%; opacity: 1; }
            }
            @keyframes blink-caret {
                from, to { border-color: transparent; }
                50% { border-color: #0f0; }
            }
            a {
                color: #0f0;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>LeetWrap</h1>
            <h2>API Features:</h2>
            <ul>
                <li>Question Information</li>
                <li>Similar Questions</li>
                <li>Question Statistics</li>
                <li>Question Hints</li>
                <li>Topic Tags</li>
                <li>Question Notes</li>
                <li>Question Status</li>
                <li>Problem Set Lists</li>
                <li>Daily Coding Challenge</li>
                <li>User Submissions</li>
                <li>User Profile Data</li>
            </ul>
            <p style="text-align: center;">
                <a href="/docs">API Documentation</a> | 
                <a href="/redoc">ReDoc Documentation</a>
            </p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Include routers
app.include_router(
    questionEndpoints.router,
    prefix="/api",
    tags=["questions"]
)

app.include_router(
    userEndpoints.router,
    prefix="/api",
    tags=["users"]
)

app.include_router(
    submissionEndpoints.router,
    prefix="/api",
    tags=["submissions"]
)

app.include_router(
    miscEndpoints.router,
    prefix="/api",
    tags=["miscellaneous"]
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        workers=4
    )
