import pandas as pd
import numpy as np

def topic_sizes_by_class(model, classes, reduced=False):
    '''Calculate the number of documents belonging to each topic divvied up by class.

    Arguments:
        model : a fitted top2vec model
        classes : a pandas series of class labels
        reduced : boolean indicating whether or not to use reduced topics
    
    Returns:
        A pandas Series containing number of documents per topic and class.
    '''
    if reduced:
        df = pd.DataFrame({"topic": model.doc_top_reduced, "class": classes})
    else: 
        df = pd.DataFrame({"topic": model.doc_top, "class": classes})
    
    return df.groupby(["topic", "class"], as_index=True).size()



def find_new_centers(model, class_belonging, reduced=False):
    '''Computes new topic vectors for each class as the (normalized) mean document vector for combinations of class and (original) topic.

    Arguments:
        model = a fitted top2vec model
        class_belonging = a pandas Series of class labels (in the same order as the index passed to the doc2vec model)
        reduced : boolean, whether to use reduced topics or not

    Returns:
        A dictionary containing {class_label, topic_vectors}
    '''

    if reduced:
        topic_belonging = model.doc_top_reduced
    else:
        topic_belonging = model.doc_top
    
    class_topic = {}

    for class_ in set(class_belonging):

        topic_centers = []

        for topic in set(topic_belonging):

            is_in_topic = topic_belonging==topic
            is_in_class = class_belonging==class_
            index = np.logical_and(is_in_class, is_in_topic)

            subset = model.document_vectors[index, :]
            center = model._l2_normalize(subset.mean(axis=0))

            topic_centers.append(center)
        
        class_topic[class_] = np.vstack(topic_centers)
    
    return class_topic
