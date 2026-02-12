from fastapi import FastAPI
import httpx

app = FastAPI()

WEBHOOK_URL = "https://discord.com/api/webhooks/1471316904001015934/QpWzcRqOoB4OEUp7Npt7xbOsN-lcMZIYFslO9mEhj3_jX9-jqsngeju7nqNbnf4_GiwE/github"

@app.post("/deploy")
async def deploy():
    async with httpx.AsyncClient() as client:
        await client.post(
            WEBHOOK_URL,
            json={"content": "Deploy completed successfully 🚀"}
        )

    return {"status": "ok"}
