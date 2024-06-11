import google.generativeai as genai
import json

genai.configure(api_key='AIzaSyCs_q7nIoDNyST3L8A8c_kBb2Tkd9OhJpk')

def getRecipes(ingredients):
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }
  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
  ]


  model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
  )
  
  try:
    response = model.generate_content("Give me the list of dishes and step by step recipe of how I can make using the following items: "
                                      +str(ingredients)
                                      + " Give the output in the json of having one field list which is a list of Recipe = { dish_name: str , ingredients_required: numbered list, recipe: bullet list }  with only json part and without the text and quotes before or after")
    
    start_index = response.text.find('{')
    end_index = response.text.rfind('}') + 1
    jsonresponse = json.loads(response.text[start_index:end_index])
  except:
    jsonresponse = {
    "list": [
      {
        "dish_name": "Sorry, some unknown error occured!",
        "ingredients_required": [" "],
        "recipe": [" "]
      }
    ]
  }
  return jsonresponse



import google.generativeai as genai

genai.configure(api_key='AIzaSyCs_q7nIoDNyST3L8A8c_kBb2Tkd9OhJpk')

def getNutrition(recipeName):
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }
  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
  ]


  model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
  )
  
  try:
    response = model.generate_content("Can you give me the nutritional breakdown of "+ str(recipeName) + ". It should include all the nutrients available in the meal, and the ones that are not"
                                      + " Give the output in the format as List<Recipe> where Recipe = { dish_name: str , nutreints_present: bullet list, nutreints_absent: bullet list }") 
    start_index = response.text.find('{')
    end_index = response.text.rfind('}') + 1
    jsonresponse = json.loads(response.text[start_index:end_index])
  except:
    jsonresponse = {
    "list": [
      {
        "dish_name": "Sorry, some unknown error occured!",
        "nutreints_present": [" "],
        "nutreints_absent": [" "]
      }
    ]
  }
  return jsonresponse

print(getRecipes(["tomato", "onion", "potato", "soyabean", "soya sauce", "salt", "pepper", "chilli powder", "ginger", "garlic", "coriander", "cumin", "turmeric", "garam masala", "oil"]))
print(getNutrition("Simple Potato & Onion Curry"))