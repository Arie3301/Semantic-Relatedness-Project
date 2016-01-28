# Given a set of entities of the form [name, description, connections, relations, types]:
#  - Generate a list of all trigrams in language (in lexicographic order)
#  - Create a string-to-integer mapping for trigrams, relations, entity types (as shown in the e.g. under section "create dictionaries that map...")
#  - Express entity as a list of lists of the form [name, description, connections, relations, types]
#  - Call function get_vector_representation to get a vector representation of the entity.

# e.g. (an example like the Miami Heat example in the DSRM paper)
# Consider a language over the alphabet {a,b} consisting of words of length 1, 2, and 3.
# Vocabulary: a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb
# Trigrams: _a_, _b_, _aa, aa_, _ab, ab_, _ba, ba_, _bb, bb_, _aa, aaa, aab, aba, abb, baa, bab, bba, bbb
# Trigrams lexicographic order: _a_, _aa, _ab, _b_, _ba, _bb, aa_, aaa, aab, ab_, aba, abb, ba_, baa, bab, bb_, bba, bbb
# Size of vocabulary: 14
# Number of trigrams over vocabulary: 3 x 2 x 3 = 18 because [_,a,b] * [a,b] * [_,a,b]

# e.g. of an entity in this language
# Entity name: ab aba abb
# Entity description: bb bbb bba
# Connected entities: aa, aaa, aab
# Relations:          ba, baa, bab
# Entity Types:       a
# Note: 13 out of 14 vocab words are used in this example. We imagine that the word 'b' is an unused entity type.

# declare entity in standardized input format. Goal: represent this information in a vector
entity1_name = ['ab aba abb']  # entity name is always a list containing 1 string
entity1_description = ['bb bbb bba']  # entity description is always a list containing 1 string
entity1_connections = ['aa', 'aaa', 'aab']
entity1_relations = ['ba', 'baa', 'bab']
entity1_types = ['a']
entity1 = [entity1_name, entity1_description, entity1_connections, entity1_relations, entity1_types]

# declare variables for turning entities into vectors
num_trigrams = 18
num_relations = 3
num_entitytypes = 2

# create lists of all possible trigrams, relations, and entity types
trigrams_list = ['_a_', '_aa', '_ab', '_b_', '_ba', '_bb', 'aa_', 'aaa', 'aab', 'ab_', 'aba', 'abb', 'ba_', 'baa', 'bab', 'bb_', 'bba', 'bbb']
relations_list = ['ba', 'baa', 'bab']
entitytypes_list = ['a', 'b']

# create dictionaries that map trigrams, relation types and entity types to vector indices.
#  e.g. relations_list = ['ba', 'baa', 'bab'] produces relations_index = {'bab': 2, 'baa': 1, 'ba': 0}
trigrams_index = {}
for i in range(len(trigrams_list)):
    trigrams_index[trigrams_list[i]] = i

relations_index = {}
for i in range(len(relations_list)):
    relations_index[relations_list[i]] = i

entitytypes_index = {}
for i in range(len(entitytypes_list)):
    entitytypes_index[entitytypes_list[i]] = i


# helper functions for word hashing
def get_trigrams(words):
    '''
    Return trigrams for a list of words.
    :param word: a list of words with end-of-word marks
    :return: a list of trigrams
    '''
    trigrams = []
    for word in words:
        i = 3
        while i <= len(word): # eg the word _is_ has length 4 and consists of trigrams _is and is_
            trigrams.append(word[i-3:i])
            i += 1
    return trigrams


def get_hash(trigrams, mapping, length):
    '''
    Return a word hashed vector from a list of trigrams and a vector length.
    :param trigrams: a list of trigrams
    :param mapping: a dictionary that maps trigrams to vector indices
    :param length: length of vector
    :return: a trigram based word hashed vector
    '''
    # initialize vector to all zeroes
    vector = []
    for i in range(length):
        vector.append(0)
    # increment vector for trigrams
    for trigram in trigrams:
        #print("putting trigram ", trigram, " at index ", mapping[trigram])
        vector[mapping[trigram]] += 1
    return vector


def get_hash_vector(text, mapping, length):
    '''
    Represent a list of strings as a trigram based word hashed vector.
    :param text: a list of strings
    :param mapping: a dictionary that maps trigrams to vector indices
    :param length: length of vector
    :return: a trigram based word hashed vector
    '''
    # step 1: turn text into words with end-of-word marks
    bow = [] # bag of words
    for string in text:
        bow += string.split()
    bow_eow = [] # bag of words with end-of-word marks
    for word in bow:
        bow_eow.append('_' + word + '_')
    # step 2: turn words into trigrams
    trigrams = get_trigrams(bow_eow)
    # step 3: return word hashed vector
    return get_hash(trigrams, mapping, length)


def get_onehot_vector(text, mapping, length):
    '''
    Return sum of one-hot vectors from a list of strings
    :param text: a list of strings
    :param mapping: a dictionary that maps strings to vector indices
    :param length: length of vector
    :return: a word-based sum of one-hot vectors
    '''
    # initialize vector to all zeroes
    vector = []
    for i in range(length):
        vector.append(0)
    # increment vector for trigrams
    for string in text:
        #print("putting string ", string, " at index ", mapping[string])
        vector[mapping[string]] += 1
    return vector


# Main function for word hashing
def get_vector_representation(entity, trigrams_index, num_trigrams, relations_index, num_relations, entitytypes_index, num_entitytypes):
    '''
    Represent an entity as a vector.
    :param entity: a list of lists of the form [name, description, connections, relations, types]
    :param trigrams_index: a dictionary that maps trigrams to vector indices
    :param num_trigrams: number of trigrams
    :param relations_index: a dictionary that maps strings to vector indices
    :param num_relations: number of relations
    :param entitytypes_index: a dictionary that maps strings to vector indices
    :param num_entitytypes: number of entity types
    :return: vector representation of entity
    '''
    name_vec = get_hash_vector(entity[0], trigrams_index, num_trigrams)
    print("name_vec: ", name_vec)
    description_vec = get_hash_vector(entity[1], trigrams_index, num_trigrams)
    print("description_vec: ", description_vec)
    connections_vec = get_hash_vector(entity[2], trigrams_index, num_trigrams)
    print("connections_vec: ", connections_vec)
    relations_vec = get_onehot_vector(entity[3], relations_index, num_relations)
    print("relations_vec: ", relations_vec)
    types_vec = get_onehot_vector(entity[4], entitytypes_index, num_entitytypes)
    print("types_vec: ", types_vec)
    return name_vec + description_vec + connections_vec + relations_vec + types_vec

# test:
print(get_vector_representation(entity1, trigrams_index, num_trigrams, relations_index, num_relations, entitytypes_index, num_entitytypes))

# Not tested: entities with no connections, no description, or no entity type