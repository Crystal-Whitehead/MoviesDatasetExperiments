Goals:

    To allow a user to, using a web interface, enter in a movie title and get back recommendations with a confidence score (as percentage 1-100) that says how similar the movie is. Retrieval should be limited to the top 20 titles for now to keep things simple.

Steps to complete project:

1. Build front end page that allows to submit a movie title and get info back (done by John, will be further iterated by Crystal).
2. Build an AWS Lambda (or similar) to act as the middleware functionality that hosts the recommdation engine
3. Build a recommendation engine that ingests a movie title and maximum result count and returns a list of movies with title, description, and confidence score. 
    - Calculate Term Frequency-Inverse Document Frequency on plot
        - https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089
        - https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction
    - Get top actors, director, related genres and the movie plot keywords and build data set from those
        - Use data set to compare various titles

Considerations:

    - AWS lambda may charge on per usage basis - be sure to set a spend limit
    - Some of the recommdation calculations may be pre-calculated/saved to make user interaction faster