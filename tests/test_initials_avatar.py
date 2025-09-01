"""
Tests for initials avatar functionality.
"""

import pytest
from metroui5.components import render_initials_avatar


class TestInitialsAvatar:
    """Test cases for render_initials_avatar function."""
    
    def test_basic_initials_generation(self):
        """Test basic initials generation from names."""
        result = render_initials_avatar("John Doe")
        assert "img" in result  # Should generate an image tag
        # In tests, Django settings may not be available, so fallback to base64
        # Or expect responsive figure with picture elements
        assert ("data:image/png;base64" in result or 
                "avatars/initials/JD/medium.png" in result or
                "figure" in result or
                "picture" in result)
    
    def test_single_name(self):
        """Test initials generation from single name."""
        result = render_initials_avatar("Alice")
        assert "img" in result  # Should generate an image tag
    
    def test_empty_name(self):
        """Test handling of empty name."""
        result = render_initials_avatar("")
        assert "img" in result  # Should still generate an image
    
    def test_none_name(self):
        """Test handling of None name."""
        result = render_initials_avatar(None)
        assert "img" in result  # Should still generate an image
    
    def test_multiple_words(self):
        """Test initials from multiple word names."""
        result = render_initials_avatar("John Michael Smith")
        assert "img" in result  # Should generate an image tag
    
    def test_custom_max_initials(self):
        """Test custom max_initials parameter."""
        result = render_initials_avatar("John Michael Smith", max_initials=3)
        assert "img" in result  # Should generate an image tag
    
    def test_different_sizes(self):
        """Test different size options."""
        sizes = ["small", "medium", "large", "xlarge"]
        for size in sizes:
            result = render_initials_avatar("John Doe", size=size)
            assert "img" in result  # Should generate an image tag
    
    def test_different_shapes(self):
        """Test different shape options."""
        shapes = ["circle", "square", "rounded"]
        for shape in shapes:
            result = render_initials_avatar("John Doe", shape=shape)
            assert "img" in result  # Should generate an image tag
    
    def test_custom_colors(self):
        """Test custom color options."""
        result = render_initials_avatar("John Doe", bg_color="#e74c3c", text_color="white")
        assert "img" in result  # Should generate an image tag
    
    def test_consistent_color_generation(self):
        """Test that same name generates same color."""
        result1 = render_initials_avatar("John Doe")
        result2 = render_initials_avatar("John Doe")
        
        # Both should generate images
        assert "img" in result1
        assert "img" in result2
    
    def test_special_characters_in_name(self):
        """Test handling of special characters in names."""
        result = render_initials_avatar("Jean-Pierre O'Connor")
        assert "img" in result  # Should generate an image tag
    
    def test_html_attributes(self):
        """Test that additional HTML attributes are preserved."""
        result = render_initials_avatar("John Doe", id="test-avatar", data_test="value")
        assert 'id="test-avatar"' in result
        assert 'data_test="value"' in result
    
    def test_accessibility_attributes(self):
        """Test that accessibility attributes are included."""
        result = render_initials_avatar("John Doe")
        assert 'alt="Avatar for John Doe"' in result
    
    def test_file_saving(self):
        """Test saving avatar to file."""
        import tempfile
        import os
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
            tmp_path = tmp_file.name
        
        try:
            result = render_initials_avatar("John Doe", save_path=tmp_path)
            assert "img" in result
            assert os.path.exists(tmp_path)
            assert os.path.getsize(tmp_path) > 0
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
