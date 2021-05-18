import os
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
os.chdir("C:/Users/86135/Desktop/pythonProject/Practical 14")
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

def dict_founder(terms):
    dict = {}
    for term in terms:
        is_a = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
        id_all = term.getElementsByTagName("id")[0].childNodes[0].data
        for father_id in is_a:
            if father_id in dict:
                dict[father_id].append(id_all)
            else:
                dict[father_id] = [id_all]
    return dict

def related_gene(terms,molecule):
    gene = []
    for term in terms:
        defstrs = term.getElementsByTagName("defstr")[0]
        a = defstrs.childNodes[0].data
        id_related = term.getElementsByTagName("id")[0].childNodes[0].data
        if not molecule.isupper():
            a = a.lower()
        if molecule in a:
            gene.append(id_related)
    return set(gene)

def getall(dict,lists):
    all = []
    for f in lists:
        if f in dict:
            child = dict[f]
            all += child
            all += getall(dict,child)
    return all
def counting_the_childnodes(terms,molecular):
    dict = dict_founder(terms)
    match = related_gene(terms,molecular)
    all_childnodes = getall(dict,match)
    num = len(set(all_childnodes))
    return num

DNA = counting_the_childnodes(terms, "DNA")
RNA = counting_the_childnodes(terms, "RNA")
Protein = counting_the_childnodes(terms, "protein")
Carbohydrate = counting_the_childnodes(terms, "carbohydrate")
print("The number of childNodes of all DNA-associated terms is: ",DNA)
print("The number of childNodes of all RNA-associated terms is: ",RNA)
print("The number of childNodes of all protein-associated terms is: ",Protein)
print("The number of childNodes of all carbohydrate-associated terms is: ",Carbohydrate)
labels = 'DNA', 'RNA', 'protein', 'carbohydrate'
sizes = [DNA, RNA, Protein, Carbohydrate]
explode = (0.1, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%', shadow=False, startangle=90)
plt.title('Practical 14')
plt.axis('equal')
plt.show()