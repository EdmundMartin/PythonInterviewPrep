class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def get_youngest_common_ancestor(
    top_ancestor: AncestralTree,
    descendant_one: AncestralTree,
    descendant_two: AncestralTree,
) -> AncestralTree:
    ancestors = dict()

    while descendant_one:
        ancestors[descendant_one.name] = descendant_one
        descendant_one = descendant_one.ancestor

    while descendant_two:
        if descendant_two.name in ancestors:
            return descendant_two
        descendant_two = descendant_two.ancestor
