from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.api.endpoints import questionEndpoints, userEndpoints, submissionEndpoints, miscEndpoints

app = FastAPI(
    title="LeetCode API Wrapper",
    description="A FastAPI wrapper for LeetCode's GraphQL API",
)

@app.get("/", response_class=HTMLResponse)
def rootMessage():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First FastAPI Project</title>
    <style>
        body {
            background-color: #000;
            color: #0f0;
            font-family: 'Courier New', Courier, monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            border: 2px solid #0f0;
            padding: 20px;
            max-width: 80%;
        }
        .prompt {
            font-size: 1em;
            display: inline-block;
            overflow: hidden;
            white-space: nowrap;
            margin: 0;
            letter-spacing: .1em;
            border-right: .15em solid #0f0;
            animation: 
                typing 3s steps(40, end),
                blink-caret .75s step-end infinite;
        }
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: #0f0; }
        }
    </style>
</head>
<body>
    <div class="container">
        <p class="prompt">Oi, let's go, my first, from scratch project</p>
    </div>
</body>
</html>
    """
    return HTMLResponse(content=html_content)

app.include_router(questionEndpoints.router, prefix="/api", tags=["questions"])
app.include_router(userEndpoints.router, prefix="/api", tags=["users"])
app.include_router(submissionEndpoints.router, prefix="/api", tags=["submissions"])
app.include_router(miscEndpoints.router, prefix="/api", tags=["miscellaneous"])