import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a test", [], {"href": "https://www.google.com"})
        self.assertEqual(' href="https://www.google.com"', node.props_to_html())

    def test_props_to_html2(self):
        node = HTMLNode(
            "p",
            "This is a test",
            [],
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )

    def test_leaf_to_html_no_children(self):
        node = LeafNode("p", "This is a test.")
        self.assertEqual("<p>This is a test.</p>", node.to_html())

    def test_leaf_to_html_with_prop(self):
        node = LeafNode("a", "This is a test.", {"href": "https://www.google.com"})
        self.assertEqual(
            '<a href="https://www.google.com">This is a test.</a>', node.to_html()
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is a test.")
        self.assertEqual(node.to_html(), "This is a test.")

    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>",
            node.to_html(),
        )

    def test_parent_to_html_nesting_parent(self):
        node = ParentNode(
            "i",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
            "p",
            [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), node],
        )

        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i><b>Bold text</b>Normal text</i></p>",
            node2.to_html(),
        )

    def test_parent_to_html_double_nesting(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
            "h",
            [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), node],
        )
        node3 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                node2,
            ],
        )

        self.assertEqual(
            "<p><b>Bold text</b>Normal text<h><b>Bold text</b>Normal text<h2><b>Bold text</b>Normal text</h2></h></p>",
            node3.to_html(),
        )

    def test_eq(self):
        node1 = HTMLNode(
            "p",
            "This is a test",
            [LeafNode("b", "Bold text")],
            {"href": "https://www.google.com"},
        )

        node2 = HTMLNode(
            "p",
            "This is a test",
            [LeafNode("b", "Bold text")],
            {"href": "https://www.google.com"},
        )
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "This is a test",
            [],
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            "HTMLNode(p, This is a test, [], {'href': 'https://www.google.com', 'target': '_blank'})",
            repr(node),
        )

    def test_leaf_repr(self):
        node = LeafNode("a", "This is a test.", {"href": "https://www.google.com"})
        self.assertEqual(
            "LeafNode(a, This is a test., {'href': 'https://www.google.com'})",
            repr(node),
        )

    def test_parent_repr(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            "ParentNode(p, children: [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, Italic text, None), LeafNode(None, Normal text, None)], None)",
            repr(node),
        )


if __name__ == "__main__":
    unittest.main()
