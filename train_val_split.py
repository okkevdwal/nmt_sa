def train_val_split (path_source, path_train_file, path_val_file):
    with open(path_source) as f:
        text = f.read()
        sentences = text.split('.')
        training_set = sentences[:-5000]
        val_set = sentences[-5000:]

    with open(path_train_file,"w") as output:
        for sentence in training_set:
            output.write(sentence)

    with open(path_val_file,"w") as output:
        for sentence in val_set:
            output.write(sentence)