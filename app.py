import pyttsx3
from sanic import Sanic, Request
from sanic.response import file_stream, text, html
from sanic_ext import openapi

app = Sanic(__name__)
app.extend(cors_origin="*")

@app.get("/")
@openapi.summary(" ")
@openapi.description("Homepage Endpoint")
async def homepage(req):
    return html("<h2>Static homepage</h2>")


@app.post("/savefile")
@openapi.summary(" ")
@openapi.description("This endpoint requires a form input text with a name attribute of (txt) which the values will be collected and stored in a speech format")
async def savefile(req: Request):
    req.form
    user_form_detail = req.form.get("txt")
    engine = pyttsx3.init()
    engine.save_to_file(user_form_detail, 'test.mp3')
    engine.runAndWait()
    engine.stop()
    return text("Saved Successfully")


@app.get("/download")
@openapi.summary(" ")
@openapi.description("This endpoint requies a download button for downloading the the speech file")
async def sendtxtfile(req):
    return await file_stream("test.mp3", headers={"Content-Type": "audio/mpeg"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, fast=True, single_process=False, auto_reload=True)
