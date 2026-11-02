import tempfile
import unittest
from pathlib import Path
from scripts.denoise_html import denoise_html


def test_denoise_html(tmp_path=None):
    if tmp_path is None:
        with tempfile.TemporaryDirectory() as td:
            return test_denoise_html(Path(td))
    # Create a dummy HTML file with typical layout noise
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Page</title>
        <style>body { color: red; }</style>
    </head>
    <body>
        <header>
            <nav>
                <a href="/home">Home</a>
                <a href="/about">About</a>
            </nav>
        </header>
        
        <aside class="sidebar">
            <h3>Recent Posts</h3>
            <ul>
                <li>Post 1</li>
                <li>Post 2</li>
            </ul>
        </aside>
        
        <main id="main-content">
            <article>
                <h1>How to Fabricate Stainless Steel Screens</h1>
                <p>This is the actual core content of the article with <strong>full-sentence bold anchor</strong>.</p>
                <h2>Why Does Grade 316L Beat 304 in Coastal Air?</h2>
                <p>It has details about fabrication parameters like mesh size and wire diameter.</p>
                <table>
                    <tr><th>Grade</th><th>Tolerance</th></tr>
                    <tr><td>316L</td><td>±0.15 mm</td></tr>
                </table>
                <div class="callout-card">
                    Direct text inside a div before a span <span>and inside a span</span> with <strong>bold tail</strong>.
                </div>
            </article>
        </main>
        
        <footer class="footer">
            <p>&copy; 2026 Stainless Steel Screen Co.</p>
        </footer>
        
        <script>
            console.log("Noise Script");
        </script>
    </body>
    </html>
    """
    
    input_file = tmp_path / "input.html"
    output_file = tmp_path / "output.md"
    
    input_file.write_text(html_content, encoding="utf-8")
    
    denoise_html(input_file, output_file)
    
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    
    # Assert main content and Markdown structure (headings, bold, tables) exist
    assert "# How to Fabricate Stainless Steel Screens" in content
    assert "## Why Does Grade 316L Beat 304 in Coastal Air?" in content
    assert "**full-sentence bold anchor**" in content
    assert "| Grade | Tolerance |" in content
    assert "| 316L | ±0.15 mm |" in content
    assert "Direct text inside a div before a span and inside a span with **bold tail**." in content
    
    # Assert noise tags are stripped
    assert "Home" not in content
    assert "Recent Posts" not in content
    assert "Noise Script" not in content
    assert "2026 Stainless Steel Screen Co" not in content


class DenoiseHtmlTestCase(unittest.TestCase):
    def test_denoise(self):
        test_denoise_html()

