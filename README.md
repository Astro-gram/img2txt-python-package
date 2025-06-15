# img2txt-python-sdk

A Python SDK for the [img2txt.io](https://img2txt.io) API. Easily upload images and convert them to plain text or structured output programmatically.

## Installation

```powershell
pip install img2txtio
```

Or install directly from source:

```powershell
git clone https://github.com/yourusername/img2txt-python-sdk.git
cd img2txt-python-sdk
pip install .
```

## Quick Start

```python
from img2txtio import Img2TxtClient

# Initialize client with your API key
token = "YOUR_API_KEY_HERE"
client = Img2TxtClient(api_key=token)

# Convert an image to plain text
result = client.process(
    image_path="path/to/image.jpg",
    output_type="raw",           # default: raw text
    description="Receipt from grocery",  # optional
    outputStructure=""           # optional JSON string for structured output
)

# `result` is a dict containing the API response
print(result)
```

## API Reference

### Class: `Img2TxtClient`

#### `__init__(api_key: str)`

Create a new client instance.
- `api_key` (str): Your img2txt.io API key. You can generate one from the [img2txt.io dashboard](https://img2txt.io/dashboard?api-settings=true).

#### `process(image_path: str, output_type: str = "raw", description: str = "", outputStructure: str = "") -> dict`

Uploads the image at `image_path` and converts it to text or structured output.

Parameters:

- `image_path` (str): Local path to the image file. Must exist, otherwise raises `FileNotFoundError`.
- `output_type` (str): The output format. Defaults to `raw`. Other valid types depend on the API (e.g., `json`, `structured`).
- `description` (str): Optional description or context to improve text extraction.
- `outputStructure` (str): Optional JSON string defining a structure/schema for the output. Must be valid JSON or raises `ValueError`.

Returns:

- `dict`: Parsed JSON response from the API. On failure, raises `RuntimeError`.  
- Example response:
    ```python
    {
        'text_output': [
            'Los Angeles', 'Florida', '$235', 'Round trip', 'Economy',
            '1 passenger', 'Lowest total price'
        ],
        'job_id': '16e2364a-e1e2-468e-9be9-e07b695b2afd',
        'creditsLeft': 86.115,
        'success': True,
        'message': 'Image processed successfully.'
    }
    ```


## Error Handling

- Network or HTTP errors raise `requests.exceptions.HTTPError`.
- Missing files raise `FileNotFoundError`.
- Invalid JSON in `outputStructure` raises `ValueError`.
- API failures raise `RuntimeError`.

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.