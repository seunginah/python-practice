# python-practice
My python practice snippets :) Let's always follow best practices of
- DevOps
- CI/CD
- Python conventions


# Initialize project...

### Set up environment management with [**virtualenv**](https://virtualenv.pypa.io/en/latest/)
`♥ 14:41:30 ♥ python3
Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14)
[Clang 6.0 (clang-600.0.57)] on darwin
♥ 14:44:10 ♥ virtualenv venv --python $(which python3)
created virtual environment CPython3.9.10.final.0-64 in 1081ms
  creator CPython3Posix(dest=/Users/seungin/projects/python-practice/venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/seungin/Library/Application Support/virtualenv)
    added seed packages: pip==24.3.1, setuptools==75.6.0, wheel==0.45.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator`

Activate my virtual environment
`♥ 14:45:53 ♥ source venv/bin/activate`

Upgrade pip
`(venv) ♥ 15:19:35 ♥  pip install --upgrade pip`

### Set up repo structure
`
python-practice/
├── src/
│   ├── __init__.py
│   └── my_module.py
├── tests/
│   ├── __init__.py
│   └── test_my_module.py
└── setup.py
`

### Linting & Formatting with [**flake8**](https://flake8.pycqa.org/en/latest/index.html)

TODO: add github actions, flake8 https://github.com/marketplace/actions/flake8-action