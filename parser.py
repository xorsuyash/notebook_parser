import nbformat 
import requests 
import os 

def parse_notebook(notebook_content, output_file_path):

    try:
        notebook=nbformat.reads(notebook_content,as_version=4)

        with open(output_file_path,'w',encoding='utf-8') as output_file:
            for cell in notebook.cells:

                if cell.cell_type=='code':
                    output_file.write(f'### Cell {cell.execution_count}\n')
                    output_file.write(cell.source)
                    output_file.write("\n\n")
    except nbformat.reader.NotJSONError as e:
        raise ValueError("The notebook file could not be read") from e
    except Exception as e:
        raise RuntimeError("An error occured while extracting code from notebook") from e

def fetch_notebook_from_url(url):

    try:
        response=requests.get(url)
        response.raise_for_status()
        return response.text 
    except requests.RequestException as e:
        raise RuntimeError("An error occured by fetching notebook from url") from e

def read_notebook_file(file_path):

    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except OSError as e:
        raise RuntimeError(f"An error occurred while reading the file: {file_path}") from e