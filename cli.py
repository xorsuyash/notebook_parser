import argparse
from parser import parse_notebook, fetch_notebook_from_url, read_notebook_file

def main():
    parser = argparse.ArgumentParser(description='Extract code cells from a Jupyter Notebook and save them to a text file.')
    parser.add_argument('input', type=str, help='Path to the local Jupyter Notebook file or a URL to the notebook on GitHub')
    parser.add_argument('output', type=str, help='Path to the output text file')

    args = parser.parse_args()

    try:
        if args.input.startswith('http://') or args.input.startswith('https://'):
            notebook_content = fetch_notebook_from_url(args.input)
        else:
            notebook_content = read_notebook_file(args.input)
        
        parse_notebook(notebook_content, args.output)
        print(f"Code has been extracted to {args.output}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
