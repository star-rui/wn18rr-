def load_entity_id_mapping(file_path):
    entity_id_mapping = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        # Skip header if exists
        next(file)
        for line in file:
            entity_name, entity_id = line.strip().split('\t')
            entity_id_mapping[entity_name] = int(entity_id)
    return entity_id_mapping


def load_relation_id_mapping(file_path):
    relation_id_mapping = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        # Skip header if exists
        next(file)
        for line in file:
            relation_name, relation_id = line.strip().split('\t')
            relation_id_mapping[relation_name] = int(relation_id)
    return relation_id_mapping


def load_triple_data(file_path):
    triples = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            head_id, tail_id, relation_id = map(int, line.strip().split(' '))
            triples.append((head_id, tail_id, relation_id))
    return triples


def save_triple_data(triples, entity_id_mapping, relation_id_mapping, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for head_id, tail_id, relation_id in triples:
            head_name = list(entity_id_mapping.keys())[list(entity_id_mapping.values()).index(head_id)]
            tail_name = list(entity_id_mapping.keys())[list(entity_id_mapping.values()).index(tail_id)]
            relation_name = list(relation_id_mapping.keys())[list(relation_id_mapping.values()).index(relation_id)]
            file.write(f"{head_name}\t{relation_name}\t{tail_name}\n")


def main():
    # Load entity and relation mappings
    entity_id_mapping = load_entity_id_mapping('entity2id.txt')
    relation_id_mapping = load_relation_id_mapping('relation2id.txt')

    # Load triple data
    triples = load_triple_data('n-n.txt')

    # Save triple data to a new file
    save_triple_data(triples, entity_id_mapping, relation_id_mapping, 'n-n_test.txt')


if __name__ == "__main__":
    main()
