"""Regression checks for source links, Liquid escaping and rendered validation."""
import tempfile
from pathlib import Path
import unittest

from check_docs import rendered_checks
from sync_docs import page, rewrite_links, write_outputs


class DocumentationTools(unittest.TestCase):
    def setUp(self):
        self.manifest = {"repositories": {"core": {"repository": "Example/core", "revision": "abc"}},
                         "imports": [{"repository": "core", "source": "docs/a.md", "destination": "docs/guides/a.md"}],
                         "copies": [], "anchor_corrections": {"old-anchor": "new-anchor"}}

    def test_source_links_and_code_literals(self):
        text = '[Guide](a.md#old-anchor)\n[API](../src/api.js)\n```js\n"[literal](a.md)"\n```\n'
        result = rewrite_links(text, "core", "docs/b.md", "docs/guides/b.md", self.manifest)
        self.assertIn('[Guide](a.md#new-anchor)', result)
        self.assertIn('https://github.com/Example/core/blob/abc/src/api.js', result)
        self.assertIn('"[literal](a.md)"', result)

    def test_liquid_examples_are_wrapped_and_nested_raw_rejected(self):
        result = page("Example", "Guides", '{{name}}')
        self.assertIn('{% raw %}\n{{name}}\n{% endraw %}', result)
        with self.assertRaises(ValueError):
            page("Example", "Guides", '{% endraw %}')

    def test_check_mode_does_not_mutate(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertTrue(write_outputs({'page.md': 'hello\n'}, root, True))
            self.assertFalse((root / 'page.md').exists())
            write_outputs({'page.md': 'hello\n'}, root, False)
            self.assertFalse(write_outputs({'page.md': 'hello\n'}, root, True))

    def test_rendered_links_and_fragments(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'index.html').write_text('<a href="/guide#present">ok</a><a href="/guide#missing">bad</a>')
            (root / 'guide.html').write_text('<h2 id="present">Guide</h2>')
            result = rendered_checks(root)
            self.assertEqual(result['local_links_checked'], 2)
            self.assertEqual(result['errors'], ['index.html: missing rendered anchor /guide#missing'])


if __name__ == "__main__":
    unittest.main()
