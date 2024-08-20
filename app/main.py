from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import questionEndpoints, userEndpoints, submissionEndpoints, miscEndpoints
import os

app = FastAPI(
    title="LeetWrap",
    description="A FastAPI wrapper for LeetCode's GraphQL API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
)


port = int(os.getenv("PORT", 8000))

@app.get("/", response_class=HTMLResponse)
def rootMessage():
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
            li:nth-child(1) { animation-delay: 0s; }
            li:nth-child(2) { animation-delay: 0s; }
            li:nth-child(3) { animation-delay: 0s; }
            li:nth-child(4) { animation-delay: 0s; }
            li:nth-child(5) { animation-delay: 0s; }
            li:nth-child(6) { animation-delay: 0s; }
            li:nth-child(7) { animation-delay: 0s; }
            li:nth-child(8) { animation-delay: 0s; }
            li:nth-child(9) { animation-delay: 0s; }
            li:nth-child(10) { animation-delay: 0s; }
            li:nth-child(11) { animation-delay: 0s; }
            li:nth-child(12) { animation-delay: 0s; }
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
            <p>This is an API that provides access to LeetCode information.</p>
            <h2>Available Information:</h2>
            <ul>
                <li>Daily coding challenge questions</li>
                <li>User's favorite questions</li>
                <li>User's session progress</li>
                <li>User's streak information</li>
                <li>User's recent accepted submissions</li>
                <li>User's public profile information</li>
                <li>Detailed question information</li>
                <li>Similar questions</li>
                <li>Question statistics</li>
                <li>Submission details</li>
                <li>Question hints and notes</li>
                <li>User's question status</li>
            </ul>
            <p>Swagger UI Documentation, <a href="/docs">/docs</a>.</p>
            <p>More may come</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

app.include_router(questionEndpoints.router, prefix="/api", tags=["questions"])
app.include_router(userEndpoints.router, prefix="/api", tags=["users"])
app.include_router(submissionEndpoints.router, prefix="/api", tags=["submissions"])
app.include_router(miscEndpoints.router, prefix="/api", tags=["miscellaneous"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)