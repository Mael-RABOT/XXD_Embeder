# XXD Embeder

This script is a simple script that help automate the creation of embedded resources in C/C++ using the xxd tool.

## Usage

```bash
python3 embeder.py <input_folder> <output_file>
```

- The input must be a valid folder
- The output must be a valid .h/.hpp file

Currently, this tool only work on `.png` files.<br>
To add more file types, you can modify the `embeder.py` file at the `allowed_file_types` list.

## License

This project use the GPL-3.0 License. You can read more about it [here](https://www.gnu.org/licenses/gpl-3.0.html).
