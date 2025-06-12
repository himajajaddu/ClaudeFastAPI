import boto3, json, os
from dotenv import load_dotenv

load_dotenv()

bedrock = boto3.client(
    "bedrock-runtime",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

def invoke_claude(prompt: str, model_id: str = "arn:aws:bedrock:us-east-1:304358820241:inference-profile/us.anthropic.claude-opus-4-20250514-v1:0") -> str:
    prefixed_prompt = f"Human: {prompt}\n\nAssistant:"
    response = bedrock.invoke_model(
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
             "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 1000,
            "temperature": 0.3,
            "system": ""
        })
    )
    


    return json.loads(response["body"].read())["content"][0]["text"]