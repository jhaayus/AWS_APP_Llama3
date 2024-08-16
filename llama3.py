import boto3
import json 

prompt_data = "what is capital of india? and what is population of India?"

bedrock = boto3.client(service_name="bedrock-runtime")
payload = {
    "prompt": "[INST]" + prompt_data + "[/INST]",
    "max_gen_len": 512,
    "temperature": 0.1,
    "top_p": 0.9
}

body = json.dumps(payload)
model_id = "meta.llama3-70b-instruct-v1:0"


response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)
    
response_body = json.loads(response['body'].read().decode('utf-8'))
response_text = response_body.get('generation', 'No generation found')
print("Response text:", response_text)
