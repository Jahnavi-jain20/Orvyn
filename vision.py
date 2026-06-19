from PIL import Image
from google import genai

from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_image(
    image_path,
    question="Describe this image in detail."
):

    try:

        image = Image.open(image_path)

        # Try the preferred model first
        try:

            response = client.models.generate_content(

                model="gemini-2.5-flash",

                contents=[question, image]

            )

        except Exception:

            # Fallback if the first model is busy
            response = client.models.generate_content(

                model="gemini-2.0-flash",

                contents=[question, image]

            )

        if hasattr(response, "text") and response.text:

            return response.text

        return "I couldn't analyze the image."

    except Exception as e:

        print("Vision Error:", e)

        return (
            "⚠️ The image analysis service is temporarily unavailable.\n"
            "Please try again in a few moments."
        )