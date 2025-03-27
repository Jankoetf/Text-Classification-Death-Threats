import openai
import pandas as pd
import random

from DatasetManagment.keyboard_neighborhood import keyboard_neighborhood
from DatasetManagment.dataset_const import (TEST_DATASETS_ROOT, DATASETS_ROOT)

class DatasetAugmentation:
    """
    A class for augmenting datasets through paraphrasing and noise injection.
    
    This class utilizes the OpenAI API to paraphrase sentences and adds typographical errors to simulate noise
    """
    def __init__(self, keyboard_neighborhood = keyboard_neighborhood, engine = "gpt-4o", root_relative_path = TEST_DATASETS_ROOT):
        self.engine = engine
        self.keyboard_neighborhood = keyboard_neighborhood
        self.root_relative_path = root_relative_path
        self.sheet_name_default = "All"
        self.prompt_setup()

    def generate_response(self, prompt, temperature = 0.8, n_of_responses = 1):
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256,
            n=n_of_responses,
            temperature=temperature,
            top_p = 1
        )

        responses = [choice['message']['content'].strip() for choice in response['choices']]
        return responses
    
    def path_from_name(self, dataset_name):
        return self.root_relative_path + dataset_name + ".xlsx"

    def prompt_setup(self):
        self.promt_intro = "Parafraziraj sledeću rečenicu tako da može zadržati ili promeniti značenje, ali je važno da priroda rečenice "

        conditional_part_contex_normal = "(rečenica ne predstavlja pretnju fizičkim nasiljem niti nagovaranje na isto) ostane ista. "
        conditional_part_contex_violence = "(rečenica predstavlja pretnju fizičkim nasiljem ili nagovaranje na isto) ostane ista. "
        self.conditional_part_contex = [conditional_part_contex_normal, conditional_part_contex_violence]

        self.prompt_middle = "Molim te da koristiš sinonime, promeniš imena, brojeve, redosled reči, i preformulišeš delove rečenice.\n"

        conditional_part_example_normal =  "Na primer ako ti dam rečenicu: Idemo na piknik sutra u 6 Stefane. Tvoj odgovor može biti: Nikola, planiramo izlet za sutra uveče u 8!."
        conditional_part_example_violence =  "Na primer ako ti dam rečenicu: Prebiću te večeras Marija. Tvoj odgovor može biti: Jovane razbuću ti nos kasnije."
        self.conditional_part_example = [conditional_part_example_normal, conditional_part_example_violence]

    def create_prompt(self, old_text, old_label):
        new_prompt = self.promt_intro + self.conditional_part_contex[old_label] + self.prompt_middle + self.conditional_part_example[old_label] + f"\nRečenica: {old_text}"
        return new_prompt

    def new_dataset_by_paraphrazing(self, original_dataset, new_dataset_name, hyperparams = None):
        """
        Create a new dataset by paraphrasing sentences from the original dataset.

        For each sentence in the original dataset, the method generates multiple paraphrased versions
        using various temperature settings, and saves the new dataset to an Excel file.
        """
        texts, labels = [], []
        if hyperparams == None:
            n_responses_per_request = 2
            list_of_temperatures = [0.75, 0.85, 0.95]
        else:
            n_responses_per_request = hyperparams["n_responses_per_request"]
            list_of_temperatures = hyperparams["list_of_temperatures"]

        n_of_temperatures = len(list_of_temperatures)
        augmentation = n_responses_per_request*n_of_temperatures

        for item in original_dataset:
            old_text, old_label = item["text"], item["label"]
            texts.append(old_text)
            labels.append(old_label)
            for temperature in list_of_temperatures:
                prompt = self.create_prompt(old_text, old_label)
                new_texts = self.generate_response(prompt, temperature, n_responses_per_request)
                texts.extend(new_texts)
            labels.extend([old_label]*augmentation)

        df = pd.DataFrame({
          'text': texts,
          'label': labels
        })

        df.to_excel(self.path_from_name(new_dataset_name), sheet_name=self.sheet_name_default, index=False)

    def add_typo(self, original_text, typo_prob = 0.03):
        """
        Introduce typographical errors into the original text.

        Each character in the text has a probability (typo_prob) of being replaced with a neighboring key.

        Args:
            original_text (str): The text to which typos will be added.
            typo_prob (float): The probability for each character to be replaced by a typo.

        Returns:
            tuple: A tuple containing the new text with typos and the count of typos added.
        """
        typos_count = 0
        new_text = []
        for char in original_text:
            if random.random() < typo_prob:
                is_alphabet, is_uppercase = char.isalpha(), char.isupper()
                if is_alphabet and is_uppercase:
                    lower_char = char.lower()
                    if lower_char in self.keyboard_neighborhood:
                        new_char = random.choice(self.keyboard_neighborhood[lower_char])
                        typos_count += 1
                        if new_char.isalpha():
                            new_char = new_char.upper()
                    else:
                        new_char = char
                else:
                    if char in self.keyboard_neighborhood:
                        new_char = random.choice(self.keyboard_neighborhood[char])
                        typos_count += 1
                    else:
                        new_char = char
            else:
               new_char = char

            new_text.append(new_char)

        return ''.join(new_text), typos_count

    def new_dataset_by_adding_noise(self, original_dataset, new_file_name):
        """
        Create a new dataset by adding typographical noise to some texts in the original dataset.

        With a certain probability, a sentence will have typos introduced and the noisy version
        will be added to the new dataset. The dataset is saved as an Excel file.
        """
        add_noise_prob = 0.1
        texts, labels = [], []
        for item in original_dataset:
            old_text, old_label = item['text'], item['label']
            texts.append(old_text)
            labels.append(old_label)
            if random.random() < add_noise_prob:
                new_text, typos_count = self.add_typo(original_text = old_text)
                if typos_count > 0:
                    texts.append(new_text)
                    labels.append(old_label)

        df = pd.DataFrame({
          'text': texts,
          'label': labels
        })

        df.to_excel(self.path_from_name(new_file_name), sheet_name=self.sheet_name_default, index=False)

    def filter_duplicates(self, original_dataset_path, new_file_name):
        df = pd.read_excel(original_dataset_path, sheet_name = self.sheet_name_default)
        df_cleaned = df.drop_duplicates(subset=['text'])
        df_cleaned.to_excel(self.path_from_name(new_file_name), sheet_name = self.sheet_name_default, index=False)