from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("invalid markdown syntax, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)
# zipmap -- one list for alt text, one for urls

# need to handle **bold**, _italics_, `code`...
# if no matching closing delimiter, raise exception about invalid markdown syntax. count occurences in string?
# order to check for different delimiters matters
# recursion in order to handle a node with multiple instances "**bold**, _italic_, `code`"
# recursion in order to handle a node with different instances "this is **bolded**, this is also **bolded**"
