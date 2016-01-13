#Consider a language over the alphabet {a,b} consisting of words of length 1, 2, and 3.
#vocabulary: a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb
#3-grams: #a#, #b#, #aa, aa#, #ab, ab#, #ba, ba#, #bb, bb#, #aa, aaa, aab, aba, abb, baa, bab, bba, bbb
#3-grams lexicographic order: #a#, #aa, #ab, #b#, #ba, #bb, aa#, aaa, aab, ab#, aba, abb, ba#, baa, bab, bb#, bba, bbb

# size of vocabulary: 14
# number of 3-grams: 18 -- 3 x 2 x 3 for [#,a,b] * [a,b] * [#,a,b]

# procedure:
# generate vocabulary
# generate all 3-grams in vocabulary in lexicographic order
# index vector by trigram.

# e.g. 1 (an example like the Miami Heat example in the DSRM paper)
# Entity name: ab aba abb
# Connected entities: aa, aaa, aab
# Relations:          ba, baa, bab
# Entity Types:       a
# Entity description: bb bbb bba
# Note: 13 out of 14 vocab words are used in this example. We imagine that the word 'b' is an unused entity type.

# declare variables for turning entities into vectors
vocab_size = 14
num_3grams = 18
num_relations = 3
num_entity_types = 2

trigrams_list = ['_a_', '_aa', '_ab', '_b_', '_ba', '_bb', 'aa_', 'aaa', 'aab', 'ab_', 'aba', 'abb', 'ba_', 'baa', 'bab', 'bb_', 'bba', 'bbb']
trigrams_index = {}
relations_list = ['ba', 'baa', 'bab']
relations_index = {}
entitytypes_list = ['a', 'b']
entitytypes_index = {}

for i in range(len(trigrams_list)):
    trigrams_index[trigrams_list[i]] = i
for i in range(len(relations_list)):
    relations_index[relations_list[i]] = i
for i in range(len(entitytypes_list)):
    entitytypes_index[entitytypes_list[i]] = i

print(trigrams_index)
print(relations_index)
print(entitytypes_index)

entity1_name = ['ab aba abb']
entity1_connections = ['aa', 'aaa', 'aab']
entity1_relations = ['ba', 'baa', 'bab']
entity1_type = ['a']
entity1_description = ['bb bbb bba']

