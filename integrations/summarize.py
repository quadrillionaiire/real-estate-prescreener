from agent.extractor import extract_structured

SUMMARY_PROMPT = """
Summarize the conversation in 5 bullets. Also extract: intent, budget, move_timeline, urgency.
Conversation:
{transcript}
Return JSON.
"""

def summarize_transcript(transcript):
    prompt = SUMMARY_PROMPT.format(transcript=transcript)
    return extract_structured(prompt)
