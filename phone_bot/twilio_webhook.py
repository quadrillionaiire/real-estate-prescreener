from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# ----- VOICE CALL HANDLER -----
@app.route("/call", methods=["POST"])
def handle_call():
    resp = VoiceResponse()
    resp.say("Hello! I am your real estate assistant. Are you buying or selling a home today?")
    resp.pause(length=1)
    resp.say("Please say: I am buying, or, I am selling.")
    return str(resp)


# ----- SMS HANDLER -----
@app.route("/sms", methods=["POST"])
def handle_sms():
    incoming = request.form.get("Body", "").strip()

    reply = MessagingResponse()
    reply.message(f"You said: {incoming}. I can help pre-screen you for a home or listing.")

    return str(reply)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
