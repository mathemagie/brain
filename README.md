# Brain Project.

A Python tool to convert web content to markdown and PDF formats, with optional Kindle delivery support.

## Features

- Convert web content to markdown using jina.ai service
- Generate PDFs from markdown files
- Send PDFs to Kindle via email
- Extract and process non-YouTube links from markdown files
- Custom styling support for PDF generation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/brain.git
cd brain
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Development Setup

### Pre-commit Setup

1. Install pre-commit:
```bash
pip install pre-commit
```

2. Create a `.pre-commit-config.yaml` file:
```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
    -   id: check-merge-conflict

-   repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
    -   id: black

-   repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
    -   id: flake8
        args: ['--max-line-length=88']  # Match black's line length

-   repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
    -   id: isort
        args: ["--profile", "black"]
```

3. Install the pre-commit hooks:
```bash
pre-commit install
```

This will set up the following code quality checks:
- Black (code formatting)
- Flake8 (code linting)
- isort (import sorting)
- Various file checks (trailing whitespace, merge conflicts, etc.)

## Environment Setup

1. Create a `.env` file in the project root:
```bash
touch .env
```

2. Add your configuration:
```env
KINDLE_EMAIL=your-kindle-email@kindle.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-specific-password
```

## Usage

1. To process a single URL:
```python
from get_md import get_and_save_md

get_and_save_md("https://example.com/article")
```

2. To process links from a markdown file:
```python
python get_md.py
```

3. To send a PDF directly to Kindle:
```python
python send_to_kindle.py path/to/your/file.pdf
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
