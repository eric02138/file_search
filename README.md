# file_search
#### Command line app that searches for files based on a search pattern

## Assumptions
* os.listdir and similar functions were out, but anything else included with Python was fair game (os.path, glob, argparse)
* We don't have to search for special files (e.g. .bashrc, weird names)
* Legibility > Minimization

## Installation

> Run as a standalone script (Again, a pip install isn't really warranted here.) 

* Download the repo and change directory to json_tree directory
```
cd /path/to/file_search
```

## Usage example
Basic Usage:
```
python main.py ./sample/ ir
```

With Case-Insensitive Option:
```
python main.py ./sample/ ir --ignore-case
python main.py ./sample/ ir -i
```

Run Tests:
```
python test.py
```

## Release History
* 0.0.1
    * Works

## Meta

Distributed under MIT Public license. See ``LICENSE`` for more information.

## Contributing

1. Fork it (<https://github.com/eric02138/file_search/fork>)
2. Create your feature branch (`git checkout -b feature/someaddition`)
3. Commit your changes (`git commit -am 'Add someaddtion'`)
4. Push to the branch (`git push origin feature/someaddition`)
5. Create a new Pull Request