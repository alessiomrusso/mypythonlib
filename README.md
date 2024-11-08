# mypythonlib
mypythonlib provides a basic structure for creating a Python library

## Installation

To install mypythonlib, you need to follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/alessiomrusso/mypythonlib.git
    ```

2. **Navigate to the project directory:**

    ```sh
    cd mypythonlib
    ```

3. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install the necessary dependencies:**

    ```sh
    pip install wheel
    pip install setuptools
    pip install twine
    pip install pytest
    pip install pytest-runner
    ```

5. **Running tests**
    
    ```sh
    python setup.py pytest
    ```

7. **Build the library:**

    ```sh
    python setup.py bdist_wheel
    ```

7. **Install the library:**

    ```sh
    pip install dist/mypythonlib-0.1.0-py3-none-any.whl
    ```

## Usage

After installing the library, you can import and use it in your Python scripts:

```python
import haversine
from haversine import myfunctions

# Example usage of the haversine function
distance = haversine.haversine(lon1, lat1, lon2, lat2)
print(f"The distance is {distance} kilometers.")
```