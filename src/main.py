from textnode import TextNode, TextType

def main():
    example_node = TextNode("anchor text",TextType.Link,"https://www.boot.dev")
    print(example_node)

if __name__ == "__main__":
    main()
