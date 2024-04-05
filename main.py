from LeitorXML import LeitorXML
import pandas as pd

xml_reader = LeitorXML("lesson.xml")

df_questionario = xml_reader.analisar_questionario()
df_questoes = xml_reader.analisar_questoes()
df_tentativas = xml_reader.analisar_tentativas()


#print("Questionnaire Data:")
#print(df_questionario)
print("\nQuestions Data:")
df_questoes.head()
#print(df_questoes)
#print("\nAttempts Data:")
#print(df_tentativas)
