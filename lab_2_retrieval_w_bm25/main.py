"""
Lab 2.

Text retrieval with BM25
"""
# pylint:disable=too-many-arguments, unused-argument

import math


def tokenize(text: str) -> list[str] | None:
    """
    Tokenize the input text into lowercase words without punctuation, digits and other symbols.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list[str] | None: A list of words from the text.

    In case of corrupt input arguments, None is returned.
    """
    if not isinstance(text, str):
        return None

    extra_symb = ',.:?!;%$#№"&()[]{}~0123456789‘’º -\n><*=@+/\''
    word = ''
    result = []
    for letter in text.lower():
        if not letter in extra_symb:
            word += letter
        else:
            if len(word) > 0:
                result.append(word)
            word = ''
    if len(word) > 0:
        result.append(word)
    return result


def remove_stopwords(tokens: list[str], stopwords: list[str]) -> list[str] | None:
    """
    Remove stopwords from the list of tokens.

    Args:
        tokens (list[str]): List of tokens.
        stopwords (list[str]): List of stopwords.

    Returns:
        list[str] | None: Tokens after removing stopwords.

    In case of corrupt input arguments, None is returned.
    """
    if not isinstance(tokens, list) or not isinstance(stopwords, list):
        return None
    if not tokens or not stopwords:
        return None

    for stopword in stopwords:
        if not isinstance(stopword, str):
            return None

    result = []
    for token in tokens:
        if not isinstance(token, str):
            return None
        if not token in stopwords:
            result.append(token)
    return result


def build_vocabulary(documents: list[list[str]]) -> list[str] | None:
    """
    Build a vocabulary from the documents.

    Args:
        documents (list[list[str]]): List of tokenized documents.

    Returns:
        list[str] | None: List with unique words from the documents.

    In case of corrupt input arguments, None is returned.
    """
    if not isinstance(documents, list):
        return None

    unique = set()
    for document in documents:
        if not isinstance(document, list):
            return None
        for token in document:
            if not isinstance(token, str):
                return None
            unique.add(token)
    if not unique:
        return None

    return list(unique)


def calculate_tf(vocab: list[str], document_tokens: list[str]) -> dict[str, float] | None:
    """
    Calculate term frequency for the given tokens based on the vocabulary.

    Args:
        vocab (list[str]): Vocabulary list.
        document_tokens (list[str]): Tokenized document.

    Returns:
        dict[str, float] | None: Mapping from vocabulary terms to their term frequency.

    In case of corrupt input arguments, None is returned.
    """
    if not isinstance(vocab, list) or not isinstance(document_tokens, list):
        return None

    result = {}
    for word in vocab:
        if not isinstance(word, str):
            return None
        nb_occurence = document_tokens.count(word)
        if len(document_tokens) > 0:
            result[word] = nb_occurence / len(document_tokens)

    if not vocab:
        return None

    for word in document_tokens:
        if not isinstance(word, str):
            return None
        if not word in vocab:
            nb_occurence = document_tokens.count(word)
            if len(document_tokens) > 0:
                result[word] = nb_occurence / len(document_tokens)

    if not result:
        return None

    return result

def calculate_idf(vocab: list[str], documents: list[list[str]]) -> dict[str, float] | None:
    """
    Calculate inverse document frequency for each term in the vocabulary.

    Args:
        vocab (list[str]): Vocabulary list.
        documents (list[list[str]]): List of tokenized documents.

    Returns:
        dict[str, float] | None: Mapping from vocabulary terms to its IDF scores.

    In case of corrupt input arguments, None is returned.
    """
    if not isinstance(vocab, list) or not isinstance(documents, list):
        return None

    if not vocab or not documents:
        return None

    for document in documents:
        if not isinstance(document, list):
            return None
        for word in document:
            if not isinstance(word, str):
                return None

    numb = len(documents)
    idf = {}
    for word in vocab:
        if not isinstance(word, str):
            return None
        summ = 0
        for document in documents:
            if word in document:
                summ += 1

        idf[word] = math.log((numb - summ + 0.5) / (summ + 0.5))

    return idf


def calculate_tf_idf(tf: dict[str, float], idf: dict[str, float]) -> dict[str, float] | None:
    """
    Calculate TF-IDF scores for a document.

    Args:
        tf (dict[str, float]): Term frequencies for the document.
        idf (dict[str, float]): Inverse document frequencies.

    Returns:
        dict[str, float] | None: Mapping from terms to their TF-IDF scores.

    In case of corrupt input arguments, None is returned.
    """
    if not isinstance(tf, dict) or not isinstance(idf, dict):
        return None

    result = {}
    for word in tf:
        if not isinstance(word, str) or not word in idf:
            return None
        result[word] = tf[word] * idf[word]

    if not result:
        return None
    return result



def calculate_bm25(
    vocab: list[str],
    document: list[str],
    idf_document: dict[str, float],
    k1: float = 1.5,
    b: float = 0.75,
    avg_doc_len: float | None = None,
    doc_len: int | None = None,
) -> dict[str, float] | None:
    """
    Calculate BM25 scores for a document.

    Args:
        vocab (list[str]): Vocabulary list.
        document (list[str]): Tokenized document.
        idf_document (dict[str, float]): Inverse document frequencies.
        k1 (float): BM25 parameter.
        b (float): BM25 parameter.
        avg_doc_len (float | None): Average document length.
        doc_len (int | None): Length of the document.

    Returns:
        dict[str, float] | None: Mapping from terms to their BM25 scores.

    In case of corrupt input arguments, None is returned.
    """


def rank_documents(
    indexes: list[dict[str, float]], query: str, stopwords: list[str]
) -> list[tuple[int, float]] | None:
    """
    Rank documents for the given query.

    Args:
        indexes (list[dict[str, float]]): List of BM25 or TF-IDF indexes for the documents.
        query (str): The query string.
        stopwords (list[str]): List of stopwords.

    Returns:
        list[tuple[int, float]] | None: Tuples of document index and its score in the ranking.

    In case of corrupt input arguments, None is returned.
    """


def calculate_bm25_with_cutoff(
    vocab: list[str],
    document: list[str],
    idf_document: dict[str, float],
    alpha: float,
    k1: float = 1.5,
    b: float = 0.75,
    avg_doc_len: float | None = None,
    doc_len: int | None = None,
) -> dict[str, float] | None:
    """
    Calculate BM25 scores for a document with IDF cutoff.

    Args:
        vocab (list[str]): Vocabulary list.
        document (list[str]): Tokenized document.
        idf_document (dict[str, float]): Inverse document frequencies.
        alpha (float): IDF cutoff threshold.
        k1 (float): BM25 parameter.
        b (float): BM25 parameter.
        avg_doc_len (float | None): Average document length.
        doc_len (int | None): Length of the document.

    Returns:
        dict[str, float] | None: Mapping from terms to their BM25 scores with cutoff applied.

    In case of corrupt input arguments, None is returned.
    """


def save_index(index: list[dict[str, float]], file_path: str) -> None:
    """
    Save the index to a file.

    Args:
        index (list[dict[str, float]]): The index to save.
        file_path (str): The path to the file where the index will be saved.
    """


def load_index(file_path: str) -> list[dict[str, float]] | None:
    """
    Load the index from a file.

    Args:
        file_path (str): The path to the file from which to load the index.

    Returns:
        list[dict[str, float]] | None: The loaded index.

    In case of corrupt input arguments, None is returned.
    """


def calculate_spearman(rank: list[int], golden_rank: list[int]) -> float | None:
    """
    Calculate Spearman's rank correlation coefficient between two rankings.

    Args:
        rank (list[int]): Ranked list of document indices.
        golden_rank (list[int]): Golden ranked list of document indices.

    Returns:
        float | None: Spearman's rank correlation coefficient.

    In case of corrupt input arguments, None is returned.
    """
