"""
Generate a question set in a Jupyter notebook. 
"""

import nbformat
import importlib.util
import argparse 
import inspect 
import sqlalchemy as db
import pandas as pd

def main():
	p = argparse.ArgumentParser(description="""Generate a Jupyter notebook from a python problem set file.""")
	p.add_argument('mod', help='A python module containing a problem set.')
	p.add_argument('output', help='The name of a file to write.')
	args = p.parse_args()

	mod = importlib.import_module(args.mod)

	# Get the db_url variable. 
	db_url = mod.db_url 
	engine = db.create_engine(db_url)

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
	nb.cells.append(nbformat.v4.new_code_cell(
		f"""%load_ext sql
%config SqlMagic.autolimit=100
%sql {db_url}"""
	))
	for q in questions:
		# Question cell
		nb.cells.append(nbformat.v4.new_markdown_cell(q.__doc__))	

		# Preview cell
		df = pd.read_sql_query(q.answer, engine)
		preview = """*This is a preview of the table yielded by the correct query. The preview is limited to five rows and the answer may have more.*"""
		preview += df.to_html(index=False, notebook=True, max_rows=5, show_dimensions=True)
		nb.cells.append(nbformat.v4.new_markdown_cell(preview))	

		# Answer cell 
		nb.cells.append(nbformat.v4.new_code_cell("%%sql\n\n"))

	nbformat.write(nb, args.output)

if __name__ == '__main__':
	main()
