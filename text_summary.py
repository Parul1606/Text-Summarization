import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """Artificial intelligence (AI) is transforming various industries, from healthcare to finance. Machine learning algorithms analyze vast datasets to provide insights and predictions, improving decision-making processes. Chatbots and virtual assistants powered by AI have revolutionized customer service. As technology continues to advance, AI's potential applications seem limitless, promising a future of increased automation and smarter systems."""


def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    print(stopwords)

    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    print(doc)

    tokens = [token.text for token in doc]
    print(tokens)

    #word frequnecy dictionary
    word_freq = {}
    for word in doc: 
      if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in word_freq.keys():
          word_freq[word.text] =1
        else:
          word_freq[word.text] +=1
    print(word_freq)

    max_freq = max(word_freq.values())
    print(max_freq)

    for word in word_freq.keys():
      word_freq[word] = word_freq[word]/max_freq
    print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    print(sent_tokens)

    #sentence score dictionary
    sent_scores = {}
    for sent in sent_tokens:
      for word in sent:
        if word.text in word_freq.keys():
          if sent not in sent_scores.keys():
            sent_scores[sent] = word_freq[word.text]
          else: 
            sent_scores[sent] += word_freq[word.text]

    print(sent_scores)

    #after selecting all the selected sentences we are getting the no of sentences/lines it requires to print the given text
    select_len = int(len(sent_tokens) * 0.3)
    print(select_len)

    summary = nlargest(select_len, sent_scores, key = sent_scores.get)
    print(summary)

    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    print(summary)

    print("length of original text", len(text.split(' ')))
    print("length of original text", len(summary.split(' ')))
    
    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))

