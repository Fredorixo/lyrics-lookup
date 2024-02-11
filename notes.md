# Notes

- Use `pipenv` to create a virtual environment to allow the packages required for your project to stay isolated with those of other projects.

- To maintain different versions of python for different projects, use `pyenv`.

- You can create also create different virtual environments using different python versions with the help of `pipenv shell --python <python_version>`.

- Decided to perform sentence transformation over the song lyrics, as a single string as opposed to an array of strings.

- Serialization was required to store the vector embeddings in MongoDB.

- Set up cron jobs to regularly update MongoDB collection with new songs using web scraping.