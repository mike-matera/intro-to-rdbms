"""
Generate a question set in a Jupyter notebook from a question file. The Jupyter 
notebook will contain questions that ask students to make SQL queries with previews for 
the correct result of the query. The question file provides an SQL Alchemy URL for 
connecting to a database and queries that generate the preview. 

A question file is a Python module that contains:

  db_url: The URL used to connect to the db. If the URL is for an SQLite db it 
    should be relative to the input file. 

  Question*: The module is searched for classes starting with "Question". Each 
    question must have an "answer" variable with the query and a docstring with 
	markdown that will be the question text.  

This tool should be run from the directory containing the question file and will 
generate a notebook in the same directory. This is to ensure that the notebook 
interprets the URL in the same way as the preview generator. 

The output file will have the same name as a module. For example: 

./gen_questions.py my_questions

This expects a my_questions.py in the current directory and generates my_questions.ipynb
"""

import nbformat
import importlib.util
import argparse 
import inspect 
import sqlalchemy as db
import pandas as pd
import sys 
import re 
import requests
import shutil
import tempfile 
import pathlib 
import subprocess 

query_limit = 500

setup_md_head = f"""# Setup 
The code in the cell below connects your notebook to the database. Queries are limited to 
returning {query_limit} rows to prevent your browser from being overwhelmed by a large result set. 
Each query has a preview of what you should see if you get the correct answer. The previews
are also limited to {query_limit} results. 
"""

setup_code = f"""import pathlib
import subprocess 
if not pathlib.Path('{{filename}}').exists():
    subprocess.run('wget {{url}}', shell=True)
%load_ext sql
%config SqlMagic.autolimit={query_limit}
%sql sqlite:///{{filename}}"""

setup_md_tail = """*Run this cell before you begin.*"""

preview_md = """<div style="padding: 1em;">
<i>This is a preview of the table yielded by the correct query:</i>
{preview_html}
</div>
"""

# Make sure we can import from WD
sys.path.append('.')

def import_questions(modname):
	"""Import a question set.""" 
	mod = importlib.import_module(modname)

	# Validate the module. 
	if mod.__doc__ is None: 
		raise ValueError("The question module has no docstring. It can't be used.")

	if "db_url" not in mod.__dict__:
		raise ValueError("A question set must have a 'db_url' function.")
	
	return mod


def main():
	p = argparse.ArgumentParser(description="""Generate a Jupyter notebook from a python problem set file.""")
	p.add_argument('mod', help='A python module containing a problem set.')
	args = p.parse_args()

	mod = import_questions(args.mod)
	outfile = args.mod + '.ipynb'

	# Download the DB 
	db_url = mod.db_url 
	filename = db_url.split('/')[-1]
	with tempfile.TemporaryDirectory() as tmpdir:
		subprocess.run(f"wget {db_url}", shell=True, cwd=tmpdir)

		# Get the db_url variable. 
		engine = db.create_engine(f"sqlite:///{tmpdir}/{filename}")

		# Search for questions
		questions = []
		for key in sorted(mod.__dict__):
			if key.startswith('Question') and inspect.isclass(mod.__dict__[key]):
				questions.append(mod.__dict__[key])

		# Generate the document. 
		nb = nbformat.v4.new_notebook()
		nb["metadata"] = {  
			"kernelspec": {
				"display_name": "Python 3",
				"language": "python",
				"name": "python3",
			},
		}
		nb.cells.append(nbformat.v4.new_markdown_cell(mod.__doc__))
		nb.cells.append(nbformat.v4.new_markdown_cell(setup_md_head))
		nb.cells.append(nbformat.v4.new_code_cell(setup_code.format(url=db_url, filename=filename)))
		nb.cells.append(nbformat.v4.new_markdown_cell(setup_md_tail))

		for q in questions:
			# Question cell
			nb.cells.append(nbformat.v4.new_markdown_cell(q.__doc__))	

			# Preview cell
			query = q.answer.replace(';', '')
			if re.search(r'(?i)limit', query) is None:
				query += f' limit {query_limit}'

			df = pd.read_sql_query(query, engine)
			html = df.to_html(index=False, notebook=True, max_rows=10)
			rows = df.shape[0]
			nb.cells.append(nbformat.v4.new_markdown_cell(
				preview_md.format(
					preview_html = html,
					rows = rows)))

			# Answer cell 
			nb.cells.append(nbformat.v4.new_code_cell("%%sql\n\n"))


	nbformat.write(nb, outfile)


if __name__ == '__main__':
	main()
