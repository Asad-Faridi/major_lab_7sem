family_tree = {
    "Grandfather": ["Father", "Uncle"],
    "Father": ["You", "Sister"],
    "Uncle": ["Cousin", "Cousin2"],
    "You": [],
    "Sister": [],
    "Cousin": [],
    "Cousin2": []
}
def find_descendants(person):
    descendants = []
    def dfs(current):                       # current represents the person we're currently visiting
        for child in family_tree[current]:
            descendants.append(child)
            dfs(child)
    dfs(person)
    return descendants
person = "Father"
result = find_descendants(person)
print("Descendants of", person, ":", result)