import openai
import pandas as pd
import random
from DatasetManagment.keyboard_neighborhood import keyboard_neighborhood

class DatasetAugmentation:
    def __init__(self, keyboard_neighborhood = keyboard_neighborhood, engine = "gpt-4o"):
        self.engine = engine
        self.keyboard_neighborhood = keyboard_neighborhood
        self.prompt_setup()

    def generate_response(self, prompt, temperature = 0.9, n_of_responses = 2):
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

    def new_dataset_by_paraphrazing(self, original_dataset, new_dataset_name):
        texts, labels = [], []
        n_responses_per_request = 2
        list_of_temperatures = [0.75, 0.85, 0.95]
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

        df.to_excel(new_dataset_name + ".xlsx", sheet_name="All", index=False)

    def add_typo(self, original_text, typo_prob = 0.03):
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

        df.to_excel(new_file_name + ".xlsx", sheet_name="All", index=False)