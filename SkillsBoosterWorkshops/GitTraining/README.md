# GitWorkshop

To generate the final HTML file:

1. Run `python generate_index_file.py`. This code will aggregate participants into the participants.xml file.	
2. Create the HTML file by running: `python publish_html.py`.

Open the final `index.html` file with your favorite browser!

**Note: ** The generated HTML file is not version controlled. You can see that it's not flagged as a new file by Git. This is thanks to the .gitignore file that exists in this repository. This file is used to exclude certain files using patterns or file names from being version controlled by Git.