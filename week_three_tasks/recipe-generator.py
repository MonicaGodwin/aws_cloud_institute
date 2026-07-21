# Import the required libraries for AWS service interaction and JSON processing.
import boto3
import json

# Connect to Amazon Bedrock.
bedrock = boto3.client("bedrock-runtime")

while True:
    pet_type = input("Enter your pet type: ").lower()
    if pet_type == "close":
        break

    if pet_type != "dog" and pet_type != "cat":
        print("pet must be a CAT or a DOG")
        continue
   
    ingredient = input("Enter the ingredients you have: ")
    allergies = input("Enter pet allergy if they is one: ")

    prompt = f"Generate a recipe for my dog: a {pet_type} with this ingredients.NB: he's allergic to {allergies}"
    max_token = 512
    temperature = 0.7

    request = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "inferenceConfig": {
        "maxTokenCount": max_token,
        "temperature": temperature,
        "topP": 0.9,
        }
    }
    response = bedrock.invoke_model(
        modelId="amazon.nova-lite-v1:0",
        body=json.dumps(request)
    )
    response_body = json.loads(response["body"].read())
    # Process and display the recipe.
    response_body = json.loads(response["body"].read())
    print(f"\nRecipe generated with {max_token} max tokens and a temperature of {temperature}.\n")
    if response_body["output"]["message"]["content"][0]["text"].startswith(" - The generated text has been blocked"):
        print("I apologize, but I cannot provide specific pet food recipes. For your pet's safety, please consult with a veterinarian about proper nutrition and diet plans.")
    else:
        print(response_body["output"]["message"]["content"][0]["text"])


