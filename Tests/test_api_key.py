from dotenv import load_dotenv
import os
import openai

from DatasetManagment.augmentation import DatasetAugmentation

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


augmentation_instance = DatasetAugmentation()
response = augmentation_instance.generate_response("eeeeeeej what is going on", 0.9, 1)
print(response)

response = augmentation_instance.generate_response("eeeeeeej what is going on", 0.8, 2)
print(response)




