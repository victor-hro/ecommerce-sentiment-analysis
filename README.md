projeto/
└── src/
    ├── config/
    │   ├── __init__.py
    │   └── config.py
    └── dataset/
        ├── __init__.py
        └── data.py

# setup

python setup.py sdist bdist_wheel

pip install -e .