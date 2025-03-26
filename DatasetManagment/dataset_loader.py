import math
import pandas as pd

class DatasetLoader:
    def __init__(self):
        pass

    def add_all_sheets_from_all_files(self, path_file_names, list_of_sheet_names):
        output_dataset = []
        for index, path_file_name in enumerate(path_file_names):
            for sheet_name in list_of_sheet_names[index]:
                output_dataset.extend(pd.read_excel(path_file_name, sheet_name=sheet_name).to_dict(orient='records'))
        self.check_if_classes_are_balanced(output_dataset)
        return output_dataset

    def check_if_classes_are_balanced(self, dataset):
        examples_labels = {}
        for item in dataset:
            label = item["label"]
            examples_labels[label] = examples_labels.get(label, 0) + 1

        print("0: ", examples_labels[0], "1: ", examples_labels[1])
        if examples_labels[0] == examples_labels[1]:
            print("dataset is balanced")
            return True
        else:
            print("!!!!!!!!!! not balanced")
            return False

    @staticmethod
    def closest_power_of_2(number):
       logarithm = math.ceil(math.log2(number))
       return 2 ** logarithm

    @staticmethod
    def get_max_tokens(dataset, tokenizer):
        max_tokens = 0
        for item in dataset:
            tokenized_text = tokenizer.encode(item['text'], truncation = True)
            num_tokens = len(tokenized_text)
            max_tokens = max(max_tokens, num_tokens)
        return max_tokens
