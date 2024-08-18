# PyJsonX Syntax for VSCode

## Overview

This VSCode extension enables syntax highlighting for JSON files containing embedded Python code. It supports seamless integration of Python code within JSON structures, enhancing readability and debugging.

## Features

- **Syntax Highlighting**: Distinguishes JSON and Python code within the same file.
- **Error Detection**: Highlights common syntax errors in both JSON and Python.
- **Code Folding**: Supports code folding for better navigation through embedded Python sections.

## Installation

1. Open VSCode.
2. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
3. Search for `PyJsonX Syntax`.
4. Click `Install`.

## Usage

1. Create or open a `.pyjsonX` file.
2. Embed Python code within the JSON structure using the `<?py ... ?>` tags.
3. The extension will automatically highlight Python code and JSON syntax.

## Example

```pyjsonX
{
    "example": "value",
    <?py
        # Python code here
        ret = "result"
    ?>
}
```

## Configuration

No additional configuration is required. The extension works out of the box with your JSON files containing Python code.

## Contributing

Feel free to submit issues or pull requests on the [GitHub repository](#).

## License

This extension is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
