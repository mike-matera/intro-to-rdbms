# Setup Cloud9 IDE 

This lab will take you through claiming your Cloud9 IDE account and installing the class' Jupyter Notebooks. 

## Login to AWS 

Make sure you know your username and password. You can figure out what they are by reading the Access FAQ: 

> [Computer Access FAQ](../faq.html)

Sign in to AWS using this link: 

> [Cloud9 IDE](https://957903271915.signin.aws.amazon.com/console)

## Install the Course Files 

The course content is delivered using [Jupyter](https://jupyter.org/) Notebooks. The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

### Step 1: Initialize my Installer 
Copy and paste the following command in your Cloud9 terminal:

```bash
cd ~ && wget -q -O - https://github.com/mike-matera/CourseNotebook/archive/master.tar.gz | tar -zxvf - --strip-components=1
```

The output should look like this:

<img src="../_static/images/jupyter_initial_setup.png" width="600" />

### Step 2: Set the Course Location

Now execute this command to set the location of course content:

```bash
cd ~ && echo "https://s3-us-west-2.amazonaws.com/notebooks-course-content/cis-54/content.tar.gz" > .course
```

### Step 3: Run the Updater

Finally run the `update` command to setup your Cloud9 environment and install the notebooks. 

```bash
update
```

The initial update will take a couple of minutes. After the update is complete you should see the course content in the left pane. 

<img src="../_static/images/jupyter_setup_complete.png" width="600" />

> Note: The course content changes so this picture might not look exactly like your finished install. 

## Run the Notebook 

If you have done everything correctly you should be able to run the `notebook` command:

```bash
notebook
```

The `notebook` command will have output that presents you a URL. Open the URL in Cloud9 by clicking on it and selecting "Open". See the picture below: 

<img src="../_static/images/jupyter_open_notebook.png" width="600" />
