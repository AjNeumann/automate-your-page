
# This is the "generate_concept_HTML" function 
# from the previous work_session. You do not need to modify it.
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

# This is one way you may have written make_HTML.
# You do not need to modify it.
def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

# This is an example of what a list of concepts might look like.
EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]

# This is the function you will write.
def make_HTML_for_many_concepts(list_of_concepts):
    result = ""
    for concept in list_of_concepts:
        result += make_HTML(concept)
    return result

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
