import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_desciption = docx2txt.process('ADD RESUME  PATH')

resume = docx2txt.process('ADD RESUME SAMPLE PATH')

content = [job_desciption, resume]

cv = CountVectorizer()

# to convert doc file to vector
matrix = cv.fit_transform(content)

# to check the similirity of resume
similarity_matrix = cosine_similarity(matrix)

print(similarity_matrix)