
import boto3
import json
import base64
import io
from gtts import gTTS
import autoplay
from io import BytesIO

aws_bedrock = boto3.client('bedrock-runtime')
bedrock_model_id = "stability.stable-diffusion-xl-v1"
def decode_image_from_response(response):
    
    #Decodes the image from the model's response.
    
    response_body = json.loads(response['body'].read())
    image_artifacts = response_body['artifacts']
    image_bytes = base64.b64decode(image_artifacts[0]['base64'])
    return BytesIO(image_bytes)

def generate_image(prompt, style):
    """
    Generates an image based on the provided prompt and style.
    """
    
    request_payload = json.dumps({
        "text_prompts": [{"text": f"{style} {prompt}"}],
        "cfg_scale":9, #default fidelity to prompt
        "steps": 50, # default detail level
    })
    
    model_response = aws_bedrock.invoke_model(body = request_payload, modelId = bedrock_model_id)
    return decode_image_from_response(model_response)
