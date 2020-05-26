from nltk.tag.stanford import CoreNLPNERTagger


def get_continuous_chunks(tagged_sent):
    continuous_chunk = []
    current_chunk = []

    for token, tag in tagged_sent:
        if tag != "O":
            current_chunk.append((token, tag))
        else:
            if current_chunk:  # if the current chunk is not empty
                continuous_chunk.append(current_chunk)
                current_chunk = []
    # Flush the final current_chunk into the continuous_chunk, if any.
    if current_chunk:
        continuous_chunk.append(current_chunk)
    return continuous_chunk


stner = CoreNLPNERTagger()
tagged_sent = stner.tag(
    'Rami Eid is studying at Stony Brook University in NY'.split())

named_entities = get_continuous_chunks(tagged_sent)
named_entities_str_tag = [
    (" ".join([token for token, tag in ne]), ne[0][1]) for ne in named_entities]


print(named_entities_str_tag)
