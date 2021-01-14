# Import packages
import wikipedia
import re
# Specify the title of the Wikipedia page
#wiki = wikipedia.page('Web scraping')
# Extract the plain text content of the page
#text = wiki.content
# Clean text
#text = re.sub(r'==.*?==+', '', text)
#text = text.replace('\n', '')
text="Expand_Horizons, IoT, Testing, Back_To_Technical, Leadership, Developer_at_heart, Update, Joy_of_learning"

#text="Testing, Technical_Management, SAP_ABAP,Digital_Transformation,PLM, Embedded_systems,Solution_Architecture, Automation, Cloud_Platforms, Team_Management, Agile, Scrum_Master"

print(text)

# Import packages
import matplotlib.pyplot as plt
#%matplotlib inline
# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud)
    # No axis details
    plt.axis("off");
    plt.show()

# Import package
from wordcloud import WordCloud, STOPWORDS
# Generate word cloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='green', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
# Plot
plot_cloud(wordcloud)