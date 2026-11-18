#!/usr/bin/env python3
"""
Test script for file component
"""

import sys
import os

# Add the metroui5 package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'metroui5'))

from metroui5.components.file import render_file, render_file_button, render_file_drop, render_file_with_icon, render_file_multiple

def test_file_component():
    """Test file component functionality"""
    print("Testing File Component...")

    # Basic test
    html = render_file()
    print(f"Basic: {html}")
    assert 'data-role="file"' in html
    assert 'type="file"' in html
    print("✓ Basic component test passed")

    # Test with parameters
    html = render_file(label="Select file:", mode="button")
    print(f"With parameters: {html}")
    assert 'data-label="Select file:"' in html
    assert 'data-mode="button"' in html
    print("✓ Component with parameters test passed")

    # Test validation states
    html = render_file(error=True, error_message="Please select a file")
    print(f"With error: {html}")
    assert 'data-error="true"' in html
    assert 'error' in html
    print("✓ Error state test passed")

    # Test utility functions
    html = render_file_button("Choose File")
    print(f"Button mode: {html}")
    assert 'data-mode="button"' in html
    assert 'data-button-title="Choose File"' in html
    print("✓ Button mode test passed")

    html = render_file_drop("Drop here")
    print(f"Drop mode: {html}")
    assert 'data-mode="drop"' in html
    assert 'data-drop-title="Drop here"' in html
    print("✓ Drop mode test passed")

    html = render_file_with_icon("mif-folder")
    print(f"With icon: {html}")
    assert 'data-prepend=' in html
    assert 'mif-folder' in html
    print("✓ With icon test passed")

    html = render_file_multiple()
    print(f"Multiple files: {html}")
    assert 'multiple="multiple"' in html
    print("✓ Multiple files test passed")

    # Test file type restriction
    html = render_file(accept="image/*")
    print(f"With accept: {html}")
    assert 'accept="image/*"' in html
    print("✓ File type restriction test passed")

    # Test disabled state
    html = render_file(disabled=True)
    print(f"Disabled: {html}")
    assert 'disabled="disabled"' in html
    print("✓ Disabled state test passed")

    # Test required state
    html = render_file(required=True)
    print(f"Required: {html}")
    assert 'required="required"' in html
    print("✓ Required state test passed")

    print("🎉 All tests passed!")

if __name__ == "__main__":
    test_file_component()
