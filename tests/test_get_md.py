import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import requests
from unittest.mock import patch, mock_open, MagicMock
from get_md import (
    is_valid_url,
    download_markdown,
    save_markdown,
    get_and_save_md,
    get_non_youtube_links,
    convert_markdown_to_pdf,
)

# Test data
VALID_URL = "https://example.com/article"
INVALID_URL = "not_a_url"
SAMPLE_MARKDOWN = "# Test Markdown\nThis is a test."
SAMPLE_LINKS_MD = """
# Test Document
[Valid Link](https://example.com)
[YouTube Link](https://outube.com/watch?v=123)
[Another Link](https://test.com)
"""


@pytest.fixture
def mock_response():
    mock = MagicMock()
    mock.text = SAMPLE_MARKDOWN
    mock.raise_for_status = MagicMock()
    return mock


def test_is_valid_url():
    assert is_valid_url(VALID_URL) == True
    assert is_valid_url(INVALID_URL) == False
    assert is_valid_url("") == False


@patch("requests.get")
def test_download_markdown_success(mock_get, mock_response):
    mock_get.return_value = mock_response
    result = download_markdown(VALID_URL)
    assert result == SAMPLE_MARKDOWN
    mock_get.assert_called_once()


@patch("requests.get")
def test_download_markdown_invalid_url(mock_get):
    result = download_markdown(INVALID_URL)
    assert result is None
    mock_get.assert_not_called()


@patch("requests.get")
def test_download_markdown_request_error(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException()
    result = download_markdown(VALID_URL)
    assert result is None


def test_save_markdown(tmp_path):
    test_file = tmp_path / "test.md"
    result = save_markdown(SAMPLE_MARKDOWN, str(test_file))
    assert result == True
    assert test_file.read_text() == SAMPLE_MARKDOWN


def test_save_markdown_error(tmp_path):
    # Test with an invalid path
    invalid_path = "/invalid/path/test.md"
    result = save_markdown(SAMPLE_MARKDOWN, invalid_path)
    assert result == False


@patch("os.path.exists")
@patch("get_md.download_markdown")
@patch("get_md.save_markdown")
@patch("get_md.convert_markdown_to_pdf")
@patch("get_md.send_email")
def test_get_and_save_md_success(
    mock_send_email, mock_convert_pdf, mock_save, mock_download, mock_exists
):
    mock_exists.return_value = False
    mock_download.return_value = SAMPLE_MARKDOWN
    mock_save.return_value = True
    mock_convert_pdf.return_value = "test.pdf"
    mock_send_email.return_value = True

    result = get_and_save_md(VALID_URL)
    assert result == True


def test_get_non_youtube_links(tmp_path):
    # Create a temporary markdown file
    test_file = tmp_path / "test.md"
    test_file.write_text(SAMPLE_LINKS_MD)

    links = get_non_youtube_links(str(test_file))
    assert len(links) == 2
    assert "youtube.com" not in "".join(links)
    assert "https://example.com" in links
    assert "https://test.com" in links


@patch("os.system")
@patch("os.path.exists")
def test_convert_markdown_to_pdf(mock_exists, mock_system, tmp_path):
    test_file = tmp_path / "test.md"
    test_file.write_text(SAMPLE_MARKDOWN)

    # Mock both file existence checks
    mock_exists.side_effect = [True, True]  # md file exists, css file exists

    result = convert_markdown_to_pdf(str(test_file))
    assert result == str(test_file).replace(".md", ".pdf")
    mock_system.assert_called_once()


def test_convert_markdown_to_pdf_missing_file():
    result = convert_markdown_to_pdf("nonexistent.md")
    assert result == False
