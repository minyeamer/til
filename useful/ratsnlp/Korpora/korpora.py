from dataclasses import dataclass
from typing import List, Union


@dataclass
class KorpusData:
    name: str
    texts: List[str]

    def __len__(self):
        return len(self.texts)

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __getitem__(self, index):
        return self.texts[index]

    def get_all_texts(self):
        return self.texts

    def __str__(self):
        attributes = ""
        for var_name, var in self.__dict__.items():
            if var_name not in {'name', 'description', 'self'}:
                attributes += f'  - {self.name}.{var_name} : list[{var[0].__class__.__name__}]\n'
        s = f"""{self.name}: size={len(self.texts)}\n{attributes}"""
        return s

    def __repr__(self):
        return self.__str__()


@dataclass
class LabeledSentence:
    text: str
    label: Union[int, float, str, bool]


class LabeledSentenceKorpusData(KorpusData):
    labels: List[Union[str, int]]

    def __init__(self, name, texts, labels):
        if not (len(texts) == len(labels)):
            raise ValueError('All two arguments must be same length')
        super().__init__(name, texts)
        self.labels = labels

    def __getitem__(self, index):
        return LabeledSentence(self.texts[index], self.labels[index])

    def get_all_labels(self):
        return self.labels


@dataclass
class SentencePair:
    text: str
    pair: str


class SentencePairKorpusData(KorpusData):
    pairs: List[str]

    def __init__(self, name, texts, pairs):
        if not (len(texts) == len(pairs)):
            raise ValueError('All two arguments must be same length')
        super().__init__(name, texts)
        self.pairs = pairs

    def __getitem__(self, index):
        return SentencePair(self.texts[index], self.pairs[index])

    def get_all_pairs(self):
        return self.pairs


@dataclass
class LabeledSentencePair:
    text: str
    pair: str
    label: Union[str, int, float, bool]


class LabeledSentencePairKorpusData(KorpusData):
    pairs: List[str]
    labels: List

    def __init__(self, name, texts, pairs, labels):
        if not (len(texts) == len(pairs) == len(labels)):
            raise ValueError('All three arguments must be same length')
        super().__init__(name, texts)
        self.pairs = pairs
        self.labels = labels

    def __getitem__(self, index):
        return LabeledSentencePair(self.texts[index], self.pairs[index], self.labels[index])

    def get_all_pairs(self):
        return self.pairs

    def get_all_labels(self):
        return self.labels


@dataclass
class WordTag:
    text: str
    words: List[str]
    tags: List[str]


class WordTagKorpusData(KorpusData):
    words: List[List[str]]
    tags: List[List[str]]

    def __init__(self, name, texts, words, tags):
        if not (len(texts) == len(words) == len(tags)):
            raise ValueError('All three arguments must be same length')
        super().__init__(name, texts)
        self.words = words
        self.tags = tags

    def __getitem__(self, index):
        return WordTag(self.texts[index], self.words[index], self.tags[index])

    def get_all_words(self):
        return self.words

    def get_all_tags(self):
        return self.tags


class Korpus:
    description: str
    license: str

    def __init__(self, description, license):
        self.description = description
        self.license = license
        print(f"""
    Korpora ??? ?????? ????????? ?????? ???????????? ??????????????? ???????????????
    ????????? ????????????, ????????? ??? ?????? ???????????? ???????????????.

    ??????????????? ????????? ?????? ???????????? ???????????????, ??? ????????? ??? ????????? ??????????????? ?????? ????????????.
    ?????? ???????????? ?????? ????????? ?????? ????????? ?????? ????????? description ??? ??????,
    ?????? ???????????? ??????/????????? ???????????? ???????????? ????????? ????????? ??????????????? ????????? ????????? ????????????.

    # Description
{description}

    # License
{license}\n""")

    def __str__(self):
        classname = self.__class__.__name__
        s = f"{classname}\n{self.description}\n\nAttributes\n----------\n"
        for var_name, var in self.__dict__.items():
            if isinstance(var, KorpusData):
                s += f'{str(var)}'
        return s

    def cleaning(self, raw_documents: List[str], **kargs):
        """`raw_data` to `sentences`"""
        raise NotImplementedError('Implement this function')

    def get_all_texts(self):
        texts = []
        for name, var in sorted(self.__dict__.items()):
            if isinstance(var, KorpusData):
                texts += var.get_all_texts()
        return texts

    def save(self, root_dir):
        """save prorce` to `sentences`"""
        raise NotImplementedError('Implement this function')
