from app.services.ai_service import call_ai
from app.services.fallback_service import fallback_response

async def process_query(query: str):
    try:
        ai_result = await call_ai(query)

        if ai_result is None:
            raise Exception("AI returned null")

        return ai_result

    except Exception as e:
        print(f"❌ AI failed: {e}")
        print("⚡ Switching to fallback")

        return fallback_response(query)