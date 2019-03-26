ai_text='''Knowledge engineering is a core part of AI research. Machines can often act and react like humans only if they have abundant information relating to the world. Artificial intelligence must have access to objects, categories, properties and relations between all of them to implement knowledge engineering. Initiating common sense, reasoning and problem-solving power in machines is a difficult and tedious task.Machine learning is also a core part of AI. Learning without any kind of supervision requires an ability to identify patterns in streams of inputs, whereas learning with adequate supervision involves classification and numerical regressions. Classification determines the category an object belongs to and regression deals with obtaining a set of numerical input or output examples, thereby discovering functions enabling the generation of suitable outputs from respective inputs. Mathematical analysis of machine learning algorithms and their performance is a well-defined branch of theoretical computer science often referred to as computational learning theory.Machine perception deals with the capability to use sensory inputs to deduce the different aspects of the world, while computer vision is the power to analyze visual inputs with a few sub-problems such as facial, object and gesture recognition.Robotics is also a major field related to AI. Robots require intelligence to handle tasks such as object manipulation and navigation, along with sub-problems of localization, motion planning and mapping.'''
ai_text.split()
print(ai_text.split())
import re
ai_text_split=re.split('[ ,.]',ai_text)
print(ai_text_split)
dic={}
for word in ai_text_split:
    if word not in dic:
        dic[word]=1
    else:
        dic[word]=dic[word]+1
print(dic)
print(dic.items())
import operator
ai_result=sorted(dic.items(),key=operator.itemgetter(1),reverse=True)
print(ai_result)
from nltk.corpus import stopwords
import nltk
#nltk.download('stopwords')
stop_words=stopwords.words('English')
print(stop_words)
for k,v in ai_result:
    if k not in stop_words:
        if k!='':
            print(k,v)
from collections import Counter
c=Counter(ai_text_split)
print(c)
for sw in stop_words:
    del c[sw]
del c['']
print(c)