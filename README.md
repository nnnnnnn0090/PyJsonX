# PyJsonX

[Switch to Japanese: 日本語](https://github.com/nnnnnnn0090/PyJsonX/blob/main/README.ja.md)

### Overview

`PyJsonX` is a Python library inspired by PHP's capability to embed code within templates. It allows you to embed Python code within JSON files, facilitating the generation of dynamic and programmable JSON content. This library provides a way to create flexible JSON structures directly from within Python, similar to how PHP allows embedding code within HTML.

### Installation

You can install `PyJsonX` using pip:

```bash
pip3 install PyJsonX
pip3 install git+https://github.com/nnnnnnn0090/PyJsonX
```

### File Extension

- `PyJsonX` uses the `.pyjsonX` extension. [example.pyjsonX](https://github.com/nnnnnnn0090/PyJsonX/blob/main/PyJsonX/example.pyjsonX)  
  VSCode has an extension for `.pyjsonX` files. [VisualStudio MarketPlace](https://marketplace.visualstudio.com/items?itemName=nnnnnnn0090.pyjsonX)

### Usage

#### Embedding Python in JSON

You can embed Python code within JSON using `<?py ... ?>` tags. Here’s an example:
<img width="660" alt="スクリーンショット 2024-08-18 19 32 56" src="https://github.com/user-attachments/assets/0af18fc9-6aa5-4c01-b3aa-072660347d17">
↓
```json
{
    "static_field": "value",
    "unixtime": 1723977194,
    "dynamic_0": "0",
    "dynamic_1": "2",
    "dynamic_2": "4",
    "dynamic_3": "6",
    "dynamic_4": "8",
    "another_static_field": "another_value"
}
```

#### Executing Embedded Python

1. **From JSON String:**

    ```python
    import PyJsonX

    json_str = '''
    {
        "static_field": "value",
        <?py
            result = ""
            # Generate dynamic fields with values from 0 to 4
            for i in range(5):
                result += f'"dynamic_{i}": "{i * 2}", \n'
            return result
        ?>
        "another_static_field": "another_value"
    }
    '''

    # Process the JSON string and execute the embedded Python code
    processed_str = PyJsonX.execute(json_str)
    print(processed_str)  # Output the processed JSON
    ```

2. **From JSON Files:**

    ```python
    import PyJsonX

    input_json_path = 'input.json'  # Path to the input JSON file
    output_json_path = 'output.json'  # Path to the output JSON file

    # Process the JSON file and execute the embedded Python code
    PyJsonX.execute_file(input_json_path, output_json_path)
    ```

### Features

- **Dynamic Content Generation:** Embed and execute Python code directly within JSON to generate dynamic content.
- **Flexible Data Creation:** Generate complex JSON structures dynamically based on programmatic logic.
- **Inspired by PHP:** Draws inspiration from PHP's templating capabilities, allowing for similar embedded code functionality within JSON.

### Documentation

For more detailed information, visit the [PyJsonX Documentation](https://github.com/nnnnnnn0090/PyJsonX). (Coming Soon)

### Contributing

Contributions are welcome! Please submit a pull request or open an issue on our [GitHub repository](https://github.com/nnnnnnn0090/PyJsonX).

### License

`PyJsonX` is licensed under the MIT License. See [LICENSE](https://github.com/nnnnnnn0090/PyJsonX/blob/main/LICENSE) for details.

---
