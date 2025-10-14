# Examples
Distributed Systems subject examples.

Several python examples in this repository use Python's `venv` module to create isolated environments. This ensures that dependencies are managed separately for each project. For these examples, follow the steps below to set up and run the code (a Makefile is also provided in each example directory for convenience).

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
A `requirements.txt` file is provided in each example directory. Install the dependencies using pip:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the example code
Run the example code as specified in the example's README or Makefile.

## Exit (and remove) the virtual environment

To exit the virtual environment, run:

```bash
deactivate
```

Finally, if you want to remove the virtual environment, simply delete the `venv` directory:

```bash
rm -rf venv
```
